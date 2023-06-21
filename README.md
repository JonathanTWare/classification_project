# <a name="top"></a>WHY ARE CUSTOMERS CHURNING
![]()


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___



## <a name="project_description"></a>Project Description:

In this project we will be using the Telco Data Set. Exploring the data, we will find features that are indepent and dependent on churn(using a stats test), in order to run features through a model that will predict whether a customer will churn. The goal is to beat baseline accuracy using one of the three algorythms: KNNeighbor, RandomForest and Logistic Regression.

[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]


### Objective

Find out whether a customer will churn by utilizing three algorythms and running the best scoring algrothym test score.



### Target variable
The target variable of this project is churn.


### Need to haves (Deliverables):
-Need to explore the data.
-Run features through statistical test.
-Select features for modeling
-Run features through 3 different algorythms.



### Nice to haves (With more time):
Further feature explore to see if accuracy can be improved.


***

## <a name="findings"></a>Key Findings:
- The longer a customer has been with the company the less likely they are to churn.
- Being male or female was independent of churn.
- The higher the monthly charges the higher the probability was that the customer has churned.

[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| total_charges | total accumulated charges| float |
| monthly_charges|customers charges monthly | float |
| tenure |months a customer has been with company |int |
| gender_female |customer is or is not female | int |
| gender |sex of customer |  object
| senior_citizen   |customer stats of senior or not senior | int64
| partner  | has partner or does not |  int64
| dependents  |does customer have dependents |  int64
|     phone_service |customer purchsed phone service |    int64
|    multiple_lines |customer has multiple lines |   object
|   online_security |customer signed up for online security |   object
|     online_backup |customer opt in to online backup|   object
| device_protection |customer is enrolled in device protection |   object
|      tech_support |customer opt in for tech support |   object
|      streaming_tv |customer signed up for streaming television |   object
|  streaming_movies |customer signed up for streaming movies |   object
| paperless_billing |enrolled in e-bill |    int64
|           churn   |customer is active or is not active | object
|    contract_type  |service contract customer selected |  object
|internet_service_type |info for what kind of internet service customer chose  |  object
| payment_type | info for customer preffered payment method |  object
| has_churned  | whether a customer has churned |  int64
|multiple_lines_No phone service  |multiple phone lines  | uint8
|                   multiple_lines_Yes  | multiple lines  | uint8
|  online_security_No internet service  | customer doesnt have online security  | uint8
|                  online_security_Yes  | customer has online security  | uint8
|    online_backup_No internet service  | customer does not have online back up  | uint8
|                    online_backup_Yes  | customer has online back up  | uint8
|device_protection_No internet service  | customer does not have device protection  | uint8
|                device_protection_Yes  |  customer does have device protection | uint8
|     tech_support_No internet service  | customer does not have tech support  | uint8
|                     tech_support_Yes  | customer has tech support  | uint8
|     streaming_tv_No internet service  | customer does not have tv streaming  | uint8
|                     streaming_tv_Yes  | customer can stream tv  | uint8
| streaming_movies_No internet service  |  customer cannot stream movies | uint8
|                 streaming_movies_Yes  |customer is able to stream movies   | uint8
|               contract_type_One year  | customer is on a one year contract  | uint8
|               contract_type_Two year  | customer is on a two year contract  | uint8
|    internet_service_type_Fiber optic  | customer has fiber internet  | uint8
|           internet_service_type_None  |  customer does not have internet | uint8
| payment_type_Credit card (automatic)  |  customer pays via credit card | uint8
|        payment_type_Electronic check  | customer pays via e-check  | uint8
|            payment_type_Mailed check  | customer pays with mail-in check  | uint8
**

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 
- dropped unwanted columns.
- created dummies for certain features
- replaced strings with numeric values that needed to be converted


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - prepare.py
    - acquire.py
    


### Takeaways from exploration:
- Four features were chosen for statistical testing: Tenure, Total Charges, Monthly Charges, and Gender.


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: Chi2 Test

The chi-square test is a statistical method used to examine the relationship between categorical variables.

By using the chi-square test, we aim to determine whether there is a significant relationship between the independent variable and the dependent variable. The test helps us assess if the observed frequencies of the categorical variables differ significantly from what we would expect under the assumption of independence.

To perform the chi-square test in Python, we can use the chi2_contingency function from the scipy.stats module. This function takes the individual clusters as input and returns the chi-square statistic (chi2) and the p-value (p). The chi-square statistic represents the ratio of two variances, while the p-value indicates the probability of obtaining test results as extreme as the observed results, assuming the null hypothesis is true.

### Stats Test 2: Independent T-Test
The independent t-test is a statistical method used to examine the association between a categorical variable and a continuous variable.

By using the independent t-test, we aim to determine whether there is a significant association between the both one categorical variable and a continuous variable. 

### Hypothesis

In summary, the hypotheses for the independent t-test and chi2 test can be stated as follows:

Null Hypothesis (H0): Tenure does not have an association with churn.
Alternative Hypothesis (H1): Tenure associated with churn.

### 2nd Hypothesis

Null Hypothesis (H0): Monthly charges is not associated with churn.
Alternative Hypothesis (H1): Monthly charges is associated with churn.

### 3rd Hypothesis

Null Hypothesis (H0): Total charges is not associated with churn.
Alternative Hypothesis (H1): Total charges is associated with churn.

### 4th Hypothesis

Null Hypothesis (H0): Sex is independent of churn.
Alternative Hypothesis (H1): Sex is dependent of churn.

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:

| Feature | P - Value | Less than Alpha|
| ---- | ---- | ---- |
| Tenure | 4.577513863553669e-115 | True |
| Monthly Charges | 1.0736272928972876e-35| True |
| Total Charges | 1.2955473562990627e-34 | True |
| Gender | 1.0 | False |


#### Summary: 
Tenure, Total Charges, and Monthly Charges hold a p-value less than 0.05. Gender has a p-value greater than alpha. We will be using Tenure, Total Charges, and Monthly Charges for our modeling.




***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 

| Model | Train Score | 
| ---- | ---- | 
| Baseline | 0.73 | 

- Selected features to input into models:
    - features = Tenure, Total Charges and Monthly Charges

***

### Models
    
    
#### Model 1:K-Nearest Neighbor(KNN)



##### KNN model had a train accuracy of 82% which was 9% over baseline, a validation score of 78%




### Model 2 : Random Forest(RF)


 
##### RandomForest model had a train accuracy of 81% which was 8% over baseline, a validation score of 78%



### Model 3 : Logistic Regression 


##### Logistic Regression model had a train accuracy of 79% which was 6% over baseline, a validation score of 78%


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Train Score | Validation Score |
| ---- | ----| ---- |
| Baseline | 0.73 | |
| KNN| 0.82 | 0.78 |  
| Random Forest| 0.81 | 0.78|  
| Logistic Regression | 0.79 | 0.78 |  



##### Random Forrest preformed best


## Testing the Model

- Model Testing Results

| Model | Max Depth | Train Score | Validation Score | Test Score |
| ---- | ----| ---- | ---- | ---- |
| KNN| 9 | 0.82 | 0.78| 0.78 |  



***

## <a name="conclusion"></a>Conclusion:

#### Based on the information provided, it seems that the KNN model has the highest train accuracy of 82%, which is 9% over the baseline. 
#### 
#### On the other hand, the RandomForest model has a slightly lower train accuracy of 81%, which is 8% over the baseline. 
#### 
#### The Logistic Regression model has a train accuracy of 79%, which is 6% over the baseline.
#### 
#### Considering all models have the same validation score, KNN was chosen due to the models slight training accuracy advantage.
####
#### After running the KNN model, a test score of 0.78 was given
[[Back to top](#top)]