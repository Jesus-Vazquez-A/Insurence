# Insurence-Proyect

### Definition of the problem.

Create a machine learning algorithm with the goal of estimating the health insurance charges.
To later use it to create an application and upload it to herouku.

### Features of dataset.

* Age  of the insured.
* BMI  body mass index.
* Children  Number of children of the insured.
* Region User's place of residence.
* Smoker  Whether the user smokes or not.
* Charges  Health insurance price.


### Project composition


* **Exploratory analysis.**    We understand the nature of data

* **Feature Engineering.**     We remove or transform the outliers.  We transform outliers to missing values and replace them using a linear regression model.

* **Search for the right model.**   We make comparisons between different models. As well as looking for the best combination of parameters. We will use the MSE as a performance metric, since it is less sensitive to outliers and what we are looking for is a model that generalizes well.  We create 3 models: **polynomial regression**, **Gradient Boosting** and **XGBoost**.


* **Definitive model.**   Create the best model again. And we save it for later use.

* **App in  Streamlit.**  We use streamlit which is a specialized library for data science. That allows us to create applications easily.

# Project summary.

* **Definition of the problem** 

When performing a histogram, we notice the presence of atypical values, that is, values that are out of the norm.

We deduce that these values can have a better explanation if we add more variables.

We create a box and whisker plot where we add the variable smoker. We discovered that it is a variable that greatly influences the price of health insurance.

We also found that if the user is a smoker and has an advanced BMI. The insurance charge increases more, since the insured will have more charges due to his state of health.

The BMI maintains a linear trend relationship compared to the predicted insurance. That is, one value increases proportionally to the other.


The variable age has a strong linear relationship with the variable charges,it does not increase the price of insurance as considerably since most people who smoke are healthier.


But for the group of non-smokers it has a significant number of outliers, The main challenge will be the treatment of outliers. Since we cannot delete them, due to the amount of data we have, we will have to find an ingenious way to deal with them.

The main challenge will be the treatment of outliers. Since we cannot eliminate them, due to the amount of data we have, we'll have to find an ingenious way to deal with them.

* **Approach**


We decided to separate the data into smokers and non-smokers, with the aim of giving the data a better treatment.

We apply the central limit theorem, which is a technique used to establish confidence intervals. That is, to select values that follow a normal trend, it is usually used to eliminate outliers. But in this case we calculate the upper interval and transform to missing value those values that exceed the established interval.

As described above, for non-smokers we observed a linear trend with respect to age and position. And I thought why instead of replacing the missing values before, why not create a linear regression model? Train the model with normal values, to later replace the missing values with new values closer to the original value.

They have a significant advantage over replacing it with a basic statistical measure such as the average and the median. Since it could affect the distribution of the data.

For smokers, since there were few outliers, we decided to replace them with normal values close to the highest values, within the normal range.





### GIF Proyect

<img src="https://media.giphy.com/media/BileRHL3JLUMtG4vH5/giphy.gif" width=350>

### Link app

https://insurence-app-predict.herokuapp.com/
