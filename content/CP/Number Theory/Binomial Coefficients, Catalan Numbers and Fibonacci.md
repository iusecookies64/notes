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
There are many problems in which the solution finally falls down to calculation of Catalan Number, few of them are discussed below.