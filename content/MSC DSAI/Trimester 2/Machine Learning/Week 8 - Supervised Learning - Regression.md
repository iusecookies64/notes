
---
## **START: INTRODUCTION TO REGRESSION**
---

### Defining Regression
Regression is a fundamental statistical method and a branch of **supervised learning**. In supervised learning, a model learns from a labeled dataset consisting of input features ($X$) and corresponding target labels ($Y$). The specific goal of regression is to find the underlying mathematical relationship or mapping between $X$ and $Y$ to predict outcomes for new, unseen data.

Unlike classification, where the output is categorical (e.g., "Spam" or "Not Spam"), regression focuses on predicting **continuous numerical values**.

### Regression vs. Classification
While both are supervised learning tasks, they differ significantly in the nature of their output:

| Feature | Classification | Regression |
| :--- | :--- | :--- |
| **Output Type** | Discrete / Categorical. | Continuous / Numerical. |
| **Output Values** | Finite and fixed (e.g., Cat, Dog, Fish). | Infinite possible values (e.g., 100.5, 101.2). |
| **Goal** | Assign a class label. | Predict a specific quantity. |
| **Examples** | Email spam filters, Image recognition. | House price prediction, Stock market value. |

### Key Components of Regression
To build a regression model, we utilize several key elements:
* **Training Set:** A collection of historical data containing both features and the actual target values used to "teach" the model.
* **Features ($X$):** The independent variables or "questions" (e.g., square footage, number of bedrooms).
* **Target ($Y$):** The dependent variable or "answer" we want to predict (e.g., price).
* **Hypothesis Function ($H(x)$ or $F(x)$):** The mathematical model that represents the relationship between features and the target.

### The Linear Hypothesis Function
A linear regression model assumes that the relationship between the input and output is a straight line. In its simplest form (single feature), the hypothesis function is expressed as:

$$h_{\theta}(x) = \theta_0 + \theta_1x$$

Where:
* **$\theta_0$ (Theta zero):** The **y-intercept**, representing the value of $y$ when $x$ is zero.
* **$\theta_1$ (Theta one):** The **slope**, representing the rate of change in $y$ for every unit change in $x$.
* **$\theta$ (Parameters/Weights):** These are the values the learning algorithm must "tune" to find the line that best fits the data with the **minimum error**.

### Multivariate Regression
In real-world scenarios, a target is rarely dependent on just one feature. For example, a house's price depends on area, location, and the number of floors. When we have multiple input features ($x_1, x_2, x_3, \dots, x_n$), we use **Multivariate Regression**.

The hypothesis function expands to accommodate these extra dimensions:
$$h_{\theta}(x) = \theta_0 + \theta_1x_1 + \theta_2x_2 + \dots + \theta_nx_n$$

In a 2D feature space, this relationship is visualized not as a line, but as a **response plane**. In higher dimensions, it is referred to as a **hyperplane**. The objective remains the same: identify the best set of parameters ($\theta$) that fits the multidimensional data points with the least possible error.

---
## **END: INTRODUCTION TO REGRESSION**
---

---
## **START: THE COST FUNCTION FOR LINEAR REGRESSION**
---

### The Need for a Cost Function
In linear regression, we use a hypothesis function $h_{\theta}(x) = \theta_0 + \theta_1x$ to represent our model. The challenge lies in finding the "best" values for the parameters $\theta_0$ (intercept) and $\theta_1$ (slope). A **Cost Function** (also known as a Loss or Error function) is a mathematical formula that measures how well our model's predictions match the actual data. It serves as a penalty for incorrect predictions; the higher the cost, the worse the model's fit.

### Residual Error and the Vertical Distance
For any given data point, the difference between the **Actual Value** ($y$) and the **Predicted Value** ($\hat{y}$) is the error, often called the **residual**. Visually, this is the vertical distance between a data point and the regression line.

### Why Sum of Squared Errors (SSE)?
While we could simply sum up the errors ($y - \hat{y}$), this is a "bad idea" because positive and negative errors can cancel each other out, potentially resulting in a total error of zero even for a poorly fitted model. To solve this, we use the **Sum of Squared Errors**:

1.  **Eliminates Signs:** Squaring ensures all errors are positive.
2.  **Magnifies Large Errors:** Larger deviations are penalized more heavily due to the squaring term.
3.  **Differentiability:** The squared function is a smooth, differentiable curve, which is essential for optimization algorithms like Gradient Descent.

### Mean Squared Error (MSE)
To find the average error across all $m$ training examples, we use the **Mean Squared Error (MSE)**. This is the standard cost function for linear regression, denoted as $J(\theta_0, \theta_1)$.

The mathematical formulation is:
$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)})^2$$

> **Note:** The $2$ in the denominator ($2m$) is added for mathematical convenience during calculus (to cancel out the power of 2 when taking the derivative).

### Visualizing the Cost Function
The cost function can be visualized depending on the number of parameters we are optimizing:

* **One Parameter:** If we fix $\theta_0$ and only vary the slope $\theta_1$, the cost function $J(\theta_1)$ forms a 2D **parabola**. The goal is to find the value of $\theta_1$ at the very bottom of this curve.
* **Two Parameters:** When optimizing both $\theta_0$ and $\theta_1$, the cost function becomes a 3D surface. For linear regression, this surface is a **convex bowl-shaped function**. 

### Optimization Objective
The ultimate objective of our learning algorithm is to **minimize $J(\theta_0, \theta_1)$**. We want to find the specific coordinates $(\theta_0, \theta_1)$ that land us at the global minimum (the bottom-most point) of the "bowl." 

There are two primary ways to reach this minimum:
1.  **Closed-form Solution:** Solving the math directly.
2.  **Iterative Solution:** Gradually stepping down the curve using algorithms like **Gradient Descent**.

---
## **END: THE COST FUNCTION FOR LINEAR REGRESSION**
---

---
## **START: OPTIMISATION WITH GRADIENT DESCENT**
---

### The Intuition Behind Gradient Descent
Gradient Descent is an iterative optimization algorithm used to minimize the cost function $J(\theta_0, \theta_1)$. The goal is to find the values of $\theta_0$ and $\theta_1$ that result in the lowest possible error.

A common analogy is standing on a hillside in a thick fog. Your goal is to reach the bottom of the valley (the global minimum) as quickly as possible. Since you cannot see the path, you feel the slope of the ground under your feet and take a step in the direction of the steepest descent. You repeat this process until you reach a point where the ground is flat, signifying you have reached the minimum.

### The Gradient Descent Algorithm
The algorithm starts with random initial values for $\theta_0$ and $\theta_1$ and updates them repeatedly using the following formula:

$$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta_0, \theta_1)$$

Where:
* **$:=$** denotes an assignment operator (updating the value).
* **$\alpha$ (Alpha):** The **Learning Rate**, which determines the size of the step we take.
* **$\frac{\partial}{\partial \theta_j} J(\theta_0, \theta_1)$:** The **Partial Derivative** (Gradient), which represents the slope of the cost function at the current point.

### The Role of the Learning Rate ($\alpha$)
The learning rate is a crucial hyperparameter that dictates the efficiency of the optimization:
* **Too Small $\alpha$:** The algorithm will take tiny steps, making the convergence extremely slow and computationally expensive.
* **Too Large $\alpha$:** The algorithm might overstep the minimum, leading to "ping-pong" behavior where the values oscillate or even diverge away from the bottom.

### Direction of Movement
The partial derivative tells us the direction of the slope:
* **Positive Slope:** The derivative is positive. Subtracting this value moves $\theta$ to the left (down the hill).
* **Negative Slope:** The derivative is negative. Subtracting a negative value (adding) moves $\theta$ to the right (down the hill).

### Simultaneous Update Rule
To ensure the algorithm descends correctly toward the global minimum, all parameters must be updated **simultaneously**. This means we calculate the gradients for both $\theta_0$ and $\theta_1$ using the current values before updating either of them. Updating one and then using that new value to calculate the gradient for the second is incorrect and leads to skewed results.

### Convergence
We repeat the update process until **convergence**, which is the point where the cost function no longer decreases significantly with further iterations. At this point, the partial derivative is nearly zero, indicating the model has found the optimal parameters for the linear regression line.

---
## **END: OPTIMISATION WITH GRADIENT DESCENT**
---