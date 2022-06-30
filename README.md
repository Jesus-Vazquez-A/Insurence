# Insurence-Proyect

### Definition of the problem.

### Features of dataset.

* Age  of the insured.
* BMI  body mass index.
* Children  Number of children of the insured.
* Region User's place of residence.
* Smoker  Whether the user smokes or not.
* Charges  Health insurance price.


When performing a histogram, we notice the presence of atypical values, that is, values that are out of the norm.

We deduce that these values can have a better explanation if we add more variables.

We create a box and whisker plot where we add the variable smoker. We discovered that it is a variable that greatly influences the price of health insurance.

We also found that if the user is a smoker and has an advanced BMI. The insurance charge increases more, since the insured will have more charges due to his state of health.

The BMI maintains a linear trend relationship compared to the predicted insurance. That is, one value increases proportionally to the other.

The variable age has a strong linear relationship with the variable charges,it does not increase the price of insurance as considerably since most people who smoke are healthier.

But for the group of non-smokers it has a significant number of outliers, The main challenge will be the treatment of outliers. Since we cannot delete them, due to the amount of data we have, we will have to find an ingenious way to deal with them.

The main challenge will be the treatment of outliers. Since we cannot eliminate them, due to the amount of data we have, we'll have to find an ingenious way to deal with them.



### Project composition


* **Exploratory analysis.**    We understand the nature of data

* **Feature Engineering.**     We remove or transform the outliers.  We transform outliers to missing values and replace them using a linear regression model.

* **Search for the right model.**   We make comparisons between different models. As well as looking for the best combination of parameters. We will use the MSE as a performance metric, since it is less sensitive to outliers and what we are looking for is a model that generalizes well.  We create 3 models: **polynomial regression**, **Gradient Boosting** and **XGBoost**.


* **Definitive model.**   Create the best model again. And we save it for later use.

* **App in  Streamlit.**  We use streamlit which is a specialized library for data science. That allows us to create applications easily.

# Project summary.

* **Approach**

Feature engineering consists of dealing with missing values or outliers. Where an optimal treatment for such data is found, this step is very important for the performance of the model. Since it is the data that we are going to give to train the model.

We decided to separate the data into smokers and non-smokers, with the aim of giving the data a better treatment.

We apply the central limit theorem, which is a technique used to establish confidence intervals. That is, to select values that follow a normal trend, it is usually used to eliminate outliers. But in this case we calculate the upper interval and transform to missing value those values that exceed the established interval.

As described above, for non-smokers we observed a linear trend with respect to age and position. And I thought why instead of replacing the missing values before, why not create a linear regression model? Train the model with normal values, to later replace the missing values with new values closer to the original value.

They have a significant advantage over replacing it with a basic statistical measure such as the average and the median. Since it could affect the distribution of the data.

For smokers, since there were few outliers, we decided to replace them with normal values close to the highest values, within the normal range.


* **Model Interpretation**

For both models, we use the same variables.
We apply data rescaling process, although for assembly models it is not necessary. Since these algorithms work through decision trees, they use mathematical inequalities.

We do not discriminate any variable, although in the EDA. We found that the variables smoker, age and bmi influence the cost of health insurance.

Although it could eliminate variables such as gender and region. I didn't want to remove it as the difference between humans and algorithms. It is that we take the most important variables, while the algorithms use these variables and complement them with other variables in which they find unknown patterns. They favor the quality of the prediction.

We create 3 regression algorithms:

* **Polynomial Regression:**  It consists of raising the predictor variables to a certain power. In order for the model to have better predictions than a linear regression.


* **Ensemble algorithms:** Gradient Boosting and XGBoost are some algorithms that belong to this category. These algorithms work using weaker algorithms, usually decision trees. That each time they are improving with respect to the learning rate and the number of estimators,one of the main differences is that XGBoost can be executed through a GPU, something that allows faster training. 

![Captura de pantalla (66)](https://user-images.githubusercontent.com/85312561/176789617-8f9aea02-c54c-42a0-806b-792ae67e7178.png)

For the assembly algorithms, we perform various analyzes.

We use the same parameters for XGBoost and Gradient Boosting.

* max_depth:  It refers to the maximum depth of the decision tree. For the first evaluation we use a maximum depth of 2 and in the second of 3.
* n_estimators: Number of decision trees. The range of estimators we used was from 100 to 1000.
* learing_rate: It is the room for improvement for each iteration. We use a learning rate of 0.01


    
* The polynomial model gives excellent predictions for non-smokers, while its counterpart gives mediocre predictions.

* Gradient Boosting suits both cases very well.

* XGBoost is better than Gradient Boosting, has a lower MSE for validation data, and is faster.

After several analyzes we conclude that the best model is the XGBoost. Since more number of estimators can be used, it minimizes the MSE and has fewer symptoms of overfitting.






### GIF Proyect

<img src="https://media.giphy.com/media/BileRHL3JLUMtG4vH5/giphy.gif" width=350>

### Link app

https://insurence-app-predict.herokuapp.com/
