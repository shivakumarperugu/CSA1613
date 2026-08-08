x <- c(200,300,400,600,1000)

# Min-Max Normalization
minmax <- (x-min(x))/(max(x)-min(x))
minmax

# Z-score Normalization
zscore <- (x-mean(x))/sd(x)
zscore