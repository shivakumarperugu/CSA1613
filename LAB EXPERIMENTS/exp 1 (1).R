# Grouped data
lower <- c(1, 5, 15, 20, 50, 80)
upper <- c(5, 15, 20, 50, 80, 110)
freq <- c(200, 450, 300, 1500, 700, 44)

N <- sum(freq)
cf <- cumsum(freq)

N2 <- N/2

median.class <- which(cf >= N2)[1]

L <- lower[median.class]
f <- freq[median.class]
cf.prev <- ifelse(median.class==1,0,cf[median.class-1])
h <- upper[median.class]-lower[median.class]

median <- L + ((N2-cf.prev)/f)*h

cat("Approximate Median =", median)