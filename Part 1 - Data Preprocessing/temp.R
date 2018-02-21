 getwd();
 
 path = "C://Users/madh9981/Documents/Learning/Udemy_ML/Part 1 - Data Preprocessing";
print(path)
 setwd(path);
  setwd("C://Users/madh9981/Documents/Learning/Udemy_ML/Part 1 - Data Preprocessing");
 
 dataset = read.csv('Data.csv');
 
 #unlike python the index starts with 1 not 0
 #in R we don't have to make distinction between matrix of features and depedent variables vector
 
 #taking care of missing data
 dataset$Age = ifelse(is.na(dataset$Age),
                      ave(dataset$Age, FUN =function(x) mean(x,na.rm = TRUE) ),
                      dataset$Age)
 
 dataset$Salary = ifelse(is.na(dataset$Salary),
                         ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                         dataset$Salary)
 
 
 