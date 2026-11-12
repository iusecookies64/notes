# 1. Deep Learning vs. Traditional Machine Learning

Before we dive into how neural networks are trained, we need to answer a more basic question: *why do we bother with deep learning at all?* Classical machine learning already solves a great many problems, so what went wrong with it, and what exactly does deep learning change? In this section we first look at where traditional machine learning struggles, then at the central idea that deep learning brings (learning the features themselves), and finally at the theory that explains why stacking layers is such a powerful way to build functions.

## 1.1 Limitations of Traditional Machine Learning

Traditional machine learning works remarkably well in many settings, and the lecture is careful to say so. The trouble is that three recurring weaknesses showed up as people tried to apply it to harder, messier problems. We will take them one at a time.

### Manual Feature Engineering and Domain Dependency

In a classical pipeline, the model never sees the raw data directly. A human first decides *which* quantities describe each example, and only then is a learning algorithm fitted on those quantities. Formally, if the raw data live in some space $\mathcal{X}$ and the targets live in $\mathcal{Y}$, the pipeline is a composition of two stages:

$$
\mathcal{X} \xrightarrow{\ \phi(\cdot)\ } \mathbb{R}^d \xrightarrow{\ f_\theta\ } \mathcal{Y}
$$

Here $\phi(\cdot)$ is a **hand-crafted feature extractor** that turns a raw object into a vector of $d$ numbers, and $f_\theta$ is the learnable model (a linear model, a tree ensemble, a kernel machine, and so on) with parameters $\theta$. The important point is that only $f_\theta$ is learned from data. The map $\phi(\cdot)$ is fixed in advance by a person.

Why is this a problem? Because designing $\phi(\cdot)$ requires knowing the domain. In healthcare you must know which clinical biomarkers matter; in banking you might engineer quantities such as transaction velocity ratios; in telecom you might aggregate tenure and contract information into summary columns. In the lecture's words, you need to understand whatever industry you work in, use that knowledge to decide which features to create or fetch, and then manually check that all the necessary features are present. Three difficulties follow from this:

- **Labour cost:** feature design is slow, iterative, and needs scarce expert time.
- **Fragility:** a feature set built for one problem or one data source rarely transfers to another, and a missing or poorly chosen feature silently caps what the model can ever achieve.
- **Human inductive bias:** $\phi(\cdot)$ bakes in the designer's assumptions about what is relevant. If those assumptions are wrong or incomplete, no choice of $f_\theta$ can recover the information that $\phi(\cdot)$ discarded.

> [!note] Where the information bottleneck sits
> Whatever $\phi(\cdot)$ throws away is gone for good. The learning algorithm can only be as good as the representation it is handed, which is why the quality of manual features often matters more than the choice of model in classical machine learning.

### Constraint to Structured Tabular Modalities

The second weakness is closely related. Classical models implicitly assume **structured, tabular** data: a table whose rows are observations $\mathbf{x}_i \in \mathbb{R}^d$, treated as independent and identically distributed (i.i.d.), and whose columns are explicit variables with a fixed meaning. Column $j$ means the same thing in every row, and the model is free to treat the coordinates as an unordered collection of named quantities. The lecture describes this as the clean, Excel-sheet form of data, with rows and columns that may be numeric or categorical.

Now consider **unstructured** data: images, audio, video, and text. The lecture points out that you cannot simply "put an image in a tabular format". Let us see why these modalities break the tabular assumptions:

- **Images** are pixel grids, naturally elements of $\mathbb{R}^{H \times W \times C}$ (height, width, colour channels). You *can* flatten them into a vector, but then coordinate $j$ no longer has a stable meaning. A cat shifted a few pixels to the right activates entirely different coordinates, even though it is the same object. The information lives in *spatial locality* and *translation invariance*, which a flat table ignores.
- **Audio** is a continuous acoustic waveform whose meaning lies in temporal structure at several time scales.
- **Video** adds a time axis to the image grid, giving spatio-temporal tensors.
- **Text** is a variable-length sequence of discrete tokens whose meaning is distributed across order and context. The lecture notes that text is structured only to some extent, but not completely.

In all four cases the *position* of a value carries meaning, and the number of raw coordinates is huge. A model that treats columns as independent, fixed-meaning variables has no way to exploit this, so classical methods applied to such data performed poorly, even when people did try them.

### Early Performance Saturation

The third weakness concerns what happens as we feed the model more data. A shallow model working on a fixed feature space has a finite **capacity**: a finite set of parameters, or a fixed kernel basis, through which it can express functions. Once that capacity is used up, adding more training examples cannot help, because the model simply has no more expressive room to absorb the extra information. As the training-set size $N$ grows, test performance therefore rises at first and then flattens out at a plateau set by the model class and its fixed features, rather than by the amount of data.

This is exactly the lecture's "early saturation" point: if the dataset (and the representation) stays the same, then improving the model again and again will eventually produce a flat performance curve. In short, traditional machine learning was useful for some use cases, but it did not keep improving as problems and datasets became larger and richer, and that gap motivated the search for an extension that would.

## 1.2 The Deep Learning Paradigm: Representation Learning

Each of the three limitations above has a counterpart in the deep learning answer. The manual step $\phi(\cdot)$ is removed from human hands and put inside the learning problem. The structured-data restriction is lifted by architectures designed to read raw inputs. And the performance ceiling is pushed outwards because models can keep growing. Let us unpack each idea.

### Automated Hierarchical Feature Extraction

A deep model is a long composition of simple parametrised transformations, called **layers**. Writing $L$ for the number of layers, the model computes

$$
f_\theta(\mathbf{x}) = \big(f^{(L)}_{\theta_L} \circ f^{(L-1)}_{\theta_{L-1}} \circ \dots \circ f^{(1)}_{\theta_1}\big)(\mathbf{x})
$$

where $\theta = (\theta_1, \dots, \theta_L)$ collects the parameters of all layers. Every layer is differentiable, so the whole composition is differentiable from the raw input all the way to the final output. This is what "end-to-end" means: a single error signal at the output can adjust *every* layer, including those that play the role that $\phi(\cdot)$ used to play.

What do the intermediate layers actually produce? If we set $\mathbf{h}^{(0)} = \mathbf{x}$ and let $\mathbf{h}^{(l)} = f^{(l)}(\mathbf{h}^{(l-1)})$ be the output of layer $l$, then each $\mathbf{h}^{(l)}$ is a learned description of the input, which we call a latent feature map or representation. Early layers describe the input in simple terms, and later layers describe it in progressively more abstract terms. This is exactly the automated feature extraction that the lecture contrasts with manual feature selection.

> [!abstract] Definition: Representation Learning (Automated Feature Learning)
> Representation learning is the practice of learning the intermediate latent feature maps $\mathbf{h}^{(l)} = f^{(l)}(\mathbf{h}^{(l-1)})$ **directly from raw inputs**, by gradient-based optimisation of a single end-to-end objective, instead of constructing the features by hand.

In plain terms: classical machine learning asks the human to supply $\phi(\cdot)$ and asks the algorithm to learn only $f_\theta$; deep learning asks the algorithm to learn *both* the features and the predictor at once. The word *hierarchical* in the heading matters, because features at layer $l$ are built out of features at layer $l-1$. We will come back to why that hierarchy is so valuable in Section 1.3 under hierarchical feature reuse. How the parameters of all these layers are actually adjusted is the subject of Section 2.

### Native Processing of Unstructured Data and Continuous Scaling

The lecture explains that deep learning can "understand the features inside the data directly" because of its **architecture**, that is, the structure with which the layers are wired. Different architectures build different assumptions into the layers: some are designed to exploit spatial locality in grids, others to exploit order in sequences. These assumptions are called *architectural inductive biases*. Because the right bias is built into the model, raw pixels, waveforms, or token sequences can be fed in as they are, and no one has to flatten them into a table first. This is why deep learning handles the image, audio, video, and text data that classical methods could not (the specific architectures are left for later weeks).

The second advantage is **continuous scaling**. The lecture uses an analogy: an application designed for 10 users will break if 2,000 arrive, so a robust system should keep working as the load grows. Deep networks are like this in three respects. We can scale the amount of training data $N$, the model capacity (the number of parameters $P$), and the compute budget $C$ used for training. As the use case becomes more complex, we can add more layers and more units, and performance keeps improving rather than hitting the early ceiling we saw in Section 1.1. This is also why modern generative and agentic AI systems, which the lecture mentions, are built on deep learning methods.

To keep the comparison in one place, here is a summary of the differences discussed so far, together with the practical trade-offs that come with deep learning.

| Aspect | Traditional Machine Learning | Deep Learning |
| :--- | :--- | :--- |
| **Data modality** | Structured, clean tabular data (rows and columns) | Unstructured data (images, audio, video, text) as well as tabular data |
| **Feature engineering** | Manual, domain-driven design of $\phi(\cdot)$ | Automatic, learned hierarchically from raw inputs |
| **Scaling behaviour** | Saturates early as $N$ grows, because capacity is fixed | Keeps improving as data, parameters, and compute are scaled |
| **Compute profile** | Light; often trainable on a CPU | Heavy; relies on specialised hardware and long training |
| **Data hunger** | Works with comparatively small datasets | Typically needs large datasets to exploit its capacity |
| **Interpretability** | Features are human-designed and usually easy to inspect | Learned latent features are harder to interpret |

> [!note] Trade-off, not a free lunch
> Removing manual feature engineering is not free. The price is higher computational cost, a greater appetite for data, and less transparent models. The lecture's message is that when the data are unstructured or the problem is complex enough to demand scaling, this price is worth paying.

## 1.3 Expressivity: Universal Approximation, Depth, and Width

We have claimed that deep networks can represent very complicated functions. In this subsection we make that claim precise, look at what the famous Universal Approximation Theorem does and does not promise, and then explain why *depth* in particular is so valuable.

### Architectural Anatomy: Input, Hidden, and Output Layers

A **feedforward multilayer network** is arranged in stages. The **input layer** receives the raw (or lightly preprocessed) data $\mathbf{x}$. The **output layer** produces the prediction. Everything in between is a **hidden layer**: it is not directly observed in the data, but it holds the intermediate representations $\mathbf{h}^{(l)}$ from Section 1.2. The lecture notes that there may be one hidden layer or many, and that the harder the problem, the more hidden layers one can use. Information flows in one direction, from input to hidden layers to output.

Two numbers describe the size of such a network, and it is very important to keep them apart:

> [!abstract] Definition: Width and Depth of a Network
> The **width** of layer $l$ is the number of neurons that sit side by side in that layer,
> $$
> d_l = \dim\big(\mathbf{h}^{(l)}\big).
> $$
> The **depth** of the network is the number $L$ of stacked layers through which the signal passes sequentially.

So width measures how many computations happen *in parallel* within one layer, while depth measures how many *sequential* stages of computation the input goes through. As the lecture puts it, depth is layers one on top of another, and width is side by side.

> [!warning] Do not swap "wide" and "deep"
> In the live Q&A the terms were verbally swapped at one point, which contradicts the slide explanation. The correct usage, which we follow throughout these notes, is: **wide** means many neurons in a single layer ($d_l$ large), and **deep** means many layers composed one after another ($L$ large). When you hear that a layer-by-layer pipeline extracts features step by step from an image, that is a statement about *depth*, not width.

### The Universal Approximation Theorem

A natural question is whether a network with just one hidden layer is already enough, provided we are willing to give that layer enough neurons. Remarkably, the answer in terms of pure representability is yes. The lecture summarises it as follows: with suitable mathematical functions (the activation functions) applied inside the units of a single hidden layer, the network can approximate anything, given sufficient width. The formal statement is:

> [!theorem] Universal Approximation Theorem (Cybenko / Hornik)
> Let $K \subset \mathbb{R}^n$ be compact and let $\sigma(\cdot)$ be a non-polynomial activation function (in the classical form, a continuous, bounded, non-constant sigmoidal function). Then for every continuous function $f \in C(K)$ and every $\varepsilon > 0$, there exists a feedforward network $\hat{f}$ with a single hidden layer of finitely many neurons $m$ such that
> $$
> \sup_{\mathbf{x} \in K} \big|\hat{f}(\mathbf{x}) - f(\mathbf{x})\big| < \varepsilon.
> $$

Let us unpack this. The theorem says that, on any bounded region of input space (compactness), a single hidden layer can get *uniformly* close to any continuous target, meaning the worst-case error over the whole region is below any tolerance $\varepsilon$ we choose. The role of the nonlinear activation is crucial: it is the non-polynomial nonlinearity that lets the hidden units bend and combine into arbitrary shapes. (In Section 5 we will see that without nonlinearity, stacking layers gains nothing.) Each hidden unit is a simple building block, and enough of them, with suitable weights, can be added together to sketch out any continuous curve or surface. This is the sense of the lecture's remark that as complexity grows, the layer has the capacity to take up a complex pattern and approximate it.

But we should read the theorem carefully, because it is easy to over-interpret.

> [!warning] Existence vs. Learnability and Tractable Width
> The theorem only guarantees that a good single-hidden-layer network **exists**. It says nothing about three practical questions:
> 1. **How large must $m$ be?** In the worst case the required width can grow exponentially with the input dimension $n$, on the order of $\mathcal{O}(\varepsilon^{-n})$, which is hopelessly large for high-dimensional inputs such as images.
> 2. **Can we find the weights?** There is no guarantee that gradient descent will actually discover the weights whose existence the theorem asserts.
> 3. **Will it generalise?** Approximating the target on the training region is a statement about representability, not about performance on unseen data.

In other words, universal approximation tells us a shallow network is *sufficient in principle*, but not that it is *efficient or learnable in practice*. To see how to do better than "just make one layer enormous", we now turn to depth.

### Depth vs. Width Trade-Offs and Hierarchical Feature Reuse

If one wide layer can in principle do everything, why do practitioners stack many layers? The answer is **parameter efficiency**. Many real-world functions are *compositional*: they can be written as a chain

$$
f = g_L \circ \dots \circ g_1
$$

of simpler functions, each of which depends on the output of the previous one. A deep network mirrors this structure directly, using one layer per simple function, so the number of parameters it needs grows only polynomially (roughly like $\mathcal{O}(L \cdot d^2)$ for $L$ layers of width $d$). A shallow, wide network has to represent the whole composition in a single step, and for certain compositional families it needs a width that grows exponentially, on the order of $\mathcal{O}(2^L)$, to capture the same number of piecewise-linear regions or compositional interactions. Depth buys expressive power much more cheaply than width does.

The lecture adds a complementary intuition. Suppose you want to solve a complex problem and want the network to detect many different complex patterns. Adding more hidden layers, one on top of another, lets the signal be refined stage by stage, and this can work better than a shallow, wide arrangement, although the lecture is careful to say that this is *not true in every case*. The natural mechanism behind this is reuse.

> [!abstract] Definition: Hierarchical Feature Reuse
> Hierarchical feature reuse is the property that **lower layers learn simple, general primitives** (for example edges and local gradients in images, or short n-gram patterns in text), and these primitives are **shared and recombined** along many pathways by deeper layers to form progressively more complex, high-level concepts. The deeper layers do not recompute the primitives from scratch.

Think of how an image is understood. Early layers pick up simple patterns such as edges. Later layers combine edges into corners and textures, then into object parts, and finally into whole objects. The same edge detector is useful for recognising thousands of different parts, so it is computed once and reused many times. The lecture states this in the same spirit: small, lower layers take up the ordinary patterns, deeper layers take up the complex ones, and the deeper layers can build on what the lower layers have already extracted instead of redoing all the computation. Reuse is what turns a linear growth in layers into an exponential growth in the number of distinct patterns the network can express.

Depth and width are therefore two different ways of spending a parameter budget, and neither dominates in all circumstances. The following remark summarises the trade-off.

> [!note] Architectural Trade-Off: Width vs. Depth Across Modalities
> - **Expressive efficiency:** depth composes features sequentially and reuses them, which suits hierarchical data such as images, audio, and language. Width adds parallel capacity within a single stage.
> - **Computational parallelism:** a wide layer is one large matrix multiplication that a GPU can spread across many cores at once. A deep network must evaluate its layers one after another, so each additional layer adds sequential latency that cannot be parallelised away.
> - **Optimisation difficulty:** very deep networks are harder to train, because the learning signal has to travel back through many layers (we study this problem and its remedies in Section 2). Very wide shallow layers avoid that issue, but may need impractically many neurons.
>
> In practice, successful architectures balance the two rather than maximising either one.

To summarise what this section has established:

> [!summary] Why Deep Learning?
> Traditional machine learning depends on hand-made features, is tied to clean tabular data, and saturates early. Deep learning replaces the hand-made feature map with a differentiable stack of layers that learns hierarchical representations end to end, reads unstructured data natively, and keeps improving as it is scaled. The Universal Approximation Theorem shows that even one wide hidden layer is expressive enough in principle, but depth achieves the same expressive power far more efficiently through compositional structure and hierarchical feature reuse, at the cost of harder optimisation and sequential computation.

---

# 2. Neural Network Training Pipeline & Backpropagation

In the previous section we asked *what* a deep network can represent. Now we ask the practical question: how does a network with millions of randomly initialised weights actually *learn* those good representations? The answer is a surprisingly compact loop that repeats four steps: make a prediction, measure how wrong it was, work out which weights are to blame, and nudge them. In this section we first lay out that loop, then open up the hardest step, the blame assignment, which is called **backpropagation**, and finally study why that blame signal can fade away or blow up in deep networks and what we do about it.

## 2.1 The Four-Stage Iterative Training Loop

Think of training as a student practising past exam papers. The student attempts a paper (forward pass), marks it against the key (loss evaluation), identifies which concepts caused the lost marks (backward pass), and revises those concepts (parameter update). Then the cycle repeats with new papers. A neural network does exactly this, only with calculus instead of a red pen.

Throughout, we consider a feedforward network with $L$ layers. Layer $l$ has width $d_l$, weight matrix $\mathbf{W}^{(l)} \in \mathbb{R}^{d_l \times d_{l-1}}$, bias vector $\mathbf{b}^{(l)} \in \mathbb{R}^{d_l}$, and an activation function $\sigma^{(l)}$ applied element-wise. We collect all learnable weights and biases into a single parameter vector $\theta$.

### Stage 1: Forward Propagation (Forward Pass)

The forward pass is a deterministic, layer-by-layer mapping from the input to the prediction. We start by setting the "activation" of layer $0$ to be the input itself, $\mathbf{a}^{(0)} = \mathbf{x}$. Then for each layer $l = 1, \dots, L$ we first compute the **pre-activation** (the affine step), and then the **activation** (the nonlinear step):

$$
\begin{aligned}
\mathbf{z}^{(l)} &= \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)} \\
\mathbf{a}^{(l)} &= \sigma^{(l)}\big(\mathbf{z}^{(l)}\big)
\end{aligned}
$$

The output of the last layer is the network's prediction, $\hat{\mathbf{y}} = \mathbf{a}^{(L)}$. In other words, the whole network is just the composition of $L$ simple "affine then nonlinear" blocks, with each block feeding the next.

> [!note] Why Intermediate Values Matter
> The forward pass does more than produce $\hat{\mathbf{y}}$. The intermediate quantities $\mathbf{z}^{(l)}$ and $\mathbf{a}^{(l)}$ are exactly what the backward pass will need later. This is why they are normally kept in memory during training rather than discarded.

### Stage 2: Loss Evaluation

A prediction on its own tells us nothing about quality. We need a single number that says "how wrong are we?". This is the job of the **loss function** $\mathcal{L}(\hat{\mathbf{y}}, \mathbf{y})$, which compares the prediction $\hat{\mathbf{y}}$ with the ground-truth target $\mathbf{y}$ and returns a non-negative scalar, where smaller means better.

In practice we rarely evaluate one sample at a time. We take a sample or a **mini-batch** $\mathcal{B}$ of $|\mathcal{B}|$ examples and average the per-example losses, which gives the empirical risk

$$
\mathcal{L}(\theta) = \frac{1}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} \mathcal{L}\big(\hat{\mathbf{y}}_i, \mathbf{y}_i\big).
$$

Because the loss must be a *scalar*, it gives the optimisation a single, unambiguous direction to improve in. The specific loss functions used for regression and classification are developed in a later section of this note.

### Stage 3: Backward Propagation (Backward Pass)

We now know how wrong we are, but a single number does not tell us *which of the millions of parameters* to adjust or in which direction. What we need is the gradient $\nabla_{\mathbf{W}^{(l)}} \mathcal{L}$ and $\nabla_{\mathbf{b}^{(l)}} \mathcal{L}$ for every layer, which measures how sensitive the loss is to each parameter.

The backward pass computes these exact partial derivatives by working in the reverse direction, from $l = L$ down to $l = 1$. It starts at the loss, where the sensitivity is easiest to write down, and passes that sensitivity backwards through each layer using the chain rule. This is a form of **reverse-mode automatic differentiation**. Section 2.2 develops the mathematics in full.

### Stage 4: Parameter Update and Convergence Criteria

With gradients in hand, the update is simple. The gradient points in the direction of steepest *increase* of the loss, so we step in the opposite direction by an amount controlled by the **learning rate** $\eta > 0$:

$$
\theta^{(t+1)} = \theta^{(t)} - \eta \, \nabla_\theta \mathcal{L}\big(\theta^{(t)}\big).
$$

This is **gradient descent**. The choice of $\eta$, and smarter update rules than this plain one, are discussed in the next section of this note.

#### Epochs and Iterations

Two words describe how long training has run. One **iteration** is a single pass through the four stages on one mini-batch, which produces one parameter update. One **epoch** is a complete sweep of the entire training set, so that every training example has been used once. If the training set has $N$ examples and the mini-batch size is $|\mathcal{B}|$, one epoch consists of $\lceil N / |\mathcal{B}| \rceil$ iterations.

#### When Do We Stop?

The loop could run forever, so we need stopping criteria. Common ones are:

- **Loss plateau:** the improvement over the last $k$ iterations falls below a tolerance $\tau$, that is $|\mathcal{L}^{(t)} - \mathcal{L}^{(t-k)}| < \tau$.
- **Gradient norm convergence:** $\|\nabla_\theta \mathcal{L}\| \to 0$, meaning we have reached a stationary point where there is no first-order direction left to improve.
- **Early stopping:** we monitor the loss on a held-out validation set and halt when it stops improving, even if the training loss is still falling. This guards against overfitting, which is studied in a later section.

> [!summary] The Training Loop in One Line
> Repeat: forward pass $\to$ loss $\to$ backward pass $\to$ update, over many mini-batches and epochs, until a stopping criterion is met.

## 2.2 Mathematical Mechanics of Backpropagation

The backward pass sounds almost magical: a single sweep gives the gradient with respect to *every* parameter. Why is that possible? The reason is that the network is a long composition of simple functions, and the chain rule lets us reuse partial results from later layers when computing earlier ones. We now build this up carefully.

### The Multivariable Chain Rule in Computational Graphs

Recall the chain rule for scalars: if $y = f(g(x))$ then $\frac{dy}{dx} = f'(g(x))\, g'(x)$. Our network, however, passes *vectors* between layers, so we need the multivariable version.

Suppose $\mathbf{u} \in \mathbb{R}^m$ is computed from $\mathbf{v} \in \mathbb{R}^n$ by a vector-valued function $\mathbf{u} = g(\mathbf{v})$, and a scalar $\mathcal{L}$ is computed from $\mathbf{u}$. Every component $v_j$ may influence $\mathcal{L}$ through *every* component $u_k$, so the influences along all these paths must be added up:

$$
\frac{\partial \mathcal{L}}{\partial v_j} = \sum_{k=1}^{m} \frac{\partial \mathcal{L}}{\partial u_k} \frac{\partial u_k}{\partial v_j}.
$$

Collecting the partial derivatives $\frac{\partial u_k}{\partial v_j}$ into the **Jacobian matrix** $\mathbf{J} \in \mathbb{R}^{m \times n}$ with entries $J_{kj} = \frac{\partial u_k}{\partial v_j}$, the same statement in vector form becomes

$$
\nabla_{\mathbf{v}} \mathcal{L} = \mathbf{J}^\top \nabla_{\mathbf{u}} \mathcal{L}.
$$

So sensitivity flows *backwards* through a function by multiplying with the transpose of its Jacobian. A neural network is a **computational graph**: each node is an intermediate quantity ($\mathbf{z}^{(l)}$ or $\mathbf{a}^{(l)}$) and each edge is a function. Backpropagation is nothing more than applying this rule node by node, starting at the loss and moving towards the input, and storing each result so that it can be reused by the next node further back.

### Layer-Wise Error Sensitivities and Parameter Gradients

To organise the computation, we give a name to the most useful intermediate quantity: the sensitivity of the loss to each pre-activation.

> [!abstract] Definition: Backpropagated Error Signal (Local Gradient)
> For layer $l$, the error signal is the gradient of the loss with respect to that layer's pre-activation:
> $$
> \boldsymbol{\delta}^{(l)} \equiv \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} \in \mathbb{R}^{d_l}.
> $$
> Its $j$-th component is $\delta^{(l)}_j = \frac{\partial \mathcal{L}}{\partial z^{(l)}_j}$.

In words, $\delta^{(l)}_j$ tells us how much the loss would change if the pre-activation of neuron $j$ in layer $l$ were nudged slightly. Why $\mathbf{z}^{(l)}$ and not $\mathbf{a}^{(l)}$? Because $\mathbf{z}^{(l)}$ is the quantity that parameters $\mathbf{W}^{(l)}$ and $\mathbf{b}^{(l)}$ act on directly, so once we know $\boldsymbol{\delta}^{(l)}$, the parameter gradients follow almost immediately. The following theorem summarises the whole algorithm.

> [!theorem] The Four Fundamental Equations of Backpropagation
> Let $\odot$ denote the element-wise (Hadamard) product, and assume each $\sigma^{(l)}$ acts element-wise. Then:
> 1. **Output layer error:**
> $$
> \boldsymbol{\delta}^{(L)} = \nabla_{\mathbf{a}^{(L)}} \mathcal{L} \odot (\sigma^{(L)})'\big(\mathbf{z}^{(L)}\big)
> $$
> 2. **Recursive backward propagation of the error:**
> $$
> \boldsymbol{\delta}^{(l)} = \Big( \big(\mathbf{W}^{(l+1)}\big)^\top \boldsymbol{\delta}^{(l+1)} \Big) \odot (\sigma^{(l)})'\big(\mathbf{z}^{(l)}\big), \qquad l = L-1, \dots, 1
> $$
> 3. **Bias gradient:**
> $$
> \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}
> $$
> 4. **Weight gradient:**
> $$
> \frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)} \big(\mathbf{a}^{(l-1)}\big)^\top
> $$

**Proof:** We prove each equation component by component using the multivariable chain rule, and then restate it in vector form.

*Equation 1.* The loss depends on $z^{(L)}_j$ only through the output activations. By the chain rule,

$$
\delta^{(L)}_j = \frac{\partial \mathcal{L}}{\partial z^{(L)}_j} = \sum_{k=1}^{d_L} \frac{\partial \mathcal{L}}{\partial a^{(L)}_k} \frac{\partial a^{(L)}_k}{\partial z^{(L)}_j}.
$$

Because the activation is applied element-wise, $a^{(L)}_k = \sigma^{(L)}\big(z^{(L)}_k\big)$ depends only on $z^{(L)}_k$. Hence $\frac{\partial a^{(L)}_k}{\partial z^{(L)}_j}$ is zero unless $k = j$, in which case it equals $(\sigma^{(L)})'\big(z^{(L)}_j\big)$. The sum collapses to a single term:

$$
\delta^{(L)}_j = \frac{\partial \mathcal{L}}{\partial a^{(L)}_j} \, (\sigma^{(L)})'\big(z^{(L)}_j\big),
$$

which is the component form of $\boldsymbol{\delta}^{(L)} = \nabla_{\mathbf{a}^{(L)}} \mathcal{L} \odot (\sigma^{(L)})'(\mathbf{z}^{(L)})$.

*Equation 2.* The pre-activation $z^{(l)}_j$ influences the loss only by changing the next layer's pre-activations $z^{(l+1)}_k$, for every neuron $k$ in layer $l+1$. Summing over all these paths,

$$
\delta^{(l)}_j = \frac{\partial \mathcal{L}}{\partial z^{(l)}_j} = \sum_{k=1}^{d_{l+1}} \frac{\partial \mathcal{L}}{\partial z^{(l+1)}_k} \frac{\partial z^{(l+1)}_k}{\partial z^{(l)}_j} = \sum_{k=1}^{d_{l+1}} \delta^{(l+1)}_k \frac{\partial z^{(l+1)}_k}{\partial z^{(l)}_j}.
$$

From the forward pass, $z^{(l+1)}_k = \sum_{m} W^{(l+1)}_{km}\, \sigma^{(l)}\big(z^{(l)}_m\big) + b^{(l+1)}_k$. Differentiating with respect to $z^{(l)}_j$, only the term $m = j$ survives:

$$
\frac{\partial z^{(l+1)}_k}{\partial z^{(l)}_j} = W^{(l+1)}_{kj} \, (\sigma^{(l)})'\big(z^{(l)}_j\big).
$$

Substituting back gives

$$
\delta^{(l)}_j = \Big( \sum_{k=1}^{d_{l+1}} W^{(l+1)}_{kj} \, \delta^{(l+1)}_k \Big) (\sigma^{(l)})'\big(z^{(l)}_j\big).
$$

The bracketed sum is exactly the $j$-th entry of $\big(\mathbf{W}^{(l+1)}\big)^\top \boldsymbol{\delta}^{(l+1)}$ (note that we sum over the *row* index $k$ of $\mathbf{W}^{(l+1)}$, which is the definition of multiplying by the transpose). This is the vector equation $\boldsymbol{\delta}^{(l)} = \big( (\mathbf{W}^{(l+1)})^\top \boldsymbol{\delta}^{(l+1)} \big) \odot (\sigma^{(l)})'(\mathbf{z}^{(l)})$.

*Equation 3.* The bias $b^{(l)}_j$ enters the loss only through $z^{(l)}_j = \sum_m W^{(l)}_{jm} a^{(l-1)}_m + b^{(l)}_j$, and $\frac{\partial z^{(l)}_j}{\partial b^{(l)}_j} = 1$. Therefore

$$
\frac{\partial \mathcal{L}}{\partial b^{(l)}_j} = \frac{\partial \mathcal{L}}{\partial z^{(l)}_j} \frac{\partial z^{(l)}_j}{\partial b^{(l)}_j} = \delta^{(l)}_j,
$$

that is, $\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}$.

*Equation 4.* The weight $W^{(l)}_{jm}$ connects input $a^{(l-1)}_m$ to neuron $j$ and affects the loss only through $z^{(l)}_j$. From the same expression for $z^{(l)}_j$, we get $\frac{\partial z^{(l)}_j}{\partial W^{(l)}_{jm}} = a^{(l-1)}_m$. Hence

$$
\frac{\partial \mathcal{L}}{\partial W^{(l)}_{jm}} = \frac{\partial \mathcal{L}}{\partial z^{(l)}_j} \frac{\partial z^{(l)}_j}{\partial W^{(l)}_{jm}} = \delta^{(l)}_j \, a^{(l-1)}_m.
$$

The collection of all entries $\delta^{(l)}_j a^{(l-1)}_m$, indexed by row $j$ and column $m$, is precisely the outer product $\boldsymbol{\delta}^{(l)} \big(\mathbf{a}^{(l-1)}\big)^\top \in \mathbb{R}^{d_l \times d_{l-1}}$, which has the same shape as $\mathbf{W}^{(l)}$ as it must. $\blacksquare$

#### Reading the Four Equations as an Algorithm

The equations assemble into a complete procedure. After the forward pass (which stores every $\mathbf{z}^{(l)}$ and $\mathbf{a}^{(l)}$), equation 1 seeds the error at the output. Equation 2 then walks the error backwards one layer at a time, each step needing only the *next* layer's error, the weights, and the stored pre-activations. At every layer, equations 3 and 4 convert the error into gradients for that layer's parameters. The name "backpropagation" comes from this backward flow of $\boldsymbol{\delta}$.

> [!note] Role of Stored Forward Values
> Equation 4 needs $\mathbf{a}^{(l-1)}$ and equations 1 and 2 need $\mathbf{z}^{(l)}$ (through $\sigma'$). This is the mathematical reason forward-pass values must be retained until the backward pass reaches them.

> [!warning] Non-Element-Wise Activations
> The Hadamard form of equations 1 and 2 relies on the activation being applied element-wise, which makes its Jacobian diagonal. If an output activation mixes components (as softmax does), the Jacobian $\frac{\partial \mathbf{a}^{(L)}}{\partial \mathbf{z}^{(L)}}$ is no longer diagonal, and equation 1 must be written with the full Jacobian: $\boldsymbol{\delta}^{(L)} = \big(\frac{\partial \mathbf{a}^{(L)}}{\partial \mathbf{z}^{(L)}}\big)^\top \nabla_{\mathbf{a}^{(L)}} \mathcal{L}$. The other three equations are unchanged.

### Why Reverse-Mode Differentiation Is Efficient

Suppose the network has $P$ parameters. Why do we not simply estimate each partial derivative by perturbing the parameter slightly and re-running the network, as in the finite-difference estimate $\frac{\partial \mathcal{L}}{\partial \theta_i} \approx \frac{\mathcal{L}(\theta + \epsilon \mathbf{e}_i) - \mathcal{L}(\theta)}{\epsilon}$?

The cost tells the story. One forward pass costs $\mathcal{O}(P)$, since each parameter is used a constant number of times. Finite differences need one extra forward pass *per parameter*, which is $P$ passes of $\mathcal{O}(P)$ each, for a total of $\mathcal{O}(P^2)$. Forward-mode differentiation has the same issue, because it propagates the derivative with respect to a single input direction at a time. For a network with millions of parameters, $\mathcal{O}(P^2)$ is hopeless.

Reverse mode exploits the fact that the loss is a *single scalar output*. One backward sweep propagates the sensitivity of that one output to all intermediate quantities at once, and each of the four equations does a constant amount of work per parameter. So one forward plus one backward pass delivers all $P$ gradients in $\mathcal{O}(P)$ time, with a cost of only a small constant multiple of a forward pass. This asymmetry, with many inputs (parameters) and one scalar output (loss), is exactly the regime in which reverse mode shines, and it is why deep learning is practical at all.

## 2.3 Gradient Stability and Mitigation Mechanisms

Equation 2 hides a subtle danger. It says the error at layer $l$ is obtained from the error at layer $l+1$ by multiplying by a weight matrix and a derivative factor. In a deep network this happens many times in a row. What does repeated multiplication do to a quantity? If the multiplier is slightly smaller than $1$ it shrinks to nothing, and if it is slightly larger than $1$ it explodes. This section turns that intuition into mathematics and then looks at the tools that tame it.

### The Vanishing and Exploding Gradient Problems

Define the layer-to-layer error map. Equation 2 can be written as $\boldsymbol{\delta}^{(k)} = \operatorname{diag}\!\big(\sigma'(\mathbf{z}^{(k)})\big) \big(\mathbf{W}^{(k+1)}\big)^\top \boldsymbol{\delta}^{(k+1)}$, since an element-wise product with a vector equals multiplication by the corresponding diagonal matrix. Unrolling this recursion from the output layer back to an early layer $l$ yields

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} = \left( \prod_{k=l}^{L-1} \operatorname{diag}\!\big(\sigma'(\mathbf{z}^{(k)})\big) \big(\mathbf{W}^{(k+1)}\big)^\top \right) \boldsymbol{\delta}^{(L)}.
$$

The error at an early layer is therefore the output error multiplied by a product of $L - l$ matrices. The size of such a product is governed by the size of its factors, which we measure with spectral norms (largest singular values).

> [!abstract] Definition: Vanishing and Exploding Gradients
> Let each factor $\operatorname{diag}\!\big(\sigma'(\mathbf{z}^{(k)})\big) \big(\mathbf{W}^{(k+1)}\big)^\top$ have spectral norm bounded as follows.
> - **Vanishing gradients:** if the norm is less than $1 - \epsilon$ for some $\epsilon > 0$, then the norm of the product is at most $(1-\epsilon)^{L-l}$, so the gradient reaching early layers decays exponentially with the distance $L - l$ from the output. Early layers receive almost no learning signal and effectively freeze.
> - **Exploding gradients:** if the norm is greater than $1 + \epsilon$ in the relevant directions, the gradient can grow like $(1+\epsilon)^{L-l}$, exponentially with depth. This leads to numerical overflow and huge, destabilising weight updates.

The bound in the vanishing case follows from the sub-multiplicativity of operator norms, $\|\mathbf{A}\mathbf{B}\| \le \|\mathbf{A}\|\|\mathbf{B}\|$, applied to the product. Notice that the problem is *exponential in depth*, which is why it becomes severe precisely in the deep networks that Section 1 argued are so valuable. Two ingredients control the factor norms: the weights $\mathbf{W}$ and the activation derivatives $\sigma'$. We examine the latter next.

### Activation Function Saturation vs. Non-Saturating Rectifiers (ReLU)

#### Saturating Activations: Sigmoid and Tanh

The **sigmoid** is $\sigma(z) = \frac{1}{1 + e^{-z}}$. Its derivative can be written in terms of itself:

$$
\sigma'(z) = \sigma(z)\big(1 - \sigma(z)\big).
$$

Since $\sigma(z) \in (0,1)$, the product $\sigma(1-\sigma)$ is largest when $\sigma = \tfrac{1}{2}$, so $\sigma'(z) \in (0, 0.25]$. Even in the *best* case every sigmoid layer contributes a factor of at most $0.25$ from its derivative alone. The **hyperbolic tangent** has derivative

$$
\tanh'(z) = 1 - \tanh^2(z) \in (0, 1],
$$

which is better since its maximum is $1$, but this maximum is attained only at $z = 0$.

For both functions, when $|z|$ is large the output is pinned close to its asymptote (this is called **saturation**), the curve is almost flat, and the derivative tends to $0$. A saturated neuron therefore passes essentially no error backwards. Combined with the product formula above, saturation makes vanishing gradients very likely even at moderate depth.

#### Non-Saturating Rectifiers: ReLU

> [!abstract] Definition: Rectified Linear Unit (ReLU)
> $$
> \operatorname{ReLU}(z) = \max(0, z), \qquad \operatorname{ReLU}'(z) = \mathbb{I}(z > 0) \in \{0, 1\}
> $$
> where $\mathbb{I}(\cdot)$ is the indicator function. The derivative at $z = 0$ is not defined and is conventionally set to $0$ (or $1$) in practice.

For ReLU the derivative is exactly $1$ on the whole active half-space $z > 0$. A neuron that is active therefore multiplies the passing error by $1$ rather than by a number smaller than $0.25$, so the derivative factor does not cause a multiplicative decay no matter how large $z$ becomes. Inactive neurons ($z < 0$) block the error completely, but this creates sparse gradient paths along which the signal travels undiminished. The remaining factor, the weight matrix, must still be kept at a sensible scale to avoid explosion.

> [!warning] The Dying ReLU Phenomenon
> If a large negative update to a bias or weights pushes $z_i < 0$ for *every* training input, then neuron $i$ outputs $0$ everywhere and its derivative is $0$ everywhere. No gradient reaches its parameters, so it can never recover and stays permanently inactive ("dead"). Variants such as **Leaky ReLU**, $\max(\alpha z, z)$ with a small $\alpha > 0$, **ELU**, and **GELU** keep a non-zero slope (or a smooth, non-zero response) for negative inputs so that a gradient can still flow.

### Residual Connections (Skip Connections)

Better activations help, but a very deep stack of layers can still suffer, because the gradient has to pass through many transformations. Residual connections attack the problem structurally: instead of forcing the signal through every layer, they give it an express lane around them.

> [!abstract] Definition: Residual Block and Identity Skip Connection
> A residual block computes its output by *adding* its input to a learned transformation $\mathcal{F}$ of that input:
> $$
> \mathbf{a}^{(l)} = \mathbf{a}^{(l-1)} + \mathcal{F}\big(\mathbf{a}^{(l-1)}; \theta^{(l)}\big).
> $$
> The path that carries $\mathbf{a}^{(l-1)}$ forward unchanged is the identity skip connection.

The block only has to learn the *residual* correction $\mathcal{F}$ rather than the full mapping, and if the best thing a layer can do is nothing, it can simply learn $\mathcal{F} \approx \mathbf{0}$. The real payoff, however, is in the backward pass. Differentiating one block with respect to its input gives

$$
\frac{\partial \mathbf{a}^{(l)}}{\partial \mathbf{a}^{(l-1)}} = \mathbf{I} + \frac{\partial \mathcal{F}}{\partial \mathbf{a}^{(l-1)}}.
$$

Compare this with a plain layer, where the Jacobian was just a product of weights and derivatives that could shrink. Here the identity matrix $\mathbf{I}$ is *added* to the Jacobian of the learned part. To see the effect over many blocks, unroll the forward recursion from layer $l$ to layer $L$:

$$
\mathbf{a}^{(L)} = \mathbf{a}^{(l)} + \sum_{k=l+1}^{L} \mathcal{F}\big(\mathbf{a}^{(k-1)}; \theta^{(k)}\big).
$$

Differentiating with respect to $\mathbf{a}^{(l)}$ and applying the chain rule to the loss yields the telescoped form (writing the sum from the perspective of the blocks between $l$ and $L$)

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(L)}} \left( \mathbf{I} + \frac{\partial}{\partial \mathbf{a}^{(l)}} \sum_{k=l}^{L-1} \mathcal{F}\big(\mathbf{a}^{(k)}; \theta^{(k)}\big) \right).
$$

The crucial feature is the additive identity term $\mathbf{I}$. It means the gradient arriving at layer $l$ always contains a *direct copy* of the gradient at the output, $\frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(L)}}$, which has not been multiplied by any weight matrix or activation derivative along the way. This forms a gradient highway that bypasses arbitrarily many intermediate transformations. Even if the learned terms inside the bracket become small, the identity term keeps the total from vanishing, so very deep networks remain trainable.

> [!summary] Taming Gradient Instability
> Vanishing and exploding gradients arise because backpropagation multiplies one factor per layer. Saturating activations (sigmoid, tanh) make these factors small; non-saturating rectifiers (ReLU and its variants) keep the derivative factor at one on the active region; and residual connections add an identity path so that the gradient never has to rely solely on a long chain of products.

---

# 3. Learning Rate Dynamics, Optimisers, & Regularisation

Backpropagation (Section 2) tells us *which direction* every parameter should move to reduce the loss. It says nothing about *how far* to move, *how to combine* the directions we get from successive mini-batches, or *how to stop* the network from simply memorising its training data. This section answers those three questions in turn: first the step size (the learning rate and its schedule), then the update rules built on top of the raw gradient (SGD, momentum, RMSprop, Adam), and finally the tools that make a trained network generalise (weight penalties, dropout, batch normalisation).

## 3.1 Learning Rate Dynamics and Scheduling

### Step-Size Regimes and Convergence Behavior

Gradient descent follows the update $\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta_t)$ from the training loop. The gradient gives a direction; the scalar $\eta$ decides how aggressively we commit to it. Choosing it badly can ruin training even when the gradients are perfectly correct.

> [!abstract] Definition: Learning Rate ($\eta$)
> The learning rate $\eta > 0$ is the scalar hyperparameter that scales the gradient and therefore controls the magnitude of the parameter displacement along the negative gradient direction at each update.

To see precisely how large $\eta$ may be, zoom in on a local minimum $\theta^*$, where $\nabla_\theta \mathcal{L}(\theta^*) = \mathbf{0}$. A second-order Taylor expansion gives

$$
\mathcal{L}(\theta) \approx \mathcal{L}(\theta^*) + \frac{1}{2}(\theta - \theta^*)^\top \mathbf{H} (\theta - \theta^*),
$$

where $\mathbf{H}$ is the Hessian at $\theta^*$. Its gradient is $\mathbf{H}(\theta - \theta^*)$, so the update becomes

$$
\theta_{t+1} - \theta^* = (\mathbf{I} - \eta \mathbf{H})(\theta_t - \theta^*).
$$

Because $\mathbf{H}$ is symmetric, we can diagonalise it and look at the error component along each eigenvector separately. Along an eigenvector with eigenvalue $\lambda_i > 0$, the error is multiplied by $(1 - \eta\lambda_i)$ at every step. The error shrinks to zero only if $|1 - \eta\lambda_i| < 1$, that is $0 < \eta < 2/\lambda_i$. This must hold for *every* direction, so the binding constraint comes from the steepest direction:

$$
0 < \eta < \frac{2}{\lambda_{\max}}.
$$

In other words, the sharpest curvature of the landscape caps the usable learning rate, while the flattest directions (small $\lambda_i$) are the ones that crawl. The ratio between the two is the condition number discussed in Section 4.

The sign and size of $1 - \eta\lambda_i$ also explain the behavioural regimes:

1. **Suboptimally small $\eta$ ($\eta \ll 1/\lambda_{\max}$):** every factor $1 - \eta\lambda_i$ is just below $1$, so the iterates are over-damped. Convergence is monotone but sluggish and needs excessive epochs. Worse, on flat plateaus or in shallow local traps the tiny steps can stall long before a good solution is reached.
2. **Balanced $\eta$:** the factors are comfortably inside $(-1, 1)$ and well below $1$ in magnitude along the important directions, producing rapid, essentially monotone descent into the basin of attraction.
3. **Excessively high $\eta$:** for $1/\lambda_{\max} < \eta < 2/\lambda_{\max}$ the steepest-direction factor becomes negative, so the iterate overshoots the minimum and flips sides on each step. The trajectory is under-damped and zigzags across the narrow valley walls while still slowly converging. For $\eta > 2/\lambda_{\max}$ the factor has magnitude above $1$, the oscillations grow at every step, and the loss diverges (exploding weights and numerical overflow).

> [!note] Learning Rate and Gradient Stability
> The learning rate interacts with the gradient-stability issues of Section 2.3. Exploding gradients make the effective step $\eta\|\nabla\mathcal{L}\|$ enormous even for a moderate $\eta$, whereas vanishing gradients make it negligible even for a large $\eta$. A good learning rate is therefore always relative to the typical gradient scale and curvature of the network, which is exactly what the adaptive optimisers of Section 3.2 try to automate.

### Learning Rate Schedules and Warmup

If one fixed $\eta$ were enough, we could tune it once and forget it. It is not, for two reasons. Early in training we are far from any minimum and want large steps to explore quickly. Late in training each mini-batch gradient is a noisy estimate, so a large constant step keeps the iterate bouncing around the minimum at a noise-dominated radius; only a smaller step lets it settle. A **learning rate schedule** lowers $\eta_t$ as the iteration count $t$ grows, aiming for fast progress first and precise convergence later.

The common schedules are:

- **Step decay:** hold $\eta$ constant and multiply it by a fixed factor less than $1$ every fixed number of epochs, producing a staircase.
- **Exponential decay:** a smooth, continuous version of the same idea,
  $$
  \eta_t = \eta_0 e^{-\kappa t},
  $$
  where $\kappa > 0$ is the decay rate.
- **Cosine annealing:** the rate glides from $\eta_{\max}$ to $\eta_{\min}$ over a horizon of $T$ steps along half a cosine wave,
  $$
  \eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max} - \eta_{\min})\left(1 + \cos\!\left(\frac{t}{T}\pi\right)\right).
  $$
  It decays slowly at the start, fastest in the middle, and flattens again near $\eta_{\min}$, so the network spends its final steps at a tiny rate.
- **Linear warmup:** for the first few iterations $\eta_t$ increases linearly from near zero to its target value, after which one of the decay schedules above takes over.

Why is warmup useful? With randomly initialised weights, the very first gradients are unreliable and can be large, and for adaptive optimisers the moment estimates have not yet accumulated meaningful statistics. A full-sized step at that moment can throw the weights into a bad region, from which training may never recover. Warming up gives the network a few gentle steps in which the loss surface is probed safely before the full rate is applied.

## 3.2 First-Order and Adaptive Optimisation Algorithms

### Batch, Stochastic, and Mini-Batch Gradient Descent (SGD)

Which data do we use to compute the gradient? **Batch gradient descent** uses the full training set, giving the exact gradient but at a cost proportional to the dataset size for every single update. **Stochastic gradient descent** uses one sample per update, which is cheap but extremely noisy. **Mini-batch gradient descent** is the practical compromise: at step $t$ we draw a random subset $\mathcal{B}_t$ and use the estimator

$$
\mathbf{g}_t = \frac{1}{|\mathcal{B}_t|} \sum_{i \in \mathcal{B}_t} \nabla_\theta \mathcal{L}(\mathbf{x}_i, y_i; \theta_t).
$$

Because the samples are drawn uniformly, $\mathbf{g}_t$ is an unbiased estimator of the full gradient, $\mathbb{E}[\mathbf{g}_t] = \nabla_\theta \mathcal{L}(\theta_t)$, and averaging $|\mathcal{B}_t|$ roughly independent per-sample gradients reduces the variance in proportion to $1/|\mathcal{B}_t|$:

$$
\operatorname{Var}(\mathbf{g}_t) \propto \frac{1}{|\mathcal{B}_t|}.
$$

So the batch size is a dial between noise and cost: larger batches give more reliable directions and map well onto parallel hardware, smaller batches give cheaper, noisier steps. (The helpful side of this noise is discussed in Section 4.3.) The term *SGD* is generally used for the mini-batch version with the update $\theta_{t+1} = \theta_t - \eta\,\mathbf{g}_t$.

> [!warning] Pathologies of Vanilla SGD
> Plain SGD applies the *same* scalar $\eta$ to every coordinate. In an ill-conditioned landscape (a long, narrow ravine) the gradient is dominated by the steep walls, so the iterate oscillates across the ravine while making only slow progress along its floor. We cannot fix this with a single scalar: lowering $\eta$ to calm the oscillation slows the flat direction even more. The next optimisers each address this in a different way.

### SGD with Momentum

Look at the ravine problem again. Across the ravine the gradient components keep flipping sign from step to step, while along the ravine they consistently point the same way. If we average gradients over recent steps, the flipping components cancel and the consistent components survive. That is precisely what momentum does.

> [!abstract] Definition: Momentum Update Rule
> SGD with momentum maintains a velocity vector $\mathbf{v}_t$, an exponentially decaying moving average of past gradients, with decay factor $\beta \in [0, 1)$:
> $$
> \begin{aligned}
> \mathbf{v}_t &= \beta \mathbf{v}_{t-1} + \mathbf{g}_t \\
> \theta_{t+1} &= \theta_t - \eta \mathbf{v}_t
> \end{aligned}
> $$
> (An equivalent convention uses $\beta \mathbf{v}_{t-1} + (1-\beta)\mathbf{g}_t$, which merely rescales $\eta$.)

The physical picture is a heavy ball rolling on the loss surface: gradients act as forces, $\mathbf{v}_t$ is the ball's velocity, and $\beta$ is friction. Unrolling the recursion shows $\mathbf{v}_t = \sum_{k \ge 0} \beta^k \mathbf{g}_{t-k}$. If the gradient is the same in every step along some direction, the geometric series gives a terminal velocity amplified by a factor $\frac{1}{1-\beta}$. For example, $\beta = 0.9$ makes the effective step along a persistent descent direction ten times larger. Along directions where the gradient alternates in sign, successive terms cancel and the velocity stays small. Hence momentum gives **constructive interference** along persistent low-curvature directions and **destructive cancellation** along oscillating high-curvature directions, allowing faster progress with less zigzagging.

**Nesterov Accelerated Gradient (NAG)** is a refinement worth knowing at the conceptual level: instead of evaluating the gradient at the current position, it evaluates it at the "look-ahead" position that the velocity is about to carry the parameters to. This gives the ball an early correction when it is about to overshoot.

### RMSprop (Root Mean Square Propagation)

Momentum fixes the *direction* by smoothing, but still uses one global $\eta$. RMSprop instead gives each parameter its own effective learning rate, based on how large its gradients have recently been.

> [!abstract] Definition: RMSprop Update Rule
> RMSprop keeps an exponentially decaying moving average $\mathbf{s}_t$ of the elementwise squared gradients and divides each coordinate of the step by its root:
> $$
> \begin{aligned}
> \mathbf{s}_t &= \beta \mathbf{s}_{t-1} + (1 - \beta)(\mathbf{g}_t \odot \mathbf{g}_t) \\
> \theta_{t+1} &= \theta_t - \frac{\eta}{\sqrt{\mathbf{s}_t + \epsilon}} \odot \mathbf{g}_t
> \end{aligned}
> $$
> where $\epsilon > 0$ is a small constant for numerical stability and all operations are elementwise.

The quantity $\sqrt{\mathbf{s}_t}$ is a running estimate of the typical magnitude of each coordinate's gradient. Dividing by it normalises the step: coordinates with steep, volatile gradients receive *smaller* steps, while coordinates with gentle or rarely non-zero gradients receive *larger* ones. In the ravine picture, the steep cross-ravine direction is damped and the shallow along-ravine direction is boosted, so the optimiser behaves as if the landscape were better conditioned.

The leaky factor $\beta$ is the key difference from its ancestor Adagrad, which accumulates squared gradients with no decay. Adagrad's accumulator can only grow, so its effective learning rate shrinks monotonically and eventually vanishes, which is harmful on non-convex, non-stationary landscapes where useful gradients may appear late. RMSprop's exponential forgetting keeps the denominator tracking only *recent* gradient scale, so learning does not die out.

### Adam (Adaptive Moment Estimation) and Decoupled Weight Decay (AdamW)

Momentum tames direction and RMSprop tames scale; Adam combines both.

> [!abstract] Definition: Adam Optimiser
> Adam tracks a first-moment estimate $\mathbf{m}_t$ (momentum, decay $\beta_1 \approx 0.9$) and an uncentered second-moment estimate $\mathbf{v}_t$ (squared gradients, decay $\beta_2 \approx 0.999$), corrects both for their zero initialisation, and updates:
> $$
> \begin{aligned}
> \mathbf{m}_t &= \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1)\mathbf{g}_t, & \hat{\mathbf{m}}_t &= \frac{\mathbf{m}_t}{1 - \beta_1^t} \\
> \mathbf{v}_t &= \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2)(\mathbf{g}_t \odot \mathbf{g}_t), & \hat{\mathbf{v}}_t &= \frac{\mathbf{v}_t}{1 - \beta_2^t} \\
> \theta_{t+1} &= \theta_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \odot \hat{\mathbf{m}}_t
> \end{aligned}
> $$

Why the correction terms? Both moment buffers start at $\mathbf{m}_0 = \mathbf{v}_0 = \mathbf{0}$, so in the first iterations they are biased towards zero. Unrolling the first-moment recursion gives

$$
\mathbf{m}_t = (1 - \beta_1)\sum_{k=1}^{t} \beta_1^{\,t-k}\mathbf{g}_k.
$$

Take expectations and assume, for the derivation, that the gradient has a stationary mean, $\mathbb{E}[\mathbf{g}_k] = \mathbb{E}[\mathbf{g}]$ for all $k$:

$$
\begin{aligned}
\mathbb{E}[\mathbf{m}_t] &= (1 - \beta_1)\,\mathbb{E}[\mathbf{g}]\sum_{k=1}^{t}\beta_1^{\,t-k} \\
&= (1 - \beta_1)\,\mathbb{E}[\mathbf{g}]\,\frac{1 - \beta_1^t}{1 - \beta_1} \\
&= \mathbb{E}[\mathbf{g}]\,(1 - \beta_1^t).
\end{aligned}
$$

So $\mathbf{m}_t$ underestimates the true mean by exactly the factor $1 - \beta_1^t$, and dividing by it yields an unbiased estimate. The identical argument with $\mathbf{g}_t \odot \mathbf{g}_t$ and $\beta_2$ gives the $1 - \beta_2^t$ correction for $\mathbf{v}_t$. As $t$ grows, $\beta^t \to 0$ and the corrections fade to $1$. Because $\beta_2$ is so close to $1$, the second-moment correction matters for many more iterations than the first. $\blacksquare$

The final update divides the smoothed direction $\hat{\mathbf{m}}_t$ by the per-coordinate scale $\sqrt{\hat{\mathbf{v}}_t}$, so each parameter moves by roughly $\eta$ per step regardless of the raw gradient magnitude. This makes Adam fast and relatively insensitive to the initial scale of gradients, which is why it is a popular default for complex architectures and sparse gradients.

**AdamW** addresses a subtle problem with regularisation. If an $L_2$ penalty (Section 3.3) is added to the loss, its gradient $\lambda\mathbf{W}$ enters $\mathbf{g}_t$ and is then divided by $\sqrt{\hat{\mathbf{v}}_t}$ along with everything else, so the effective shrinkage differs from coordinate to coordinate and no longer behaves like true weight decay. AdamW *decouples* the two: the adaptive step is computed from the loss gradient only, and the weights are shrunk by a separate multiplicative term $\eta\lambda\theta_t$ applied directly to the parameters.

### Comparative Synthesis: Selecting an Optimiser by Use Case

All the optimisers above can be viewed as answers to one question: *what should we do with a noisy, ill-conditioned gradient signal?* Momentum smooths the direction, RMSprop equalises per-coordinate scale, and Adam does both. The table summarises how they differ and where each tends to shine.

| Optimiser | What it adapts | Extra state per parameter | Typical behaviour | Typical use case |
| :--- | :--- | :--- | :--- | :--- |
| SGD (mini-batch) | Nothing; fixed scalar $\eta$ | None | Slow, oscillates in ravines, very sensitive to $\eta$ | Baseline; theoretical analysis |
| SGD + Momentum | Direction (smoothed gradient) | One buffer ($\mathbf{v}$) | Faster along persistent directions, damps oscillation; needs a tuned $\eta$ and schedule | Well-tuned vision tasks, often reaching flat minima that generalise well |
| RMSprop | Per-coordinate scale | One buffer ($\mathbf{s}$) | Balanced step sizes, handles non-stationary, noisy objectives | Noisy or non-stationary objectives |
| Adam / AdamW | Direction and per-coordinate scale | Two buffers ($\mathbf{m}$, $\mathbf{v}$) | Fast convergence, robust to gradient scale; AdamW gives proper weight decay | Sparse gradients and complex, deep architectures |

> [!note] Reading an Optimiser Comparison
> When the trajectories of these optimisers are compared on the same loss, the theory predicts the pattern: plain SGD zigzags and is slow; momentum overshoots slightly but then accelerates along the valley; RMSprop and Adam take more direct paths because per-coordinate scaling removes the ravine's disparity in steepness. Adaptive methods tend to converge faster early, but faster is not automatically *better generalising*: SGD with momentum and a decaying schedule is often favoured when the final test performance of a carefully tuned model matters most, whereas Adam-type methods are favoured when fast, low-tuning convergence is the priority. There is no universally best optimiser; the right choice balances convergence speed, stability, tuning effort, memory (extra buffers cost memory, a point revisited in Section 5.3), and generalisation.

## 3.3 Overfitting and Regularisation Mechanisms

### Generalisation Gap, Bias-Variance, and Overfitting

A network that drives its training loss to zero has not necessarily learned anything useful; it may have memorised. We therefore distinguish the loss we *minimise* from the loss we *care about*.

> [!abstract] Definition: Overfitting and Generalisation Gap
> The empirical training risk $\hat{\mathcal{R}}_{\text{train}}(\theta)$ is the average loss over the finite training sample, while the population (test) risk $\mathcal{R}_{\text{test}}(\theta)$ is the expected loss over the true data distribution. The **generalisation gap** is $\mathcal{R}_{\text{test}}(\theta) - \hat{\mathcal{R}}_{\text{train}}(\theta)$. A model **overfits** when the training risk keeps decreasing while the test risk stagnates or increases, so the gap widens.

This is the variance side of the bias-variance trade-off. A model that is too simple has high bias and underfits; a model that is too flexible has high variance and fits the noise in the particular training sample. Modern deep networks are usually over-parameterised, with enough capacity to fit even random noise, so without a counterweight they readily memorise. **Regularisation** is any modification to the learning procedure that reduces the generalisation gap, typically by trading a small increase in training error for a larger decrease in test error. Early stopping on validation loss, mentioned with the stopping criteria of Section 2.1, is one such mechanism; the rest of this section covers explicit ones.

### Parameter Norm Penalties: $L_2$ (Weight Decay) and $L_1$ Regularisation

The most direct way to discourage complex fits is to penalise large weights, since wildly varying functions generally require large weights. We add a penalty $\Omega(\theta)$ to the objective:

$$
\tilde{\mathcal{L}}(\theta) = \mathcal{L}(\theta) + \Omega(\theta).
$$

**$L_2$ regularisation (Ridge / weight decay)** uses $\Omega(\theta) = \frac{\lambda}{2}\|\mathbf{W}\|_2^2$, where $\lambda \ge 0$ sets the strength of the penalty. Its gradient is $\lambda\mathbf{W}$, so

$$
\nabla_{\mathbf{W}}\tilde{\mathcal{L}} = \nabla_{\mathbf{W}}\mathcal{L} + \lambda\mathbf{W}.
$$

Substituting into the gradient descent update gives

$$
\mathbf{W}_{t+1} = \mathbf{W}_t - \eta\left(\nabla_{\mathbf{W}}\mathcal{L} + \lambda\mathbf{W}_t\right) = (1 - \eta\lambda)\mathbf{W}_t - \eta\nabla_{\mathbf{W}}\mathcal{L}.
$$

This explains the name *weight decay*: at every step each weight is first multiplied by the factor $1 - \eta\lambda < 1$ (shrinkage proportional to its size) and then moved along the loss gradient. Weights survive only if the data gradient keeps pushing them, so parameters that are not useful decay towards small values and the function becomes smoother.

**$L_1$ regularisation (Lasso)** uses $\Omega(\theta) = \lambda\|\mathbf{W}\|_1$, giving

$$
\nabla_{\mathbf{W}}\tilde{\mathcal{L}} = \nabla_{\mathbf{W}}\mathcal{L} + \lambda\operatorname{sign}(\mathbf{W}).
$$

Here the shrinkage per step is a *constant* amount $\eta\lambda$ towards zero regardless of the weight's size, rather than a fraction of it. Small weights are therefore driven all the way to exactly zero, which yields **sparse** weight matrices and acts like automatic feature selection.

> [!note] $L_2$ vs. $L_1$
> $L_2$ shrinks all weights smoothly and proportionally, rarely producing exact zeros, and prefers spreading weight across many features. $L_1$ shrinks at a constant rate and produces exact zeros, preferring sparse solutions. Both introduce a bias in exchange for lower variance, with $\lambda$ controlling the trade-off.

### Dropout: Stochastic Subnetwork Ensembling

Penalties act on the weights; dropout acts on the *architecture*. The idea is to randomly silence neurons during training so that no neuron can rely on the presence of specific others.

> [!abstract] Definition: Inverted Dropout
> During training, with drop probability $p$, sample for each layer a Bernoulli mask $\mathbf{r}^{(l)} \sim \operatorname{Bernoulli}(1-p)$ elementwise (entry $1$ means keep) and compute
> $$
> \tilde{\mathbf{a}}^{(l)} = \frac{1}{1-p}\left(\mathbf{r}^{(l)} \odot \mathbf{a}^{(l)}\right).
> $$
> At inference time no mask and no scaling are applied: the layer is the identity.

The factor $\frac{1}{1-p}$ is what makes this the *inverted* version. Each activation is kept with probability $1-p$, so $\mathbb{E}[\tilde{\mathbf{a}}^{(l)}] = \mathbf{a}^{(l)}$: rescaling during training keeps the expected activation the same as at test time, so inference needs no special correction.

Why does this regularise? A fresh mask is drawn for every mini-batch, so the network trained at each step is a different "thinned" subnetwork. Since a neuron cannot count on any particular partner being present, it is forced to learn features that are useful on their own and in many contexts, breaking complex **co-adaptations**. With $K$ droppable units there are $2^K$ possible subnetworks, all sharing weights, so training approximates training an exponentially large ensemble. The deterministic full network used at inference approximates the (geometric) average of the predictions of this ensemble, and ensembles generally have lower variance than single models.

### Batch Normalisation

Regularisation is not the only way to help training. Batch normalisation attacks a different difficulty: the distribution of the inputs to each layer keeps shifting as earlier layers update, which makes optimisation delicate. It standardises the pre-activations within each mini-batch.

> [!abstract] Definition: Batch Normalisation Transformation
> For a mini-batch $\mathcal{B}$ of pre-activations $z_i$, compute the batch statistics $\mu_{\mathcal{B}}$ and $\sigma_{\mathcal{B}}^2$ (mean and variance over the batch, per feature). Standardise
> $$
> \hat{z}_i = \frac{z_i - \mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}},
> $$
> and then apply a learnable affine restoration
> $$
> y_i = \gamma\hat{z}_i + \beta,
> $$
> where $\gamma$ and $\beta$ are trained by backpropagation. During training the layer also maintains running exponential moving averages of $\mu_{\mathcal{B}}$ and $\sigma_{\mathcal{B}}^2$, which replace the batch statistics at inference time.

The learnable $\gamma$ and $\beta$ matter: pure standardisation would force every layer's output to zero mean and unit variance, which may be a poor choice for the next nonlinearity. The affine step lets the network recover any scale and shift it prefers, including the identity transformation, so representational power is not lost. The running averages are needed because at inference the prediction for one sample must not depend on whatever other samples happen to be in its batch.

Batch normalisation helps in several connected ways:

- **Smoother loss surface:** by controlling the scale of activations it makes the loss and its gradients change more gently with the parameters (a smaller effective Lipschitz constant), so gradients are more predictive.
- **Higher learning rates:** a smoother surface means the stability limit $2/\lambda_{\max}$ of Section 3.1 is effectively relaxed, so larger $\eta$ and faster training become safe.
- **Reduced saturation:** keeping pre-activations in a moderate range prevents sigmoid or tanh units from drifting into their flat regions, which alleviates the vanishing gradients of Section 2.3.
- **Implicit regularisation:** the batch statistics depend on which samples were drawn, injecting mild random noise into every activation, which acts as a regulariser similar in spirit to dropout.

> [!note] Why Biases Before Batch Normalisation Are Redundant
> Subtracting the batch mean removes any constant added by a bias term, and the learnable shift $\beta$ takes over its role. A layer immediately followed by batch normalisation can therefore omit its own bias.

> [!summary] Section 3 in One Paragraph
> The learning rate must satisfy a curvature-imposed stability bound and is best varied over time with warmup followed by decay. Mini-batch SGD supplies unbiased but noisy gradients; momentum smooths their direction, RMSprop equalises their per-coordinate scale, and Adam combines both with bias correction (with AdamW fixing weight decay). No optimiser dominates universally, so the choice trades speed, tuning effort, memory, and generalisation. To close the generalisation gap, $L_2$ and $L_1$ penalties constrain the weights, dropout trains an implicit ensemble of subnetworks, and batch normalisation stabilises activations while also adding a regularising noise.

---

# 4. Cost Functions & High-Dimensional Loss Landscapes

In the training loop we kept saying "evaluate the loss, then backpropagate." But the loss is not a neutral bookkeeping device. It is the *only* signal the network ever receives about what we want. Every gradient that flows backward starts from $\nabla \mathcal{L}$, so the shape of $\mathcal{L}$ decides which errors the network cares about, how loudly it hears them, and how the optimiser moves through parameter space. In this section we first study the standard cost functions for regression and classification (and what each one silently assumes about the data), then zoom out to the geometry of the surface $\mathcal{L}(\theta)$ that these costs create in millions of dimensions.

## 4.1 Regression Cost Functions and Outlier Sensitivity

When the target $y_i \in \mathbb{R}$ is a continuous quantity, the network outputs a prediction $\hat{y}_i$ and the cost must turn the residual $e_i = y_i - \hat{y}_i$ into a non-negative penalty. The three classical choices differ in one thing only: how the penalty grows as $|e_i|$ grows. That single design decision determines outlier robustness, gradient behaviour near the optimum, and even which statistic of the data the network learns to predict.

### Mean Squared Error (MSE / $L_2$ Loss)

Squaring the residual is the most natural first idea: it is non-negative, smooth, and differentiable everywhere.

> [!abstract] Definition: Mean Squared Error (MSE)
> $$
> \mathcal{L}_{\text{MSE}}(\mathbf{y}, \hat{\mathbf{y}}) = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2
> $$

Why this particular form, rather than, say, a fourth power? The answer comes from probability. Suppose the data are generated as $y_i = f_\theta(\mathbf{x}_i) + \varepsilon_i$ with additive noise $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$, independent across samples. Then $y_i \mid \mathbf{x}_i \sim \mathcal{N}(\hat{y}_i, \sigma^2)$ with $\hat{y}_i = f_\theta(\mathbf{x}_i)$, and the maximum likelihood estimate maximises the log-likelihood of the observed targets.

**Derivation (MSE as Gaussian MLE):** The log-likelihood is
$$
\begin{aligned}
\log p(\mathbf{y} \mid \mathbf{X}, \theta) &= \sum_{i=1}^N \log \left[ \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\left( -\frac{(y_i - \hat{y}_i)^2}{2\sigma^2} \right) \right] \\
&= -\frac{N}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^N (y_i - \hat{y}_i)^2 .
\end{aligned}
$$
The first term does not depend on $\theta$, and $\frac{1}{2\sigma^2}$ is a positive constant. Maximising the log-likelihood is therefore the same as minimising $\sum_i (y_i - \hat{y}_i)^2$, which is $N$ times the MSE. So MSE is not an arbitrary choice; it is exactly what we get when we believe the noise is Gaussian. $\blacksquare$

A useful by-product is that the minimiser of the squared error over a constant prediction is the *mean* of the targets, so a network trained with MSE learns to predict the conditional mean $\mathbb{E}[y \mid \mathbf{x}]$.

The gradient with respect to a prediction is
$$
\frac{\partial \mathcal{L}_{\text{MSE}}}{\partial \hat{y}_i} = -\frac{2}{N}(y_i - \hat{y}_i).
$$
Read this carefully, because it contains both the strength and the weakness of MSE. The gradient is *linear* in the residual: as the prediction approaches the target, the gradient shrinks smoothly to zero, which gives gentle, stable convergence without extra tricks. But the same linearity means that a sample with a huge residual produces a huge gradient, and the quadratic penalty $(y_i - \hat{y}_i)^2$ lets a handful of outliers dominate the entire update. This extreme sensitivity is a flaw when outliers are corrupted measurements, yet it is a desirable property when large deviations are genuinely catastrophic (for example, when under-forecasting a very large demand must be punished hard).

### Mean Absolute Error (MAE / $L_1$ Loss)

If outliers worry us, the obvious remedy is to penalise the residual only linearly.

> [!abstract] Definition: Mean Absolute Error (MAE)
> $$
> \mathcal{L}_{\text{MAE}}(\mathbf{y}, \hat{\mathbf{y}}) = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|
> $$

Just as MSE corresponds to Gaussian noise, MAE is the maximum likelihood objective under *Laplacian* noise, whose density is $p(\varepsilon) \propto \exp(-|\varepsilon|/b)$. Repeating the log-likelihood calculation above, the quadratic term is replaced by $-\frac{1}{b}\sum_i |y_i - \hat{y}_i|$, so maximising likelihood means minimising the sum of absolute residuals. Heavy-tailed Laplacian noise assigns non-negligible probability to large errors, which is precisely why MAE does not panic about them. Statistically, the minimiser of the absolute error over a constant prediction is the *median*, so an MAE-trained network predicts the conditional median rather than the conditional mean.

Its (sub)gradient is
$$
\frac{\partial \mathcal{L}_{\text{MAE}}}{\partial \hat{y}_i} = -\frac{1}{N}\operatorname{sign}(y_i - \hat{y}_i).
$$
Here the gradient magnitude is bounded and does not depend on how large the residual is, so a corrupted target pulls on the weights no harder than any other mistaken sample. That is the source of MAE's robustness. The price is paid near the optimum: $|e|$ has a kink at $e_i = 0$, where the derivative is undefined (we only have a subgradient), and because the gradient magnitude never shrinks as we approach the minimum, a fixed learning rate keeps bouncing across it. Without learning-rate decay, training with MAE oscillates around the minimum instead of settling.

### Huber Loss (Smooth $L_1$ Loss)

MSE converges nicely but fears outliers; MAE ignores outliers but cannot settle. Huber loss stitches the good half of each together: quadratic where residuals are small, linear where they are large.

> [!abstract] Definition: Huber Loss
> For a threshold $\delta > 0$,
> $$
> \mathcal{L}_\delta(y, \hat{y}) = \begin{cases} \frac{1}{2}(y - \hat{y})^2 & \text{if } |y - \hat{y}| \le \delta \\ \delta\left(|y - \hat{y}| - \frac{1}{2}\delta\right) & \text{if } |y - \hat{y}| > \delta \end{cases}
> $$

The constants in the second branch are not arbitrary. At $|e| = \delta$ the first branch equals $\frac{1}{2}\delta^2$, and the second equals $\delta(\delta - \frac{1}{2}\delta) = \frac{1}{2}\delta^2$, so the function is continuous. The derivatives with respect to $e$ are $e$ on the inner branch and $\delta\operatorname{sign}(e)$ on the outer branch, which both equal $\pm\delta$ at the junction, so the derivative is continuous too. In other words, the gradient behaves like MSE's (shrinking smoothly to zero) in the well-fitted core and like MAE's (bounded by $\pm\delta$) in the tails. The threshold $\delta$ is a hyperparameter that says "residuals bigger than this count as outliers."

The three losses side by side:

| Property | MSE ($L_2$) | MAE ($L_1$) | Huber ($\delta$) |
| --- | --- | --- | --- |
| Functional form | $e^2$ | $\lvert e\rvert$ | Quadratic for $\lvert e\rvert \le \delta$, linear beyond |
| Derivative w.r.t. $\hat{y}$ | Linear in $e$, unbounded | $\pm 1$, bounded, undefined at $0$ | Linear inside $\delta$, saturates at $\pm\delta$ |
| Statistical estimator (noise model) | Conditional mean (Gaussian) | Conditional median (Laplacian) | Between mean and median |
| Outlier robustness | Low | High | High beyond $\delta$ |
| Optimisation behaviour | Smooth, self-damping near the optimum | Constant-size steps, oscillates near the optimum | Smooth near optimum and stable in tails |

> [!note] Choosing a regression loss
> The loss is really a statement about your noise. Gaussian noise and costly large errors point to MSE; contaminated targets point to MAE; and when you want smooth convergence plus protection against occasional wild targets, Huber is the compromise, at the price of tuning $\delta$.

## 4.2 Classification Cost Functions and Class Imbalance

For classification the network outputs a *probability*, and the natural way to score a probability is by the likelihood it assigned to the truth. This makes cross-entropy, rather than squared error, the standard cost. We will also see why that choice matters for the *gradients*, and how it can still fail when classes are badly imbalanced.

### Binary Cross-Entropy (BCE) Loss

Take a binary label $y_i \in \{0, 1\}$ and a network that produces a real-valued **logit** $z_i$, turned into a probability by the sigmoid $\hat{p}_i = \sigma(z_i) = \frac{1}{1 + e^{-z_i}}$.

> [!abstract] Definition: Binary Cross-Entropy Loss
> $$
> \mathcal{L}_{\text{BCE}}(y, \hat{p}) = -\frac{1}{N}\sum_{i=1}^N \big[y_i \log(\hat{p}_i) + (1 - y_i)\log(1 - \hat{p}_i)\big]
> $$

**Derivation from the Bernoulli likelihood:** If $y_i \mid \mathbf{x}_i \sim \operatorname{Bernoulli}(\hat{p}_i)$, then $p(y_i \mid \mathbf{x}_i) = \hat{p}_i^{\,y_i}(1 - \hat{p}_i)^{1 - y_i}$. Taking the logarithm of the product over independent samples gives $\sum_i [y_i \log \hat{p}_i + (1 - y_i)\log(1 - \hat{p}_i)]$. Maximising this is equivalent to minimising its negative average, which is $\mathcal{L}_{\text{BCE}}$. $\blacksquare$

The intuition is easy to read off: when $y_i = 1$ only $-\log \hat{p}_i$ survives, which is near zero if the network is confident and correct and blows up as $\hat{p}_i \to 0$; the case $y_i = 0$ is symmetric. Confident mistakes are punished very hard.

Why not simply use MSE on the sigmoid output? The answer lies in the gradient with respect to the logit.

> [!theorem] BCE Gradient with Respect to the Logit
> For $\hat{p}_i = \sigma(z_i)$,
> $$
> \frac{\partial \mathcal{L}_{\text{BCE}}}{\partial z_i} = \frac{1}{N}(\hat{p}_i - y_i).
> $$

**Proof:** Work with the single-sample loss $\ell = -[y\log \hat{p} + (1-y)\log(1-\hat{p})]$ and apply the chain rule through $\hat{p} = \sigma(z)$. First,
$$
\frac{\partial \ell}{\partial \hat{p}} = -\frac{y}{\hat{p}} + \frac{1-y}{1-\hat{p}} = \frac{\hat{p} - y}{\hat{p}(1-\hat{p})}.
$$
Second, the sigmoid derivative is $\frac{\partial \hat{p}}{\partial z} = \sigma(z)(1 - \sigma(z)) = \hat{p}(1-\hat{p})$. Multiplying,
$$
\frac{\partial \ell}{\partial z} = \frac{\hat{p} - y}{\hat{p}(1-\hat{p})} \cdot \hat{p}(1-\hat{p}) = \hat{p} - y .
$$
The saturating factor $\hat{p}(1-\hat{p})$ cancels exactly. Averaging over the $N$ samples gives the factor $\frac{1}{N}$. $\blacksquare$

This cancellation is the whole point. If we had used MSE on the probability, the chain rule would give $-(y - \hat{p}) \cdot \hat{p}(1-\hat{p})$, and the sigmoid factor vanishes whenever the unit saturates. A network that is *confidently wrong* (large $|z|$, wrong side) would then receive almost no gradient and learn extremely slowly: the exact opposite of what we want. With BCE the gradient is simply "prediction minus target": large when wrong, small when right, regardless of saturation.

> [!warning] Numerical stability and `BCEWithLogitsLoss`
> Computing $\sigma(z)$ first and then $\log(\sigma(z))$ is numerically fragile: for large $|z|$ the sigmoid rounds to exactly $0$ or $1$ in floating point, and the logarithm returns $-\infty$ or the term $\log(1-\hat p)$ underflows. The fix is to fuse the sigmoid and the loss into a single expression evaluated with the **log-sum-exp trick**, which works directly on the logit $z$ without ever forming an extreme probability. This fused layer is what `BCEWithLogitsLoss` implements, which is why in practice the final layer of a binary classifier outputs raw logits and *no* sigmoid is applied before the loss. In the customer-churn pipeline of this module, the network's last linear layer therefore feeds `BCEWithLogitsLoss` directly.

### Categorical Cross-Entropy Loss and Softmax

With $C$ mutually exclusive classes, the network outputs a logit vector $\mathbf{z} \in \mathbb{R}^C$, and the sigmoid is generalised by the softmax, which makes the outputs positive and sum to one.

> [!abstract] Definition: Softmax and Categorical Cross-Entropy
> $$
> \hat{p}_c = \frac{e^{z_c}}{\sum_{j=1}^C e^{z_j}}, \qquad \mathcal{L}_{\text{CE}}(\mathbf{y}, \hat{\mathbf{p}}) = -\sum_{c=1}^C y_c \log(\hat{p}_c)
> $$
> where $\mathbf{y}$ is a one-hot label vector.

Because $\mathbf{y}$ is one-hot, only the term of the true class $k$ survives, so $\mathcal{L}_{\text{CE}} = -\log \hat{p}_k$: we penalise the negative log-probability assigned to the correct class. BCE is simply the $C=2$ special case.

There is a clean information-theoretic reading. The cross-entropy between the true distribution $\mathbf{y}$ and the model distribution $\hat{\mathbf{p}}$ is $H(\mathbf{y}, \hat{\mathbf{p}}) = -\sum_c y_c \log \hat{p}_c$, and it splits as
$$
D_{\text{KL}}(\mathbf{y} \parallel \hat{\mathbf{p}}) = H(\mathbf{y}, \hat{\mathbf{p}}) - H(\mathbf{y}).
$$
The entropy $H(\mathbf{y})$ of the labels does not depend on the model parameters (and equals zero for one-hot labels), so minimising cross-entropy is exactly the same as minimising the KL divergence from the true label distribution to the predicted one. Training the classifier means pulling the predicted distribution toward the true one.

> [!theorem] Softmax Cross-Entropy Gradient with Respect to the Logits
> $$
> \frac{\partial \mathcal{L}_{\text{CE}}}{\partial \mathbf{z}} = \hat{\mathbf{p}} - \mathbf{y}
> $$

**Proof:** Write $\mathcal{L}_{\text{CE}} = -\sum_c y_c\left(z_c - \log\sum_j e^{z_j}\right) = -\sum_c y_c z_c + \log\sum_j e^{z_j}$, using $\sum_c y_c = 1$. Differentiating with respect to a single logit $z_m$:
$$
\frac{\partial \mathcal{L}_{\text{CE}}}{\partial z_m} = -y_m + \frac{e^{z_m}}{\sum_j e^{z_j}} = \hat{p}_m - y_m .
$$
Stacking over $m = 1, \dots, C$ gives the vector result. $\blacksquare$

As in the binary case, the logarithm of the loss cancels the exponential of the softmax, and the error signal reaching the output layer is just "predicted probabilities minus one-hot truth." This is also the output-layer error $\boldsymbol{\delta}^{(L)}$ that starts the backward pass of Section 2.

### Class Imbalance Pathology and Focal Loss

Cross-entropy is statistically principled, yet it can still mislead badly on **imbalanced** data. Think of screening for a rare disease, or of the telecom churn problem where most customers (well over four in five) do not churn. The loss is a sum over samples, so the majority class contributes far more terms than the minority class.

Here is the mechanism. Let $p_t$ denote the probability the model assigns to the *true* class of a sample. For an easy, well-classified negative, $p_t$ is already large, so its loss $-\log(p_t)$ is small but not zero. Individually negligible, these tiny losses and their tiny gradients are added up over thousands of easy majority samples, and collectively they can overwhelm the gradient signal from the few rare, hard positives. The optimiser then finds that the cheapest way to reduce the total loss is to become very good at the majority class and to be lazy about the minority class.

> [!warning] High accuracy does not mean a good model
> This is exactly what happened in the churn case study: the network reached a respectable overall accuracy (about $76\%$) while its recall on the churners, the minority class we actually care about, was poor. Accuracy is dominated by the majority class, so it hides the failure, while recall on the minority class exposes it. On imbalanced problems one must therefore monitor minority-class precision/recall, and consider re-weighting the loss (for example with a positive-class weight in `BCEWithLogitsLoss`) or changing the loss itself, as focal loss does.

Focal loss attacks the problem at its root by *down-weighting easy examples automatically*. To state it compactly, define the probability of the true class
$$
p_t = \begin{cases} p & \text{if } y = 1 \\ 1 - p & \text{otherwise.} \end{cases}
$$
Then cross-entropy is simply $-\log(p_t)$, for both classes.

> [!abstract] Definition: Focal Loss (Lin et al.)
> With a class-balancing weight $\alpha_t \in [0, 1]$ and a focusing parameter $\gamma \ge 0$,
> $$
> \mathcal{L}_{\text{Focal}}(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)
> $$

Let us unpack the two knobs. The weight $\alpha_t$ is a static class-balancing factor (typically larger for the rare class). The new ingredient is the **modulating factor** $(1 - p_t)^\gamma$. For an easy example, $p_t \to 1$, so $(1 - p_t) \to 0$ and the factor $(1-p_t)^\gamma$ vanishes, and for $\gamma > 0$ it vanishes faster the larger $\gamma$ is. That means easy examples are suppressed by a large multiplicative factor. For a hard, misclassified example, $p_t$ is small, $(1-p_t)$ is close to $1$, and the loss is almost unchanged. The net effect is that gradient updates are dynamically concentrated on hard examples (which, in an imbalanced problem, are mostly minority samples) instead of being drowned by the crowd of easy ones. Setting $\gamma = 0$ recovers ordinary (class-weighted) cross-entropy, so $\gamma$ is a dial that controls how aggressively easy examples are ignored.

## 4.3 Navigating High-Dimensional Loss Landscapes

Having chosen a cost function, we obtain a surface $\mathcal{L}(\theta)$ over the parameter space $\theta \in \mathbb{R}^d$, where $d$ can be in the millions or billions. Training is a walk on this surface. Our low-dimensional intuition (a bowl with one bottom, or a mountain range with many tempting valleys) is a poor guide here, so this subsection builds the correct picture.

### Critical Points: Local Minima vs. Saddle Points

A gradient-based optimiser stalls wherever the gradient vanishes, so we start by naming those places.

> [!abstract] Definition: Critical Points and Saddle Points
> A point $\theta^*$ is a **critical point** of $\mathcal{L}$ if $\nabla_\theta \mathcal{L}(\theta^*) = \mathbf{0}$. A critical point that is neither a local minimum nor a local maximum is a **saddle point**: the loss curves upward along some directions and downward along others.

In two dimensions, local minima feel like the main danger. In very high dimensions, the picture changes, and a heuristic probabilistic argument shows why. At a critical point, whether it is a minimum, maximum or saddle is decided by the signs of the $d$ eigenvalues of the Hessian. If we model the sign of each eigenvalue at a randomly located critical point as positive with probability $\tfrac{1}{2}$, independently, then a true local minimum requires *all* $d$ eigenvalues to be positive, which has probability
$$
\left(\tfrac{1}{2}\right)^d = 2^{-d} \approx 0 \quad \text{for } d \sim 10^6 \text{ to } 10^9 .
$$
The same holds for a local maximum, so almost every critical point has a mix of positive and negative curvature and is therefore a saddle. High-dimensional non-convex landscapes are thus dominated by saddle points rather than bad local minima. Near a saddle the gradient is tiny along flat directions, so progress can stall on a plateau, even though there are escape directions along which the loss decreases. This is why the main practical difficulty is not "being trapped in a bad valley" but slow progress through flat, saddle-rich regions.

> [!note] A heuristic, not a theorem
> The independence-and-probability-$\tfrac12$ assumption is an idealisation meant to convey the scaling: the chance that *every* direction curves upward shrinks exponentially with dimension. Its message, that saddles vastly outnumber minima, is what we carry forward.

### Hessian Curvature and Ill-Conditioning

To tell the critical points apart, and to understand why the optimiser zigzags, we need second-order information, which is captured by the Hessian.

> [!abstract] Definition: Hessian Matrix and Local Curvature
> $$
> \mathbf{H} = \nabla^2_\theta \mathcal{L}(\theta) \in \mathbb{R}^{d \times d}, \qquad \mathcal{L}(\theta + \Delta\theta) \approx \mathcal{L}(\theta) + \nabla_\theta \mathcal{L}^\top \Delta\theta + \frac{1}{2} \Delta\theta^\top \mathbf{H} \Delta\theta
> $$

The Hessian is symmetric, so it has real eigenvalues $\lambda_i$ with orthogonal eigenvectors. In the quadratic approximation, moving a distance $s$ along the eigenvector of $\lambda_i$ changes the loss by $\frac{1}{2}\lambda_i s^2$ (plus the gradient term), so each eigenvalue is the curvature along its own direction. The signs classify a critical point:

- **All $\lambda_i > 0$ (positive definite):** an upward bowl in every direction, a local minimum.
- **All $\lambda_i < 0$ (negative definite):** a downward dome in every direction, a local maximum.
- **Mixed signs (indefinite):** a saddle point, with escape directions along eigenvectors with negative eigenvalues.
- **Some $\lambda_i \approx 0$ (degenerate):** flat directions, a plateau where first-order gradient information stalls.

Curvature also governs how hard the problem is for first-order methods. Eigenvalues of very different magnitudes mean the surface is steep in some directions and nearly flat in others.

> [!abstract] Definition: Condition Number
> $$
> \kappa(\mathbf{H}) = \frac{|\lambda_{\max}|}{|\lambda_{\min}|}
> $$

When $\kappa \gg 1$ the level sets of the loss are long, thin ellipses, forming an elongated **ravine**. The gradient is dominated by the steep direction and therefore points nearly *perpendicular* to the long axis that actually leads to the minimum. Gradient descent then bounces across the narrow walls while crawling slowly along the floor. This also explains the learning-rate constraint from Section 3: the step size must be small enough for the steepest direction ($\lambda_{\max}$), yet that same small step makes progress along the flattest direction ($\lambda_{\min}$) painfully slow. It is exactly the situation that momentum and per-parameter adaptive scaling (RMSprop, Adam) were designed to alleviate.

### Stochastic Gradient Noise and Sharp vs. Flat Minima

Finally, noise plays two very different roles on the loss landscape, and it is worth separating them.

The first kind is *label or measurement noise* in the data itself, which corrupts the targets and degrades the fidelity of every gradient; this is harmful, and it is part of what robust losses such as MAE and Huber try to tolerate. The second kind is *intrinsic mini-batch sampling noise*,
$$
\boldsymbol{\xi}_t = \mathbf{g}_t - \nabla\mathcal{L}(\theta_t),
$$
the difference between the mini-batch gradient estimate and the true full-batch gradient. Unlike the first kind, this noise is often helpful. Its covariance is anisotropic (larger in some directions than others), and it constantly jostles the trajectory. Near a saddle, this jostling helps kick the parameters off the plateau along an escape direction; near a minimum, it can eject the trajectory from a **sharp** minimum, where the Hessian eigenvalues are large and small perturbations raise the loss sharply, and let it settle into a **flat** minimum, where the curvature is low.

Flat minima are generally preferred because they generalise better. A model that sits in a wide, flat basin barely changes its loss when the test distribution shifts the effective loss surface slightly, whereas a model in a narrow sharp basin can be thrown up the walls by the same shift. This is one reason smaller mini-batches (noisier gradients) are often associated with better generalisation, and why the optimiser comparison in Section 3 mentions SGD with momentum for finding flat minima.

> [!summary] Section summary
> The cost function encodes assumptions about the data: MSE assumes Gaussian noise and predicts the mean, MAE assumes Laplacian noise and predicts the median, and Huber blends them. For classification, cross-entropy follows from the Bernoulli/categorical likelihood and yields the clean logit gradient $\hat{\mathbf{p}} - \mathbf{y}$, with `BCEWithLogitsLoss` as the numerically stable fused implementation. On imbalanced data plain cross-entropy yields high accuracy but poor minority recall, which focal loss and class weighting address. The landscape itself is dominated by saddle points rather than local minima, its ill-conditioned curvature creates ravines that slow first-order methods, and mini-batch noise is a helpful ally for escaping saddles and finding flat, well-generalising minima.

---

# 5. Linear Layers, Parameter Counting, & Memory Footprint

Every deep network, no matter how exotic, is built from a small number of repeating blocks, and the workhorse among them is the **linear (dense) layer**. Before we can talk about speed or hardware (that comes in [[#6. Computational Efficiency, Roofline Model, & Hardware Acceleration]]), we need to answer three very practical questions. What exactly does a linear layer compute? How many numbers (parameters) does it store? And how much memory does a whole training run really consume? This section answers them in that order.

## 5.1 Affine Linear Transformations in Neural Networks

### Single-Sample and Batched Matrix Formulations

Think back to the forward pass from Section 2: each layer takes the previous layer's output, mixes its coordinates with a set of weights, and shifts the result by a bias. The linear layer is precisely that "mix and shift" step, and it is called *fully connected* because every input coordinate influences every output coordinate.

> [!abstract] Definition: Dense (Fully Connected / Linear) Layer
> Let $\mathbf{x} \in \mathbb{R}^{d_{\text{in}}}$ be an input vector, $\mathbf{W} \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$ a weight matrix, and $\mathbf{b} \in \mathbb{R}^{d_{\text{out}}}$ a bias vector. The dense layer computes
> $$
> \mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b} \in \mathbb{R}^{d_{\text{out}}}
> $$

In other words, the $i$-th output is $z_i = \sum_{j=1}^{d_{\text{in}}} W_{ij} x_j + b_i$: a weighted sum of all inputs plus an offset. The matrix $\mathbf{W}$ has one row per output neuron and one column per input feature, so $d_{\text{out}}$ is the width of the layer being produced. Strictly speaking, a map of the form $\mathbf{x} \mapsto \mathbf{W}\mathbf{x} + \mathbf{b}$ is **affine** rather than linear (a linear map would have $\mathbf{b} = \mathbf{0}$), but deep learning libraries call the layer "linear" by convention, and we will use both words.

In practice we never push one sample at a time through the network; we process a mini-batch so that the hardware is used efficiently. Stack $B$ samples as the rows of a matrix $\mathbf{X} \in \mathbb{R}^{B \times d_{\text{in}}}$. Because each row of $\mathbf{X}$ is a sample *written as a row*, the weight matrix gets transposed:

$$
\mathbf{Z} = \mathbf{X}\mathbf{W}^\top + \mathbf{1}_B \mathbf{b}^\top \in \mathbb{R}^{B \times d_{\text{out}}}
$$

Here $\mathbf{1}_B \in \mathbb{R}^{B}$ is a column of ones, so $\mathbf{1}_B\mathbf{b}^\top$ simply copies the same bias row onto every sample. Frameworks implement this copy by **broadcasting**, meaning the bias vector is added to each row without ever being physically replicated. The key takeaway is that a batch turns $B$ matrix-vector products into a single matrix-matrix product, which is exactly the operation that GPUs are best at.

> [!note] Same Weights for Every Sample
> The same $\mathbf{W}$ and $\mathbf{b}$ are shared by all $B$ samples in the batch. Batching therefore changes how much *data* flows through the layer, but never how many *parameters* the layer owns. Keep this distinction in mind, because it separates parameter memory from activation memory in Section 5.3.

### Geometric Interpretation and the Necessity of Nonlinearity

What is a linear layer actually doing to the data? Look at one row $\mathbf{w}_i^\top$ of $\mathbf{W}$. The $i$-th output $z_i = \mathbf{w}_i^\top \mathbf{x} + b_i$ measures how far $\mathbf{x}$ lies along the direction $\mathbf{w}_i$, shifted by $b_i$. Setting $z_i = 0$ describes a hyperplane in input space, with $\mathbf{w}_i$ as its normal vector. So each row acts as a **feature detector** that responds strongly to inputs aligned with $\mathbf{w}_i$, and the bias $b_i$ slides the hyperplane away from the origin, acting as an affine threshold offset. A layer with $d_{\text{out}}$ neurons therefore evaluates $d_{\text{out}}$ such oriented, shifted "views" of the input at once.

This sounds powerful, so why do we insist on inserting nonlinear activations between layers? The answer is that without them, stacking layers buys us nothing. This is made precise below.

> [!theorem] Collapse of Stacked Linear Layers
> Consider $L$ affine layers composed without any nonlinear activation in between:
> $$
> \mathbf{z}^{(k)} = \mathbf{W}_k \mathbf{z}^{(k-1)} + \mathbf{b}_k, \qquad k = 1, \dots, L, \qquad \mathbf{z}^{(0)} = \mathbf{x}
> $$
> Then there exist a matrix $\mathbf{W}_{\text{eff}}$ and a vector $\mathbf{b}_{\text{eff}}$ such that, for every input $\mathbf{x}$,
> $$
> \mathbf{z}^{(L)} = \mathbf{W}_{\text{eff}}\mathbf{x} + \mathbf{b}_{\text{eff}}
> $$
> where $\mathbf{W}_{\text{eff}} = \mathbf{W}_L \mathbf{W}_{L-1} \cdots \mathbf{W}_1$ and $\mathbf{b}_{\text{eff}} = \sum_{k=1}^{L} \left(\mathbf{W}_L \cdots \mathbf{W}_{k+1}\right)\mathbf{b}_k$, with the empty product for $k = L$ taken to be the identity matrix.

**Proof:** We argue by induction on the number of layers $m$, claiming that after $m$ layers the output is $\mathbf{z}^{(m)} = \mathbf{W}^{[m]}\mathbf{x} + \mathbf{b}^{[m]}$ for some matrix $\mathbf{W}^{[m]}$ and vector $\mathbf{b}^{[m]}$ that do not depend on $\mathbf{x}$.

*Base case ($m = 1$).* By definition $\mathbf{z}^{(1)} = \mathbf{W}_1\mathbf{x} + \mathbf{b}_1$, so the claim holds with $\mathbf{W}^{[1]} = \mathbf{W}_1$ and $\mathbf{b}^{[1]} = \mathbf{b}_1$.

*Inductive step.* Suppose the claim holds for $m - 1$. Feeding that output into layer $m$ gives
$$
\begin{aligned}
\mathbf{z}^{(m)} &= \mathbf{W}_m \mathbf{z}^{(m-1)} + \mathbf{b}_m \\
&= \mathbf{W}_m\left(\mathbf{W}^{[m-1]}\mathbf{x} + \mathbf{b}^{[m-1]}\right) + \mathbf{b}_m \\
&= \underbrace{\left(\mathbf{W}_m \mathbf{W}^{[m-1]}\right)}_{\mathbf{W}^{[m]}}\mathbf{x} + \underbrace{\left(\mathbf{W}_m \mathbf{b}^{[m-1]} + \mathbf{b}_m\right)}_{\mathbf{b}^{[m]}}
\end{aligned}
$$
This is again of the form (matrix)$\,\cdot\,\mathbf{x}\,+\,$(vector), with $\mathbf{W}^{[m]} = \mathbf{W}_m\mathbf{W}^{[m-1]}$ and $\mathbf{b}^{[m]} = \mathbf{W}_m\mathbf{b}^{[m-1]} + \mathbf{b}_m$, neither depending on $\mathbf{x}$. Unrolling these two recursions yields $\mathbf{W}^{[L]} = \mathbf{W}_L \cdots \mathbf{W}_1$ and $\mathbf{b}^{[L]} = \sum_{k=1}^{L}(\mathbf{W}_L\cdots\mathbf{W}_{k+1})\mathbf{b}_k$, which are the stated $\mathbf{W}_{\text{eff}}$ and $\mathbf{b}_{\text{eff}}$. $\blacksquare$

The conclusion is striking: a "deep" stack of $L$ linear layers represents exactly the same family of functions as one layer. A product of matrices is just another matrix, so the extra layers add parameters and compute but no representational power. In fact the rank of $\mathbf{W}_{\text{eff}}$ can never exceed the smallest rank among the factors, so narrow intermediate layers can only restrict the model further.

> [!warning] Depth Without Nonlinearity Is Redundant
> The advantages of depth discussed in Section 1.3 (hierarchical feature reuse, compositional efficiency) rely on a nonlinear activation $\sigma(\cdot)$ between layers. Without it, the composition collapses and the network is merely a single affine model, no more expressive than classical linear regression. The nonlinearity is what prevents the matrices from merging into one.

## 5.2 Parameter Counting and Computational Complexity

### Exact Parameter Counting Formulas for MLPs

How big is a network? The natural measure is the number of trainable scalars it stores, since this drives both memory use and the risk of overfitting. For a linear layer this count is easy to read straight off the definition: $\mathbf{W}$ contributes one scalar per (input, output) pair, and $\mathbf{b}$ one scalar per output.

> [!abstract] Definition: Parameter Count of a Linear Layer
> For layer $l$ mapping $\mathbb{R}^{d_{l-1}} \to \mathbb{R}^{d_l}$,
> $$
> P_{\text{weights}}^{(l)} = d_{l-1} \cdot d_l, \qquad P_{\text{biases}}^{(l)} = d_l, \qquad P_{\text{total}}^{(l)} = (d_{l-1} + 1)\, d_l
> $$

The combined form $(d_{l-1}+1)d_l$ has a neat reading: each of the $d_l$ neurons owns one weight per incoming connection plus one extra bias "weight", which behaves like a connection from a constant input of $1$. Notice that the count depends only on the layer widths, never on the batch size $B$.

For a multilayer perceptron (MLP) with $L$ dense layers and widths $d_0$ (input), $d_1, \dots, d_L$, the parameters of different layers are independent, so we simply add them up:

$$
P_{\text{total}} = \sum_{l=1}^{L} (d_{l-1} + 1)\, d_l
$$

Because the weight term is a *product* of adjacent widths, parameter count grows roughly quadratically when we widen the whole network, but only linearly when we add more layers of fixed width. This is the quantitative backbone of the width-versus-depth trade-off from Section 1.3.

Some layers are deliberately built without a bias, giving $P^{(l)} = d_{l-1}d_l$. A common case is a linear layer that is immediately followed by Batch Normalisation (Section 3.3): the normalisation subtracts the mini-batch mean, which would cancel any constant offset $\mathbf{b}$, and its own learnable shift $\beta$ then plays the role of the bias. Keeping $\mathbf{b}$ would simply waste parameters.

### FLOPs and MACs in Forward and Backward Passes

Parameters measure *storage*; we also care about *work*. The basic unit of work in a linear layer is the **multiply-accumulate (MAC)**: one multiplication followed by adding the product to a running total. Computing a single output entry $z_i$ of one sample needs $d_{\text{in}}$ MACs (one per input coordinate). There are $d_{\text{out}}$ outputs per sample and $B$ samples, so the forward pass of the layer costs

$$
\text{MACs} = B \cdot d_{\text{in}} \cdot d_{\text{out}}
$$

Each MAC consists of two floating-point operations (a multiply and an add), hence

$$
\text{FLOPs}_{\text{fwd}} \approx 2 \cdot B \cdot d_{\text{in}} \cdot d_{\text{out}}
$$

where we ignore the bias addition, which costs only $B\,d_{\text{out}}$ operations and is negligible next to the matrix product.

What about the backward pass? From the backpropagation equations of Section 2.2, the layer needs two separate products. Let $\boldsymbol{\delta} \in \mathbb{R}^{B \times d_{\text{out}}}$ denote the batch of backpropagated error signals at the layer's output. The first product gives the weight gradient, and the second passes the error to the layer below:

$$
\nabla_{\mathbf{W}}\mathcal{L} = \boldsymbol{\delta}^\top \mathbf{X}, \qquad \nabla_{\mathbf{X}}\mathcal{L} = \boldsymbol{\delta}\,\mathbf{W}
$$

Each is a matrix-matrix product whose three dimensions are again $B$, $d_{\text{in}}$ and $d_{\text{out}}$, so each costs about the same $2 B d_{\text{in}} d_{\text{out}}$ FLOPs as the forward product. The backward pass therefore costs roughly $2\times$ the forward pass, and one full training step (forward plus backward) costs about $3\times$ the forward FLOPs. Inference, which needs only the forward pass, is correspondingly cheaper.

> [!note] Capacity-Complexity Trade-Off
> More parameters mean more representational capacity, but also more memory, more FLOPs per step, and a greater tendency to memorise noise (Section 3.3). The goal is to match the parameter count to the complexity of the task and the size of the dataset: too small a model underfits, while an oversized one wastes memory and compute and invites overfitting.

## 5.3 Anatomy of Neural Network Memory Footprint

A common surprise for newcomers is that a model with $P$ parameters needs far more than $P$ numbers' worth of GPU memory (VRAM) to *train*. The reason is that the parameters are only one of several tensors that must coexist. We split the footprint into a **static** part, which scales with $P$, and a **dynamic** part, which scales with the batch.

### Static Model Memory: Parameters, Gradients, and Optimiser States

Suppose the model has $P$ parameters and each element is stored with a given precision in bytes per element. Three buckets of memory are proportional to $P$:

1. **Model weights ($\theta$):** the parameters themselves,
   $$
   M_{\text{weights}} = P \cdot b_{\text{param}}
   $$
   where $b_{\text{param}}$ is the bytes per parameter. This is the only bucket needed at inference time.
2. **Parameter gradients ($\nabla_\theta\mathcal{L}$):** the backward pass produces one gradient per parameter, which must be stored until the update step uses it,
   $$
   M_{\text{grad}} = P \cdot b_{\text{grad}}
   $$
   This bucket exists only during training and is zero at inference.
3. **Optimiser state buffers:** adaptive optimisers keep running statistics for every parameter (Section 3.2). The number of extra tensors depends on the algorithm:
   - Vanilla SGD stores nothing extra, so the cost is $0$.
   - SGD with momentum or RMSprop keeps one extra tensor (the velocity $\mathbf{v}$ or the squared-gradient accumulator $\mathbf{s}$), costing $1 \cdot P \cdot b_{\text{opt}}$.
   - Adam and AdamW keep two extra tensors (the first moment $\mathbf{m}$ and the second moment $\mathbf{v}$), costing $2 \cdot P \cdot b_{\text{opt}}$.

Adding the buckets gives the total static training memory $M_{\text{static}} = M_{\text{weights}} + M_{\text{grad}} + M_{\text{opt}}$. If all tensors use the same precision of $b$ bytes per element, then Adam training needs $b P + b P + 2 b P = 4bP$ bytes, which is four times the raw size of the weights alone. The optimiser you choose, in other words, directly changes how large a model fits on a given device, even before a single activation is stored.

### Dynamic Activation Memory and Why Forward Activations Must Be Cached

The static memory ignores the data flowing through the network. Why do activations need to be remembered at all? Because backpropagation reuses them. Recall the two key backward equations at layer $l$:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)} \left(\mathbf{a}^{(l-1)}\right)^\top, \qquad \boldsymbol{\delta}^{(l)} = \left(\left(\mathbf{W}^{(l+1)}\right)^\top \boldsymbol{\delta}^{(l+1)}\right) \odot \sigma'\!\left(\mathbf{z}^{(l)}\right)
$$

The first equation needs the forward activation $\mathbf{a}^{(l-1)}$ that entered the layer. The second needs the pre-activation $\mathbf{z}^{(l)}$ in order to evaluate $\sigma'$. Both were produced long ago in the forward pass, but the backward pass reaches them only after traversing all later layers. So nothing can be discarded early: during training, the activations of every layer $l = 1, \dots, L$ for every one of the $B$ samples must sit in memory at the same time, giving

$$
M_{\text{act}}^{\text{train}} = B \cdot b_{\text{act}} \sum_{l=1}^{L} d_l
$$

where $b_{\text{act}}$ is the bytes per activation element. (This counts one stored tensor per layer; real frameworks may also cache pre-activations or masks, which scales the constant but not the structure of the formula.) Unlike the static buckets, this term grows linearly with the batch size $B$ and with the total width summed over depth, which is why increasing the batch size or the depth is often what triggers out-of-memory errors.

At inference, the picture changes completely. There are no gradients and no optimiser buffers, and since nothing will be revisited, each layer's input can be overwritten as soon as the next layer has consumed it. Only two adjacent layers' activations need to coexist, so the requirement is governed by the widest adjacent pair:

$$
M_{\text{act}}^{\text{infer}} = B \cdot b_{\text{act}} \max_{l}\,(d_{l-1} + d_l)
$$

This is independent of the depth $L$, which is why a model that is impossible to train on a device can often still be run on it.

> [!note] Activation Checkpointing (Gradient Checkpointing)
> If activation memory is the bottleneck, we can trade compute for memory. In *activation checkpointing* we store the activations of only a subset of layers during the forward pass and **recompute** the missing ones from the nearest stored checkpoint when the backward pass needs them. The price is a roughly one extra forward pass of recompute FLOPs, and the gain is that activation memory grows more slowly with depth (on the order of $\sqrt{L}$ instead of $L$ when checkpoints are spaced evenly).

> [!summary] Memory Footprint of Training vs. Inference
> Training memory is the sum of three parameter-proportional buckets (weights, gradients, optimiser states), which depend on $P$ and the optimiser, plus activation memory, which depends on batch size and total layer widths. Inference keeps only the weights and a small, depth-independent activation buffer. Parameter counting (Section 5.2) tells us $P$; precision and optimiser choice scale it; and the batch size controls the rest.

---

# 6. Computational Efficiency, Roofline Model, & Hardware Acceleration

In the previous section we counted parameters, FLOPs, and bytes of memory. Counting is only half the story, though. The natural follow-up question is: *given those numbers, how fast will a network actually run on real hardware?* The surprising answer is that the number of arithmetic operations alone rarely tells you. Very often the processor is not busy calculating at all. It is waiting for data. This section builds the vocabulary and the model needed to reason about that situation, and then surveys the standard remedies.

## 6.1 The Memory Wall and Hardware Memory Hierarchy

### Compute Throughput vs. Memory Bandwidth Divergence

Imagine a chef who can chop vegetables at lightning speed but whose assistant can only carry ingredients from the pantry slowly. Buying a faster knife does nothing, because the bottleneck is the carrying. Modern processors are in exactly this position. Over successive hardware generations, arithmetic throughput has grown much faster than the speed at which data can be moved from main memory to the compute units.

We denote the peak arithmetic throughput of a processor by $\pi_{\text{peak}}$ (measured in FLOP/s, typically TFLOP/s) and the peak off-chip memory bandwidth by $\beta_{\text{mem}}$ (measured in bytes/s, typically GB/s or TB/s).

> [!abstract] Definition: The Memory Wall
> The *memory wall* is the growing gap between a processor's peak arithmetic throughput $\pi_{\text{peak}}$ and the off-chip memory bandwidth $\beta_{\text{mem}}$ available to feed it, such that moving data between memory and compute units, rather than executing arithmetic, dominates latency and energy consumption.

In other words, the arithmetic units are often *starved*. A workload that performs only a few operations per byte fetched cannot keep them busy, no matter how many cores the chip contains. Moving a number from off-chip memory also costs far more energy than performing a floating-point operation on it, which is why data movement matters for power as well as speed.

> [!note] Why this matters for deep learning
> Neural networks move enormous tensors (weights, activations, gradients). The efficiency of a network is therefore determined not only by *how much* arithmetic it requires (Section 5) but by *how much data traffic* that arithmetic induces.

### GPU Memory Hierarchy: HBM/VRAM vs. On-Chip SRAM and Registers

Accelerators such as GPUs do not have a single flat memory. They have a hierarchy that trades capacity against speed:

- **Off-chip High-Bandwidth Memory (HBM, also called DRAM, global memory, or VRAM):** large, holding tens of gigabytes (model weights, activations, and optimiser states live here), but comparatively slow, with bandwidth on the order of one to a few TB/s.
- **On-chip SRAM (L1 cache / shared memory) and register files:** tiny, holding only tens of megabytes in total, but extremely fast, with bandwidth an order of magnitude higher (tens of TB/s) and much lower latency.

The design principle follows directly. Every time a value must travel to or from HBM we pay a heavy price, whereas values kept in SRAM or registers are almost free to reuse. Much of the optimisation toolkit in the rest of this section is about one thing: **keep data on-chip and reuse it as many times as possible before sending it back to HBM.**

## 6.2 Arithmetic Intensity and the Roofline Performance Model

### Operational (Arithmetic) Intensity

To decide whether a computation will be limited by arithmetic or by memory, we need a single number that describes how "arithmetic-heavy" the computation is relative to the data it touches. That number is the arithmetic intensity.

> [!abstract] Definition: Arithmetic Intensity ($I$)
> The arithmetic intensity of a computational kernel is the ratio of the total floating-point operations it performs, $W_{\text{FLOPs}}$, to the total bytes it transfers across the memory bus, $Q_{\text{Bytes}}$:
> $$
> I = \frac{W_{\text{FLOPs}}}{Q_{\text{Bytes}}} \quad \left[\frac{\text{FLOPs}}{\text{Byte}}\right]
> $$

Intuitively, $I$ measures how many useful operations we extract from each byte we pay to fetch. A high $I$ means every fetched byte is reused many times (good); a low $I$ means each byte is touched once or twice and then discarded (bad).

### The Roofline Model and Ridge Point

Suppose a kernel has intensity $I$ on a machine with parameters $\pi_{\text{peak}}$ and $\beta_{\text{mem}}$. There are two separate ceilings on its speed. It can never exceed the compute peak $\pi_{\text{peak}}$. And since it moves $I^{-1}$ bytes per FLOP, the memory system can supply at most $\beta_{\text{mem}} \cdot I$ FLOP/s worth of data. The kernel is limited by whichever ceiling is lower.

> [!theorem] The Roofline Performance Bound
> The attainable throughput $P_{\text{actual}}$ (in FLOP/s) of a kernel with arithmetic intensity $I$ on hardware with peak compute $\pi_{\text{peak}}$ and peak memory bandwidth $\beta_{\text{mem}}$ is bounded by
> $$
> P_{\text{actual}}(I) = \min\!\big(\pi_{\text{peak}}, \; \beta_{\text{mem}} \cdot I\big)
> $$

Plotted against $I$ on log-log axes, this is a slanted line (the memory roof, with slope set by $\beta_{\text{mem}}$) that rises until it meets a flat line (the compute roof at height $\pi_{\text{peak}}$). The silhouette resembles a roof, hence the name.

> [!figure] Figure Placeholder: Roofline plot - attainable FLOP/s versus arithmetic intensity, showing the slanted memory-bandwidth roof, the flat compute roof, and the ridge point where they meet

The corner where the two roofs meet has a special name.

> [!abstract] Definition: Ridge Point ($I_{\text{ridge}}$)
> The ridge point is the arithmetic intensity at which the memory roof intersects the compute roof:
> $$
> I_{\text{ridge}} = \frac{\pi_{\text{peak}}}{\beta_{\text{mem}}}
> $$

The ridge point is a property of the *hardware*, and it divides all kernels into two regimes:

- **Memory-bound regime ($I < I_{\text{ridge}}$):** the compute cores sit partly idle waiting for data from HBM. Faster arithmetic units will not help. Speedups must come from moving fewer bytes (quantisation, kernel fusion, better caching or reuse).
- **Compute-bound regime ($I \ge I_{\text{ridge}}$):** the memory system keeps up and the arithmetic units are the bottleneck. Speedups must come from more arithmetic throughput (Tensor Cores, lower-precision math).

> [!warning] Diagnose before you optimise
> Applying a compute-side optimisation to a memory-bound kernel (or vice versa) gives almost no benefit. The roofline model tells you which side of the ridge you are on, and therefore which family of optimisations is worth trying.

### How Batching Transitions Linear Layers from Memory-Bound to Compute-Bound

Now we apply the model to the central building block of Section 5, the linear layer. Why does a larger batch size make hardware run so much more efficiently? The arithmetic intensity gives a precise answer.

Consider $\mathbf{Y} = \mathbf{X}\mathbf{W}^\top$ with $\mathbf{X} \in \mathbb{R}^{B \times d}$ and $\mathbf{W} \in \mathbb{R}^{d \times d}$, where every number occupies $b$ bytes. We assume ideal caching, meaning each of the three matrices is moved between HBM and the chip exactly once.

**Derivation:**

First count the work. Each of the $B d$ output entries is a dot product of length $d$, costing $d$ multiplications and about $d$ additions, so

$$
W_{\text{FLOPs}} = 2 B d \cdot d = 2 B d^2
$$

Next count the traffic. We read $\mathbf{W}$ ($d^2$ numbers), read $\mathbf{X}$ ($Bd$ numbers), and write $\mathbf{Y}$ ($Bd$ numbers):

$$
Q_{\text{Bytes}} = b\left(d^2 + Bd + Bd\right) = b\left(d^2 + 2Bd\right)
$$

Dividing, and then dividing numerator and denominator by $d^2$:

$$
\begin{aligned}
I(B) &= \frac{2 B d^2}{b\,(d^2 + 2Bd)} \\
     &= \frac{2B}{b\left(1 + \frac{2B}{d}\right)}
\end{aligned}
$$

Now read the result in two limits.

- **Unbatched ($B = 1$, a matrix-vector product, GEMV):** for large $d$ the term $\frac{2B}{d}$ is negligible, so $I(1) \approx \frac{2}{b}$. This is a tiny, size-independent constant, well below the ridge point of any modern accelerator. The kernel is strictly memory-bound: the entire weight matrix $\mathbf{W}$ must be streamed from HBM to perform just one vector's worth of work, and every weight is used only once.
- **Batched ($1 \ll B \ll d$, a matrix-matrix product, GEMM):** the denominator stays close to $b$, so $I(B) \approx \frac{2B}{b}$, which grows linearly with $B$. The same weight fetch is now *amortised* across $B$ samples, since each weight loaded is reused $B$ times.

Increasing $B$ therefore slides the kernel to the right along the roofline, from the memory-bound slope toward the compute roof. This growth cannot continue forever: as $B$ becomes comparable to or larger than $d$, the factor $\frac{2B}{d}$ dominates the denominator and $I(B)$ saturates at $\frac{d}{b}$, which is set by the layer width. Wider layers can therefore reach higher intensity. $\blacksquare$

> [!note] Training vs. single-request inference
> This explains why serving one request at a time (small $B$) tends to underuse a GPU, whereas training with large mini-batches uses it well. It also adds a hardware reason, beyond gradient noise (Section 3), for preferring mini-batches over single-sample updates.

## 6.3 Hardware Acceleration and System-Level Optimisations

The roofline picture suggests three levers: reduce bytes (quantisation), raise the compute roof (specialised units), and raise the effective intensity by avoiding round trips to HBM (fusion and tiling).

### Model Quantisation and Numerical Precision Formats

If memory traffic is the bottleneck, then storing each number in fewer bits directly reduces $Q_{\text{Bytes}}$, which raises $I$ and also shrinks the memory footprint from Section 5.

> [!abstract] Definition: Model Quantisation
> Model quantisation is the mapping of high-precision floating-point values (typically FP32) onto lower bit-width discrete representations (FP16, BF16, INT8, INT4).

The formats differ in how they split their bits between *range* (exponent) and *precision* (mantissa):

| Format | Sign bits | Exponent bits | Mantissa bits | Character |
|---|---|---|---|---|
| FP32 | 1 | 8 | 23 | Wide range, high precision; the default training format |
| FP16 | 1 | 5 | 10 | Higher precision than BF16, but narrow range (overflow/underflow risk) |
| BF16 | 1 | 8 | 7 | Same range as FP32, coarse precision; robust for training |
| INT8 / INT4 | n/a | n/a | n/a | Uniform integer grids; very compact, mainly used for inference |

BF16 deliberately keeps FP32's eight exponent bits, so it covers the same dynamic range and avoids the overflow and underflow problems that make FP16 fragile, at the cost of fewer mantissa bits.

For integer formats, a real value $x$ is mapped to an integer through a scale $S$ and zero-point $Z$:

$$
q = \operatorname{clip}\!\big(\lfloor x / S \rceil + Z,\; q_{\min},\; q_{\max}\big)
$$

and recovered approximately by dequantisation:

$$
\hat{x} = S\,(q - Z)
$$

Here $\lfloor \cdot \rceil$ denotes rounding to the nearest integer and $\operatorname{clip}$ saturates values to the representable integer range $[q_{\min}, q_{\max}]$. The recovered $\hat{x}$ differs from $x$ by a rounding error, which is the price paid for compression.

Going from FP32 (32 bits) to INT4 (4 bits) shrinks the memory footprint by a factor of $8$. For a memory-bound kernel, where speed is set by bytes moved, this translates into roughly an $8\times$ boost in effective throughput, since eight times as many values pass through the same bandwidth.

### Specialised Compute Units: Scalar/SIMD Cores vs. Tensor Cores

Quantisation attacks the memory roof. To raise the *compute* roof, hardware designers add specialised units. General-purpose GPU cores (SIMT, or "CUDA" cores) execute scalar fused multiply-add instructions, one per thread per cycle. Deep learning, however, is dominated by matrix multiplication, so GPUs also include **Tensor Cores**: systolic matrix-multiply-accumulate units that compute a whole small matrix tile operation

$$
\mathbf{D} = \mathbf{A}\mathbf{B} + \mathbf{C}
$$

in a single instruction, operating across mixed precisions (for example low-precision inputs with higher-precision accumulation). Because they perform many multiply-adds per cycle, Tensor Cores raise $\pi_{\text{peak}}$ dramatically for matrix workloads. A side effect is that $I_{\text{ridge}}$ moves to the right, so more kernels fall on the memory-bound side, which makes the memory-side optimisations even more important.

### Kernel Fusion and SRAM-Aware Block Tiling

A deep network is a long chain of small operations. If each operation is a separate GPU kernel, each one reads its input from HBM and writes its output back, even though the very next kernel immediately reads it again. Such element-wise steps do very little arithmetic per byte, so they sit far to the left of the ridge point.

> [!abstract] Definition: Kernel Fusion
> Kernel fusion compiles a sequence of distinct element-wise or reduction operations (for instance bias addition, normalisation, ReLU, and dropout) into a single GPU kernel, so intermediate tensors remain in on-chip registers or SRAM instead of being written to and re-read from HBM after every operation.

Fusion leaves the FLOP count $W_{\text{FLOPs}}$ unchanged but removes the intermediate traffic from $Q_{\text{Bytes}}$, so it raises $I$ and pushes the workload up the memory roof.

The same idea extends to large operations through **SRAM-aware block tiling**. Rather than materialising a huge intermediate matrix in HBM, the computation is broken into blocks small enough to fit in SRAM. Each block is loaded once, processed fully on-chip, and only the final result is written back. The fused-attention approach mentioned in the lecture (FlashAttention-style blocking) is an instance of this: it avoids writing the enormous intermediate attention matrix to HBM, turning a memory-bound computation into one dominated by fast SRAM-resident work.

> [!summary] Week 1 Key Takeaways
> - **Paradigm:** Deep learning replaces hand-crafted features with end-to-end learned hierarchical representations, handling unstructured data and scaling with data and compute. Universal approximation guarantees existence, while depth gives parameter-efficient compositional power.
> - **Training:** Learning is the iterative loop of forward pass, loss, backward pass, and parameter update. Backpropagation computes all gradients efficiently through the chain rule, and gradient stability is protected by non-saturating activations and residual connections.
> - **Optimisation:** The learning rate, its schedule, and the optimiser (momentum, RMSprop, Adam) govern convergence. Regularisation (weight penalties, dropout, batch normalisation) controls the generalisation gap.
> - **Loss and landscape:** The loss should match the data's noise and task (MSE, MAE, Huber, cross-entropy, focal loss for imbalance). High-dimensional landscapes are dominated by saddle points and ill-conditioned curvature rather than bad local minima.
> - **Resources:** Layer shapes determine parameter counts, FLOPs, and memory (weights, gradients, optimiser states, cached activations).
> - **Efficiency:** Real speed is governed by data movement as much as arithmetic. The roofline model, via arithmetic intensity and the ridge point, tells us whether a kernel is memory-bound or compute-bound, and batching, quantisation, Tensor Cores, and kernel fusion are the levers for improving it.

---

# Skeleton Index

## 1. Deep Learning vs. Traditional Machine Learning

### 1.1 Limitations of Traditional Machine Learning

**Manual Feature Engineering and Domain Dependency**
- Describe the structure of a classical machine learning pipeline, identifying which stage is learned and which is designed by a human.
- Explain why designing the feature extractor requires domain knowledge, using examples from healthcare, banking, and telecom.
- Discuss the labour cost, fragility, and human inductive bias associated with manual feature design.
- Explain why information discarded by the feature extractor cannot be recovered by the model.

**Constraint to Structured Tabular Modalities**
- State the structural assumptions that tabular models make about rows and columns.
- Explain why images, audio, video, and text violate these assumptions.
- Discuss the roles of spatial locality, translation invariance, and temporal structure in unstructured data.

**Early Performance Saturation**
- Explain why the performance of a shallow model with a fixed feature space plateaus as the training set grows.
- Relate this plateau to model capacity.

### 1.2 The Deep Learning Paradigm: Representation Learning

**Automated Hierarchical Feature Extraction**
- Write the end-to-end compositional form of a deep model and explain what "end-to-end differentiable" means.
- Define Representation Learning (Automated Feature Learning).
- Contrast what is learned in a classical pipeline with what is learned in a deep model.
- Explain the meaning of "hierarchical" in hierarchical feature extraction.

**Native Processing of Unstructured Data and Continuous Scaling**
- Explain what architectural inductive biases are and how they let a network process raw unstructured inputs.
- Explain what continuous scaling means and along which three quantities a deep model can be scaled.
- Compare Traditional ML and Deep Learning in terms of data modality, feature engineering, scaling behaviour, compute profile, data hunger, and interpretability.
- Discuss the trade-offs incurred by removing manual feature engineering.

### 1.3 Expressivity: Universal Approximation, Depth, and Width

**Architectural Anatomy: Input, Hidden, and Output Layers**
- Describe the roles of the input, hidden, and output layers in a feedforward multilayer network.
- Define the width and the depth of a network.
- Distinguish correctly between a wide network and a deep network.

**The Universal Approximation Theorem**
- State the Universal Approximation Theorem, including its conditions on the domain and the activation function.
- Explain in plain language what the theorem guarantees and why the nonlinearity is essential.
- Analyse the limitations of the theorem regarding existence, required width, learnability, and generalisation.

**Depth vs. Width Trade-Offs and Hierarchical Feature Reuse**
- Explain why deep networks are parameter-efficient for compositional functions, compared with shallow wide networks.
- Define Hierarchical Feature Reuse.
- Illustrate how features are reused across layers when understanding an image.
- Compare width and depth in terms of expressive efficiency, computational parallelism, and optimisation difficulty.
- Summarise why deep learning is preferred over traditional machine learning.

## 2. Neural Network Training Pipeline & Backpropagation

### 2.1 The Four-Stage Iterative Training Loop

**Stage 1: Forward Propagation (Forward Pass)**
- Describe the layer-by-layer computation that turns an input into a prediction, defining pre-activation and activation at each layer.
- Explain why intermediate values from this stage must be retained.

**Stage 2: Loss Evaluation**
- Define the role of the loss function and the scalar it returns.
- Write the empirical risk over a mini-batch and explain why a scalar is required.

**Stage 3: Backward Propagation (Backward Pass)**
- State what quantities the backward pass computes and in which direction it proceeds.
- Name the differentiation paradigm it implements.

**Stage 4: Parameter Update and Convergence Criteria**
- State the gradient descent update rule and explain the direction of the step.
- Distinguish an iteration from an epoch, and relate the two through dataset and batch size.
- List and explain the stopping criteria used to end training.

### 2.2 Mathematical Mechanics of Backpropagation

**The Multivariable Chain Rule in Computational Graphs**
- Derive the multivariable chain rule for a scalar loss computed through a vector-valued function.
- Express it using the Jacobian matrix and explain how sensitivity flows backwards through a function.
- Explain how a neural network forms a computational graph and how backpropagation traverses it.

**Layer-Wise Error Sensitivities and Parameter Gradients**
- Define the backpropagated error signal (local gradient) and justify why it is defined with respect to the pre-activation.
- State the four fundamental equations of backpropagation, including the assumptions on the activation.
- Prove the output layer error equation.
- Prove the recursive backward error propagation equation.
- Prove the bias gradient equation.
- Prove the weight gradient equation and explain its shape.
- Describe how the four equations combine into a complete algorithm.
- Explain why forward-pass values must be stored for the backward pass.
- Analyse what changes in the output error equation when the activation is not applied element-wise.

**Why Reverse-Mode Differentiation Is Efficient**
- Compare the computational cost of reverse-mode differentiation with finite-difference and forward-mode perturbation methods in terms of the number of parameters.
- Explain why a scalar loss makes reverse mode especially well suited to training networks.

### 2.3 Gradient Stability and Mitigation Mechanisms

**The Vanishing and Exploding Gradient Problems**
- Derive the expanded product form of the error at an early layer in terms of the output error.
- Define vanishing and exploding gradients using norm conditions on the layer-wise factors.
- Explain why the effect is exponential in depth.

**Activation Function Saturation vs. Non-Saturating Rectifiers (ReLU)**
- Define the sigmoid and derive its derivative and its range.
- State the tanh derivative and its range, and explain saturation for both functions.
- Analyse the consequence of saturation for gradient flow in deep networks.
- Define ReLU and its derivative, and explain why it avoids multiplicative decay on the active region.
- Explain the dying ReLU phenomenon and the activation variants that address it.

**Residual Connections (Skip Connections)**
- Define a residual block and the identity skip connection.
- Derive the Jacobian of a residual block with respect to its input.
- Derive the gradient from the output back to an earlier layer across several residual blocks.
- Explain how the identity term creates a gradient highway and why it supports very deep networks.

## 3. Learning Rate Dynamics, Optimisers, & Regularisation

### 3.1 Learning Rate Dynamics and Scheduling

**Step-Size Regimes and Convergence Behavior**
- Define the learning rate and state its role in the gradient descent update.
- Derive, using a second-order expansion around a local minimum, the condition on the learning rate for stable convergence.
- Explain which direction of the loss surface limits the usable learning rate and which direction converges slowest.
- Describe the behaviour of gradient descent for a suboptimally small, a balanced, and an excessively high learning rate, distinguishing oscillatory convergence from divergence.
- Explain how the learning rate interacts with exploding and vanishing gradients.

**Learning Rate Schedules and Warmup**
- Explain why a static learning rate is suboptimal over the full training trajectory.
- State and compare step decay, exponential decay, and cosine annealing, including their formulas.
- Explain the purpose of linear warmup and why it matters at the start of training.

### 3.2 First-Order and Adaptive Optimisation Algorithms

**Batch, Stochastic, and Mini-Batch Gradient Descent (SGD)**
- Compare batch, stochastic, and mini-batch gradient descent in terms of cost and gradient noise.
- State the mini-batch gradient estimator and establish its bias and variance properties.
- Analyse the effect of the batch size on the gradient estimate.
- Explain the pathologies of vanilla SGD in ill-conditioned landscapes.

**SGD with Momentum**
- Define the momentum update rule.
- Explain the heavy-ball intuition behind momentum and derive the amplification effect along persistent gradient directions.
- Explain how momentum behaves along oscillating directions.
- Describe how Nesterov Accelerated Gradient differs from classical momentum.

**RMSprop (Root Mean Square Propagation)**
- Define the RMSprop update rule.
- Explain how the per-coordinate normalisation changes step sizes along steep and gentle directions.
- Compare RMSprop with Adagrad and explain the role of the decay factor.

**Adam (Adaptive Moment Estimation) and Decoupled Weight Decay (AdamW)**
- Define the Adam optimiser, including both moment estimates and their typical decay settings.
- Derive the expected value of the first-moment estimate and show why bias correction is needed.
- Explain why the two corrections matter for different numbers of iterations.
- Explain how Adam combines the ideas of momentum and RMSprop.
- Explain the problem of combining an $L_2$ penalty with an adaptive optimiser and how AdamW resolves it.

**Comparative Synthesis: Selecting an Optimiser by Use Case**
- Compare SGD, SGD with momentum, RMSprop, and Adam/AdamW in terms of what they adapt, their state, and their behaviour.
- Evaluate which optimiser suits which use case and justify the choice.
- Discuss the trade-off between convergence speed and generalisation across optimisers.
- Interpret the expected trajectories of the different optimisers on the same loss surface.

### 3.3 Overfitting and Regularisation Mechanisms

**Generalisation Gap, Bias-Variance, and Overfitting**
- Define training risk, population risk, the generalisation gap, and overfitting.
- Relate underfitting and overfitting to bias and variance.
- Explain why over-parameterised networks tend to memorise noise without regularisation.
- Define regularisation and give an example other than an explicit penalty.

**Parameter Norm Penalties: $L_2$ (Weight Decay) and $L_1$ Regularisation**
- Write the regularised objective in general form.
- Define $L_2$ regularisation, derive the resulting parameter update, and explain why it is called weight decay.
- Define $L_1$ regularisation, derive its gradient, and explain its effect on the weights.
- Compare $L_2$ and $L_1$ regularisation in terms of shrinkage behaviour and sparsity.

**Dropout: Stochastic Subnetwork Ensembling**
- Define inverted dropout for training and inference.
- Explain the purpose of the rescaling factor.
- Explain how dropout breaks co-adaptation and why it approximates an ensemble of subnetworks.

**Batch Normalisation**
- Define the batch normalisation transformation, including the learnable parameters and the inference-time behaviour.
- Explain why the learnable affine step is needed and why running statistics are used at inference.
- Analyse the effects of batch normalisation on the loss surface, learning rate, activation saturation, and regularisation.
- Explain why a bias term before batch normalisation is unnecessary.

## 4. Cost Functions & High-Dimensional Loss Landscapes

### 4.1 Regression Cost Functions and Outlier Sensitivity

**Mean Squared Error (MSE / $L_2$ Loss)**
- Define Mean Squared Error.
- Derive MSE as the maximum likelihood objective under additive Gaussian noise.
- State which conditional statistic of the target an MSE-trained network learns.
- Derive the gradient of MSE with respect to a prediction and analyse its behaviour near the optimum and for large residuals.
- Evaluate when strong outlier sensitivity is undesirable and when it is desirable.

**Mean Absolute Error (MAE / $L_1$ Loss)**
- Define Mean Absolute Error.
- Explain the maximum likelihood derivation of MAE and the conditional statistic it estimates.
- Determine the (sub)gradient of MAE and explain its effect on outlier robustness.
- Explain the optimisation difficulties MAE causes near the minimum and how they can be mitigated.

**Huber Loss (Smooth $L_1$ Loss)**
- Define Huber loss and the role of its threshold parameter.
- Show that Huber loss and its derivative are continuous at the threshold.
- Compare the gradient behaviour of Huber loss in its inner and outer regions with MSE and MAE.
- Compare MSE, MAE and Huber loss in terms of functional form, derivative, statistical estimator, outlier robustness and optimisation behaviour.
- Explain how the choice of regression loss reflects assumptions about the noise.

### 4.2 Classification Cost Functions and Class Imbalance

**Binary Cross-Entropy (BCE) Loss**
- Define Binary Cross-Entropy loss and the logit-to-probability mapping it uses.
- Derive BCE from the Bernoulli likelihood.
- Interpret the penalty BCE assigns to confident correct versus confident wrong predictions.
- State and prove the gradient of BCE with respect to the logit.
- Explain why MSE on sigmoid outputs is a poor choice for classification.
- Explain the numerical instability of applying sigmoid before the logarithm and how `BCEWithLogitsLoss` resolves it.

**Categorical Cross-Entropy Loss and Softmax**
- Define softmax and categorical cross-entropy.
- Explain how categorical cross-entropy relates to BCE.
- Explain the information-theoretic link between cross-entropy and KL divergence.
- State and prove the gradient of softmax cross-entropy with respect to the logits.

**Class Imbalance Pathology and Focal Loss**
- Explain the mechanism by which standard cross-entropy fails on severely imbalanced datasets.
- Explain how a model can show high accuracy yet poor minority-class recall, and which metrics and remedies address this.
- Define the true-class probability and Focal Loss, including the roles of the class-balancing weight and the focusing parameter.
- Analyse the modulating factor for easy versus hard examples.
- Determine how Focal Loss relates to ordinary cross-entropy for particular parameter settings.

### 4.3 Navigating High-Dimensional Loss Landscapes

**Critical Points: Local Minima vs. Saddle Points**
- Define critical points and saddle points.
- Present the dimensional/probabilistic argument for the prevalence of saddle points over local minima.
- Explain the practical difficulty saddle points pose for gradient-based training.
- Evaluate the status of the probabilistic argument as a heuristic.

**Hessian Curvature and Ill-Conditioning**
- Define the Hessian matrix and the quadratic approximation of the loss around a point.
- Explain the meaning of Hessian eigenvalues as directional curvature.
- Classify critical points according to the signs of the Hessian eigenvalues, including degenerate cases.
- Define the condition number of the Hessian.
- Explain how a large condition number creates ravines and why the gradient is misaligned with the path to the minimum.
- Relate ill-conditioning to learning-rate limits and to the motivation for momentum and adaptive optimisers.

**Stochastic Gradient Noise and Sharp vs. Flat Minima**
- Distinguish label/measurement noise from mini-batch sampling noise.
- Define the stochastic gradient noise term and discuss the role of its covariance structure.
- Explain how mini-batch noise influences escape from saddle points and from sharp minima.
- Compare sharp and flat minima in terms of curvature and generalisation.

## 5. Linear Layers, Parameter Counting, & Memory Footprint

### 5.1 Affine Linear Transformations in Neural Networks

**Single-Sample and Batched Matrix Formulations**
- Define a dense (fully connected / linear) layer, stating the shapes of the input, weight matrix, and bias vector.
- Explain why a "linear" layer is strictly affine.
- Derive the batched formulation for a mini-batch and explain how the bias is broadcast.
- Explain which quantities are shared across samples in a batch and which grow with batch size.

**Geometric Interpretation and the Necessity of Nonlinearity**
- Interpret a row of the weight matrix and the corresponding bias entry geometrically.
- State the theorem on stacked linear layers without intermediate activations.
- Prove the theorem, and determine the effective weight matrix and effective bias.
- Analyse what this result implies about the value of depth and about the rank of the composite map.
- Explain why nonlinear activations are essential for the benefits of depth.

### 5.2 Parameter Counting and Computational Complexity

**Exact Parameter Counting Formulas for MLPs**
- Define the parameter count of a linear layer (weights, biases, total) in terms of adjacent layer widths.
- Derive the total parameter count of an $L$-layer MLP.
- Compare how parameter count scales when widening versus deepening a network.
- Explain when a bias is omitted and why this is justified before Batch Normalisation.

**FLOPs and MACs in Forward and Backward Passes**
- Define a multiply-accumulate operation and derive the MAC and FLOP counts of a linear layer's forward pass.
- Derive the cost of the backward pass of a linear layer, identifying the two products involved.
- Determine the relative cost of one full training step versus inference.
- Discuss the capacity-complexity trade-off when choosing a model's parameter count.

### 5.3 Anatomy of Neural Network Memory Footprint

**Static Model Memory: Parameters, Gradients, and Optimiser States**
- List the parameter-proportional memory buckets in training and give the expression for each.
- Compare the optimiser-state memory of SGD, SGD with momentum, RMSprop, and Adam/AdamW.
- Determine which buckets exist at inference time.
- Derive the total static training memory under a uniform precision and compare it to the raw weight size for Adam.

**Dynamic Activation Memory and Why Forward Activations Must Be Cached**
- Explain, using the backpropagation equations, why forward activations must be retained during training.
- Derive the training-time activation memory in terms of batch size, precision, and layer widths.
- Derive the inference-time activation memory and explain why it differs from training.
- Explain the mechanism of activation checkpointing and its compute-versus-memory trade-off.
- Summarise the components that make up training memory versus inference memory.

## 6. Computational Efficiency, Roofline Model, & Hardware Acceleration

### 6.1 The Memory Wall and Hardware Memory Hierarchy

**Compute Throughput vs. Memory Bandwidth Divergence**
- Define the memory wall and the two quantities $\pi_{\text{peak}}$ and $\beta_{\text{mem}}$ whose gap it describes.
- Explain why data movement, rather than arithmetic, can dominate both latency and energy.

**GPU Memory Hierarchy: HBM/VRAM vs. On-Chip SRAM and Registers**
- Compare off-chip HBM and on-chip SRAM/registers in terms of capacity, bandwidth, and latency.
- Explain the design principle that this hierarchy imposes on efficient kernels.

### 6.2 Arithmetic Intensity and the Roofline Performance Model

**Operational (Arithmetic) Intensity**
- Define arithmetic intensity and state its units.
- Interpret what a high versus a low value means for data reuse.

**The Roofline Model and Ridge Point**
- State the roofline performance bound and explain the origin of each of its two terms.
- Describe the shape of the roofline plot.
- Define the ridge point and state what determines it.
- Compare the memory-bound and compute-bound regimes in terms of the bottleneck and the appropriate class of optimisations.
- Explain why diagnosing the regime must precede choosing an optimisation.

**How Batching Transitions Linear Layers from Memory-Bound to Compute-Bound**
- Derive the arithmetic intensity of a linear layer as a function of batch size, stating your assumptions about data movement and counting FLOPs and bytes explicitly.
- Analyse the behaviour of the intensity for the unbatched case (matrix-vector) and the batched case (matrix-matrix).
- Determine what limits the intensity as the batch size grows very large.
- Discuss the implications for single-request inference versus mini-batch training.

### 6.3 Hardware Acceleration and System-Level Optimisations

**Model Quantisation and Numerical Precision Formats**
- Define model quantisation and explain why it helps memory-bound kernels.
- Compare FP32, FP16, BF16, INT8, and INT4 in terms of bit layout, dynamic range, and precision.
- Explain why BF16 is often preferred over FP16 for training.
- State the affine quantisation and dequantisation equations, defining each symbol.
- Evaluate the memory and throughput consequences of compressing FP32 to INT4.

**Specialised Compute Units: Scalar/SIMD Cores vs. Tensor Cores**
- Contrast general-purpose GPU cores with Tensor Cores in terms of the operation executed per instruction.
- Analyse the effect of Tensor Cores on the compute roof and the ridge point.

**Kernel Fusion and SRAM-Aware Block Tiling**
- Define kernel fusion and explain the inefficiency of running a chain of separate kernels.
- Analyse how fusion changes the FLOP count, the byte traffic, and the arithmetic intensity.
- Explain how SRAM-aware block tiling (as in fused attention) addresses a memory-bound bottleneck.

**Week 1 Key Takeaways**
- Summarise the week's main themes across the learning paradigm, training, optimisation, loss design, resource accounting, and hardware efficiency.
