# Machine Learning Regression and Classification Examples

This repository contains examples of various regression and classification techniques in machine learning. The examples
use Python and popular libraries such as scikit-learn and seaborn.

## Requirements

Make sure to install the required libraries:

- numpy
- pandas
- scikit-learn
- seaborn
- matplotlib
- statsmodels

## Examples

### 1. Ridge Regression (L2 Regularization)

Example code demonstrating Ridge Regression (L2 regularization) with synthetic data.

[Link to Example](ridge_regression_example.py)

### 2. Lasso Regression (L1 Regularization)

Example code demonstrating Lasso Regression (L1 regularization) with synthetic data.

[Link to Example](lasso_regression_example.py)

### 3. Elastic Net Regression

Example code demonstrating Elastic Net Regression with synthetic data.

[Link to Example](elastic_net_regression_example.py)

### 4. Least Absolute Deviations (LAD) Regression (Quantile Regression)

Example code demonstrating Least Absolute Deviations (LAD) Regression (Quantile Regression) with synthetic data.

[Link to Example](lad_regression_example.py)

### 5. Robust Regression

Example code demonstrating Robust Regression with synthetic data.

[Link to Example](robust_regression_example.py)

### 6. Principal Component Regression (PCR)

Example code demonstrating Principal Component Regression (PCR) with synthetic data.

[Link to Example](pcr_example.py)

### 7. Partial Least Squares (PLS) Regression

Example code demonstrating Partial Least Squares (PLS) Regression with synthetic data.

[Link to Example](pls_regression_example.py)

### 8. Generalized Linear Models (GLM) - Logistic Regression

Example code demonstrating Logistic Regression as a Generalized Linear Model (GLM) with the Iris dataset.

[Link to Example](logistic_regression_example.py)

### 9. Generalized Linear Models (GLM) - Poisson Regression (Not Provided)

Example code demonstrating Poisson Regression as a Generalized Linear Model (GLM) with synthetic data.

[Link to Example](poisson_regression_example.py) - (To be added)

## License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---


to run jupyter:

jupyter notebook

(Use Control-C to stop this server)

----
pip install -r requirements.txt

python -m pip install jupyter

---
memory profile:

@memory_profiler.profile

python -m memory_profiler main.py

---

from line_profiler_pycharm import profile

@profile

python -m line_profiler main.py.lprof > results.txt
