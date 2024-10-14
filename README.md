# Outline

This is a repository for the assignments of the IE675b Machine Learning course at the University of Mannheim.

## 1st Assignment: Naive Bayes

Assignment has been done by pair of students:
- [Elizaveta Nosova](https://github.com/liza-no)
- [Artem Bisliouk](https://github.com/abisliouk)

In this assignment, we explored the implementation of Naive Bayes for classification using the MNIST dataset. The main focus was on implementing key functions related to training, prediction, and experimentation with the Naive Bayes model, particularly on categorical data.

### Research Area
- Naive Bayes, Dirichlet Prior, MAP Estimation, Multinomial Distribution, Confusion Matrix, Cross-Validation.

### Tasks

- **Training a Naive Bayes Classifier**:
  - Implemented the `nb_train` function that trains a Naive Bayes classifier for categorical data using a symmetric Dirichlet prior and maximum a posteriori (MAP) estimates.
  - Tested the implementation with various priors, including uniform Dirichlet prior (α = 1) and add-one smoothing (α = 2).
  - Trained the model on the MNIST dataset for the classification of hand-written digits, with the features being the pixel intensity values.

- **Prediction using Naive Bayes**:
  - Developed the `nb_predict` function to predict labels for unseen examples and compute log probabilities for each predicted label.
  - Tested and validated the predictions on both small examples and the MNIST test set.

- **Experiments on the MNIST Digits Data**:
  - Trained the Naive Bayes classifier with α = 2 on the full MNIST training dataset and evaluated its accuracy on the test set.
  - Visualized the results by plotting the test digits and the corresponding predicted labels.
  - Computed and analyzed the confusion matrix to assess the classification performance and identified common misclassifications.

- **Model Selection (Optional)**:
  - Conducted cross-validation to tune the hyperparameter α, identifying an optimal value for the Dirichlet prior.
  - Plotted accuracy as a function of α and discussed the impact of different values of α on the model’s performance.

- **Generating Data**:
  - Implemented the `nb_generate` function to generate synthetic digits for each class using the trained Naive Bayes model.
  - Generated digits for various values of α, compared the results, and discussed the influence of α on the generated samples.
  
- **Handling Missing Data**:
  - Analyzed the classification problem with missing features and derived key formulas for the following distributions:
    - `p(y|x_{1:D})`
    - `p(y|x_{1:D'})` for `1 ≤ D' < D`
    - `p(x_{D'+1:D}|x_{1:D'})` for `1 ≤ D' < D`
  - Discussed how these distributions can be used in practice and the challenges associated with missing data in Naive Bayes classification.
  
### Structure

- Assignment [task sheet](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%201/assignment01-task-sheet.pdf) 
- Assignment solution [notebook .ipynb](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%201/assignment01-notebook.ipynb)
- Assignment solution [notebook .pdf with outputs](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%201/assignment01-notebook.pdf)
- Assignment [report](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%201/assignment01-report.pdf) & Corresponding [LateX project](https://www.overleaf.com/project/670aec2240f8d8bbf5ceff97)
- Resulting [plots](https://github.com/abisliouk/IE675b-machine-learning/tree/main/Assignment%201/resulting%20plots)
