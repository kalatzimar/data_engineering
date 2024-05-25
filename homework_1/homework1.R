
# load excel data
library(readxl)
data = read_excel("homework1.xlsx")

# convert tibble to data.frame
data = data.frame(data)
data

# run a scatter plot of heights against weights
plot(data)

# perform linear regression
model = lm(heights~weights,data = data)
summary(model)

# save parameter estimates along with their standard errors
est = model$coefficients
est_se = summary(model)$coefficients[,"Std. Error"]
est_se

# create data frame of estimates
estimates = data.frame(est,est_se)

# save current date
date = format(Sys.Date(), "%d-%m-%Y")
date

# save sample size of data
sample_size = dim(estimates)[1]
sample_size

# set file name using sprintf
file_name = sprintf("restimates_%s_%1.0f",date,sample_size)
file_name

# save in a csv file
write.csv(estimates,file = file_name,row.names = F)
