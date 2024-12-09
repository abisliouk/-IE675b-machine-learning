# Outline

This is a repository for the assignments of the [IE675b Machine Learning](https://www.uni-mannheim.de/dws/teaching/course-details/courses-for-master-candidates/ie-675b-machine-learning/) course at the University of Mannheim.

The assignments focus on core machine learning concepts, algorithms, and their implementation in Python, with a strong emphasis on model training, evaluation, and analysis. Each assignment is organized into its own directory, containing code, reports, and visualizations to aid in understanding the various techniques and models applied.

## Assignments Overview

### 1st Assignment: Naive Bayes
In this assignment, we implemented a Naive Bayes classifier with a focus on classification using the MNIST dataset. Key components include:
- Training the Naive Bayes model using a Dirichlet prior with MAP estimation.
- Evaluating the model's accuracy and analyzing performance using a confusion matrix.
- Conducting experiments with model selection, data generation, and handling missing data.
  
For more details, see the full [README for Assignment 1](./Assignment%201.%20Naive%20Bayes/README.md).

### 2nd Assignment: Logistic Regression
This assignment involves logistic regression, using both MLE and MAP estimation techniques on the Spambase dataset. The main highlights include:
- Training logistic regression models with different regularization settings.
- Exploring the effects of regularization on feature importance and model interpretability.
- Comparing gradient descent and stochastic gradient descent approaches for optimization.

For more details, see the full [README for Assignment 2](./Assignment%202.%20Logistic%20Regression/README.md).

### 3rd Assignment: Singular Value Decomposition (SVD)
In this assignment, we explored the application of Singular Value Decomposition (SVD) in dimensionality reduction. Major focus areas include:
- Implementing the SVD algorithm and validating its functionality.
- Applying SVD for dimensionality reduction on high-dimensional datasets.
- Analyzing reconstruction errors and understanding the trade-off between dimensionality and performance.

For more details, see the full [README for Assignment 3](./Assignment%203.%20Singular%20Value%20Decomposition/README.md).

### 4th Assignment: Latent Variable Models (LVM)
This assignment investigates two major latent variable models: Probabilistic PCA (PPCA) and Gaussian Mixture Models (GMM). Key tasks include:
- **Probabilistic PCA**:
  - Generating and visualizing datasets with varying noise levels and analyzing the impact on data distribution.
  - Implementing MLE for PPCA and exploring the relationship between latent variables and noise.
  - Discovering the number of latent variables in a secret PPCA dataset using scree plots and validation data.
- **Gaussian Mixture Models**:
  - Generating toy datasets and performing K-Means clustering as a baseline for comparison.
  - Implementing the Expectation-Maximization algorithm for fitting GMMs using MLE.
  - Evaluating clustering results and comparing with K-Means for different numbers of components.

For more details, see the full [README for Assignment 4](./Assignment%204.%20Latent%20Variable%20Models/README.md).

## Repository Structure

- **Assignment 1**: [Naive Bayes Classifier](./Assignment%201.%20Naive%20Bayes/)
- **Assignment 2**: [Logistic Regression](./Assignment%202.%20Logistic%20Regression/)
- **Assignment 3**: [Singular Value Decomposition (SVD)](./Assignment%203.%20Singular%20Value%20Decomposition/)
- **Assignment 4**: [Latent Variable Models (LVM)](./Assignment%204.%20Latent%20Variable%20Models/)

Each assignment folder includes:
- Task sheet
- Jupyter notebooks with code and outputs
- LaTeX report and corresponding visualizations
