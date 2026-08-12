
---
## **START: INTRODUCTION TO HIERARCHICAL CLUSTERING**
---

### Comparison with K-Means Clustering
K-Means is a partition-based, hard clustering algorithm that requires the number of clusters $k$ to be specified as an input parameter a priori. The quality of the resulting clusters is highly dependent on this value; an incorrect $k$ leads to poor quality clusters that do not represent the natural groupings within the data. While natural clusters are easily visualized in two dimensions, high-dimensional data (e.g., 100 or 500 dimensions) makes manual identification of $k$ impossible.

### Methods for Finding the Optimal K in K-Means
Since K-Means cannot identify the optimal number of clusters on its own, two primary approaches are used:

* **Domain Expertise:** A human expert with knowledge of the specific field (e.g., market segmentation) determines an actionable or logical value for $k$.
* **Heuristic Methods (Elbow Method):** This involves running the algorithm multiple times with different values of $k$ and plotting the Total Sum of Squared Error (SSE) against $k$. 
    * As $k$ increases, the SSE naturally decreases. 
    * When $k$ equals the number of data points $n$, the SSE becomes zero because each point is its own centroid.
    * The "Elbow" represents the point of diminishing returns where the SSE drop transitions from drastic to marginal. This inflection point suggests a good candidate for $k$, though it is not a mathematical guarantee of the absolute optimal value.

### Fundamentals of Hierarchical Clustering
Unlike K-Means, hierarchical clustering does not require the number of clusters to be specified upfront. It produces a nested structure of clusters organized in a hierarchy, similar to a taxonomic tree.

This method is particularly useful in domains where data naturally follows a multi-level structure, such as biological classifications or geographical divisions (e.g., Earth → Continents → Countries → States).

### The Dendrogram
The primary output of hierarchical clustering is the **Dendrogram**, a tree-like diagram that records the sequences of merges or splits.

* **X-axis:** Represents the individual data points or clusters.
* **Y-axis:** Represents a measure of error or "distance" between clusters, such as SSE, diameter, radius, or general dissimilarity.
* **Functionality:** By "cutting" the dendrogram horizontally at different heights (error levels), one can obtain different numbers of clusters. This flexibility allows a domain expert to decide the most meaningful level of granularity after the algorithm has run.

### Types of Hierarchical Clustering
There are two broad strategies for building the cluster hierarchy:

#### Agglomerative Clustering (Bottom-Up)
This is the most common approach. It begins with every individual data point as its own cluster. The algorithm iteratively merges the two most similar clusters based on a proximity metric. This process continues until all points are merged into a single root cluster containing the entire dataset.

#### Divisive Clustering (Top-Down)
This approach begins with all data points in one single cluster. The algorithm iteratively splits the most heterogeneous clusters into smaller sub-clusters based on dissimilarity. This continues until every data point resides in its own individual cluster.

---
## **END: INTRODUCTION TO HIERARCHICAL CLUSTERING**
---

---
## **START: DIVISIVE AND AGGLOMERATIVE CLUSTERING**
---

### Introduction to Divisive Clustering
Hierarchical clustering can be approached in two ways: **Agglomerative** (bottom-up), where individual points are merged into a single root, and **Divisive** (top-down), where one large cluster is iteratively split. Divisive clustering begins with a single cluster containing all data points and uses a notion of dissimilarity to break it into smaller groups until the desired granularity is reached.

### Bisecting K-Means Algorithm
The most popular divisive clustering algorithm is **Bisecting K-Means**. It essentially treats the hierarchical problem as a series of partitioning tasks using the K-Means algorithm.

#### Step-by-Step Procedure:
1.  **Initialization:** Start with all data points in a single cluster $C$.
2.  **Selection:** Choose a cluster to split. In the initial step, there is only one. In subsequent steps, the cluster with the **highest Sum of Squared Error (SSE)** is typically selected for splitting to reduce overall variance.
3.  **Bisect:** Apply K-Means with $k=2$ to the selected cluster, splitting it into two smaller sub-clusters.
4.  **Iteration:** Repeat the selection and bisection process until every data point is in its own cluster (forming a full dendrogram) or a predefined stopping criterion is met.

### Strengths of Bisecting K-Means
* **No A Priori K:** Unlike standard K-Means, it does not require a fixed $k$ at the start. One can build the entire hierarchy and then decide where to "cut" the dendrogram based on the specific requirements of the domain (e.g., at the continent level or country level).
* **Natural Hierarchy:** It is well-suited for datasets that possess an inherent hierarchical structure, such as biological taxonomies or document classifications.
* **Efficiency:** It is often more efficient than some agglomerative methods when only a small number of clusters are needed, as it starts from the top.

### Weaknesses and Limitations
#### Computational Complexity
The time complexity of a single K-Means run is generally represented as $O(I \cdot k \cdot n \cdot d)$, where $I$ is iterations, $k$ is clusters, $n$ is points, and $d$ is dimensions. Since Bisecting K-Means runs K-Means repeatedly with $k=2$, its complexity is tied to the height of the tree, which is roughly $\log k$ in a balanced scenario.

#### Greedy Strategy and Local Optima
A significant drawback of this approach is its **greedy nature**. The algorithm makes the best local split at each step but cannot "undo" a split once it has been made.
* **Irreversibility:** Once two points are separated into different clusters at a higher level of the tree, they can never be merged back together.
* **Suboptimal Solutions:** Because it lacks a merging mechanism, the algorithm may split a natural cluster into two if the SSE criteria forces it, leading to a local optima rather than a globally optimal clustering of the data. 

---
## **END: DIVISIVE AND AGGLOMERATIVE CLUSTERING**
---

---
## **START: AGGLOMERATIVE CLUSTERING**
---

### Introduction to Agglomerative Clustering
Agglomerative clustering is a **bottom-up** hierarchical clustering approach. Unlike divisive methods that split clusters, agglomerative clustering begins with the most granular representation of the data and builds a hierarchy through successive merging.

### Step-by-Step Algorithm
1.  **Initialization:** Treat each data point as an individual cluster. If there are $n$ data points, the process starts with $n$ clusters.
2.  **Proximity Matrix Calculation:** Compute a proximity (similarity or distance) matrix that stores the distance between every pair of clusters.
3.  **Iterative Merging:**
    * Identify the two most similar clusters based on the proximity matrix.
    * Merge these two clusters into a single new cluster.
    * **Update the Proximity Matrix:** Recompute the distances between the newly formed cluster and all other existing clusters.
4.  **Termination:** Repeat the merging and updating steps until only one large cluster containing all data points remains.

### Proximity Matrix and Updates
The proximity matrix is an $n \times n$ matrix where each cell $(i, j)$ represents the distance between cluster $i$ and cluster $j$. Initially, when each cluster is a single point, this is simply the distance between points (e.g., Euclidean distance).
When two clusters, $C_i$ and $C_j$, are merged into $C_{new}$, the matrix must be updated. The rows and columns for $C_i$ and $C_j$ are removed and replaced with a single row and column for $C_{new}$. The values in this new row/column depend on the chosen **Linkage Criteria**.

### Linkage Criteria (Inter-cluster Similarity)
Linkage criteria define how the distance between two clusters (containing multiple points) is measured. The choice of linkage significantly impacts the shape and structure of the resulting hierarchy.

#### 1. Single Linkage (MIN)
The distance between two clusters is defined as the **minimum** distance between any single point in the first cluster and any single point in the second cluster.
* **Strength:** Can identify non-elliptical, complex shapes (continuity-based).
* **Weakness:** Susceptible to the **Chaining Effect**, where a thin line of points (or noise) can bridge two distinct clusters. It is highly sensitive to outliers.

#### 2. Complete Linkage (MAX)
The distance between two clusters is defined as the **maximum** distance between any point in the first cluster and any point in the second cluster.
* **Strength:** Avoids chaining and is less sensitive to noise. It tends to produce compact, globular clusters.
* **Weakness:** May break apart large, naturally occurring clusters to satisfy the "compactness" constraint.

#### 3. Group Average Linkage
The distance is the **average** of all pairwise distances between the points in the two clusters. This provides a compromise between the extremes of Single and Complete linkage.

#### 4. Centroid Linkage
The distance between two clusters is defined as the distance between their respective **centroids** (the mean point of the cluster).

#### 5. Ward’s Method
Ward’s method is similar to K-Means in its objective. It defines the similarity between two clusters based on the **increase in the Sum of Squared Error (SSE)** that would result from merging them. The algorithm chooses to merge the two clusters that lead to the smallest possible increase in total variance.

### Comparison Summary
| Method | Proximity Definition | Cluster Shape | Noise Sensitivity |
| :--- | :--- | :--- | :--- |
| **Single Link (MIN)** | Closest pair of points | Non-globular / Chained | High |
| **Complete Link (MAX)** | Farthest pair of points | Globular / Compact | Low |
| **Group Average** | Average of all pairs | Balanced | Low |
| **Ward's Method** | Minimum increase in SSE | Globular | Low |

### Computational Complexity
* **Space Complexity:** $O(n^2)$ is required to store the proximity matrix.
* **Time Complexity:** * The basic implementation is $O(n^3)$ because there are $n$ steps of merging, and in each step, we must search the $n \times n$ matrix for the minimum distance.
    * With optimized data structures (like priority queues), this can be reduced to $O(n^2 \log n)$.
    * Due to this high complexity, agglomerative clustering is often difficult to scale to very large datasets.

---
## **END: AGGLOMERATIVE CLUSTERING**
---