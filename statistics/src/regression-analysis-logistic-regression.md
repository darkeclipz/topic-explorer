---
title: Logistic Regression
---

[Back to index](index.html)

---
# Regression Analysis
## Logistic Regression

Logistic regression is a statistical method used for binary classification problems, where the goal is to predict the probability that an observation belongs to one of two classes. Unlike linear regression, which predicts a continuous outcome, logistic regression predicts a binary outcome, often coded as 0 and 1.

Here's a detailed explanation of logistic regression:

### Basics of Logistic Regression:
1. **Binary Dependent Variable:**
   - The dependent variable in logistic regression is binary, meaning it has two possible outcomes (e.g., success/failure, yes/no, 1/0).
   
2. **Logistic Function (Sigmoid Function):**
   - Logistic regression uses the logistic function (also known as the sigmoid function) to model the probability of the dependent variable. The logistic function is defined as:
   \[
   \sigma(z) = \frac{1}{1 + e^{-z}}
   \]
   where \( z \) is the linear combination of the predictors.

3. **Model Equation:**
   - The model equation for logistic regression is similar to that of linear regression but transformed via the logistic function:
   \[
   P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_kX_k)}}
   \]
   Here:
   - \( P(Y=1|X) \) is the probability that the dependent variable \( Y \) equals 1 given the predictors \( X \).
   - \( \beta_0 \) is the intercept.
   - \( \beta_1, \beta_2, ..., \beta_k \) are the coefficients of the predictors \( X_1, X_2, ..., X_k \).

4. **Odds and Log-Odds:**
   - The odds of an event occurring is the ratio of the probability that the event occurs to the probability that it does not occur:
   \[
   \text{Odds} = \frac{P(Y=1|X)}{1 - P(Y=1|X)}
   \]
   - Logistic regression models the log-odds (also called logit):
   \[
   \log\left(\frac{P(Y=1|X)}{1 - P(Y=1|X)}\right) = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_kX_k 
   \]

### Key Steps in Logistic Regression:
1. **Collect Data:**
   - Gather a dataset containing the binary dependent variable and independent variables (predictors).

2. **Fit the Model:**
   - Estimate the coefficients \( \beta_0, \beta_1, ..., \beta_k \) using techniques like maximum likelihood estimation (MLE).

3. **Evaluate the Model:**
   - Assess the model's performance using metrics such as the confusion matrix, accuracy, precision, recall, F1-score, and the area under the ROC curve (AUC).

4. **Interpret the Coefficients:**
   - Coefficients indicate the change in the log-odds of the dependent variable for a one-unit change in the predictor variable, holding other variables constant.

### Assumptions of Logistic Regression:
1. **Linearity:**
   - Assumes a linear relationship between the log-odds of the dependent variable and the independent variables.
   
2. **Independence:**
   - Observations should be independent of each other.
   
3. **No Multicollinearity:**
   - Predictors should not be highly correlated with each other.

4. **Large Sample Size:**
   - Logistic regression generally requires a large sample size to provide reliable results, especially when the event of interest is rare.

### Applications of Logistic Regression:
- Medical Diagnosis: Predicting the presence or absence of a disease.
- Marketing: Customer churn prediction.
- Finance: Predicting loan default.

Logistic regression is a powerful and widely used tool for binary classification problems, providing interpretable results that can guide decision-making in various fields.

---
[Back to index](index.html)
