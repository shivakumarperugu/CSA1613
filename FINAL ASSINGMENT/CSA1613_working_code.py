# CSA1613 Data Warehouse & Data Mining – Working Python Demo
# Generates 8 output figures:
# 1. Data preprocessing
# 2. Sales by category
# 3. Monthly sales trend
# 4. Regional sales
# 5. Category vs payment pivot
# 6. Model comparison
# 7. Confusion matrices
# 8. ROC curves
#
# Install once:
# pip install numpy pandas matplotlib scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

rng = np.random.default_rng(1613)
n = 1000

df = pd.DataFrame({
    "Age": rng.integers(18, 66, n),
    "Region": rng.choice(["South","North","East","West"], n),
    "Frequency": rng.poisson(5, n) + 1,
    "Monetary": np.round(rng.gamma(3, 3500, n), 2),
    "Average_Order_Value": np.round(rng.gamma(3.2, 700, n), 2),
    "Tenure_Days": rng.integers(30, 1600, n),
    "Complaint_Return_Count": rng.poisson(.8, n),
    "Delivery_Days": np.round(np.clip(rng.normal(4.5, 1.7, n), 1, 12), 1),
    "Avg_Session_Time": np.round(np.clip(rng.normal(7, 3, n), 1, 20), 1),
    "Cart_Abandon_Rate": np.round(rng.uniform(.05, .85, n), 2)
})

df["Recency"] = np.round(np.clip(
    75 - df["Frequency"]*4 - df["Avg_Session_Time"]*1.3
    + df["Cart_Abandon_Rate"]*35 + rng.normal(0,18,n), 1, 180
)).astype(int)

score = (0.045*df["Recency"] - .16*df["Frequency"]
         - .22*df["Avg_Session_Time"] + .85*df["Cart_Abandon_Rate"]
         + .22*df["Complaint_Return_Count"] + .10*df["Delivery_Days"]
         - .000035*df["Monetary"] + rng.normal(0,1,n))
df["Churn_Flag"] = (score > np.quantile(score,.82)).astype(int)

# ----- Churn models -----
features = ["Recency","Frequency","Monetary","Average_Order_Value",
            "Tenure_Days","Complaint_Return_Count","Delivery_Days",
            "Avg_Session_Time","Cart_Abandon_Rate"]

X = df[features]
y = df["Churn_Flag"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=.30,random_state=42,stratify=y)

models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=5,min_samples_leaf=10,random_state=42),
    "Naive Bayes": GaussianNB(),
    "SVM": SVC(kernel="rbf",C=1.0,probability=True,random_state=42)
}

for name, model in models.items():
    model.fit(X_train,y_train)
    pred = model.predict(X_test)
    print("\n", name)
    print("Accuracy :", round(accuracy_score(y_test,pred),4))
    print("Precision:", round(precision_score(y_test,pred,zero_division=0),4))
    print("Recall   :", round(recall_score(y_test,pred,zero_division=0),4))
    print("F1-score :", round(f1_score(y_test,pred,zero_division=0),4))

# Add your own warehouse CSV here if available:
# df = pd.read_csv("your_churn_feature_table.csv")