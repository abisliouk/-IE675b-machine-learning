# 2nd Assignment: Logistic Regression

Assignment has been done by pair of students:
- [Elizaveta Nosova](https://github.com/liza-no)
- [Artem Bisliouk](https://github.com/abisliouk)

This assignment involves implementing and analyzing logistic regression with both Maximum Likelihood Estimation (MLE) and Maximum Aposteriori Estimation (MAP), using the Spambase dataset for spam email detection. The primary objective is to explore the impact of different regularization strategies and preprocessing steps on model performance and interpretability.

### Research Area
- Logistic Regression, Maximum Likelihood Estimation (MLE), Maximum Aposteriori Estimation (MAP), Gaussian Prior, Regularization (L2), Gradient Descent, Stochastic Gradient Descent (SGD), Feature Importance, Normalization.

### Tasks

- **Dataset Statistics**:
  - Implemented kernel density plots for each feature in the dataset to examine distributions and identify potential outliers.
  - Normalized the dataset to have mean 0 and variance 1, then re-plotted kernel density distributions to compare changes post-normalization.

- **Logistic Regression with MLE**:
  - Derived analytical expressions to demonstrate that rescaling and shifting features do not alter MLE estimates when a bias term is used.
  - Completed the `log_likelihood` and `gradient` functions to compute the log-likelihood and gradient for logistic regression.
  - Implemented gradient descent (GD) for logistic regression, with the option to vectorize epochs for enhanced computational efficiency.
  - Extended the implementation to support stochastic gradient descent (SGD) and compared the behavior of both methods.

- **Prediction and Feature Analysis**:
  - Developed prediction functions to compute probabilities and classify labels using logistic regression.
  - Analyzed the learned weight vector to assess feature importance, identifying features most and least relevant to spam detection.

- **Logistic Regression with MAP**:
  - Implemented MAP estimation using a Gaussian prior (L2 regularization), modifying the gradient descent function to incorporate the regularization term.
  - Investigated the effect of varying the regularization parameter \(\lambda\) on training and test log-likelihoods, as well as prediction accuracy.
  - Examined the impact of \(\lambda\) on the weight vector, discussing the effects of strong priors on feature importance and model interpretability.
 

### Dataset Overview
The Spambase dataset consists of 4601 emails, each labeled as either spam (1) or non-spam (0). Each example has 57 features:
- **48 word frequency features** (percentage occurrences of specific words in the email)
- **6 character frequency features** (percentage occurrences of certain characters)
- **3 uppercase letter sequence features** (related to length statistics of uppercase letter sequences)

The dataset is split into:
- **Training Set:** 3065 examples
- **Test Set:** 1536 examples


### Structure

- Assignment [task sheet](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%202/assignment02-task-sheet.pdf) 
- Assignment solution [notebook .ipynb](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%202/assignment02-solution.ipynb)
- Assignment solution [notebook .pdf with outputs](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%202/assignment02-solution.pdf)
- Assignment [report](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%202/assignment02-report.pdf) & Corresponding [LateX project](https://www.overleaf.com/project/670aec2240f8d8bbf5ceff97)
- Resulting [plots](https://github.com/abisliouk/IE675b-machine-learning/tree/main/Assignment%202/resulting%20plots)




