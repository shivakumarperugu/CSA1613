marks <- c(55,60,71,63,55,65,50,55,
           58,59,61,63,65,67,71,72,75)

# Histogram
hist(marks,
     main="Histogram",
     col="lightblue")

# Equal Frequency Partition
sort(marks)

split(sort(marks),
      ceiling(seq_along(sort(marks))/6))

# Equal Width Partition
cut(marks,
    breaks=3)