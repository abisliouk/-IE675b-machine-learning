# 4th Assignment: Latent Variable Models

Assignment has been done by a pair of students:
- [Elizaveta Nosova](https://github.com/liza-no)
- [Artem Bisliouk](https://github.com/abisliouk)

This assignment focuses on the implementation and analysis of latent variable models, specifically Probabilistic Principal Component Analysis (PPCA) and Gaussian Mixture Models (GMM). The primary objective is to explore model training, performance evaluation, and clustering techniques using the provided toy datasets and secret datasets.

### Research Area
- Probabilistic Principal Component Analysis (PPCA), Gaussian Mixture Models (GMM), Maximum Likelihood Estimation (MLE), Scree Plot Analysis, Clustering, K-Means, Expectation-Maximization (EM) Algorithm, Conditional Negative Log-Likelihood.

### Tasks

- **Probabilistic PCA**:
  - **Dataset Generation and Analysis**:
    - Explored the PPCA generator to produce and visualize a toy PPCA dataset.
    - Analyzed how varying noise levels (\( \sigma^2 \)) affected the data distribution and visualization.
  - **MLE Implementation**:
    - Completed the `ppca_mle` function to implement Maximum Likelihood Estimation for PPCA.
    - Investigated why \( \hat{\sigma}^2_{\text{MLE}} = 0 \) when \( L = 2 \) for the toy PPCA dataset.
  - **Conditional Negative Log-Likelihood**:
    - Implemented the computation of conditional negative log-likelihood for a dataset given a PPCA model by completing the `ppca_nll` function.
  - **Latent Variables Discovery**:
    - Analyzed the secret PPCA dataset using scree plot analysis and validation data to determine the number of latent variables (\( L \)).
    - Compared results from both methods for consistency.

- **Gaussian Mixture Models**:
  - **Dataset Generation and Visualization**:
    - Studied the GMM generator to produce and visualize a toy GMM dataset.
  - **K-Means Clustering**:
    - Performed K-Means clustering with \( K = 5 \) on the toy GMM dataset and analyzed the results.
  - **EM Algorithm Implementation**:
    - Implemented the E-step and M-step for GMM fitting via MLE by completing the `gmm_e` and `gmm_m` functions.
  - **Model Fitting and Comparison**:
    - Fit the GMM model with \( K = 5 \) and visualized the clustering results.
    - Compared GMM-based clustering with K-Means clustering results.
  - **Exploration of Different Cluster Sizes**:
    - Repeated GMM fitting and clustering with \( K = 4 \) and \( K = 6 \), performing multiple runs to discuss the findings.


### Dataset Overview
The assignment involves the use of toy datasets generated for PPCA and GMM models, as well as secret datasets for advanced analysis. Key aspects include:
- **PPCA Dataset**:
  - Generated with varying noise levels to study distributional effects.
  - Secret dataset used for latent variable discovery.
- **GMM Dataset**:
  - Includes toy data for visualization and clustering experiments.
  - Secret dataset used for discovering the number of components.

### Structure

- Assignment [task sheet](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%204.%20Latent%20Variable%20Models/assignment04-lvm-task-sheet.pdf) 
- Assignment solution [notebook .ipynb](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%204.%20Latent%20Variable%20Models/assignment04-lvm-solution.ipynb)
- Assignment solution [notebook .pdf with outputs](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%204.%20Latent%20Variable%20Models/assignment04-lvm-solution.pdf)
- Assignment [report](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%204.%20Latent%20Variable%20Models/assignment04-lvm-report.pdf) & Corresponding [LateX project](https://www.overleaf.com/project/6751690c1f9d2afa75a91eed)
- Resulting [plots](https://github.com/abisliouk/IE675b-machine-learning/tree/main/Assignment%204.%20Latent%20Variable%20Models/resulting%20plots)
