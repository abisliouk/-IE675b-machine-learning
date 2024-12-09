# 4th Assignment: Latent Variable Models

Assignment has been done by pair of students:
- [Elizaveta Nosova](https://github.com/liza-no)
- [Artem Bisliouk](https://github.com/abisliouk)

In this assignment, we explored Latent Variable Models (LVM), focusing on **Probabilistic PCA (PPCA)** and **Gaussian Mixture Models (GMM)**. The key objective was to implement and analyze different aspects of these models using Python, specifically concentrating on the provided datasets and generator functions.

---

## Research Area
- Latent Variable Models, Probabilistic PCA, Gaussian Mixture Models, MLE, Expectation-Maximization (EM) Algorithm, Scree Plot, Negative Log-Likelihood.

---

## Tasks

### **Probabilistic PCA (PPCA)**
- **Toy Dataset Analysis**:
  - Used the provided `ppca_gen` function to generate a toy dataset. Visualized the dataset and studied the effect of varying noise levels (\( \sigma^2 \)) on the data distribution.

- **MLE for PPCA**:
  - Implemented the Maximum Likelihood Estimation (MLE) for PPCA by completing the `ppca_mle` function. Discussed why \( \hat{\sigma}^2_{\text{MLE}} = 0 \) when the model is fit with \( L = 2 \).

- **Negative Log-Likelihood**:
  - Completed the `ppca_nll` function to compute the conditional negative log-likelihood of a dataset for a given PPCA model. Verified correctness with test cases.

- **Secret Dataset Discovery**:
  - Loaded a secret PPCA dataset and determined the number of latent variables (\( L \)) using:
    - Scree plot analysis.
    - Validation data.
  - Verified consistency of results across methods.

---

### **Gaussian Mixture Models (GMM)**
- **Toy Dataset Analysis**:
  - Used the provided `gmm_gen` function to generate and visualize a toy GMM dataset. Described the characteristics of the dataset.

- **K-Means Clustering**:
  - Performed K-Means clustering on the toy GMM dataset with \( K=5 \). Analyzed and discussed the clustering results, comparing them to expectations.

- **E and M Steps of EM Algorithm**:
  - Implemented the `gmm_e` and `gmm_m` functions to complete the E and M steps of the Expectation-Maximization (EM) algorithm for GMM. Verified correctness by testing the intermediate computations.

- **GMM Clustering**:
  - Fit a GMM model to the toy dataset with \( K=5 \) using the `gmm_fit` function. Assigned each data point to its most likely component and visualized the resulting clustering. Compared the results to those of K-Means.

- **Clustering with Varying \( K \)**:
  - Repeated GMM and K-Means clustering with \( K=4 \) and \( K=6 \), analyzing and comparing the results. Discussed the differences in cluster behavior and boundaries between GMM and K-Means for varying \( K \).

- **Optional Analysis**:
  - Analyzed a secret GMM dataset to determine the number of Gaussian components (\( L \)) used. Justified the findings based on theoretical and experimental observations.

---

## Structure

- Assignment [task sheet](./assignment04-lvm-task-sheet.pdf)
- Assignment solution [notebook .ipynb](./assignment04-solution.ipynb)
- Assignment solution [notebook .pdf with outputs](./assignment04-solution.pdf)
- Assignment [report](./assignment04-report.pdf) & Corresponding [LateX project](https://www.overleaf.com)
- Resulting [plots](./resulting_plots)

---

This assignment provided a comprehensive understanding of latent variable models, particularly focusing on their theoretical foundations and practical implementations. It also emphasized the importance of matrix computations, probabilistic reasoning, and clustering analysis in the context of machine learning.
