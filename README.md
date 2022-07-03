# Insurence-Proyect

![medico-640x360](https://user-images.githubusercontent.com/85312561/176962002-f9150158-0b62-4401-a051-ec84e62eacd8.jpg)



### Project composition

* **app:** It includes the application code in streamlit, as well as the previously trained model.

* **data:**  It contains the original dataset and the clean dataset, that is, where we preprocessed outliers.

* **doc:**  Documentation in pdf.

* **src:**  Steps for creating the model and the application.

### Definition of the problem.

### Features of dataset.

* Age  of the insured.
* BMI  body mass index.
* Children  Number of children of the insured.
* Region User's place of residence.
* Smoker  Whether the user smokes or not.
* Charges  Health insurance price.


![charges_histogram](https://user-images.githubusercontent.com/85312561/176960847-5499ecaa-104d-4bcf-be35-ba695dfbafa6.png)




When performing a histogram, we notice the presence of atypical values, that is, values that are out of the norm.

We deduce that these values can have a better explanation if we add more variables.

![smoker_charges](https://user-images.githubusercontent.com/85312561/176960897-71a33ce2-458b-4563-89ff-5043961e616b.png)


We create a box and whisker plot where we add the variable smoker. We discovered that it is a variable that greatly influences the price of health insurance.


![bmi_smoker](https://user-images.githubusercontent.com/85312561/176960946-0d14daf2-a741-4c9e-9f75-166c54426583.png)


We also found that if the user is a smoker and has an advanced BMI. The insurance charge increases more, since the insured will have more charges due to his state of health.

The BMI maintains a linear trend relationship compared to the predicted insurance. That is, one value increases proportionally to the other.

![age_smoker](https://user-images.githubusercontent.com/85312561/176960976-15cc4044-da46-4f2b-bd7c-0af543f4885b.png)


The variable age has a strong linear relationship with the variable charges,it does not increase the price of insurance as considerably since most people who smoke are healthier.

#### **Conclusion**

But for the group of non-smokers it has a significant number of outliers, The main challenge will be the treatment of outliers. Since we cannot delete them, due to the amount of data we have, we will have to find an ingenious way to deal with them.

The main challenge will be the treatment of outliers. Since we cannot eliminate them, due to the amount of data we have, we'll have to find an ingenious way to deal with them.

For people who have a worse health condition, it has higher medical insurance charges. Unlike those who do not smoke, they usually have a better state of health, as a consequence the insurance charge will be lower.



# Project summary.

## **Approach**

Feature engineering consists of dealing with missing values or outliers. Where an optimal treatment for such data is found, this step is very important for the performance of the model. Since it is the data that we are going to give to train the model.

We decided to separate the data into smokers and non-smokers, with the aim of giving the data a better treatment.

### **Treatment of outliers**

We apply the central limit theorem, which is a technique used to establish confidence intervals. That is, to select values that follow a normal trend, it is usually used to eliminate outliers. But in this case we calculate the upper interval and transform to missing value those values that exceed the established interval.

![age_lm](https://user-images.githubusercontent.com/85312561/177015586-54dafddb-28a5-4b53-b8c0-3c5e87faafbe.png)


As described above, for non-smokers we observed a linear trend with respect to age and position. And I thought why instead of replacing the missing values before, why not create a linear regression model? Train the model with normal values, to later replace the missing values with new values closer to the original value.

They have a significant advantage over replacing it with a basic statistical measure such as the average and the median. Since it could affect the distribution of the data.

For smokers, since there were few outliers, we decided to replace them with normal values close to the highest values, within the normal range.


## **Model Interpretation**

For both models, we use the same variables.
We apply data rescaling process, although for assembly models it is not necessary. Since these algorithms work through decision trees, they use mathematical inequalities.

We do not discriminate any variable, although in the EDA. We found that the variables smoker, age and bmi influence the cost of health insurance.

Although it could eliminate variables such as gender and region. I didn't want to remove it as the difference between humans and algorithms. It is that we take the most important variables, while the algorithms use these variables and complement them with other variables in which they find unknown patterns. They favor the quality of the prediction.

We create 3 regression algorithms:

* **Polynomial Regression:**  It consists of raising the predictor variables to a certain power. In order for the model to have better predictions than a linear regression.


* **Ensemble algorithms:** Gradient Boosting and XGBoost are some algorithms that belong to this category. These algorithms work using weaker algorithms, usually decision trees. That each time they are improving with respect to the learning rate and the number of estimators,one of the main differences is that XGBoost can be executed through a GPU, something that allows faster training. 


For the assembly algorithms, we perform various analyzes.



We use the same parameters for XGBoost and Gradient Boosting.


* **max_depth:**  It refers to the maximum depth of the decision tree. For the first evaluation we use a maximum depth of 2 and in the second of 3.
* **n_estimators:** Number of decision trees. The range of estimators we used was from 100 to 1000.
* **learing_rate:** It is the room for improvement for each iteration. We use a learning rate of 0.01


### **Number of Estimators Gradient Boosting**


![n_estimators_gbr](https://user-images.githubusercontent.com/85312561/176790757-27ead64b-ba03-4842-b98b-987c6f0d78cf.png)




### **Number of Estimators XGBoost**


![xgb_estimators](https://user-images.githubusercontent.com/85312561/176790541-625db0aa-d35b-4f37-9bd0-bb8cb4f68293.png)


### **DataFrame Evualuation**

![df_evaluation](https://user-images.githubusercontent.com/85312561/176791543-faa2d8b6-5f79-47c3-84f0-7f31a1db8b01.png)

* **MSE:** Mean square error. It measures the average error between the original value and the predicted value.

* **R²**  : It measures the degree of adjustment of the predictions with respect to the original value. The closer it is to 1, the closer the original value will be.

* **CV:** Cross Validation consists of calculating the generalization average of the model.

Both models have quite similar metrics. But XGBoost has better results for test data, which is the data that matters to us. Since they are values that the model does not use to train, but it makes good predictions.

### **Graphic Visualization Models.**

![evaluation_plot](https://user-images.githubusercontent.com/85312561/176791917-021c2ae8-229a-4ad1-a922-af9d78040e5d.png)

* **Polynomial Regression**: It gives good predictions for non-smokers, while for smokers it gives moderate estimates.

* **Gradient Boosting**:  It gives good predictions for both groups.

* **XGBoost:**  It has good predictions for both groups. It has a better MSE than Gradient Boosting and is faster when it comes to training. Because it can be trained using GPUs something that will greatly speed up the training.


### **Opening the Black Box**

### **Feature Importance**

![bar_features_xgb](https://user-images.githubusercontent.com/85312561/176793014-40f6ef62-4d39-44c9-b02d-acebc4db2268.png)


![shap_xgb](https://user-images.githubusercontent.com/85312561/176793018-fbd6fad1-f21a-4287-b700-09ec7fc20561.png)

We visualize the degree of importance of the XGboost model.

As we had previously estimated in the EDA. The Smoker variable positively influences the price of the medical insurance charge.

Followed by variables such as age and BMI. What are physical health attributes, such as the variable smoker. It makes sense that the price of the insured is higher when they have a worse health condition.

Variables such as the number of children of the insured, as well as gender and region. They do not have as much relevance compared to the variables that describe the person's health.

However, we leave them, since they can complement the value of the predictions. Since as I mentioned earlier, humans only rely on relevant variables, while machines use these variables and complement them with variables that at first glance can be irrelevant. But that positively impact the value of the prediction.

## **Results**

 The XGBoost model performs extraordinarily well for smokers and non-smokers, unlike the polynomial model that did not give good results for the group of smokers. It also has the advantage of not requiring data rescaling. Since they work based on decision trees that use mathematical inequalities in the form of questions. At the same time, it is a very fast model since it can be trained by dedicated graphics cards. What can I expect from a very powerful algorithm and winner of several Kaggle competitions.





### GIF Proyect

<img src="https://media.giphy.com/media/BileRHL3JLUMtG4vH5/giphy.gif" width=350>

### Link app

https://insurence-app-predict.herokuapp.com/
