# Experiment 4: Smoothing by Binning

data <- c(11,13,13,15,15,16,19,20,20,20,21,21,
          22,23,24,30,40,45,45,45,71,72,73,75)

# Number of bins = 8 (3 values in each bin)
bins <- matrix(data, ncol = 3, byrow = TRUE)

cat("Original Bins:\n")
print(bins)

# a) Smoothing by Bin Mean
cat("\nSmoothing by Bin Mean\n")
for(i in 1:nrow(bins)){
  mean_value <- mean(bins[i, ])
  print(rep(mean_value, 3))
}

# b) Smoothing by Bin Median
cat("\nSmoothing by Bin Median\n")
for(i in 1:nrow(bins)){
  median_value <- median(bins[i, ])
  print(rep(median_value, 3))
}

# c) Smoothing by Bin Boundaries
cat("\nSmoothing by Bin Boundaries\n")
for(i in 1:nrow(bins)){
  low <- bins[i,1]
  high <- bins[i,3]
  
  boundary <- ifelse(abs(bins[i,]-low) <= abs(bins[i,]-high),
                     low, high)
  print(boundary)
}