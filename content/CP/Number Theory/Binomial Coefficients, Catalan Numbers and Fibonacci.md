## Binomial Coefficients

### Different Ways to Calculate Binomial Coefficients

#### Method 1 (Factorial Method)
The first way to calculate the value of binomial coefficients mod $P$ (where $P$ is a prime) is to simply pre-compute values of factorials in an array and then the value of $^nC_r$ can be calculated as $^nC_r = (fact[n] \times modInv(fact[r] \times fact[n-r]) \% P$. This method works for values of $n \leq 10^6$.

```c++
long long N = 1001000;
long long mod = 1e9+7;
long long fact[N];

void computeFactorials()
{
	fact[0] = 1;
	for(int i = 1;i < N; i++)
	{
		fact[i] = fact[i-1] * i % mod;
	}
}

long long getNCR(long long n, long long r)
{
	return fact[n] * binpow(fact[r]*fact[n-r] % mod, mod-2) % mod;
}
```

#### Method 2 (Pascals Triangle Method)
The second method is to use pascal triangle law to pre-compute values of $^nC_r$ i.e using the law $^nC_r = ^{n-1}C_r + ^{n-1}C_{r-1}$. This method works for $n \leq 4000$ and lets us calculate the value of $^nC_r$ mod $P$ where $P$ can be positive integer (not necessarily a prime number). This is because we are not longer dividing to calculate the value, we are just adding.

![[Pasted image 20240908172617.png | center]]

```c++
typedef long long ll;
ll N = 4000;
ll ncr[N+1][N+1];

void preCompute()
{
	ncr[0][0] = ncr[1][0] = ncr[1][1] = 1;
	for(int i = 2; i < N; i++)
	{
		ncr[i][0] = 1;
		for(int j = 1; j <= i; j++)
		{
			ncr[i][j] = (ncr[i-1][j] + ncr[i-1][j-1]) % mod;
		}
	}
}

ll getNCR(ll n, ll r) return ncr[n][r];
```

#### Method 3 (Multiplication Method)
This method can be when value of $r$ or $n-r$ is $\leq 10^6$ and we want to calculate the value of $^nC_r$ once. The idea comes from the formula of $^nC_r$ which is $^nC_r = \frac {n!}{(r)!(n-r)!} = \frac {n (n-1) (n-2) \dots (n-r+1)}{1.2.3\dots r}$. We can calculate this value iteratively as $\prod^{i=r}_{i=0} \frac {n - i}{i+1}$, note that this value always stays integer during the computation as product of $i$ consecutive integers is always divisible by $i!$.

```c++
long long getNCR(long long n, long long r)
{
	if(r >= n/2) r = n - r;
	long long res = 1;
	for(int i = 0; i < r; i++)
	{
		res *= (n - i);
		res /= (i + 1);
	}
	return res;
}
```

### Properties of Binomial Coefficients
#### Summation Relation
This can be proved by putting $x = 1$ in the binomial expansion of $(1+x)^n$.

$$\newline\sum^{r=n}_{r=0} \binom nr = \binom n0 + \binom n1 + \dots + \binom nn = 2^n\newline$$

Another relation that comes from derivative of $(1+x)^n$ and putting $x = 1$ is,

$$\newline\sum^{r=n}_{r=0} r.\binom nr = 0.\binom n0 + 1.\binom n1 + 2.\binom n2 + \dots + n.\binom nn = n.2^{n-1}\newline$$

#### Hockey Stick Formula
This formula describes the relation in the value of items in pascals triangle and diagonals. The formula is,

$$\newline\sum^{m=n}_{m=k} \binom mk = \binom kk + \binom {k+1}k + \binom {k+2}k + \dots + \binom nk = \binom {n+1}{k+1}\newline$$

**Algebraic Proof** of this can be done using induction where we know that the result is true for $n = k$ i.e $\binom kk = \binom {k+1}{k+1}$, now we assume that the result is true for some $n \gt k$ and easily prove that it is true for $n+1$ as well.

**Combinatorial Proof** the right hand side is simply number of ways to select $k+1$ items from $n+1$ items. We calculate the value using $\binom {n+1}{k+1}$ or we can first try to fix the right most item and then choose remaining. The choice for right selected items starts from item $k+1$, because if we choose $i < k+1$ as the right most items then there won't be enough items to its left available to be selected. Now if we choose the right most item as $k+1$ then number of ways to choose remaining $k$ items is $\binom kk$, similarly if we choose item $k+2$ as the right most item then number of ways to select $k$ items would be $\binom {k+1}k$ and so on.

**The Reason** this formula is called hockey stick formula is because its representation in pascals triangle looks like a hockey stick.

![[Pasted image 20240907143335.png | center]]

#### Vandermonde's Identity
It gives a formula to calculate the number of ways to select $k$ items out of $n + m$ items i.e $\binom {n+m}k$ and it goes by,

$$\newline\binom {n+m}k = \sum_{i=0}^{i=k} \binom ni \binom m{k-i}\newline$$

i.e the summation of choosing $i$ items from group with $n$ items and remaining $k-i$ items from group with $m$ items.

In this if we put $m = n$ and $k = n$ we get,

$$\newline\sum_{i=0}^{n} \binom ni^2 = \binom {2n}{n}\newline$$

#### Solutions Of Unit Coefficient Linear Equation
Lets say we need to find the number of solutions to the equation $x_1 + x_2 + \dots + x_k = R$ where $R$ and $x_i \geq 0$ is a positive integer, then the number of solutions are equal to $\binom {R + k - 1}{k-1}$. The proof for this is simple, we take $R$ balls and $k-1$ dividers, then we arrange the dividers and balls, the dividers create $k$ partitions and the count of balls in $ith$ partition we assign to $x_i$ and adding all of the $x_i$ gives a total equal to number of balls which is $R$ i.e this gives us a solution. Hence number of solutions is simply number of ways to arrange $R$ identical balls and $k-1$ dividers.

![[Pasted image 20240908173508.png | center]]

The problem can be restated as number of ways to divide $R$ identical items into $k$ groups.

**Note:** If the condition was that each group has at least $1$ items then we simply first give $1$ item in each group and then solve the same problem with $R-k$ items.

#### Sum of Diagonals In Pascal's Triangle
In a pascals triangle, the sum of elements on a diagonal has a relation with Fibonacci numbers, more formally

$$\newline\sum _{i=0}^{n/2} \binom {n-i}{i} = Fib(n+1)\newline$$

Visually this looks something like this,

![[Pasted image 20240908174826.png | center]]
#### Lucas Theorem
This theorem helps us in finding the value of $\binom nr$ mod $p$  and is given by,

$$\newline\binom nr mod \hspace{1mm} p = \binom {\lfloor \frac np \rfloor} {\lfloor \frac rp \rfloor} \binom {n \hspace{1mm} mod \hspace{1mm} p}{r\hspace{1mm} mod \hspace{1mm} p}\hspace{1mm} mod \hspace{1mm} p\newline$$

Using this formula we can calculate the value in $log(P)$ time. What this formula says is that we represent $n$ and $r$ in base $p$ number system i.e lets say $(n)_p = n_1 n_2 n_3$ and $(r)_p = r_1r_2r_3$ then we are calculating $\prod \binom {n_i}{r_i}$. Here if the length of $n$ and $r$ is not same in base $p$ then we simply add leading $0$'s to make the length same.

**Problem:** Given a number $n \leq 10^{12}$ and we need to count the number of even and odd numbers in the set $\{\binom n0, \binom n1, \dots, \binom nn\}$. And we need to solve this for $T$ test cases where $T \leq 10^5$.

**Solution:** To find whether $\binom nr$ is odd or even we can use Lucas theorem, $\binom nr$ is odd if $\binom nr mod \hspace{1mm} 2$ is $1$, otherwise it is $0$. As told above we will use the binary representation of $n$ and $r$. We use the observation that if there is bit which is set in $r$ and not set in $n$ then in the multiplication we will get $\binom 01$ which is $0$ and the whole product becomes $0$ and we say $\binom nr$ is even. Hence $\binom nr$ is odd if and only if $r$ is a submask of $n$, so we need to count the number of such $r$'s which is simply $2^k$ where $k$ is the number of set bits in $n$.

## Catalan Numbers
### Definition And Formula

These are the numbers that form the sequence $1, 1, 2, 5, 14, 42, \dots$, the general formula for $nth$ Catalan Number is given by

$$\newline C_n = \frac 1{n+1} \binom {2n}n\newline$$

We can also calculate $nth$ Catalan Number using the recurrence relation.

$$\newline C_{n+1} = \sum_{i=0}^n C_iC_{n-i}, \forall \hspace{1mm} n >= 0 \hspace{1mm} and \hspace{1mm} C_0 = 1\newline$$

### Problems Using Catalan Numbers

#### Number Of Paths Not Crossing Diagonal
We need to find the number of paths from point $(0,0)$ to $(n, n)$ such that the path always stays below the diagonal (never crosses it). For more understanding consider the following diagram.

![[Pasted image 20240908215601.png | center]]

Now to count every invalid path we can do a need little trick which is to rotate the path about the diagonal above the main diagonal *at points* where the invalid path intersects the diagonal, and each time these invalid diagonal end up at the point $(n-1, n+1)$. For example consider the invalid path in the above diagram, and if we rotate the path about the above diagonal we see that this path also ends up at the point $(n-1, n+1)$.

![[Pasted image 20240908221512.png | center]]

Hence to the number of ways would be total number of ways subtracted from invalid number of ways.

$$\binom {2n}{n} - \binom {2n}{n-1} = \frac 1{n+1} \binom {2n}{n}$$
>[!Note]
>Another way to look at this problem is that we need to count the number of ways to arrange right and up moves such at any point the number of right moves done are greater than or equal to number of up moves. This analogy helps us to relate it with the problem of counting the number of balanced parenthesis strings.
#### Number of Balanced Parenthesis Strings
Consider the problem of counting the number of balanced parenthesis strings with $n$ pairs of brackets. To solve these types of problems it is always good to try to calculate the count for $n$ with smaller values of $n$. Here we just try to place the first pair and solve the problem for remaining $n-1$ pairs recursively. We always with placing a $($ character, at some point there will be the corresponding character $)$. Now we can write the original string $S$ from the perspective of the first pair it can be written as $(A)B$. Now the number of pairs $A$ can contain is anywhere between $[0, n-1]$, if $A$ contains $i$ pairs then $B$ will contain $n-1-i$ pairs. Total number of ways will be count of all of the ways i.e 

$$C_n = \sum_{i=0}^{n-1}C_iC_{n-1-i}$$

which is basically the formula for $nth$ Catalan number.

#### Number of Ways To Triangulate Convex Polygon
The problem of counting the number of ways to triangulate a convex polygon let $f(n)$ give the number of ways for $n$ sided polygon, clearly $f(2) = f(3) = 1$. For $n \gt 3$ we consider a the following process, we will choose a side as base, in the final answer this side will be base of some triangle, for reference look at the diagram below.

![[Pasted image 20240908231843.png | center]]

Hence if the polygon has $n$ sides, then after choosing a triangle like above we divide the polygon in two polygons. The number of sides of these polygons range from $[2, n-1]$ if one polygon has $i$ sides then other side will have $n + 1 - i$ sides where $i \in [2, n-1]$. Hence we have 

$$f(n) = f(2)f(n-1) + f(3)f(n-2) + \dots + f(n-1)f(2)$$

Now we see that $f(2) = 1 = C_0$ and $f(3) = 1 = C_1$ and using the above formula we have $f(4) = f(2)f(3) + f(3)f(2) = 2 = C_2$. Similarly we can go on and see that $f(n) = C_{n-2}$ which means that $C_n$ gives the number of ways to triangulate a polygon $n+2$ sides.

#### Number of Binary Trees
We need to count the number of rooted binary trees that can be made with $n$ nodes. We have one node at root level and we need to divide the remaining $n-1$ nodes in the left and right sides and solve the problem recursively. If we put $i$ nodes in the left side then in the right side we will have $n - 1 - i$ nodes, hence value for $n$ nodes is $f(n) = \sum_{i=0}^{n-1} f(i)f(n-1-i)$ which is basically the value of $nth$ Catalan Number.

#### Number of Non-Intersecting Handshakes
Consider that $2n$ persons are sitting at a circular table and we need to count the number of simultaneous handshakes possible such that no arms cross each other. For example consider the example of $6$ people shown below.

![[Pasted image 20240908235638.png | center]]

There are $5$ valid handshakes for $6$ persons which is equal to $C_3$. To solve this problem lets say there are $n$ pairs and we simply choose a pair of person, which divides the table in two halves such that on either side there are anywhere from $0$ to $n-1$ pairs. If there are $i$ pairs on one side then there will $n - 1 - i$ pairs on the other side which is again same as Catalan number.

## Fibonacci Numbers

### Definition And Formula

Fibonacci Number are the number of the sequence $0, 1, 1, 2, 3, 5, 8, 13, \dots$ which follow the recursion formula $F_n = F_{n-1} + F_{n-2}$ for $n \geq 2$ and $F_0 = 0$ and $F_1 = 1$. The value of $nth$ Fibonacci number can be approximated using the *Binet's Formula* as shown below

$$F_n = \frac 1{\sqrt 5}\left(\frac {1 + {\sqrt 5}}2\right)^n - \frac 1{\sqrt 5}\left(\frac {1 - {\sqrt 5}}2\right)^n$$

For larger values of $n$ the subtrahend side diminished to $\approx 0$ and we are only left with minuend i.e $\frac 1{\sqrt 5}\left(\frac {1 + {\sqrt 5}}2\right)^n$ which is also known as the *Golden Ration*.

#### Calculation of Fibonacci Numbers (Iterative Method)
The most simple way to calculate Fibonacci Numbers is to iterate and use dynamic programming.

```c++
int fib[100100];
void preCalculateFib()
{
	fib[0] = 0;
	fib[1] = 1;
	for(int i = 2; i < 100100; i++)
	{
		fib[i] = fib[i-1] + fib[i-2];
	}
}
```

This method takes $O(n)$ time to calculate Fibonacci numbers till $n$.

#### Calculating Fibonacci Number (Matrix Multiplication method)
An interesting fact about Fibonacci Numbers is that they can be represented as power of a $2\times2$ matrix as show below.

$$\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^n = \begin{bmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{bmatrix}$$

Combining this with binary exponentiation we can calculate the value of $F_n$ in $log(n)$ time.

```c++
struct TwoByTwoMatrix {
	int c11, c12, c21, c22;
	TwoByTwoMatrix(int a, int b, int c, int d)
	{
		c11 = a, c12 = b, c21 = c, c22 = d;
	}
	TwoByTwoMatrix()
	{
		c11 = 1, c12 = 0, c21 = 0, c22 = 1; // identity matrix
	}
	TwoByTwoMatrix operator*(TwoByTwoMatrix const &mat)
	{
		int a = c11*mat.c11 + c12*mat.c21;
		int b = c11.mat.c12 + c12*mat.c22;
		int c = c21*mat.c11 + c22*mat.c21;
		int d = c21.mat.c12 + c22*mat.c22;
		TwoByTwoMatrix res(a, b, c, d);
		return res;
	}
};

TwoByTwoMatrix binPow(TwoByTwoMatrix a, int b)
{
	if(b == 0) return TwoByTwoMatrix(); // returning identity matrix
	TwoByTwoMatrix res = binPow(a, b/2);
	res = res * res;
	if(b % 2) res = res * a;
	return res;
}

int getFibonacci(int n)
{
	if(n == 0) return 0;
	if(n == 1) return 1;
	TwoByTwoMatrix a(1, 1, 1, 0);
	TwoByTwoMatrix res = binPow(a, n);
	return res.c12;
}
```

#### Some Properties of Fibonacci Numbers

1. **Sum of Fibonacci Numbers** i.e $F_0 + F_1 + \dots + F_n = \sum_{i=0}^n F_i = F_{n+2} - 1$. To prove this we can simply add and subtract $F_1$ as shown below.
	$$F_1 - F_1 + (F_0 + F_1 + \dots + F_n) \newline = ((F_0 + F_1) + F_1 + \dots + F_n) - F_1 \newline = ((F_2 + F_1) + \dots + F_n) - F_1 = \dots = (F_{n+1} + F_n) - F_1 = F_{n+2} - F_1 = F_{n+2} - 1$$
	Using The Similar Idea we can generalize the sum of $k$ consecutive Fibonacci Numbers.

2. **Sum of Squares of Fibonacci Numbers** i.e $F_0^2 + F_1^2 + F_2^2 + \dots + F_n^2 = F_n . F_{n+1}$ and we can prove this using induction, the expression is trivially true for $n = 1$. Let it be true for some $n \gt 1$ then we can say that for $n+1$ we have $F_0^2 + F_1^2 + \dots + F_n^2 + F_{n+1}^2 = F_n . F_{n+1} + F_{n+1}^2 = F_{n+1}(F_n + F_{n+1}) = F_{n+1}.F_{n+2}$. Hence proved.

3. **Convolution Property:** $F_n = F_m.F_{n-m+1} + F_{m-1}.F_{n-m}$ to prove this we can substitute $F_m = F_{m-1} + F_{m-2}$ in the equation which gives us $F_n = (F_{m-1} + F_{m-2}).F_{n-m+1} + F_{m-1}.F_{n-m} = F_{m-2}.F_{n-m+1} + F_{m-1}.F_{n-m+2}$, now we substitute $F_{m-1} = F_{m-2} + F_{m-3}$ and so on, at the end we will be left with $F_n = F_1.F_n + F_0.F_{n-1} = F_n$.

4. **Division Property:** This property states that $nth$ Fibonacci number divides any $k.nth$ Fibonacci Number i.e those numbers whose positions are multiples of $n$, for example $F_3 = 2$ divides $F_6 = 8$. This also means if $F_n$ divides $F_m$ then $n$ divides $m$.

5.  **GCD Property:** This property states that $gcd(F_n, F_m) = F_{gcd(n, m)}$, this helps in finding the gcd of large Fibonacci Numbers i.e we first find $gcd(n, m)$ and then find that Fibonacci Number.


