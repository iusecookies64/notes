# Number Theory

## Sieve of Eratosthenes

This method helps find all prime number in range $[1, n]$ for all $n <= 10^7$. Below is a basic implementation of this algorithm.

```c++
vector<int> sieve(int n)
{
    vector<int> primes;
    vector<bool> isPrime(n + 1, true);	// initially we assume every number is prime
    for(int i = 2; i <= n; i++)
    {
        if(!isPrime[i]) continue;
        // i is prime so we mark all its multiples as not prime
        primes.push_back(i);
        for(int multiple_i = 2 * i; multiple_i <= n; multiple_i += i)
        {
            isPrime[multiple_i] = false;
        }
    }
    return primes;
}
```

**Time Complexity:** time complexity of this algorithm is $O(nlog(log(n)))$ which is $\approx O(n)$. It is calculated as

​							 $\frac n2 + \frac n3  + \frac n5 + ... = n * (\frac 12 + \frac 13 + \frac 15 + ...)$  

as we are looping all multiples of each prime.  And the number of prime numbers $<= n$ are $\approx \frac n{logn}$, this means $kth$ prime number is $\approx klogk$.  This makes final expression as 

​								$n * (\frac 12 + \sum_{k=2}^{k=\frac n{logn}} \frac 1{klogk})$ 

here we have taken $\frac 12$ separately because for $k = 1$ we will have $logk = 0$ and it will be division by $0$.

Now for large values of n, we can approximate this summation with integration as shown below.

​								 $$\sum_{k = 2}^{\frac n {\ln n}} \frac 1 {k \ln k} \approx \int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk.$$ 

The antiderivative for the integrand is $\ln \ln k$ . Using a substitution and removing terms of lower order, we'll get the result:

​					$$\int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk = \ln \ln \frac n {\ln n} - \ln \ln 2 = \ln(\ln n - \ln \ln n) - \ln \ln 2 \approx \ln \ln n.$$

**Small Optimization:** a small optimization would be to start looping over multiples of prime $p$ from $p * p$ and not $2 * p$ as all multiples of prime $p$ from $2 * p$ to $(p-1) * p$ has a smaller prime factor other than p and will be already marked as not prime by them. This is a constant factor optimization doesn't drastically effect the performance but good to have. One thing that we need to be careful of is that if we start from $p * p$ then this value will easily overflow if using `int` data type, so we must convert it to `long long` or simple add a check before starting the inner for loop.

```c++
if((long long)i * i <= n)
{
    // we loop over multiples of i from i * i here
}
```

---

## Segmented Sieve

Consider a problem that we need to find all prime numbers in range $[a, b]$ such that $1 <= a <= b <= 10^{12}$ and $b - a <= 10^6$.

The idea for the solution is based on the fact that for any number that is not prime has a prime factorization i.e it can be written as $P_1^{a_1} * P_2^{a_2} * P_3^{a_3} ..$ where $P_1$ $P_2$ $P_3$ are prime numbers. Among all prime factors of a number only one of them can be $>= \sqrt n$ and since the number is not prime it means that must be another prime factor which will be $<= \sqrt n$. 

Hence to find all prime factors in range $[a, b]$, we will first find all prime numbers in range $[1, \sqrt b]$. And then mark all of there multiples in range $[a, b]$ as non primes. Since $b <= 10^{12}$ we have $\sqrt b <= 10^6$ and this is a feasible solution.

```c++
// segmented sieve code
vector<long long> segmentedSieve(long long a, long long b)
{
    // finding all primes in range [1, sqrt(b)]
    long long n = sqrt(b);
    vector<bool> isPrime(n + 1, false);
    vector<long long> primes;
    for(int i = 2; i <= n; i++)
    {
        if(!isPrime[i]) continue;
        primes.push_back(i);
        if((long long)i * i > n) continue;
        for(int j = i * i; j <= n; j+=i)
        {
            isPrime[j] = false;
        }
    }
    
    // we store elements of range [a,b] in range [0, b - a] by subtracting each number with a
    vector<long long> isPrime2(b - a + 1, true);
    for(auto prime : primes)
    {
        // finding first multiple of prime in range [a, b]
        long long multiple = ((a + prime-1)/prime) * prime;
        // it might happen that multiple == prime, in that case we don't want to mark it as non prime
        if(multiple == prime)
            multiple += prime;
        for(; multiple <= b; multiple += prime)
        {
            isPrime2[multiple - a] = false;
        }
    }
    
    vector<long long> primeInSegment;
    for(long long i = 0; i <= b - a; i++)
    {
        if(isPrime2[i] && i + a >= 2)
        {
            primeInSegment.push_back(i + a);
        }
    }
    
    return primeInSegment;
}
```

---

## Fast Factorization

Here we want to find the prime factorization of all numbers in range $[1, 10^6]$ in fastest way possible. The idea is that for every number we will store its **smallest prime factor (spf)**. Then to find prime factorization we just need to keep find `spf[num]` and then divide `num / spf[num]` while `num != 1`.

Making `spf` array is simple using some modifications in sieve as shown in below implementation.

```c++
vector<int> build_spf(int n)
{
    vector<int> spf(n + 1);
    for(int i = 1; i <= n; i++)
        spf[i] = i;
    
    for(int i = 2; i <= n; i++)
    {
        if(spf[i] != i) continue;
        // current number is prime
        if((long long)i * i <= n)
        {
        	for(int j = i * i; j <= n; j+=i)
            {
                // if j is unmarked till now, spf[j] = i
                if(spf[j] == j)
                    spf[j] = i;
            }
        }
    }
    return spf;
}

vector<vector<int>> fact_factorization(int n)
{
    vector<int> spf = build_spf(n);
    vector<vector<int>> prime_factors(n + 1);
    for(int i = 2; i <= n; i++)
    {
        int num = i;
        while(num != 1)
        {
            prime_factors[i].push_back(spf[num]);
            num /= spf[num];
        }
    }
    return prime_factors;
}
```

**Note:** the number of prime factors of a number if bounded by $\log(n)$. Hence storing prime factors of all number in a range $[1,n]$ will take $O(nlogn)$ space.

Lets discuss an interesting problem that uses fast factorization.

**Problem:** Given an array of positive integers $A$ of size $n (<= 10^6)$, we need to find number of pairs $(i, j)$ such that $A_iA_j$​ is a **cube number**.

**Solution:** Consider a number $A_i$ having prime factorization $P_1^{a_1}P_2^{a_2}P_3^{a_3}$, lets define a function $norm(A_i) = P_1^{a_1\%3}P_2^{a_2\%3}P_3^{a_3\%3}$. Clearly a counter number $A_j$ such that $A_iA_j$ is a cube will have all power of $P_1P_2P_3$ as $(3 - a_1\%3)\%3$ and same for $a_2$ and $a_3$. Because then only the after multiplying we will have all powers of prime multiples of 3.

Hence for every number in array we will store it in norm form and count of numbers with which it will make a cube will be count of inverse norm of that number.

---

## Euler Totient Function

This function represented as $\phi(n)$ is the number of **coprimes of** $n$ in range $[1, n-1]$ and is defined by 

​							$$\phi(n) = n (1 - \frac 1{p_1})(1 - \frac 1{p_2})...$$

where $p_1$ $p_2$ ... are the prime factors of n.

**Derivation:** The formula for this can be derived using simple inclusion and exclusion principle. Consider the prime factors of number to be only $p_1$ and $p_2$ then number of coprime of $n$ in range $[1, n-1]$ are simple count of number that don't have factors as $p_1$ and $p_2$ which is equal to $n$ - number of multiple of  $p_1$ and $p_2$. 

Hence,

​	 $$\phi(n) = n - \frac n{p_1} - \frac n{p_2} + \frac n{p_1p_2} = n (1 - \frac 1{p_1})(1 - \frac 1{p_2})$$

Similarly we can derive this for numbers with 3 prime factors, numbers with 4 prime factors and so on.

**Implementation**: using the above formula directly in code will lead to dealing with floating point and errors associated with it. But we can use a simple process to calculate this which is described as shown.

​	 $$\phi(n) = n (1 - \frac 1{p_1})(1 - \frac 1{p_2}) = (n - \frac n{p_1})(1 - \frac 1{p_2}) = n'(1 - \frac 1{p_2}) = (n' - \frac{n'}{p_2}) = n''$$​

In other words initially we will have `phi[n] = n` then we subtract from it its first prime factor i.e $p_1$ and get `phi[n] -= phi[n] / p1` and repeat the process for all prime factors. Note that `phi[n] / p` will always be an integer since $p$ is a factor of $n$.

**Problem:** We have to find $\phi(n)$ for all number in range from $[1, n]$ where $n <= 10^6$.

**Solution:** we have to follow above process for every number in the given range, which can be easily achieved using sieve. Below is the implementation of this.

```c++
vector<int> eulerTotient(int n)
{
    vector<int> phi(n+1);
    for(int i = 1; i <= n; i++)
        phi[i] = i;
    
    // sieve
    for(int i = 2; i <= n; i++)
    {
        if(phi[i] == i)
        {
            // i is prime
            for(int j = i; j <= n; j+=i)
            {
                phi[j] -= (phi[j] / i);
            }
        }
    }
    return phi;
}
```

**Some Properties Related To Euler Totient Function**

1. $\phi(p) = p-1$, where $p$ is a prime number.
2. $\phi(p^k) = p^k - p^{k-1}$, where $p$ is a prime number.
3. $\phi(ab) = \phi(a) * \phi(b)$, if $gcd(a, b) = 1$.

---

## Factorization Based Counting Problems

Consider a number $n$ and it has prime factorization $n = P_1^{a_1} * P_2^{a_2} * P_3^{a_3} ..$ and consider $d_1, d_2,d_3,..$ to be divisors of n, then we have sum $S_k$ defined as 

​	 $$S_k = \sum d^k$$​

Based on this we have $S_0$ as the number of divisors and $S_1$​ as the sum of divisors.

Some of the most common factorization based counting problems are,

1. Number of divisors of $n = S_0 = (a_1 + 1)(a_2+1)(a_3+1)...$.

2. Sum of divisors of $n = S_1 = (P_1^0 + P_1^1 + ... + P_1^{a_1})(P_2^0 + P_2^1 + ... + P_2^{a_2})(P_3^0 + P_3^1 + ... + P_3^{a_3})... = (\frac{P_1^{a1+1} - 1}{P_1-1})(\frac{P_2^{a2+1} - 1}{P_2-1})(\frac{P_3^{a3+1} - 1}{P_3-1})...$.

3. Product of divisors $n = n^{\frac {S_0}2}$ i.e $n$ power number of divisors by 2.

   **Note:** that if number of divisors is not even that means all values $(a_1+1),(a_2+1),(a_3+1)$ are odd numbers which means $a_1,a_2,a_3$ are all even numbers and hence n is a square number in that case we product of divisors as $(\sqrt n)^{S_0}$​.

---

## Fermat's Little Theorem

The Fermat's little theorem says that for any number $a$ and a prime number $p$.

1. $a^p \equiv a$ mod $p$.
2. $a^{p-1} \equiv 1$ mod $p$, when $a$ is not divisible by $p$.

In most questions $p$ is a prime number and $a < p$ which automatically makes them coprimes.

**Problem:** given 3 numbers $a,b,c$ where $1 <= a,b,c <= 10^9$ and we need to calculate $a^{b^c}$ mod $p$ where $p = 10^9 + 7$.

**Solution:** the idea is simple $b^c$ can be written as $d(p-1) + r$ where $r$ is remainder when $b^c$ is divided with $p-1$. Clearly now the expression becomes $a^{d(p-1)}*a^r = 1 * a^r$. So, first we calculate $b^c$ mod $p-1$, let it be equal to $r$, then we calculate $a^r$ mod $p$.

```c++
void solve()
{
    int a, b, c;
    cin >> a >> b >> c;
    int p = 1e9+7;
    int r = binpow(b, c, p-1);	// b power c mod p-1
    int res = binpow(a, r, p);
    cout << res << nline;
}
```

**Euler's Theorem:** this is a general case of fermat's little theorem which states for any two integers $a$ and $m$ such that they are coprimes we have $a^x \% m = a^{x\%\phi(m)} \%m$. Where $\phi$ is **Euler totient function** and $\phi(m)$ is called **totative of m**.

---

## Power Of X In N!

Lets say we want to find the maximum power of $X$ $a$  such that $X^a$ is a divisor of $N!$.

To solve this we first need to know the method of finding the power of prime $P$ in $N!$, it is given by the below formula.

Maximum power of $P$ in $N! = \lfloor \frac N{P} \rfloor + \lfloor \frac N{P^2} \rfloor + \lfloor \frac N{P^3} \rfloor + ... + \lfloor \frac N{P^k} \rfloor$.

Let the prime factorization of $X$ be $P_1^{a_1} P_2^{a_2} P_3^{a_3}...$ and let $f(N, P)$ be the power of prime $P$ in $N!$, then power of $X$ in $N!$ is given by $min(\lfloor \frac {f(N,P)}{a_i} \rfloor)$​.

---

## Binary Exponentiation And Russian Peasant Multiplication

**Binary Exponentian:** this algorithm finds the power $a^b$ in $log_2(b)$ time complexity, the idea behind this is that $a^b = a^{\frac b2}*a^{\frac b2}$.

```c++
int binpow(int a, int b)
{
    // a^0 is 1
    if(b == 0) return 1;
    int temp = binpow(a, b/2);
    return temp * temp * (b % 2 ? a : 1);
}
```

We can also implement the above process in a iterative function rather than recursive one, this uses the fact that we can represent $a^b$ as multiplication of power of $a$ which are powers of $2$ using bit representation of $b$. For example if $b = 2^3 + 2^1 = 8 + 2$ then $a^b$ can be written as $a^b = a^8 * a^2$.

```c++
int binpow(int a, int b)
{
    int res = 1;
    while(b)
    {
        // if this bit is set, then multiply current power of a to res
        if(b & 1) res *= a;
        a *= a;
        b = (b >> 1);
    }
    return res;
}
```

**Russian Peasant Multiplication:** Consider of multiplying large numbers $a$ and $b$ modulo some number $m$. If $a,b,m$ are all of order $O(10^{18})$ then it is possible that $a * b$ will cause bit overflow and then taking mod afterwards is of no use. 

To solve this we can use **Russian Peasant Multiplication** method to multiply which uses the idea that $a * b$ can be written as multiplication of  $a$ with powers of $2$ from binary representation of $b$.Consider $b = 2^8 + 2^1$ then $a * b = 2^8*a + 2^1*a$.

We can calculate these powers of two multiples of $a$ by simply adding $a$ with itself i.e $a + a = 2a$ then $2a + 2a = 4a$ and so on. We can take mod while doing this so that in every step we only deal with increasing $a$ to $2a$.

```c++
long long multiply_mod(long long a, long long b, long long m)
{
    long long res = 0;
    while(b)
    {
        if(b&1) res = (res + a) % m;
        b >>= 1;
        a = (a + a) % m;
    }
    return res;
}
```

---

## Miscellaneous Ideas

Lets look at some miscellaneous ideas that might come in use, but are not that common.

1. Given a number $n$ we need to find number of ordered pairs of integers $(a, b)$ such that $\frac 1a + \frac 1b = \frac 1n$. Given that $n <= 10^{6}$.

   **Solution:** If we rearrange the equation we get $ab - na - nb = 0$. Adding $n^2$ on both sides we get the following equation:

   $$\Rightarrow ab - na - nb = 0$$

   $$\Rightarrow ab - na - nb + n^2 = n^2$$

   $$\Rightarrow (a-n) * (b-n) = n^2$$​

   So, we will go over all the divisors of $n^2$ using the $\sqrt n$ loop which will be $O(10^6)$. Let $d_i$ be a divisor of $n^2$, then we assign $d_i = a - n \Rightarrow a = d_i + n$.

   Similarly, we get corresponding value of $b$ as $b - n = \frac{n^2}{d_i} \Rightarrow b = n + \frac{n^2}{d_i}$.

   **Note:** Given that $a$ and $b$ can be integers i.e they can have -ve values, hence we can also assign $-d_i = a - n \Rightarrow a = -d_i + n$. And the value of $b$ will be $b - n = -\frac{n^2}{d_i} \Rightarrow b = n - \frac{n^2}{d_i}$​.

   **Note:** If $X$ is the number of factors of $n^2$ then the final answer is final answer is $2 * X - 1$, we subtract $1$ since case of $x = y = 0$ which gives $(0-n)*(0-n) = n^2$ is not valid.

2. Given a number $N$ ($N \leq 10^{12}$) and we need to find the value of $\lfloor \frac N1 \rfloor^3 + \lfloor \frac N2 \rfloor^3 + \dots + \lfloor \frac NN \rfloor^3$. Since the value might overflow we need to give answer mod $10^9+7$.

   **Solution:** Let $f(x) = \lfloor \frac Nx \rfloor$ be the function. The idea behing the solution is that there are only $O(\sqrt N)$ unique values of $f(x)$. For integers $\leq \sqrt N$, they will all have different values of $f(x)$ and for integers $\geq \sqrt N$ then will values in range $[1, \sqrt N]$. 

   But how do we use this idea, to solve the given problem. First of all we notice that values of $f(x)$ repeat, more over all integers $x$ which have same value of $f(x)$ are next to each other.

   The next observation that we use is the fact that the largest integer $i$ to have value $f(i) = k$ is $\lfloor \frac Nk \rfloor$. For example let $N = 21$ then $\lfloor \frac {21}2 \rfloor = 10$ is the largest integer to have value $2$.

   Lets say $i$ is the starting integer that have value $\lfloor \frac Ni \rfloor$, now as seen earlier the largest value to have this value is $\lfloor \frac N{\lfloor \frac Ni \rfloor} \rfloor$. And after this new value of $\lfloor \frac Ni \rfloor$ comes. So we start with $i = 1$, and calculate $la = \lfloor \frac N{\lfloor \frac Ni \rfloor} \rfloor$, then all values between $i$ and $la$ will have same value $f(x)$. After we process them we update $i = la + 1$ which will be starting integer for some other value of $f(x)$.

   Since in each iteration we find range of values of integers that have same value of $f(x)$ and we know there only $O(\sqrt N)$ unique values of $f(x)$, the time complexity of this loop will be $O(\sqrt N)$.

   ```c++
   ll modCube(ll x, ll m)
   {
       x %= m;
       return (x * x % m) * x % m;
   }
   void solve()
   {
       ll n; cin >> n;
       ll m = 1e9+7;
       ll res = 0;
       for(ll i = 1, la; i <= n; i = la + 1)
       {
           la = (n / (n / i));
           res += cube(n / i) * (la - i + 1) % m;
       }
       cout << res << nline;
   }
   ```

   

