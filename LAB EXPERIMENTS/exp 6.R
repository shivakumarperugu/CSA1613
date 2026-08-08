age <- c(23,23,27,27,39,41,47,49,50,52,
         54,54,56,57,58,58,60,61)

x <- 35

# Min-Max
(x-min(age))/(max(age)-min(age))

# Z-score
(x-mean(age))/12.94

# Decimal Scaling
x/100
