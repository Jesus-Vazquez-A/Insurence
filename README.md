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

We first performed an exploratory analysis. Where we discover that the variable smoker has great weight with the value to predict. We conclude that for non-smokers there is a linear relationship with respect to age and position. That is to say that the value increases proportionally with another, for which the conclusion for the subgroup of **non-smokers** can be solved using a **linear regression**. But for **smokers**, this model will **not be as efficient**, since there is no such relationship.

In the feature engineering section.
We divided the dataset into 2 subgroups, the first is for smokers and non-smokers. In order to clean the data more effectively. We calculated an upper range for non-smokers to be $20,000. We filter the data that is not higher than that amount, for the higher data we convert them to null values. 

We observe in a dispersion graph the variable age with respect to charges. Outliers could still be seen. Therefore, we opted to subdivide the subgroup for smokers. Where we create 3 dataframes for the subgroups that we divide between young, adult and elderly people. We replace outliers for these subgroups with normal values. Later we **create a linear regression model**, to **replace the outliers of the variable charges**. For smokers we replace values above $50,000 dollars with normal values.


In the selection of the ideal model. We created 3 regression models, one polynomial, since if we use a linear model it will not help us to describe smokers.

We use assembly models, that is, models that use other weaker models, which in each iteration improves with respect to the learning rate, similar to how an artificial neural network does. We selected Gradient Boosting and XGBoost, these algorithms have the extra advantage that they do not need to rescale variables, unlike the polynomial, which is needed. We perform an evaluation based on the number of estimators with respect to the MSE.

And we conclude that for both models a **maximum depth of 3**leads to more **overfitting** for the **training data**. While with a **maximum depth of 2** it offers **better performance**. Since the **MSE** of the **training** and **validation** are **almost on a par.**

* The **Polynomial** model gives **good results** for **smokers**, while the opposite case the **predictions are not so accurate**.

* **Gradient Boosting** has **good results** for both classes. But it has **more symptoms of overfitting and a higher MSE compared to XGBoost**.

* **XGBoost** for this case was **less susceptible to overfitting**. It offers a **smaller MSE** with a similar number of estimators.

As the penultimate step. We **created the definitive model**, the XGBoost for the reasons already mentioned above. We pass exactly the same parameters to the model. Gives the same results. Finally we save the model, to later use it in a web application.

Finally you **create a web application** with the streamlit library. And we uploaded to a free server in the United States on Heroku, since it favors geographical location.

### GIF Proyect

<img src="https://media.giphy.com/media/BileRHL3JLUMtG4vH5/giphy.gif" width=600>

### Link app

https://insurence-app-predict.herokuapp.com/
