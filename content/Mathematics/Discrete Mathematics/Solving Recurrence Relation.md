## Linear Homogeneous Recurrence Relation With Constant Coefficients

**Definition:** A linear homogeneous recurrence relation of degree k with constant coefficients is a recurrence relation of the form
$$
a_{n} = c_{1}\cdot a_{n-1} + c_{2}\cdot a_{n-2} + \dots + c_{k}\cdot a_{n-k}
$$
where $c_{1},c_{2},\dots,c_{k}$ are real numbers with $c_{k} \neq 0$.

##### Characteristic Solution

A homogeneous equation with constant coefficients usually has a solution of the type $a_{n} = r^{n}$, this is not to say that every solution fits this type, but some of them do. If $r^{n}$ is a solution, then we can plug it into the recurrence relation as follows,
$$
\begin{align}
a_{n} = c_{1}\cdot a_{n-1} + c_{2}\cdot a_{n-2} + \dots + c_{k}\cdot a_{n-k} \\
r^{n} = c_{1}\cdot r^{n-1} + c_{2}\cdot r^{n-2} + \dots + c_{k}\cdot r^{n-k}
\end{align}
$$
Dividing the equation with $r^{n-k}$, we get the following equation,
$$
r^{k} - c_{1}\cdot r^{k-1} - c_{2}\cdot r^{k-2} - \dots - c_{k} = 0
$$
This is a polynomial in $r$ with degree $k$. Each real solution of this polynomial is also a solution of the recurrence relation.

>[!Note]
>A solution of a recurrence relation is simply a sequence of numbers that satisfy the recurrence relation. When we say that $r^{n}$ is a solution, we mean that $a_{0} = r_{0}, a_{1}=r^{1}, a_{2}= r^{2}, \dots, a_{k-1} = r^{k-1}$ and after that,
$$a_{k} = r^{k} = c_{1}\cdot r^{k-1} + c_{2}\cdot r^{k-2} + \dots + c_{k}$$
> And we know that this is true since $r$ is a solution of the characteristic equation.

##### Linear Combination of Two Solutions

If $s_{n}$ and $t_{n}$ is a solution to the recurrence relation $a_{n} = c_{1}\cdot a_{n-1} + \dots + c_{k}\cdot a_{k-1}$, then linear combination $\alpha s_{n} + \beta t_{n}$ is also a solution to the recurrence relation. We can prove this using simple algebra as shown below.
$$
\begin{align}
s_{n} & = c_{1}\cdot s_{n-1} + \dots + c_{k}\cdot s_{n-k} \\ \\
t_{n} & = c_{1}\cdot t_{n-1} + \dots + c_{k}\cdot t_{n-k}
\end{align}
$$
Hence, we get
$$
\begin{align}
\alpha s_{n} + \beta t_{n} & = \alpha \cdot (c_{1}s_{n-1} + c_{2}s_{n-2} + \dots + c_{k}s_{n-k}) + \beta \cdot (c_{1}t_{n-1} + c_{2}t_{n-2} + \dots + c_{k}t_{n-k}) \\
 & = c_{1}(\alpha s_{n-1} + \beta t_{n-1}) + c_{2}(\alpha s_{n-2} + \beta t_{n-2}) + \dots + c_{k}(\alpha s_{n-k} + \beta t_{n-k})
\end{align}
$$
Hence, $\alpha s_{n} + \beta t_{n}$ is also a solution to the recurrence relation $\{ a_{n} \}$.

>[!Note]
>When we write $a_{n}$ then we mean the $nth$ term of the relation, and when we write $\{ a_{n} \}$ then we mean the entire sequence of number that form a solution to the recurrence relation.

### The Degree Two Case

**Theorem:** Let $c_{1}$ and $c_{2}$ be real numbers. Suppose that $r^{2}-c_{1}r-c_{2} = 0$ has two distinct roots $r_{1}$ and $r_{2}$.Then the sequence $\{ a_{n} \}$ is a solution of the recurrence relation $a_{n} = c_{1}a_{n-1} + c_{2}a_{n-2}$ if and only if
$$
a_{n} = \alpha_{1}r_{1}^{n} + \alpha_{2}r_{2}^{n}
$$
where $\alpha_{1}$ and $\alpha_{2}$ are constants.

**Proof:** The theorem says *if and only if* this means that we have to prove this both ways, i.e. $\alpha_{1}r_{1}^{n} + \alpha_{2}r_{2}^{n}$ is always a solution for any $\alpha_{1}$ and $\alpha_{2}$ and any solution of the recurrence relation is of the form $\alpha_{1}r_{1}^{n} + \alpha_{2}r_{2}^{n}$.

Now, we know that $r_{1}^{n}$ is a solution, since it is a solution of the recurrence relation and the same goes for $r_{2}^{n}$. Hence all linear combinations of them is also a solution as seen before, hence $\alpha_{1}r_{1}^{n} + \alpha_{2}r_{2}^{n}$ is also a solution for all $\alpha_{1},\alpha_{2} \in \mathbb{R}$.

Now, consider a solution to recurrence relation $\{ a_{0},a_{1},a_{2},\dots \}$, first we need to find $\alpha_{1}$ and $\alpha_{2}$ such that $a_{0} = \alpha_{1}r_{1}^{0} + \alpha_{2}r_{2}^{0}$ and $a_{1} = \alpha_{1}r_{1}^{1} + \alpha_{2}r_{2}^{1}$, then we show that other terms fit right in.
$$
a_{0} = \alpha_{1} + \alpha_{2}
$$
$$
a_{1} = \alpha_{1}r_{1} + \alpha_{2}r_{2}
$$
Solving the equations gives us,
$$
\alpha_{1} = \frac{a_{1}-r_{2}a_{0}}{r_{1}-r_{2}}, \alpha_{2} = \frac{a_{1}-r_{1}a_{0}}{r_{2}-r_{1}}
$$
Here we also see the use of the assumption that $r_{1} \neq r_{2}$. Hence, such $\alpha_{1}$ and $\alpha_{2}$ always exist. So, the solution is true for $n=0,1$, assuming that the assertion is also true for upto some fixed $n$, then we have
$$
\begin{align}
a_{n+1} & = c_{1}a_{n} + c_{2}a_{n-1} \\
 & = c_{1}(\alpha_{1}r_{1}^{n} + \alpha_{2}r_{2}^{n}) + c_{2}(\alpha_{1}r_{1}^{n-1} + \alpha_{2}r_{2}^{n-1}) \\
 & = \alpha_{1}(c_{1}r_{1}^{n} + c_{2}r_{1}^{n-1}) + \alpha_{2}(c_{1}r_{2}^{n} + c_{2}r_{2}^{n-1}) \\
 & = \alpha_{1}r_{1}^{n-1}(c_{1}r_{1}+c_{2}) + \alpha_{2}r_{2}^{n-1}(c_{1}r_{2}+c_{2}) \\
 & = \alpha_{1}r_{1}^{n-1}(r_{1}^{2}) + \alpha_{2}r_{2}^{n-1}(r_{2}^{2}) \\
a_{n+1} & = \alpha_{1}r_{1}^{n+1} + \alpha_{2}r_{2}^{n+1} \\
\end{align}
$$
Hence, using the principle of mathematical induction we have $a_{n} = \alpha_{1}r_{1}^{n} + \alpha_{2}r_{2}^{n}$, for every $n \in \{ 0,1,2,3,\dots \}$.

##### Degree Two With One Root

**Theorem:** Let $c_{1}$ and $c_{2}$ be real numbers with $c_{2}\neq 0$. Suppose that $r^{2} - c_{1}r-c_{2} = 0$ has only one root $r_{0}$. A Sequence $\{ a_{n} \}$ is a solution of the recurrence relation $a_{n} = c_{1}a_{n-1} + c_{2}a_{n-2}$ if and only if $a_{n} = \alpha_{1}r_{0}^{n} + \alpha_{2}nr_{0}^{n}$ for $n = 0,1,2,\dots$, where $\alpha_{1}$ and $\alpha_{2}$ are constants.

**Proof:** Again, first we need to prove to prove that $\alpha_{1}r_{0}^{n} + \alpha_{2}nr_{0}^{n}$ is always a solution, and then we have to prove that every solution is of the type $\alpha_{1}r_{0}^{n} + \alpha_{2}nr_{0}^{n}$.

The characteristic equation is $r^{2} - c_{1}r-c_{2} = 0$ and the root is $r_{0}$, then we have the following equations,
$$
\begin{align}
\text{sum of roots } & = r_{0}+r_{0} &  = -\frac{b}{a} &  = \frac{c_{1}}{1} &  = c_{1} \\
\implies c_{1} &  = 2r_{0} \\
\text{product of roots} &  = r_{0}\cdot r_{0} & = \frac{c}{a} &  = \frac{-c_{2}}{1} & = -c_{2} \\
\implies c_{2}  & = -r_{0}^{2}
\end{align}
$$

First, we prove that $\alpha_{1}r_{0}^{n} + \alpha_{2}nr_{0}^{n}$ is a solution for every $\alpha_{1},\alpha_{2}\in \mathbb{R}$. For this it must satisfy the recurrence relation.
$$
\begin{align}
a_{n} &  = c_{1}a_{n-1} + c_{2}a_{n-2} \\
 & = c_{1}(\alpha_{1}r_{0}^{n-1}+\alpha_{2}(n-1)r_{0}^{n-1}) + c_{2}(\alpha_{1}r_{0}^{n-2}+\alpha_{2}(n-2)r_{0}^{n-2}) \\
 & = \alpha_{1}(c_{1}r_{0}^{n-1}+c_{2}r_{0}^{n-2}) + \alpha_{2}(c_{1}(n-1)r_{0}^{n-1}+c_{2}(n-2)r_{0}^{n-2}) \\
 & = \alpha_{1}r_{0}^{n-2}(c_{1}r_{0}+c_{2}) + \alpha_{2}r_{0}^{n-2}(n(c_{1}r_{0}+c_{2}) - (c_{1}r_{0}+2c_{2}))
\end{align}
$$
Putting, in the values of $c_{1}$ and $c_{2}$ in the last term of the last equation we get,
$$
\begin{align}
a_{n} & = \alpha_{1}r_{0}^{n-2} (r_{0}^{2}) + \alpha_{2}r_{0}^{n-2}(nr_{0}^{2} - (2r_{0}^{2} - 2r_{0}^{2})) \\
a_{n} &  = \alpha_{1}r_{0}^{n}+\alpha_{2}nr_{0}^{n}
\end{align}
$$
Hence, $\alpha_{1}r_{0}^{n} + \alpha_{2}nr_{0}^{n}$ is a solution of the recurrence relation.

Now, for any sequence $\{ a_{n} \}$ which is a solution of the recurrence relation, for it to be of the form $\alpha_{1}r_{0}^{n} + \alpha_{2}nr_{0}^{n}$, there must exist $\alpha_{1},\alpha_{2}$ such that
$$
\begin{align}
a_{0} & = \alpha_{1}r_{0}^{0} + \alpha_{2}(0)r_{0}^{0} &  = \alpha_{1} \\
a_{1} & = \alpha_{1}r_{0} + \alpha_{2}r_{0}
\end{align}
$$
Solving the equations we get that, $\alpha_{1} = a_{0}$ and $\alpha_{2} = \frac{a_{1}-a_{0}r_{0}}{r_{0}}$. Hence, such $\alpha_{1},\alpha_{2}$ always exist.

Hence, proved the theorem.

>[!Note]
>For a general solution of a degree $2$ recurrence relation, it must have 2 degrees of freedom i.e. two independent variables. In the first solution, where the roots were distinct, we had them in the form of $\alpha_{1}$ and $\alpha_{2}$ in $\alpha_{1}r_{1}^{n}+\alpha_{2}r_{2}^{n}$. But when there is only one root, then in that case $\alpha_{1}r_{0}^{n}+\alpha_{2} r_{0}^{n}$ just collapses into $\alpha'r_{0}^{n}$. Hence we need the $n$ to make sure the two terms doesn't collapse into just one.

