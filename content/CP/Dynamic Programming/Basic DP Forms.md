# Dynamic Programming

> DP is nothing but caching, or a better word for this approach is **Memoization** which is the core idea of dp, that is to memoize results of a state after it is calculated once so that if we need it later we can use it instead of re-calculating it.

## Knapsack Style Problems ( Form 1 )

**Problem:** Given a list of $n$ items and for each items $i$ we have a $v_i$ as its value and $w_i$ as its weight. We also have a knapsack of capacity $W$, we want to find out the maximum sum of value of items that we can fit in knapsack. The value of $n \leq 3000$ and $W \leq 3000$.

**Solution:** At its core this problem simple asks us to find a subset with maximum value whose weight is $\leq W$. We can solve it using recursion where in level is the index of the list and at each level we have a choice of whether to choose or not choose the current item. Consider the function `int rec(int indx, int w){}` which returns the maximum subset value with weight $\leq w$ in the suffix or from $indx$ to $n-1$. Clearly `rec(0, W)` gives the result to this problem.

A non dp implementation of this approach is below.

```c++
int n;
vector<int> value, weight;
int rec(int indx, int w)
{
    // base case is when we reach end, then we have no choice and we return 0
    if(indx == n) return 0;
    // if we don't choose the current element
    int res = rec(indx+1, w);
    // if we choose the current element
    if(w >= weight[indx]) res = max(res, res(indx + 1, w - weight[indx]) + value[indx]);
    
    return res;
}
```

**Optimisation:** Now clearly the above solution is not optimal i.e its time complexity is still $O(2^n)$ because are generating all subsets in worst case. It is also evident that a lot of recursion states are called multiple times, hence if we cache the value of `rec(indx, w)` then we won't have to calculate it again. For caching we will create a `vector<vector<int>> dp(n, vector<int>(W+1, -1))`,  note that we have initialised the `dp` array with $-1$ since none of the states can achieve this value and hence we use this value to check if this state is calculated before or not. 

The time complexity of caching approach is equal to `# of states * Avg time for calculating a state` which is equal to $O(n * w) * O(1)$.

Caching the result implementation.

```c++
int n;
vector<int> val, weight;
vector<vector<int>> dp;

int rec(int indx, int w)
{
    // base case is when we reach end, then we have no choice and we return 0
    if(indx == n) return 0;
    // checking if this state is already calculated
    if(dp[indx][w] != -1) return dp[indx][w];
    // if we don't choose the current element
    int res = rec(indx+1, w);
    // if we choose the current element
    if(w >= weight[indx]) res = max(res, res(indx + 1, w - weight[indx]) + value[indx]);
    // caching the state value in dp array
    dp[indx][w] = res;
    return res;
}
```

> [!Note]
>
> The only reason we are able to solve this problem is because of the constraints i.e the value of $n$ and $w_i$ are $\leq 3000$ which makes the time complexity of this approach O(NW) feasible, this is generally the case with dp, the only reason a problem is solvable with dp is because of the constraints, if the constraints are high then it not possible to solve problems even with dp.

### Variations Of Knapsack

1. What if we need to print the solution as well, in that case we can have multiple approach, but a simple way is to calculate the result using the method discussed above and write another function to generate the optimal answer.

```c++
void print_solution(int indx, int w)
{
   // base case
	if(indx == n) return;    
   // result_if_we_dont_take_indx
   int res1 = rec(indx+1, w);	// O(1)
   // result_if_we_take_indx
   int res2  = 0;
   if(w >= weight[indx]) res2 = rec(indx+1, w-weight[indx]) + value[indx];
   // if taking gives better result then we print indx or else move to indx+1
   if(res2 > res1)
   {
	   cout << indx << ' ';
	   print_solution(indx+1, w - weight[indx]);
   }
   else
   {
	   print_solution(indx+1, w);
   }
}
```

2. What if we can choose an item any number of times as we want, in that case what is the max value. In this case small change in transition will do the job, if we can choose current element once, then in above solution we move to next level via `rec(indx+1, w-weight[indx])`, but in this case after we take an element we might again take it so we go to state `rec(indx, w-weight[indx])`.

3. What if we are allowed to take at max $k$ items. In this case we can simply add another parameter to the recursion `rec(int indx, int w, int k)` and in base case we can check `if(k == 0) return 0` and in transition whenever we choose an element we decrease $k$ by one.

4. What if sum of weights of chosen items is divisible by $M$. In this case when we reach end i.e $indx = n$ then we can check the total weight of selected items by $W - w$ and if this is divisible my $M$ then we return $0$ as usual, and if it is not divisible, then we return $-\infin$ because this is an invalid solution and returning $-\infin$  automatically discards this solution as result is at least $0$.

5. What if adjacent items cannot be taken. In this case when we select an item then instead of going to `rec(indx+1, w - weight[indx])` we will go to `rec(indx+2, w - weight[indx])`.

### Subset With Sum K

**Problem:** Given an array $arr$ of integers of size $n$ and a number $q$ queries, each query is an integer $q_i$ and we need to tell whether a subset exist in $arr$ with sum equal to $q_i$. The constraints are $n \leq 100$ and $arr_i \leq 10^4$ and $q, q_i \leq 10^4$.

**Solution:** Consider a recursion `bool rec(int indx, int s)` which returns whether a subset with sum $s$ exist in the suffix, for memoization we would need to create a dp array of size $n * max(s)$ which is $100 * 10^4$. Now pre calculate the values of all `dp[0][s]` i.e is it possible to get a subset of sum $s$ in the array and then each query can be answered in $O(1)$.

```c++
int rec(int indx, int sum)
{
    if(sum == 0) return 1;	// true
    if(indx == n) return 0;	// false
    // if this state already calculated
    if(dp[indx][sum] != -1) return dp[indx][sum];
    int ans = 0;
    // if not taking gets the answer then ans is 1
    if(rec(indx+1, sum)) ans = 1;
    else if(sum >= arr[indx] && rec(indx+1, sum - arr[indx])) ans = 1;
    return dp[indx][sum] = ans;
}
```

> [!Note]
>
> The default value of dp array as -1 is used to know if this state is already calculated or not, but sometimes it might happen that -1 is a possible answer for dp, in that case we need to choose some other value to know whether a dp is calculated or not. If we are unable to find a default value we can always create a visited array in which we can initialize it with false and whenever we finish the calculation of a state we will mark visited as true.

### Recursion To Iteration

Although recursion codes are mostly enough to solve a problem, but they are inherently slower because of function call overheads. Sometimes we need to convert our recursive code to iterative code to optimise for performance. The main idea of converting recursive to iterative is that we need to iterate in order or states such that states on which current state is dependent on are calculated before we reach current state. Another thing to keep in mind is the base cases, here we have to explicitly fill the dp array for base cases.

Consider the above problem, here state `rec(indx, sum) ` is dependent on `rec(indx+1, sum)` and `rec(indx+1, sum - arr[indx])`.  Also the base cases are `dp[n][0] = 1` and `dp[n][sum > 0] = 0`.

Iterative code for above problem.

```c++
// dp[i][j] = is is possible to get subset sum of j in suffix i to n-1
vector<int> solve(vector<int>& arr, vector<int>& queries)
{
    int n = arr.size();
    int maxVal = 0;
    for(int q:queries) maxVal = max(maxVal, q);
    vector<vector<int>> dp(n+1, vector<int>(maxVal+1));
    
    for(int indx = n; indx >= 0; indx--)
    {
        for(int j = 0; j <= maxVal; j++)
        {
	        // base case
	        if(indx == n)
	        {
		        if(j == 0) dp[indx][j] = 1;
		        else dp[indx][j] = 0;
		        continue;
	        }
            dp[indx][sum] = dp[indx+1][sum];
            if(sum >= arr[indx])
            {
                dp[indx][sum] = max(dp[indx][sum], dp[indx+1][sum-arr[indx]]);
            }
        }
    }
    vector<int> res;
    for(int q:queries)
    {
        res.push_back(dp[0][q]);
    }
}
```

## Ending At Index i Problems (Form 2)

In this form we cover the type of problems that can be solved by choosing something ending at index $i$. For example consider the classical problem of finding **Longest Increasing Subsequence (LIS)**.

**Problem:** Given an array $arr$ of size $n$ we need to find the largest increasing sub-sequence of this array.

**Solution:** we can choose the recursive function state as `int rec(int indx)` as the largest increasing subsequence in array ending at index $indx$. To calculate its value we just iterate over the possible last second values of this subsequence, since last element is $arr[indx]$ then the last second must be some index $j$ such that $arr[j] \lt arr[indx]$ and $0 <= j < indx$. Now for a give $j$ that matches the condition we can calculate the value of `rec(indx) = 1 + rec(j)` as $indx$ just extends the sub-sequence ending at $j$ by $1$. We need to find maximum such value among all possible $j$.

```c++
int rec(int indx)
{
    // checking if value already calculated
    if(dp[indx] != -1) return dp[indx];

	// calculating answer for current indx
	int ans = 1; // minimum is always 1 (indx itself)
	for(int i = 0; i < indx; i++)
	{
		if(arr[i] < arr[indx])
		{
			ans = max(ans, rec(i)+1);
		}
	}
	
	return dp[indx] = ans;
}
```

**Time Complexity:** The time complexity for above approach is $O(n^2)$ since we have $n$ state and for each state we have $O(n)$ average transition time. Although for this problem there is another approach which takes $O(nlogn)$ time.

From the above problem we see that in problems in which storing something ending at index $i$ we can use a simple dp array, but depending on the problem we might have to add in another parameter or two. For example look at the problem below.
### K Subarrays

**Problem:** Given an array $arr$ of size $n$ and an integer $k$ we need to divide the array in $k$ subarrays such that the sum of maximum elements of each subarray is minimal.

**Solution:** The idea for solution is again based on form 2, we will use a recursive function with state `rec(indx, x)` which will return the answer for $x$ subarrays ending at index $indx$. Now clearly the $x^{th}$ subarray will be ending at index $indx$ so we need to find an end for subarray $x-1$, let $j$ be such an index, then $j < indx$ and `rec(indx, x) = rec(j, x-1) + max(j+1,...indx)`. Obviously we need to find the one which gives the smallest value.

```c++
int rec(int indx, int x)
{
	if(indx == -1)
	{
		if(x == 0) return 0;  // case when x+1th subarray is 1st subarray
		else return inf;     // invalid state, so we return inf since we need to minimize the result
	}

	// checking if retult is already calculated
	if(dp[indx][x] != -1) return dp[indx][x];

	int ans = 1e9;
	int currMax = 0;
	// solving when xth subarray is starting at j and ending at indx
	for(int j = indx; j >=0; j--)
	{
		currMax = max(currMax, arr[j]);
		ans = min(ans, currMax + rec(j-1, x-1));
	}

	return dp[indx][x] = ans;
}
```

**Time Complexity:** for this approach is $O(n^3)$ as there are $O(n^2)$ states and for each we run a loop which is also $O(n)$.
### Maximum Sum Path And Number Of Paths

**Problem:** Given a $n \times m$ grid and we need to find the maximum sum path from $(0, 0)$ to $(n-1, m-1)$ and we also have to print the number of such paths.

**Solution:** this is also a form 2 problem where we use state `rec(int x, int y)` which gives the maximum sum path from $(0, 0)$ to $(x, y)$. Clearly the transition is `max(rec(x-1, y), rec(x, y-1)) + grid[x][y]`. Now counting the number of solutions is also simple, for every state we will store number of ways in which we get optimal answer for this state, in our case we would have to store number of ways to reach cell $(x, y)$ in the grid such that the sum of path is maximum. For this we have two cases, case one is one of `rec(i-1, j)` or `rec(i, j-1)` is greater than the other, in that case our number of ways is same as number of ways for that cell, the other case is when `rec(i-1, j) == rec(i, j-1)`, in this case we need to add number of ways for both the cells to our number of ways.

```c++
int rec(int i, int j)
{
	if(i < 0 || j < 0) return -inf; // invalid case returning -inf
	if(i == 0 && j == 0)
	{
		dp[i][j] = grid[i][j];
		ways[i][j] = 1;
		return dp[i][j];
	}

	// checking cache
	if(dp[i][j] != -1) return dp[i][j];

	int ans1 = rec(i-1, j);
	int ans2 = rec(i, j-1);
	
	if(ans1 > ans2)
	{
		dp[i][j] = ans1;
		ways[i][j] = ways[i-1][j];
	}
	else
	{
		dp[i][j] = ans2;
		ways[i][j] = ways[i][j-1];
		if(ans1 == ans2) ways[i][j] += ways[i-1][j]
	}

	return dp[i][j];
}
```
### Maximum Area of Square of 1's

**Problem:** Given a $n \times m$ grid of $0$'s and $1$'s and we need to find the area of largest square containing only $1$'s.

**Solution:** Here also we can use a recursion state `rec(int i, int j)` which returns the area of largest square whose bottom right cell is $(i, j)$. For this the transition is `1 + min(rec(i-1,j), rec(i-1,j-1), rec(i, j-1)`, because if the answer of current cell is $x$ then the value of each of `rec(i-1,j)`, `rec(i-1,j-1)` and `rec(i,j-1)` must be at least $x-1$.

```c++
int rec(int i, int j)
{
	if(int i < 0 || j < 0) return 0;
	// checking cache
	if(dp[i][j] != -1) return dp[i][j];
	int ans = 1 + min({rec(i-1, j), rec(i, j-1), rec(i-1, j-1)});

	return dp[i][j] = ans;
}
```

**Problem:** Given a $n \times m$ grid of integers between $[-1000, 1000]$, we start from cell $(0, 0)$ with some positive health, on reaching every cell our health may increase or decrease based on the integer present in the cell. If at any point our health becomes <= 0 we are dead, find the minimum health that we must start with in order to be able to reach cell $(n-1, m-1)$.

**Solution:** here if take a state like `rec(i, j)` equal to the min health we need to start with so that we can reach cell $(i, j)$, in this case for transition we would need to store the value of final health after moving from $(0, 0)$ to cell $(i, j)$. But if we use a state `rec(i, j)` to be min health we need to reach from cell $(i, j)$ to $(n-1, m-1)$. For transition we see the values of `dp[i+1][j]` and `dp[i][j+1]`, let $x$ be the value for `dp[i][j]` then clearly `x + grid[i][j] >= min(dp[i+1][j], dp[i][j+1])` which gives us `x >= min(dp[i+1][j], dp[i][j+1] - grid[i][j]` and since `x >= 1` we must take maximum of $x$ and $1$ for `dp[i][j]`. 

```c++
int rec(int i, int j)
{
	if(i >= n || j >= m) return inf;
	if(dp[i][j] != -1) return dp[i][j];

	if(i == n-1 && j == m-1)
	{
		dp[i][j] = max(1 - grid[i][j], 1);
		return dp[i][j];
	}

	dp[i][j] = max(min(rec(i+1, j), rec(i, j+1)) - grid[i][j], 1);

	return dp[i][j];
}
```
### Number Of Unique Subsequences

**Problem:** Given a string of lowercase English alphabets, we need to find the number of distinct subsequences present in the string.

**Solution:**  for this we can use a state `rec(int indx)` which returns the number of distinct subsequences ending at index $indx$. For this we will start to iterate from $indx-1$ and move towards $0$, when we see a character at index say $j$ which is different from current character, then it means adding current character to all subsequences ending $j$ will give new subsequences, hence we add `rec(j)` to our answer. When we see a character that is same as current character then adding current character to all subsequences ending with $j$ gives new distinct subsequences, but we cannot go beyond this point because then we will only make duplicate subsequences that already made by $j$.

```c++
int rec(int indx)
{
	// if state already calculated
	if(dp[indx] != -1) return dp[indx];

	int ans = 0;
	int j;
	for(j = indx-1; j >= 0; j--)
	{
		ans += rec(j);
		if(s[j] == s[indx]) break;
	}
	// s[indx] was first of its type then 's[indx]' is a subsequence that we need to add to ans
	if(j == -1) ans++;

	return dp[indx] = ans;
}
```

**Time Complexity:** For above code the time complexity is clearly $O(n^2)$. But if we use iterative dp and prefix we can solve in $O(n)$ also.

**Optimised Linear Algorithm:**  the observation is that in the code we just iterate and add previous dp values till last occurrence of current character.

```c++
int solve(vector<int>& arr)
{
	int n = arr.size();
	vector<int> dp(n), pref(n), last(26, -1);
	dp[0] = 1;
	pref[0] = 1;
	int ans = 0;
	for(int i = 1; i < n; i++)
	{
		dp[i] = pref[i-1];
		// last element of this type index
		int indx = last[s[i] - 'a'];
		if(indx == -1) dp[i] += 1;
		else if(indx > 0) dp[i] -= pref[indx-1];

		pref[i] = pref[i-1] + dp[i];
		last[s[i]-'a'] = i;

		ans += dp[i];
	}
	
	return ans;
}
```

## Multi-Sequence DP (FORM 3)

> Form 3 dp consists of solving problem involving 2 or more arrays, a classical example for this the famous **Longest Common Subsequence (LCS)**  problem. In these problems we use a dp state dp[i][j] which gives us the answer for suffix starting at i in sequence 1 and suffix starting at j in sequence 2. The final answer will then be stored in `dp[0][0]`.

### Longest Common Subsequence (LCS)

**Problem:** Given two strings $S$ and $T$ and we need to find the length of the longest common subsequence that is present in both $S$ and $T$.

**Solution:** the solution to this problem is simple, we use a recursion state `rec(int i, int j)` which is equal to length of longest common subsequence in $S[0...i]$ and $T[0...j]$ substrings. The transition will be if `S[i] == T[j]` then we have `rec(i, j) = rec(i-1, j-1) + 1`, but if `S[i] != T[j]` then we have two choices either to skip character $S[i]$ or to skip $T[j]$, clearly we choose the one with maximum answer, so we have `rec(i, j) = max(rec(i-1, j), rec(i, j-1))`. Note the case of skipping both $i$ and $j$ characters will get included in these only as `rec(i-1, j)` might go into a state `rec(i-1, j-1)` and same for `rec(i, j-1)`. Time complexity is $O(n \times m)$.

```c++
int lcs(int i, int j)
{
	if(i == n || j == m) return 0;

	if(dp[i][j] != -1) return dp[i][j];
	
	int ans = inf;
	ans = min(ans, rec(i+1, j));
	ans = min(ans, rec(i, j+1));
	if(s[i] == t[j]) ans = min(ans, rec(i+1, j+1) + 1);

	return dp[i][j] = ans;
}
```

>[!Note]
>If we have to find lcs of 3 strings then we need a recursion state `rec(i, j, k)` and if all characters i, j, and k are equal then we get result as `rec(i-1, j-1, k-1) + 1`. If they are not equal then we get result as `max(rec(i-1, j, k), rec(i, j-1, k), rec(i, j, k-1));`

### Generate Smallest Diff Utility

A **Diff Utility** is a string that gives difference between two strings, it contains characters separated by space, there are three types of characters, type 1 is simple english alphabets i.e 'A' .. 'Z', the type 2 of characters is characters with '-' before them which are character that are present only string 1, the third type of characters are those that have '+' before them, these are characters that are present in second string only. 

If we choose only characters of type 1 and type 2 we get string 1 and if choose only characters of type 1 and type 3 we get string 3.

**Example:** consider the strings `AATU` and `ATUA`, one of the possible diff strings of these strings is `-A A T U +A`. Now, there are many diff strings possible for a given pair of strings.

**Possible:** Given two strings $S$ and $T$ we need to find and print the smallest possible diff strings for these strings.

**Solution:** We will use a recursion state `rec(int i, int j)` which gives the smallest diff strings for suffix $S[i \dots n-1]$ and $T[j \dots m-1]$, clearly there are 3 transitions possible, one is if we ignore $ith$ character i.e `rec(i+1,j)+1` in this case the character $S[i]$ is of type 2. The other transition is when we ignore $jth$ character i.e `rec(i, j+1)+1` here character $T[j]$ is of type 2. The final transition is when $S[i] == T[j]$ we have $rec(i+1,j+1)+1$, here the character $S[i]$ is of type 1. Time complexity is $O(n \times m)$.

```c++
int rec(int i, int j)
{
	if(i == n && j == m) return 0;
	if(dp[i][j] != -1) return dp[i][j];

	int ans = inf, curr;

	if(i < n)
	{
		curr = rec(i+1, j) + 1;
		if(ans > curr)
		{
			ans = curr;
			type[i][j] = 1;
		}
	}
	
	if(j < m)
	{
		curr = rec(i, j+1) + 1;
		if(ans > curr)
		{
			ans = curr;
			type[i][j] = 2;
		}
	}
	
	if(i < n && j < m && s[i] == t[j])
	{
		curr = rec(i+1, j+1) + 1;
		if(ans > curr)
		{
			ans = curr;
			type[i][j] = 3;
		}
	}
	
	return dp[i][j] = ans;
}

void generate(int i, int j)
{
	if(i == n && j == m) return;
	if(type[i][j] == 1)
	{
		cout << '-' << s[i] << ' ';
		generate(i+1, j);
	}
	else if(type[i][j] == 2)
	{
		cout << '+' << t[j] << ' ';
		generate(i, j+1);
	}
	else
	{
		cout << s[i] << ' ';
		generate(i+1, j+1);
	}
}
```

### Edit Distance

**Problem:** Given two strings $S$ and $T$ and we need to find the minimum number of operations needed to convert $S$ string to $T$. In one operation we can add, remove or replace a character in string $S$.

**Solution:** here again we have to use a multi-sequence form i.e `rec(int i, int j)` is the minimum number of operations to convert $S[i \dots n-1]$ to $T[j \dots m-1]$. The transitions are either delete $ith$ or $jth$ character and get result as `rec(i+1, j) + 1` or `rec(i, j+1) + 1`. Another thing we can do is insert a character at position $ith$ to match character at position $jth$ this will leave us with `rec(i, j+1) + 1`, same for inserting a character at $jth$ same as $ith$ character. Another thing we can do is replace $ith$ character to match $jth$ character, and then we get `rec(i+1, j+1) + 1`. If $S[i] == T[j]$ then in that case we get `rec(i+1, j+1)`. Time complexity of this approach is $O(n \times m)$.

```c++
int rec(int i, int j)
{
	if(i == n && j == m) return 0;

	if(dp[i][j] != -1) return dp[i][j];

	int ans = inf;

	if(i < n) ans = min(ans, rec(i+1, j) + 1);

	if(j < m) ans = min(ans, rec(i, j+1) + 1);

	if(i < n && j < m)
	{
		ans = min(ans, rec(i+1, j+1) + 1);
		if(s[i] == t[j]) ans = min(ans, rec(i+1, j+1));
	}

	return dp[i][j] = ans;
}
```

## Interval DP (LR DP or Form 4)

### Rod Cutting Problem

**Problem:** Given a rod of length $n$, there are some $k$ points on the rod from where we want to cut the rod. If we cut the rod at some point, then the length of rod before cutting is the cost for making this cut. We want to find the minimum possible cost to cut the rod at all k points. ($n \leq 200$).

**Solution:** In these types of problem we will use a recursion state as `rec(int i, int j)` which is the minimum cost for part of rod starting at $ith$ cut point and ending at $jth$ cut point. The transition is that we loop over all cut points in between $ith$ and $jth$ point and lets say we make a cut at some $kth$ point ($i < k < j$), then cost will be `x[j] - x[i] + rec(i, k) + rec(k, j)`, we will find the minimum among all possible $k$'s.

```c++
int rec(int i, int j)
{
	// if there is not point in between i and j, then no more cuts needed
	if(i+1 == j) return 0;

	// cache check
	if(dp[i][j] != -1) return dp[i][j];

	dp[i][j] = inf;
	for(int k = i + 1; k < j; k++)
	{
		dp[i][j] = min(dp[i][j], x[j] - x[i] + rec(i, k) + rec(k, j));
	}

	return dp[i][j];
}
```

### Palindrome Queries

**Problem:** Given a string $S$ and $Q$ queries, each query is of type $l_i, r_i$ and we need to tell whether the substring $S[l_i, \dots, r_i]$ is a palindrome of not.

**Solution:** First we pre-calculate for every substring whether it is a palindrome or not and then each query can be answered in $O(1)$ time. A state `rec(int i, int j)` returning whether substring $S[i, \dots, j]$ is a palindrome or not. The transition is, if $S[i] \neq S[j]$ then `rec(i, j) = 0` other wise we check if `rec(i+1, j-1)` is also a substring or not, if yes then `rec(i, j)` is also a palindrome otherwise it is not palindrome.

```c++
int rec(int i, int j)
{
	if(i >= j) return 1;

	if(dp[i][j] != -1) return dp[i][j];

	if(s[i] == s[j] && rec(i+1, j-1)) dp[i][j] = 1;
	else dp[i][j] = 0;

	return dp[i][j];
}
```

### Palindrome Decomposition

**Problem:** Given a string $S$ and we need to divide the string into substrings such that each substring is a palindrome and number of substrings is smallest possible.

**Solution:** Here we can use a dp state `dp[i][j]` representing the answer for substring $S[i, \dots, j]$, for transition we go over every $k \in [i, j)$ such that $S[i, \dots, k]$ is a palindrome and $S[k+1, \dots, j]$ is also a palindrome. The time complexity of this approach is $O(n^3)$, but we are not forced to using LR DP, if we look closely this problem is similar to problems we did in form 2. Here a dp state `dp[i]` which is minimum number of substrings ending at $i$ can be used, for transition we simply go over all $j \in [0, i)$ such that $S[j+1, \dots, i]$ is a palindrome and number of substrings is `dp[j] + 1`. Clearly we need to find the smallest of these. For checking whether a substring is a palindrome or not we can simply use the above approach. The time complexity of this approach is $O(n^2)$.

```c++
int rec(int i)
{
	if(i < 0) return 0;

	if(dp[i] != -1) return dp[i];

	int ans = inf;
	for(int j = 0; j <= i; j++)
	{
		if(isPalindrome(j, i))
		{
			ans = min(ans, rec(j-1) + 1);
		}
	}

	return dp[i] = ans;
}
```

### Merging Elements

**Problem:** Given an array of elements $arr$, in one move we can merge any two adjacent elements, the cost of this merge is $x \times y$ and the final value after merge is $x + y$. Find the minimum cost to merge the entire array to one element.

**Solution:** Here we can use a dp state `rec(i, j)` which returns the minimum cost to merge subarray $arr[i, \dots, j]$. For transition we consider the final operation that will happen, i.e we would be merging 2 elements into 1. The number of possible ways we can have these two elements is simply equal to divide the array in two parts, one part will eventually merge into single element and other part will eventually merge into second element and then we merge these two for current state. Hence for every $k \in [i, j)$ we get cost `rec(i, k) + rec(k+1, j) + sum(i,...,k) * sum(k+1,...,j)`, and we need to find minimum such value. Time complexity of this approach is $O(n^3)$.

```c++
int rec(int i, int j)
{
	if(i == j) return 0;

	if(dp[i][j] != -1) return dp[i][j];

	int ans = inf;

	for(int k = i; k < j; k++)
	{
		ans = min(ans, rec(i, k) + rec(k+1,j) + sum(i, k) * sum(k+1, j));
	}

	return dp[i][j] = ans;
}
```

### Writing LR DP In Iterative Manner

**Problem:** Taro and Jiro will play the following game against each other. Initially, they are given a sequence $a = (a_1, a_2, \dots, a_n)$. Until becomes empty, the two players perform the following operation alternately, starting from Taro, Remove the element at the beginning or the end of $a$. The player earns $x$ points, where $x$ is the removed element. Let $X$ and $Y$ be Taro's and Jiro's total score at the end of the game, respectively. Taro tries to maximise $X-Y$, while Jiro tries to minimise $X-Y$. Assuming that the two players play optimally, find the resulting value of $X-Y$.

**Statement:** Here we use a dp state `rec(i, j)` which gives the maximum score for the first person to move on the subarray. Now the transition is if the player decides to pick the first element, then its total will be `sum(i, j) - rec(i+1, j)` and if the player chooses last element, then its score will be `sum(i, j) - rec(i, j-1)`. We obviously need to choose the maximum of these two.

**Iterative Implementation:** iterative implementation of these types of problems is not so trivial, the idea is that in transition of current subarray we always need to values from smaller subarrays, so if we loop in terms of lengths of subarrays from $1$ to $n$, then whenever we are at a subarray, the smaller subarrays will always be calculated.

```c++
int solve()
{
	int n; cin >> n;
	vector<int> arr(n);
	vector<int> pref(n);
	for(int i = 0; i < n; i++)
	{
		cin >> arr[i];
		pref[i] = arr[i] + (i > 0 : pref[i-1] : 0);
	}
	vector<vector<int>> dp(n, vector<int>(n));

	for(int len = 1; len <= n; len++)
	{
		// iterating over each subarray of length len
		for(int i = 0; i <= n - len; i++)
		{
			int j = i + len - 1;
			// base case
			if(i == j) dp[i][j] = arr[i];
			else
			{
				int sum = pref[j] - (i > 0 ? pref[i-1] : 0);
				int ans = 0;
				// case 1: choosing the first element
				ans = max(ans, sum - dp[i+1][j]);
				// case 2: choosing the last element
				ans = max(ans, sum - dp[i][j-1]);

				dp[i][j] = ans;
			}
		}
	}

	int taroScore = dp[0][n-1];
	int jiroScore = pref[n-1] - taroScore;

	cout << taroScore - jiroScore << '\n';
}
```

### Destroying Palindromes

**Problem:** Given an array of integers, in one move we can destroy any palindromic subarray of the given array. Find the minimum number of moves required to destroy the entire array.

**Solution:** Here we will use a dp state `rec(i, j)` giving the minimum moves to destroy the subarray $arr[i, \dots, j]$. Now for transition we loop over all $k \in [i, j)$ and divide the subarray further into two subarrays and find cost of destroying each of these which is `rec(i, k) + rec(k+1, j)`. We also have a special case in transition which is when `arr[i] == arr[j]` in this case we can have `rec(i, j) = rec(i+1, j-1)` this is because the last destroy operation that happens in `rec(i+1, j-1)` will be a palindrome and we can easily extend that palindrome to include `arr[i]` and `arr[j]` and delete all of `rec(i, j)` at cost same as `rec(i+1, j-1)`. We need to choose the minimum one among all the options.

```c++
int rec(int i, int j)
{
	if(i >= j) return 1;
	
	if(dp[i][j] != -1) return dp[i][j];
	
	dp[i][j] = inf;
	
	if(arr[i] == arr[j]) dp[i][j] = min(dp[i][j], rec(i+1, j-1));

	for(int k = i; k < j; k++) dp[i][j] = min(dp[i][j], rec(i, k) + rec(k+1, j));

	return dp[i][j];
}
```

### Matrix Chain Multiplication

**Problem:** Given an array $arr$ or pairs. The array represents a matrix chain that we need to multiply and each array element represents the dimensions of the array. Multiplying two matrices with dimensions $(a, b)$ and $(b, c)$ we get a cost of $a \times b \times c$,  we need to find the minimum cost to multiply all the matrices.

**Solution:** this dp state `rec(i, j)` giving the minimum cost to multiply matrices in range $arr[i, \dots, j]$ can be used. The transition is going over all $k \in [i, j)$ and we find the answer for side $arr[i, \dots, k]$ and $arr[k+1, \dots, j]$ and then multiply the results of these two sides. The cost for a given k will be `rec(i, k) + rec(k+1, j) + x[i] * y[k] * y[j]` and we need to find the minimum among all $k$'s.

**Generating The Solution:** Lets we also needed to generate a solution that gives the minimum cost. For example if we have three matrices, then we need to generate parenthesis that give order of multiplications for example `(( 1  2 ) 3 )`.

**Solution:** for each state we need to store the value of $k$ which gives the optimal answer. An then for each transition we reach we need to put an opening bracket before $i$ and $k+1$ and closing brackets after $k$ and $j$. For each index we will store the number of opening and closing brackets for before and after this matrix.

```c++
int rec(int i, int j)
{
	if(i == j) return 0;

	if(dp[i][j] != -1) return dp[i][j];

	int ans = inf;

	for(int k = i; k < j; k++)
	{
		int curr = rec(i, k) + rec(k+1, j) + x[i] * y[k] * j[k];
		if(curr < ans)
		{
			ans = curr;
			transition[i][j] = k;
		}
	}

	return dp[i][j] = ans;
}

void generate(int i, int j)
{
	if(i == j) return;
	int k = transition[i][j];
	opening[i]++;
	closing[j]++;
	opening[k+1]++;
	closing[k]++;
	generate(i, k);
	generate(k+1, j);
}
```

## Game DP (Form 5)

> When dealing with (impartial) games where 2 players play turn by turn and set of rules for each player is the same, then based on game state it is generally decided which player is going to win if both play optimally. For smaller inputs we can use dp storing the state of the game, for transition we make all possible moves that we can make in this state, if at least 1 of the states that we reach from here after making a move is losing then we say that current state is winning, otherwise if all states we can reach are winning then we say that this state is loosing.

### Subtraction Game

**Problem:** Alice and Bob are playing a game where they start with a pile of $x$ stones and in one move the player can choose to remove $2^k$ number of stones where $k \in [0, \lfloor logx \rfloor]$. The player that cannot make a move loses.

**Solution:** We use a dp state `rec(x)` which returns whether this state is winning or loosing. For transition we go over all possible powers of 2 that we can take and then check if at least one of the resulting states is loosing.

```c++
int rec(int x)
{
	if(x == 0) return 0;  // losing state
	if(dp[x] != -1) return dp[x];
	int ans = 0; // assuming this is a losing state
	for(int k = 0; (1<<k) <= x; k++)
	{
		if(rec(x - (1<<k)) == 0)
		{
			ans = 1;
			break;
		}
	}

	return dp[x] = ans;
}
```

>[!Note]
>If we run above code and print answers for first few numbers we find a patter that all integers that are multiples of 3 the game state is loosing, otherwise game state is winning. This is often the case where we use game dp to find patterns and then use the pattern to solve for higher complexity problems.

