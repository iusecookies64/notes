There are many combinatorial problems made on this idea of inclusion and exclusion principle. Below we start discussing different and lead to ideas of inclusion and exclusion principle.

**Problem 1:** Lets start the discussion with a problem that we have already discussed that is counting the number of solutions to the equation $x_1 + x_2 + \dots + x_n = R$ where $0 \leq x_i \leq R$ and we know that the answer to this problem is simply $\binom {R + n - 1}{n-1}$. 

**Problem 2:** Consider the problem of finding the number of solutions for the equation $x_1 + x_2 + x_3 \leq R$ and $0 \leq x_i \leq R$. To solve this we can add another variable $x_4$ which will convert the above equation to $x_1 + x_2 + x_3 + x_4 = R$ i.e we can always make the sum equal to $R$ by adding another variable which takes value which is balance i.e $R - (x_1 + x_2 + x_3)$. Clearly here $0 \leq x_4 \leq R$, hence total number of solutions to above equation is simply solution to the modified equation which is $\binom {R + 3}3$.

**Problem 3:** Now we need to find the number of solutions to the equation $x + y + z = 10$ where $2 \leq x, y, z \leq 6$. The range of values that $x, y, z$ take makes this problem tricky. To solve this we replace $x = a + 2$ this makes value of $a$ in range $0 \leq a \leq 4$. Similarly we will replace $y = b + 2$ and $z = c + 2$, the original equation now transforms to $x + y + z = a + b + c + 6 = 10 \rightarrow a + b + c = 4$. The solutions of this equation can be found using method used in problem $1$ which is $\binom 62$.

**Problem 4:** Lets again the equation a little bit, this time we need to solve the equation $x + y + z + w \leq 20$ and here $3 \leq x \leq 20$ and $1 \leq y \leq 20$ and $z, w \geq 0$. Here also we replace $x = a + 3$ and $y = b + 1$, this transforms the original equation to $a + b + z + w \leq 16$, where $0 \leq a \leq 17$ and $0 \leq b \leq 19$. Note that values of $a, b, z, w$ that are $\gt 16$ are not valid, hence $0 \leq a, b, z, w \leq 16$ and this problem is similar to the problem $3$ and answer to this problem is $\binom {20}4$.

**Problem 5:** Now we need to find the number of solutions to the equation $x + y + z = 8$ where $0 \leq x, y, z \leq 7$. To solve this we first consider all solutions and then we will remove invalid solutions from total solutions. Total solutions are $\binom {10}2$, in an invalid solution there will one variable among $x, y, z$ whose value will be $\gt 7$ and the remaining variables will have a value equal to $0$. The number of such solutions are clearly $3$, hence final answer is $\binom{10}2 - 3$.

**Problem 6:** A slight modification to above problem, lets try to solve $x + y + z = 6$ where $0 \leq x, y, z \leq 2$. Here total number of solutions are $\binom 82$ these contain all solutions where number of invalid variables are $\geq 0$. Then we start removing the invalid solutions, starting with solutions in which number of invalid variables are $\geq 1$. To make a variable invalid we replace it with another variable, for example if we make $x$ as invalid we can replace it with $x = a + 3$ where $0 \leq a \leq 3$ then this variable is surely invalid, if we place this in our equation we get new equation as $a + y + z = 3$ and number of solutions to this problem is $\binom 52$ because now there is not restriction on the values of the variables. Number of ways to choose $1$ invalid variable is $\binom 31$, hence total invalid solutions of this type will be $\binom 31 \binom 52$.

Note when counting number of invalid solutions with number of invalid variables $\geq 1$ there will be solution that have $2$ invalid variables and these will also be counted. Now when we fix $x$ as permanent invalid variable there will be some solution in which along with $x$, $y$ is also invalid. Similarly when we fix $y$ there will be some solution with $x$ as invalid this is over counting. To fix this we need add number of solutions with $\geq 2$ invalid variables. Replacing two variables with $a + 3$ and $b + 3$ we get $a + b + z = 0$ and number of solutions of this equation is $\binom 22$ and hence total solutions of this type will be $\binom 32 \binom 22$.

Now solutions with $\geq 3$ invalid variables is not possible so we stop here. The final answer is

$$\binom 82 - \binom 31\binom 52 + \binom 32 \binom 22$$

**Generalization:** From the above we can generalize the solution to such problem as $x_1 + x_2 + \dots + x_n = R$ and $0 \leq x_1, x_2, \dots, x_n \leq m$ as 

$$\sum_{i=0}^{n} (-1)^i \binom {R - i(m+1) + n - 1}{n-1}$$
This comes directly from inclusion exclusion principle in set theory. Below is an implementation for above general problem.

```c++
typedef long long ll;
ll numberOfSolutions(ll n, ll m, ll R)
{
	ll res = 0;
	for(int i = 0; i <= n; i++)
	{
		if(R < i * (m + 1)) break;
		ll curr = ncr(n, i) * ncr(R - i * (m + 1) + n - 1, n-1) % mod;
		if(i % 2) res = (res - curr + mod) % mod;
		else res = (res + curr) % mod;
	}
	return res;
}
```

**Problem 7:** Count of number which are divisible by $4$ and $6$ in the range $[1, N]$. Let $C_i$ denote the count of number in range $[1, N]$ which are divisible by $i$, then the answer to above problem is $C_4 + C_6 - C_{12}$, here $12 = lcm(4, 6)$.

Now consider that we need to solve above problem for $4, 6, 9$, then we again need to use inclusion exclusion
and answer will be $C_4 + C_6 + C_9 - (C_{lcm(4, 6)} + C_{lcm(4, 9)} + C_{lcm(9, 6)}) + C_{lcm(4, 6, 9)}$.

**Generalization:** Lets say we need to find the count of numbers divisible by either $x_1, x_2, x_3, \dots, x_k$ in the range $[1, N]$. The general formula to solve this will be 

$$\sum_{i=0}^k C_{x_i} - \sum_{i, j, i \neq j} C_{lcm(x_i, x_j)} + \sum_{i, j, k, i\neq j\neq k} C_{lcm(x_i, x_j, x_k)} - \dots$$
The question is how do we implement this in code. If we look closely each term in the above expression is just calculating number of divisors of $lcm$ of some subset of divisors. If the number of divisors in the subset are even then we subtract this count from answer, otherwise we add this count in our answer. Hence to solve this elegantly we can use *bitmask*.

```c++
long long numbersDivisible(long long N, vector<long long> divisor)
{
	long long n = divisor.size();
	long long res = 0;
	for(int mask = 1; mask < (1 << n); mask++)
	{
		long long count = 0;
		long long lcm = -1;
		for(int i = 0; i < n; i++)
		{
			if(!(mask & (1<<i))) continue; // i not in mask
			count++;
			if(lcm == -1) lcm = divisor[i];
			else lcm = getLcm(lcm, divisor[i]);
		}
		long long numOfFactors = N / lcm;
		if(count % 2) res += numOfFactors;
		else res -= numOfFactors;
	}
	return res;
}
```

**Problem 8:** Lets say now we need to find the $kth$ smallest number which is divisible by either $4, 6, 9$. To solve this we have to use binary search and find the smallest number $N$ such that numbers divisible by $4, 6, 9$ in range $[1, N]$ is $\geq k$.
#### Ugly Numbers Problem
Given a number $k$ and we need to find the $kth$ smallest number that is divisible by only $2, 3, 5$. Here $k \leq 10^5$. To solve this the only way we have is to generate all numbers and then return the $kth$ smallest number. Now we start with $1$ and push it into a priority queue, then we keep looping $k$ times and in each turn we get the smallest element out and multiply it with $2, 3, 5$ and push the new number that can be formed into the priority queue. After we are done we will have the $kth$ smallest integer multiple of only $2, 3, 5$.

```c++
long long kthSmallest(int k)
{
	vector<int> factors = {2, 3, 5};
	set<long long> st;
	st.insert(1);
	ll ans;
	while(k--)
	{
		long long smallest = *st.begin();
		st.erase(st.begin());
		ans = smallest;
		for(int factor : factors) st.insert(smallest * factor);
	}
	return ans;
}
```

**Problem 9:** Given an array $A$ of $N$ integers and we need to find the number of subsequence whose median is also present in the subsequence. $N \leq 1000$ and $1 \leq A[i] \leq 2000$ and we need to print the answer mod $10^9+7$.

```c++
typedef long long ll;
ll N = 2200;
ll fact[N], factInv[N];
void preCalculateFactorial()
{
	fact[0] = 1;
	factInv[0] = 1;
	for(int i = 1; i < N; i++)
	{
		fact[i] = (fact[i-1] * i) % mod;
		factInv[i] = binpow(fact[i], mod-2);
	}
}

ll ncr(ll n, ll r)
{
	return (fact[n] * factInv[r] % mod) * factInv[n-r] % mod;
}

void numberOfGoodSubsequences(vector<ll> arr)
{

}
```