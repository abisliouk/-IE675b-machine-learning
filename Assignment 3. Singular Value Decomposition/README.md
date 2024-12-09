# 3rd Assignment: Singular Value Decomposition

Assignment has been done by pair of students:
- [Elizaveta Nosova](https://github.com/liza-no)
- [Artem Bisliouk](https://github.com/abisliouk)

This assignment focuses on applying Singular Value Decomposition (SVD) to gain insights into matrix approximations, weather data analysis, and clustering tasks. The goal is to understand the role of SVD in dimensionality reduction, data reconstruction, and feature interpretation.

### Research Area
- Singular Value Decomposition (SVD), Dimensionality Reduction, Matrix Approximations, Weather Data Analysis, Clustering, Principal Component Analysis (PCA).

### Tasks

- **Intuition on SVD**:
  - Manually determined the ranks, singular values, and singular vectors of given matrices to develop an intuitive understanding of SVD.
  - Compared manual findings with computational SVD results and discussed the best rank-1 approximations.
  - Investigated the discrepancies in the number of non-zero singular values reported by manual calculations versus NumPy.

- **The SVD on Weather Data**:
  - Normalized the climate dataset to z-scores and verified the assumptions for normalization.
  - Computed the SVD of the normalized data and analyzed the rank.
  - Visualized the first 5 singular vectors on a geographic map and interpreted their significance in terms of longitude, latitude, and climate patterns.
  - Conducted scatterplot analyses of the singular vectors to explore spatial patterns.
  - Evaluated rank selection methods, including Guttman–Kaiser criterion, 90% Frobenius norm, Scree test, and entropy-based methods, to determine the optimal rank for the truncated SVD.
  - Analyzed the root-mean-square error (RMSE) of noisy data reconstruction across various noise levels and ranks.

- **SVD and Clustering**:
  - Performed k-means clustering on the weather data and visualized clusters based on geographical coordinates.
  - Investigated the cluster separability using the first two left singular vectors as positional axes.
  - Reduced the data to 1, 2, and 3 dimensions using PCA derived from SVD and repeated the clustering and visualization steps.
  - Discussed the impact of dimensionality reduction on clustering results and their interpretability.

### Dataset Overview
The weather dataset contains global climate data with features representing temperature, rainfall, and geographic coordinates. Tasks focus on leveraging this data for matrix decomposition, pattern recognition, and clustering.

### Structure

- Assignment [task sheet](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%203.%20Singular%20Value%20Decomposition/assignment03-svd-task-sheet.pdf) 
- Assignment solution [notebook .ipynb](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%203.%20Singular%20Value%20Decomposition/assignment03-svd-solution.ipynb)
- Assignment solution [notebook .pdf with outputs](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%203.%20Singular%20Value%20Decomposition/assignment03-svd-solution.pdf)
- Assignment [report](https://github.com/abisliouk/IE675b-machine-learning/blob/main/Assignment%203.%20Singular%20Value%20Decomposition/assignment03-svd-report.pdf) & Corresponding [LateX project](https://www.overleaf.com/project/673761f569936ca95af0c3f3)
- Resulting [plots](https://github.com/abisliouk/IE675b-machine-learning/tree/main/Assignment%203.%20Singular%20Value%20Decomposition/resulting%20plots)
