## State Space Optimizations

> Whenever a state variable depends on other state variables, then we remove it from the state and save space. Lets learn it through the classical **Cherry Picking**  problem.

**Problem:** Given an $n\times m$ grid and Alice is standing at cell $(0, 0)$, she has to go to cell $(n-1, m-1)$ to buy groceries, every cell in the grid has some number of chocolates, and when Alice visits them, she picks all of them, find the maximum number of chocolates Alice can collect in her journey to cell $(n-1, m-1)$ and back home in cell $(0, 0)$.

**Solution:** One idea that comes to mind immediately is that we can first calculate the maximum sum path from $(0, 0)$ to $(n-1, m-1)$ and then find a path that gives this answer and then we update the number of chocolates on this cell to be $0$, then re-run the same program, but this approach is actually wrong because of the existence of multiple possible answers for a given answer which makes the possibilities for returning path different for different choice of first path. For example consider the two maximum sum paths given in the grid, below, the maximum possible sum in return path is different based on the choice for first path.

![[Pasted image 20240818225027.png | center]]

Hence it is not optimal to take this approach, so the approach we take is first we consider the going and returning path as $2$ paths that both originate from $(0, 0)$ and finally reach $(n-1, m-1)$. We will use a dp state `rec(i, j, a, b)` which is the maximum sum to reach $(i, j)$ via path $1$ and reach $(a, b)$ via path $2$. Now, calling transitions for all possible combinations of $(i, j)$ and $(a, b)$ is very tricky because of cases of overlapping, for example if we are at cell $(i, j)$ and cell $(a, b)$ was on the path, how do we know about it now. To overcome overlapping issue, we start both the paths from $(0, 0)$ at the same time, and we move them to next cells at the same time, this way when ever these reach a common cell, they will reach at the same time and their count we add to our answer only once. Now our state is `rec(i, j, a, b)` which gives maximum sum to reach $(n-1, m-1)$ such that path $1$ starts at cell $(i, j)$ and path $2$ starts at cell $(a, b)$.

```c++
int dx[] = {1, 0};
int dy[] = {0, 1};
int rec(int i, int j, int a, int b) {
	if(i == n-1 && j == m-1) return grid[i][j]; // they both reach here at the same time

	if(dp[i][j][a][b] != -1) return dp[i][j][a][b];

	int currSum = grid[i][j];
	if(i != a || j != b) currSum += grid[a][b];
	int ans = 0;
	for(int k1 = 0; k1 < 2; k1++) {
		int ni = i + dx[k1], nj = j + dy[k1];
		if(ni >= n || nj >= m) continue;
		for(int k2 = 0; k2 < 2; k2++) {
			int na = a + dx[k2], nb = b + dy[k2];
			if(na >= n || nb >= m) continue;
			ans = max(ans, rec(ni, nj, na, nb) + currSum);
		}
	}

	return dp[i][j][a][b] = ans;
}
```

**Time Complexity:** The time complexity of this solution is $O(n^3)$, this will become more obvious when we are done with the space optimizations. A mathematical proof would be to count the number of states that we will actually visit, the idea is that since we are moving by $1$ step in each iteration, the value of $i+j$ and $a+b$ also increases by $1$ in every iteration and also these values initially are equal, hence value of $i+j = a+b$. Which tells us that these always on the diagonal, the diagonals length starts from $1$ increases to $n$ and then decreases to $1$. The cells $(i, j)$ and $(a, b)$ may represent $2$ cells on the diagonal or represent $1$ cell. Hence on a diagonal of length $k$, number of reachable states are $^kC_2 + ^kC_1$. And summing this for $k \in [1, n]$ we get following

$$
= \sum^{k=n}_{k=1} (^kC_2 + ^kC_1) \newline
 
= \sum^{k=n}_{k=1} (^kC_2) + \sum^{k=n}_{k=1} (^kC_1) \newline

= \frac 12 \sum^{k=n}_{k=1} (k^2 - k) + \sum^{k=n}_{k=1} k

= O(n^3)
$$

**Space Optimization**: The space complexity of this approach is $O(n^4)$, but can be reduced to $O(n^3)$ using the fact that $i+j = a+b$, so, we will use the state `rec(i, j, a)` and calculate the value of $b$ as `b = i + j - a`.

## State Rotation

**Problem:** Given $N$ items where $ith$ item has weight $w_i$ and value $v_i$. You need to find maximum value of items that can be fitted in a knapsack of capacity $W$. Here $N \leq 100$ and $v_i \leq 1000$ and $W \leq 10^9$.

**Solution:** Here we can no longer use the state `rec(i, w)` which returns maximum value possible among items $\leq i$ such that their weight is $\leq W$ because $W$ is too large to store. In this case we try to interchange the state i.e interchange value with weight. A state since the value $v_i \leq 1000$ and $N \leq 100$, the maximum value possible is $maxVal \leq 10^5$. Hence we can use a state `rec(i, v)` which returns minimum weight of items such that their value is equal to $v$.

```c++
int rec(int i, int v) {
	if(v <= 0) return 0; // pruning
	if(i < 0) {
		if(v <= 0) return 0;
		else return inf; // invalid case
	}

	if(dp[i][v] != -1) return dp[i][v];

	int ans1 = rec(i-1, v); // case of not choosing ith item
	int ans2 = rec(i-1, v - value[i]) + weight[i];

	return dp[i][v] = min(ans1, ans2);
}
```

## Sorting DP Idea

**Problem:** There are $N$ students in a class and we are required to divide them into two groups $A$ and $B$ such that in group $A$ there are exactly $a$ number of students and in group $B$ there are exactly $b$ number of students. For each student you are given two values $(A_i, B_i)$, if the student is put in group $A$ then it gets happiness of $A_i$ and if it is put in group $B$ it gets happiness level of $B_i$. Divide the students in such a way that maximizes the total happiness. Note $a + b \leq N$ which means it might happen that some students are not part of any group.

**Solution 1:** Here the first state that comes to mind is `rec(i, sa, sb)` which is the maximum happiness when first $i$ students are divided into groups of size $sa$ and $sb$. The transition is either we don't put $ith$ student any group, then we get `rec(i-1, sa, sb)`, and if we put it in group $A$ or $B$ we get `rec(i-1, sa-1, sb) + A[i]` or `rec(i-1, sa, sb-1) + B[i]` and we choose the case with maximum value. The time complexity of this $O(n^3)$.

**Sorted Optimization:** the idea is that we sort one of the happiness values in decreasing order. Lets say we sorted values of $A$, then we can use state `rec(i, sb)` which returns the maximum happiness among first $i$ students such that there are $sb$ students in group $B$. The benefit now is that we can choose the value for $A$ greedily i.e lets say for current state we put $ith$ student in group $B$ then we go to state `rec(i-1, sb-1) + B[i]`, but if we are not putting in $B$ then we surely need to put it in $A$ since other value of $A[j] <= A[i], j \gt i$ which is give same or worse answer. Just we need to make sure that there is space in group $A$, which can be found out by `sa = min(a, i - sb)`. The time complexity now reduces to $O(n^2)$.

```c++
int rec(int i, int sb) {
	if(i == 0) {
		if(sb == 0) return 0;
		else return -inf; // invalid case
	}

	if(dp[i][sb] != -1) return dp[i][sb];

	int sa = min(a, i - sb);
	int ans1 = rec(i-1, sb-1) + B[i]; // putting ith student in group b
	int ans2 = rec(i-1, sb) + (sa < a) ? A[i] : 0;

	return dp[i][sb] = max(ans1, ans2);
}
```

## Iterative DP Optimizations

> Iterative dp is nothing but calculating the state of dp iteratively such that the states on which current state depends on are calculated before we reach this state. Iterative dp gives better performance in cases when almost all of the dp state are reached since in iterative dp we have to loop through all of the states unlike recursion in which it automatically goes only to the states that are possible. Iterative is also more efficient because there is not function call overhead and also in cases of large dp states, it might happen that recursion stack overflows and we get error. 

**Problem:** Given an array of coin values, we have an infinite supply of these coins, we are also given a value $S$ and we need to find if it is possible to make a sum of $S$ using the coins from the array.

**Solution:** we will use a dp state `dp[i][sum]` which tells whether it is possible to make a $sum$ from using coins from $\in [i, n-1]$. The transition is that either we completely not use $ith$ coin, in that case we get `dp[i+1][sum]`, and in case we decide to use it, then we go to state `dp[i][sum-value[i]]` this is because after choosing a coin once, we might choose it again. Coding it iteratively we move from $i = n$ to $i = 0$ and $sum$ from $0$ to $S$.

```c++
bool solve(vector<int>& value, int S, int n) {
	int dp[n+1][S+1];
	for(int i = n; i >= 0; i--) {
		for(int sum = 0; sum <= S; sum++) {
			if(i == n) {
				if(sum == 0) dp[i][sum] = 1; // possible
				else dp[i][sum] = 0; // not possible
			} else {
				dp[i][sum] = 0; // default value is not possible
				if(dp[i+1][sum]) dp[i][sum] = 1;
				if(sum >= value[i] && dp[i][sum - value[i]]) dp[i][sum] = 1;
			}
		}
	}

	return dp[0][S];
}
```

### Prefix Sum Optimization In Iterative DP

**Problem:** Given an array of positive integers of size $N$, each array element represents the size of a $ith$ pile of stones. We need to find number of ways to make a pile of size $S$ by choosing stones from the piles.

**Solution 1:** We will use a dp state `dp[i][sum]` which gives number of ways to make a pile of size $sum$ by choosing stones from piles $\in [i, n-1]$. Now from current pile we can choose $j$ stones where $j \in [0, arr[i]]$ and the number of ways for `dp[i][sum]` will be $\sum^{j=arr[i]}_{j=0} dp[i+1][sum - j]$. The time complexity of this approach is $O(n * max(arr[i]) * max(arr[i]))$.

**Solution 2:** We can convert this problem to $O(n * max(arr[i]))$ using a simple optimization, which after calculating a row, we convert it into a prefix sum, then for state `dp[i][sum]` we usually add values from states `dp[i+1][sum] + dp[i+1][sum-1] + ... + dp[i+1][sum - arr[i]]` which can be easily calculated using prefix sum in $O(1)$.

```c++
int solve(vector<int>& arr, int n, int S) {
	int dp[n+1][S+1];
	for(int i = n; i >= 0; i--) {
		for(int sum = 0; sum <= S; sum++) {
			if(i == n) {
				if(sum == 0) dp[i][sum] = 1;
				else dp[i][sum] = 0;
			} else {
				dp[i][sum] = dp[i+1][sum];
				if(sum - arr[i] - 1 >= 0) dp[i][sum] -= dp[i+1][sum-arr[i]-1];
			}
		}
		// after calculating the row, we convert it into prefix sum
		for(int sum = 1; sum <= S; sum++) {
			dp[i][sum] += dp[i][sum-1];
		}
	}

	return dp[0][S];
}
```

### Iterative State Space Optimization

Consider the above problem, the space complexity of the above problem is $O(N \times S)$. But we can actually improve it further to $O(S)$ using the fact that current state `dp[i][sum]` only depends on the dp state `dp[i+1][sum]` which at a time we only need to $2$ arrays of size $S$. Now there are multiple ways to implement this .

One is using two arrays `prev` and `curr`, where `prev` will be array representing row $i+1$ and `curr` represents row $i$. After we calculate `curr` we assign it to prev for computation of next row. 

Another and the most efficient way to do this is to use a `dp[2][S]` array and map $i$ and $i+1$ to rows based on their parity i.e even or odd. For example if $i = 2$ and $i+1 = 3$ then we assign $i$ to $dp[0][S]$ and we assign $i+1$ to $dp[1][S]$. For this whenever we access $dp[i][sum]$ we simply now do $dp[i\&1][sum]$ and similarly whenever we want to access $dp[i+1][sum]$ we now do $dp[(i+1)\&1][sum]$.

Solution for above problem with this optimization is shown below

```c++
int solve(vector<int>& arr, int n, int S) {
	int dp[2][S+1];
	for(int i = n; i >= 0; i--) {
		for(int sum = 0; sum <= S; sum++) {
			if(i == n) {
				if(sum == 0) dp[i&1][sum] = 1;
				else dp[i&1][sum] = 0;
			} else {
				dp[i&1][sum] = dp[(i+1)&1][sum];
				if(sum - arr[i] - 1 >= 0) dp[i&1][sum] -= dp[(i+1)&1][sum-arr[i]-1];
			}
		}
		// after calculating the row, we convert it into prefix sum
		for(int sum = 1; sum <= S; sum++) {
			dp[i&1][sum] += dp[i&1][sum-1];
		}
	}

	return dp[0][S];
}
```

### Palindromic Paths

**Problems:** Given a grid of size $n \times m$ with lowercase alphabets, you need to find the number of paths from $(0, 0)$ to $(n-1, m-1)$ such that they are palindromic. You are allowed to move from $(x, y)$ to $(x+1, y)$ and $(x, y)$ to $(x, y+1)$. Print the answer modulo $10^9 + 7$. Constraints are $1 \leq n, m \leq 500$.

**Solution:** Just like cherry pickup problem here also we have to use a $2$ path state i.e $dp[x][y][a][b]$ which will give the number of palindromic paths from $(x, y)$ to $(a, b)$. For transition clearly if $grid[a][b] \neq grid[x][y]$ then number of ways are $0$. Otherwise the number of ways are equal to $dp[x+1][y][a-1][b] + dp[x+1][y][a][b-] + dp[x][y+1][a-1][b] + dp[x][y+1][a][b-1]$. The final sub problem will be $dp[0][0][n-1][m-1]$.

But with the given constraints we need to can't make a $O(n^4)$ array, even the optimization that we learned with cherry pickup problem we get $O(n^3)$ space complexity which is still not possible even the time complexity is feasible, but not the space complexity.

Hence we create a dp state combining both cherry pickup and iterative space optimization techniques, we define dp state $dp[x1][x2][d]$ which returns the number of palindromic paths between cells $(x1, d - x1)$ and $(x2, (n-1) + (m-1) - d - x2)$ i.e the cell $(x1,y1)$ is at distance $d$ from $(0, 0)$ and cell $(x2, y2)$ is also at distance $d$ from cell $(n-1, m-1)$. The benefit from this is that each state only depends on states at distance $d+1$ which helps to implement iterative state optimization. 

```c++
int dp[505][505][2];
int n, m;
char grid[505][505];

int getPrecalculatedValue(int x1, int y1, int x2, int y2) {
	// checking if the state is valid
	if(x1 < 0 || y1 < 0 || x1 >= n || y1 >= m) return 0;
	if(x2 < 0 || y2 < 0 || x2 >= n || y2 >= m) return 0;
	return dp[x1][x2][(x1+y1)&1];
}

int calcValue(int x1, int y1, int x2, int y2) {
	// base cases
	if(x1 > x2 || y1 > y2) return 0;
	if(x1 < 0 || y1 < 0 || x1 >= n || y1 >= m) return 0;
	if(x2 < 0 || y2 < 0 || x2 >= n || y2 >= m) return 0;

	// if the cells are same or next to each other
	if((x1 == x2 && abs(y1-y2) == 1) || (y1 == y2 && abs(x1-x2) == 1)) return 1;
	// all possible states that we can go from here
	int ans = getPrecalculatedValue(x1+1,y1,x2-1,y2);
	ans += getPrecalculatedValue(x1+1,y1,x2,y2-1);
	ans += getPrecalculatedValue(x1,y1+1,x2-1,y2);
	ans += getPrecalculatedValue(x1,y1+1,x2,y2-1);

	ans %= mod;

	return ans;
}

int numberOfPalindromicPaths() {
	int d = (n + m) / 2; // optmization because for d > (n+m)/2 there are not valid states
	while(d--) {
		for(int x1 = 0, y1 = d; x1 < n && y1 >= 0; x++, y1--) {
			if(y1 >= m) continue;
			for(int x2 = n-1, y2 = (m-1-d); x2 >= 0 && y2 < m; x2--, y2++) {
				if(y2 < 0) continue;
				dp[x1][x2][d&1] = calcValue(x1, y1, x2, y2);
			}
		}
	}
	return dp[0][n-1][0];
}
```
### Data Structure Based Optimization

Sometimes we need to use some data structure to optimize the transition time in order to make the solution get AC. For example look at the example below.

**Problem:** Bob wants to travel from city $1$ to $N$. He can travel across each consecutive city i.e $i \rightarrow i+1$ using Bus by paying cost $A[i]$, and can also travel from city $i$ to a different city $j$ , at most $k$ cities away from $i$ i.e $|i-j| <= k$ through a Flight by paying $B[i] + B[j]$ charges. Here $N \leq 10^6$ and $1 \leq k \leq N$.

Find the minimum cost to reach from city $1$ to $N$.

**Solution:** The dp state is very trivial now, we will use $dp[i]$ which gives the minimum cost to reach city $i$ from city $j$. Transition is either we choose bus, in that case we have cost $dp[i-1] + A[i-1]$, otherwise we take flight from one of the city in range $j \in [i-k, i-1]$ in that case we get cost $dp[j] + B[j] + B[i]$ and we need to choose the option with minimum cost. Time complexity of this approach is $O(N\times K)$.

**Monotone Deque Optimization:** The task of finding the city from which we take flight is the most cost taking, but we can optimize this using monotone deque which we will use to store the minimum value of $dp[j] + B[j]$ for the previous $k$ values.

```c++
struct monotone_dq {
	deque<int> dq;
	void insert(int x) {
		while(!dq.empty() && dq.back() > x) dq.pop_back();
		dq.push_back(x);
	}
	void erase(int x) {
		if(!dq.empty() && dq.front() == x) dq.pop_front();
	}
	int getMin() {
		return dq.front();
	}
}

int solve(vector<int>& A, vector<int>& B, int n) {
	int dp[n];
	monotone_dq dq;
	dp[0] = 0;
	dq.insert(dp[0] + B[0]);
	for(int i = 1; i < n; i++) {
		dp[i] = dp[i-1] + A[i-1]; // by bus
		if(i - k - 1 >= 0) dq.erase(dp[i-k-1]+B[i-k-1]); // maintaining a window of prev k
		dp[i] = min(dp[i], dq.getMin() + B[i]);
		dq.insert(dp[i] + B[i]); // adding i to dq
	}

	return dp[n-1];
}
```

### Binary Search Optimization (Problem Job Scheduling)

**Problem:** There are $n$ Jobs you can do. For each Job, you know its starting and ending days and the amount of money you would get as reward. You can only do one Job during a day. What is the maximum amount of money you can earn? As input you will given an array $A$ in which each element is description of $ith$ job which is an array of size $3$ and contains the following values $A[i] = [a_i, b_i, p_i]$, where $a_i, b_i, p_i$ are the starting and ending day and amount of money that we get from this job. The constraints are $n \leq 2* 10^5$ and $1 \leq a_i, b_i, p_i \leq 10^9$.

**Solution:** First of all we will sort the jobs in ascending order of starting day. Now we will use dp state $dp[i]$ which gives the maximum sum of money that we can earn starting from $ith$ job. Now for transition we got $2$ choices, one is that we either do current job, in that case we need to find the first index of job $j$ after $ith$ job finishes i.e $a_j > b_i$ which can be done using binary search since the jobs are sorted by start day, in this choice we get sum as $p_i + dp[j]$. The other choice is that we don't do $ith$ job, in that our sum is simply $dp[i+1]$.

```c++
// binary search to find the upper bound
int upper_bound(vector<vector<int>>& jobs, int n, int x) {
	int l = 0, r = n-1, ans = n;
	while(l <= r) {
		int mid = (l + r) / 2;
		int startDay = jobs[mid][0];
		if(startDay > x) {
			ans = mid;
			r = mid-1;
		} else {
			l = mid + 1;
		}
	}
	return ans;
}

int maxSum(vector<vector<int>>& jobs, int n) {
	sort(jobs.begin(), jobs.end());
	vector<int> dp(n);
	dp[n-1] = jobs[n-1][2]; // base case
	for(int i = n-2; i >= 0; i--) {
		dp[i] = dp[i+1]; // case of not taking i
		int currEnd = jobs[i][1];
		int j = upper_bound(jobs, n, currEnd);
		dp[i] = max(dp[i], (j < n ? dp[j] : 0) + jobs[i][2]);
	}
	return dp[0];
}
```

### Observation Based Optimization

**Problem:** You are given an array `nums`​​​ and an integer `k`​​​​​. The XOR of a segment `[left, right]` where `left <= right` is the `XOR` of all the elements with indices between `left` and `right`, inclusive: `nums[left] XOR nums[left+1] XOR ... XOR nums[right]`. Return _the minimum number of elements to change in the array_ such that the `XOR` of all segments of size `k`​​​​​​ is equal to zero. Constraints are $1 \leq k \leq nums.length() \leq 2000$ and $0 \leq nums[i] \lt 2^{10}$.

**Solution:** The idea is that all elements with same value of $index \% k$ must have the same value. Hence we will make a frequency count of numbers in each group. Then we just need to find values for first $k$ positions and calculate the cost accordingly. For this we will use the state $dp[i][j]$ which is the minimum number of changes needed to make xor of first $i$ elements equal to $j$. To calculate $dp[i][j]$ there are two options either we choose one of the element from the group to make the value of $j$, the cost of changing each element in group to $x$ will be $dp[i-1][j \hspace{1mm} XOR \hspace{1mm} x] + groupSize_i - freq_x$. The other choice we have is to choose any value for $ith$ position having to change every element in the group, in this case we have liberty that xor of elements till $i-1$ can be anything so we choose minimum of all $dp[i-1][x]$, in this case we get cost as $prevMin + groupSize$ for every $j$. We choose minimum from these choices.

**Note:** To calculate the size of group $i$ we use formula $ceil((n - i) / k)$, the group are from $[0, k-1]$.

```c++
void solve(int n, int k, vector<int>& arr)
{
	int m = (1<<10);
	vector<map<int, int>> freq(k);
	for(int i = 0; i < k; i++)
	{
		for(int j = i; j < n; j+=k)
		{
			freq[i][arr[j]]++;
		}
	}
	int inf = n;
	vector<vector<int>> dp(k, vector<int>(m, inf));
	int prevMin = 0;
	for(int i = 0; i < k; i++)
	{
		int groupSize = ceil((n - i) * 1.0 / k);
		int currMin = inf; // initialize curr min as inf
		for(int j = 0; j < m; j++)
		{
			// choosing element from the group
			for(auto &v : freq[i])
			{
				int val = v.first, count = v.second;
				if(i > 0) dp[i][j] = dp[i-1][j^val] + groupSize - count;
				else if(j == val) dp[i][j] = groupSize - count;
				else dp[i][j] = groupSize; // need to change all elements
			}
			// choosing any element
			dp[i][j] = min(dp[i][j], prevMin + groupSize);
			currMin = min(currMin, dp[i][j]);
		}
		prevMin = currMin;
	}

	cout << dp[n-1][0] << '\n';
}
```

