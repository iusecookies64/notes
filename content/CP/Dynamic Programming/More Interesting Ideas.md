### LIS in $O(nlogn)$ Time Complexity

We use the recursion state `rec(i)` which gives the maximum length of increasing sequence ending at index $i$. This approach has $O(n^2)$ time complexity, but we can do better and there is an approach that takes $O(nlogn)$ time. 

**Idea:** The idea is that we will maintain a data structure that stores the `{last, len}` i.e store the smallest possible ending of increasing sequence of length, at any point the largest length is actually the length of **LIS**. Now when inserting a new element, if this element is greater than $last$ of maximum length, in that case we just push a new `{last, len}` in our structure with current element and new maximum possible length. If this is not the case then we need to find first element that is $\geq arr[i]$ in our structure (lower_bound), let it be at position $x$, now clearly $last_x >= arr[i]$ and $last_{x-1} \lt arr[i]$, this means $arr[i]$ can also be an end of an increasing sequence of length $x$ and updating the value `{last, x}` with $arr[i]$ gives better chances of getting increasing sequence of lengths $\gt x$. Hence we update `{last, len}` with `{arr[i], x}`.

For storing such a structure we will simply use an array where index will be $lengths$ and value at index will be the $last$.

**Generating The Solution:** If we also want to generate **LIS** then when we insert an element we store the previous element at the time of inserting because that element will is end of increasing sequence of length $1$ smaller than the length of increasing sequence of which $arr[i]$ is end and the previous element is also smaller than this element, hence it can very well be the last second element of the increasing sequence of which $arr[i]$ is the end. Then when we have processed the array then we will simply take the $last$ of longest possible increasing sequence and simple keep going back to generate the **LIS** in reverse order.

```c++
int solve()
{
	int n; cin >> n;
	vector<int> arr(n);
	for(int i = 0; i < n; i++) cin >> arr[i];
	vector<int> lis, index, back(n);
	for(int i = 0; i < n; i++) {
		// finding the index of first element >= arr[i]
		int pos = lower_bound(lis.begin(), lis.end()) - lis.begin();
		if(pos == lis.size()) {
			lis.push_back(arr[i]);
			index.push_back(i);
		} else {
			lis[pos] = arr[i];
			index[pos] = i;
		}
		if(pos > 0) back[i] = index[pos-1];
		else back[i] = -1;
	}

	cout << "lis is " << lis.length() << '\n';
	vector<int> ans;
	int endIndex = index.back();
	while(endIndex >= 0)
	{
		ans.push_back(arr[endIndex]));
		endIndex = back[endIndex];
	}
	reverse(ans.begin(), ans.end());
	for(int v : ans) cout << v << ' ';
	cout << '\n';
}
```

### Number of Valid Strings

**Problem:** Given an integer $n$ and we need to find the number of binary strings of length $n$ that doesn't contain $0100$ as a subsequence.

**Solution:** we will use a dp state `rec(int i, int matchedLen)` which returns the number of possible suffix such that $matchedLen$ gives the length of subsequence that we have already matched. The answer to the above problem will then be `rec(0, 0)`. The transition is that if we place a character which matches the next character in the banned pattern then in that case we go to `rec(i+1, matchedLen+1)` and otherwise we go to `rec(i+1, matchedLen)`, and since these are the only two choices we get final answer as by adding both possibilities. The time complexity of this approach is $O(n * m)$.

```c++
string bannedPattern = "0100";
int rec(int i, int matched)
{
	if(matched == bannedPattern.length()) return 0;
	if(i == n) return 0;

	if(dp[i][matched] != -1) return dp[i][matched];

	int ans = rec(i+1, matched) + rec(i+1, matched+1);

	return dp[i][matched] = ans;
}
```

**Mathematical Approach:** If we look above solution closely, we can see that this is independent of the string i.e for any string of length $4$ the answer will be the same. When processing the string, at every level we have 2 choices, either to choose a character that doesn't increase the value of $matched$ or to choose the character that does increase the value of $matched$. Now the value of matched can only be increased by $3$, because after that we get invalid string. So the problem boils down to number of ways of choosing $(0, 1, 2, 3)$ indices where we will increase the value of matched and for all other indices the value that they can take is fixed, hence answer =  $\sum ^nC_k, k \in [0, m-1]$, where $m$ is the length of pattern. Time complexity of this approach is $O(m)$ if we have pre-calculated the factorials, otherwise it is $O(n+m)$.

### Number Of Valid Strings II

**Problem:** Given a number $n$ and we need to find number of binary strings of length $n$ that doesn't contain string $0100$ as a substring.

**Solution 1:** We can use a dp state `rec(i, last3)` that returns the number of valid strings starting index $i$ such that $last3$ gives the last three characters that we have placed. Transitions are simple, if last $3$ matches the first $3$ character of banned string, then only have one choice of character from now on and we return $1$, otherwise have $2$ choices.

For storing $last3$ we can either use strings, but a more efficient method will be to store them as binary representation of integers. To add a new character at the end we can simply do `(last3<<1)` to add $0$ and `(last3<<1)|1` to add $1$. Now to make sure that only $3$ set bits are present, after adding new choice we can do `&7` since binary of $7$ is $111$, in general for a string of length $m$ this number is `((1<<(m-1))-1)`.

```c++
string bannedString = "0100";
string removeExtraBits = 7;
int rec(int i, int last3)
{
	if(i == n) return 1;
	if(dp[i][last3] != -1) return dp[i][last3];

	// matched length
	int len = 0;
	while(len < 3)
	{
		if(s[len] == '1' && (last3 & (1<<(2-len)))) len++;
		else if(s[len] == '0' && !(last3 & (1<<(2-len)))) len++;
		else break;
	}
	// if len == 3 and i > 2 (otherwise len == 3 is not possible)
	if(len == 3 && i > 2) dp[i][last3] = 1;
	else
	{
		dp[i][last3] = rec(i+1, (last3 << 1) & removeExtraBits) + rec(i+1, ((last3<<1)|1)&removeExtraBits);
	}

	return dp[i][last3];
}
```

Time complexity of above approach is $O(n * m * 2^m)$.

**Solution 2:** This an optimised solution to the above problem. Here we use dp state `rec(int i, int matched)` which returns number of valid starting index $i$ if $matched$ is the maximum length of prefix of banned string that matches the suffix of placed items. Now lets say if current $matched$ is $2$ which means $01$ have been matched, now if we place $0$ at current position then we will move to state `rec(i+1, matched+1)`, but if we place $1$ then we move to `rec(i+1, 0)`. Deciding on maximum length prefix matched based on what character we place is classical string problem that can be solved efficiently using **KMP Algorithm**. But for now lets hard code this, what we want is a directed graph structure where nodes will be the length of prefix matched and for each character that we can place i.e $0$ or $1$, we will have edges to nodes where we reach. For string $0100$ this graph looks something like the figure shown below.

![[Pasted image 20240814153203.png | center]]

Although we have hard coded the graph here, but generating a graph like above using code is possible using **KMP**.

```c++
int rec(int i, int matched)
{
	if(i == n) return 1;
	if(dp[i][matched] != -1) return dp[i][matched];

	int ans = 0;
	// can only place 1, and we reach node matched = 2
	if(matched == 3) {
		ans = rec(i+1, 2);
	} else if(matched == 2) {
		ans = rec(i+1, 3) + rec(i+1, 0);
	} else if(matched == 1) {
		ans = rec(i+1, 1) + rec(i+1, 2);
	} else {
		ans = rec(i+1, 0) + rec(i+1, 1);
	}

	return dp[i][matched] = ans;
}
```

### Polygon Triangulation Problem

Triangulating a polygon simply means dividing it into multiple regions using its diagonals such that each region is a triangle. For example look at the polygon below, and two of the many ways to triangulate it.

![[Pasted image 20240815104241.png | center]]

**Problem:** Given coordinates of a N-Gon ($n$ sided polygon) in clockwise order. We need to find the minimum cost of triangulating the polygon if cost of making a diagonal is $sin(length)$.

**Solution:** It seems hard to even think of formulating such a problem using dp. We will use a dp state `rec(int l, int r)` which gives the min cost of triangulating polygon made by vertices in range $(l, r)$. Now for transition we will consider line segment $l$ to $r$ (if $l$ and $r$ are not adjacent we consider cost of diagonal joining $l$ and $r$ to be already included previously) as base of a triangle and loop over all possible third vertices $x$ i.e vertices in range $x \in [l+1, r-1]$, then if we make a triangle $l, x, r$, then cost of triangulating whole polygon is `rec(l, x) + rec(x, r) + sin(len(l, x)) + sin(len(x, r))`. The diagram for this transition is shown below.

![[Pasted image 20240815111907.png | center]]

```c++
vector<pair<int, int>> p;
vector<vector<double>> dp, visited;
double cost(int l, int r)
{
	// if points are next to each other, then it is a side and not a diagonal and hence cost is 0
	if(l+1 == r) return 0;
	int dx = p[l].first - p[r].first;
	int dy = p[l].second - p[r].second;
	int len = sqrt(dx*dx + dy*dy);
	return sin(len);
}

double rec(int l, int r)
{
	// base case is when polygon have <= 3 sides
	if(r - l + 1 <= 3) return 0;

	if(visited[l][r]) return dp[l][r];

	double ans = inf;

	for(int x = l+1; x < r; x++)
	{
		ans = min(ans, rec(l, x) + rec(x, r) + cost(l, x) + cost(x, r));
	}

	visited[l][r] = 1;
	return dp[l][r] = ans;
}
```

### Maximum Score

**Problem:** Given a $n \times m$ grid of integers and we are also given an integer $k$. A player can start from any cell in bottom row and it has to move to top row. The player can only move diagonally i.e can move to cell $(i-1, j-1)$ or $(i-1, j+1)$ in one move. The score of a player is total sum of values on each cell that the player visited if the sum is divisible by $k$ otherwise the score is $-1$. Find the maximum possible score a player can achieve.

**Solution:** Here a dp state `rec(int i, int j, int modValue)` which returns maximum score possible to reach on cell $(i, j)$ such that `score % k = modValue` if it exist, otherwise returns $-1$.  Clearly for transition if this is the last row, then we just need to compare if `grid[i][j] % k == modValue` and return `grid[i][j]` or `-1`. If this is not the last row, then we need to find the maximum sum from the bottom rows such their `(sum + grid[i][j])%k == modValue)`, this means that `requiredMod = sum % k == (modValue - (grid[i][j]%k) + k) % k`, since we can reach this state from cells $(i+1, j-1)$ or $(i+1, j+1)$ our transition is maximum of `rec(i+1, j-1, requiredMod)` or `rec(i+1, j+1, requiredMod)`. Our final answer will be maximum of all answers of cells in top row. The time complexity of this approach is $O(n * m * k)$.

```c++
int dp[101][101][12];
int grid[101][101];
int n, m, k;

int rec(int i, int j, int modValue) {
	if(i < 0 || i >= n || j < 0 || j >= m) return -inf;
	
	if(i == n-1) {
		if((grid[i][j]%k) == modValue) return grid[i][j];
		return -1;
	}
	// using -2 as visited state indicator
	if(dp[i][j][modValue] != -2) return dp[i][j][modValue];

	int requiredMod = (modValue - (grid[i][j] % k) + k) % k;
	int ans1 = rec(i+1, j-1, requiredMod);
	int ans2 = rec(i+1, j+1, requiredMod);
	if(ans1 == ans2 && ans1 == -1) return dp[i][j][modValue] = ans1;
	else if(ans1 == -1) return dp[i][j][modValue] = ans2 + grid[i][j];
	else if(ans2 == -1) return dp[i][j][modValue] = ans1 + grid[i][j];
	else return dp[i][j][modValue] = max(ans1, ans2) + grid[i][j];
}

void solve(int Case) {
	cin >> n >> m >> k;
	string temp;
	forn(i, 0, n) {
		cin >> temp;
		forn(j, 0, m) {
			int digit = temp[j] - '0';
			grid[i][j] = digit;
			forn(x, 0, k) dp[i][j][x] = -2;
		}
	}

	int ans = -1;
	for(int i = 0; i < m; i++) {
		int curr = rec(0, i, 0);
		ans = max(ans, curr);
	}
	cout << ans << nline;
}
```

### Balanced Bracket Sequence

**Problem:** Given a string $S$ of length $n$ ($n \leq 1000$). The string contains characters `( or ) or ?`. We can replace `?` with any of `( or )`, we need to tell number of balanced parenthesis strings that can be made out of $S$ by replacing `?` . We need to print the answer mod $10^9+7$.

**Solution:** We will use a dp state `rec(int indx, int diff)` which returns the number of valid strings in the suffix from $S[indx, \dots, n-1]$ such that $diff$ is the difference between $Count_( - Count_)$ i.e (count of opening brackets - count of closing brackets). The answer will be `rec(0, 0)`.

```c++
ll rec(int indx, int diff) {
	if(diff < 0) return 0;
	if(indx == n) {
		if(diff) return 0;
		else return 1;
	}
	if(dp[indx][diff] != -1) return dp[indx][diff];
	ll ans = 0;
	if(s[indx] == '?') {
		ans = rec(indx+1, diff-1) + rec(indx+1, diff+1);
	} else if(s[indx] == '(') {
		ans = rec(indx+1, diff+1);
	} else {
		ans = rec(indx+1, diff-1);
	}
	ans %= mod;
	return dp[indx][diff] = ans;
}
```

### Kadane's Algorithm

**Problem:** given an array and we need to find the maximum sum subarray.

**Solution:** We can use a dp state `dp[i]` which returns the maximum sum of a subarray ending at index $i$. The transition is simple, either we increase the array ending at previous index or we start a new array at index $i$ itself i.e `dp[i] = max(dp[i-1] + arr[i], arr[i])`. Notice when we are index we only need the dp value of previous index and the remaining array is kind or useless at this point, hence we only a prev variable instead of maintaining the entire array.

```c++
int maxSumSubarray(vector<int>& arr, int n) {
	int ans = -inf;
	int prev = arr[0];
	ans = max(ans, prev);
	for(int i = 1; i < n; i++) {
		int curr = max(prev + arr[i], arr[i]);
		ans = max(curr, ans);
		prev = curr;
	}
	return ans;
}
```

### Maximum Sum In Grid

**Problem:** Given an $n \times m$ grid of integers and we need to find the maximum sum sub-grid. $n, m \leq 10^5$ and $n * m \leq 10^5$.

**Solution:** The idea is that we can have a solution which is $O(n \times m \times min(n, m))$ since $n \times m \leq 10^5$ which means $min(n, m) \leq sqrt(10^5)$. Lets say $m <= n$ then we loop over all pairs of columns and fixing them, then we just have to find the maximum sum continuous rows, which can be solved using kadane's algorithm.

```c++
vector<vector<int>> pref;
void fillpref(ll n, ll m) {
	for(ll i = 1; i <= n; i++) {
		for(ll j = 1; j <= m; j++) {
			pref[i][j] = pref[i][j-1] + pref[i-1][j] - pref[i-1][j-1] + grid[i][j];
		}
	}
}

int getSum(pair<int,int> topleft, pair<int,int> bottomright) {
	int res = pref[bottomright.first][bottomright.second];
	res -= pref[topleft.first - 1][bottomright.second];
	res -= pref[bottomright.first][topleft.second-1];
	res += pref[topleft.first-1][topleft.second-1];
	return res;
}

void solve(vector<vector<int>>& grid, int n, int m) {
	pref = vector<vector<int>>(n+1, vector<int>(m+1));
	fillpref(n, m);
	int ans = -INF;

	if(n >= m) {
		for(int l = 1; l <= m; l++) {
			for(int r = l; r <= m; r++) {
				ll curr = getSum({1, l}, {1, r});
				ans = max(curr, ans);
				for(int i = 2; i <= n; i++) {
					ll currRow = getSum({i, l}, {i, r});
					curr = max(curr + currRow, currRow);
					ans = max(curr, ans);
				}
			}
		}
	} else {
		for(int l = 1; l <= n; l++) {
			for(int r = l; r <= n; r++) {
				ll curr = getSum({l, 1}, {r, 1});
				ans = max(curr, ans);
				for(int i = 2; i <= m; i++) {
					ll currCol = getSum({l, i}, {r, i});
					curr = max(curr + currCol, currCol);
					ans = max(curr, ans);
				}
			}
		}
	}

	cout << ans << nline;
}
```

>[!Note]
>In the above problem, when we fix the ends for columns, we sort of reduce the problem to now be solved for single dimension, this reduction of dimensions which still capturing the original data is called **Dimensionality Reduction**. Another problem where this approach can be used is find the maximum area rectangle in a grid with $0$ and $1$ with similar constraints.

### Uncommon Subsequences

**Problem:** Given two strings $S$ and $T$, find length of the shortest subsequence in $S$ which is not a subsequence in $T$. If no such subsequence is possible, return $−1$. $|S|, |T| \leq 1000$.

**Solution:** We will use a dp state `rec(int i, int j)` which returns the answer for prefix $S[0, \dots, i]$ and $T[0, \dots, j]$. Now there are two choices for the $ith$ character in $S$, either it is part of a subsequence that is not present in $T$ or it is not. In case it is not then answer is same as `rec(i-1, j)`. In case it is part of then we find the latest position of character $S[i]$ in $T$ which is $\leq j$. If not such position exist then simply the answer is $1$. But if it exist then and lets say it is at $k$, then the answer is `rec(i-1, k-1)+1`, this is because if the subsequence in $S$ is not present in prefix $T[0, \dots, k-1]$, then it will surely not be present in $T[0, \dots, j]$ because there is not character to match $S[i]$.

```c++
int rec(int i, int j) {
	if(i < 0) return -1; // not possible string
	if(j < 0) return 1; // any string of length >= 1 works

	if(visited[i][j]) return dp[i][j];
	visited[i][j] = 1;

	int ans = rec(i-1, j); // s[i] not in answer
	int pos = prev[s[i] - 'a'][j]; // pre calculated values of latest positions in t
	if(pos == -1) {
		ans = 1;
	} else {
		int ans2 = rec(i-1, pos-1);
		if(ans2 != -1) ans2++;
		if(ans == -1 || ans2 < ans) ans = ans2;
	}

	return dp[i][j] = ans;
}
```

### Removing Marbles

**Problem:** You are given $N$ marbles in different colours. You have to remove marbles till there are no marbles left. Each time you can choose continuous marbles with the same colour, remove them and get $k*k$ points (where $k$ is the length of the continuous marbles removed). Find the maximum points you can get.

**Solution:** One thing that is obvious is that we have to use LR Dp, but the state formulation is not trivial. Lets say that we use state `rec(int l, int r)` to be the maximum score for the range $[l, r]$. here keeping track of how many marbles are we deleting is difficult because many marbles might join after ranges between them is deleted. Hence here we use a dp state `rec(l, r, x)` which returns the maximum score in range $[l, r]$ such that there are $x$ marbles of colour same as $colour[l]$ that are to be deleted with $l$. Now for transition we have two choices, either to delete all marbles latched on to $l$ and get a score of $(1+x)^2 + rec(l+1, r, 0)$, other choice that we find another marble of same colour in the range $[l,r]$ and latch all the marbles to it, lets say that we have another marble of same colour as $colour[l]$ as index $k$, then we would need to delete marbles in range $[l+1, k-1]$ and our final answer for this range will be `rec(l+1,k-1) + rec(k, r, x+1)`, obviously we take the maximum of these.

```c++
int rec(int l, int r, int x) {
	if(l > r) return 0;
	if(dp[l][r][x] != -1) return dp[l][r][x];

	int ans = (x+1) * (x+1) + rec(l+1, r, 0);

	for(int k = l+1, k <= r; k++) {
		if(colour[k] == colour[l]) {
			ans = max(ans, rec(l+1, k-1, 0) + rec(k, r, x+1));
		}
	}

	return dp[l][r][x] = ans;
}
```

### Mountain Array

**Problem:** Given an array $arr$ of $n$ integers, we need to find the minimum number of elements that we need to delete from the array such that the remaining elements make a mountain. Note a mountain array means that exist an index $i$ such that $0 < i < arr.size()-1$ and $arr[0] < arr[1] < \dots < arr[i-1] < arr[i] > arr[i+1] > \dots > arr[n-1]$.

**Solution:** The solution is finding lis for every index in to its left and to its right and then length of mountain centered at this index will be $leftLis[i] + rightLis[i] - 1$. The answer will be $n - maxMountainLen$.

```c++
int solve(vector<int>& arr, int n) {
	vector<int> left(n), right(n), lis;
	// calculating left lis
	for(int i = 0; i < n; i++) {
		int indx = lower_bound(lis.begin(), lis.end(), arr[i]) - lis.begin();
		if(indx == lis.size()) lis.push_back(arr[i]);
		else lis[indx] = arr[i];
		left[i] = indx+1;
	}
	// calculating right lis
	lis.clear();
	for(int i = n-1; i >= 0; i--) {
		int indx = lower_bound(lis.begin(), lis.end(), arr[i]) - lis.begin();
		if(indx == lis.size()) lis.push_back(arr[i]);
		else lis[indx] = arr[i];
		right[i] = indx+1;
	}

	int ans = 0;
	for(int i = 1; i < n-1; i++) {
		ans = max(ans, left[i] + right[i] - 1);
	}

	if(ans >= 3) return n - ans;
	else return -1;
}
```

### Merge Elements

**Problem:** You are given $N$ elements, in an array $A$. You are also given $3$ constants $X$, $Y$, and $Z$. You can take any $2$ consecutive elements $a$ and $b$ and merge them. On merging you get a single element with value $(aX+bY+Z) \% 50$ and this process costs you $a*b$. After merging you will place this element in place of those $2$ elements.  Find the Minimum cost to merge all the elements into a single element.

**Solution:** We will use a dp state `rec(i, j, x)` which is the minimum cost to merge the elements in range $[i, j]$ such that final value of the range is $x$. But in recursion we will only use the state `rec(i, j)` and calculate all possible $x$ in this call only. We will loop over all $k \in [i, j)$ and then will all possible combination of values of left and right ranges.

```c++
void rec(int i, int j) {
	if(i == j) {
		dp[i][j][arr[i]] = 0;
		// for all others the dp array is initialized with inf
		return;
	}
	
	if(visited[i][j]) return;
	visited[i][j] = 1;
	for(int k = i; k < j; k++) {
		// calling rec for left and right parts
		rec(i, k);
		rec(k+1, j);
		for(int a = 0; a < 50; a++) {
			for(int b = 0; b < 50; b++) {
				int currVal = (a*x + b*y + z) % 50;
				int cost = dp[i][k][a] + dp[k+1][j][b] + a * b;
				dp[i][j][currVal] = min(dp[i][j][currVal], cost);
			}
		}
	}
}
```

### Sum Partition

**Problem:** Find the number of unordered ways, $N$ can be partitioned into $K$ positive integers i.e sum of all $K$ is equal to $N$. Print the answer modulo $10^9 + 7$.

**Solution:** The first idea is that we for every solution there are multiple permutations of it that exist and for all of these we must count $1$, for example if $N = 9$ and $K = 3$, then one of the possible solution is $\{1, 5, 3\}$, but $\{1, 3, 5\}$ is also a solution, so to fix this problem of duplicated we will find the sorted solution since sorted solutions are unique. For this we use dp state `rec(int n, int k)` which is the number of ways to get sum $n$ such that last chosen integer is $\leq k$. The transition is we can either choose $k$ and go to state `rec(n-k, k)` (since we can choose $k$ again). other wise we will go to state `rec(n, k-1)`.

The second idea that will help use to make sure that we only choose $k$ integers is that every choice of solution with $k$ integers can be mapped to a solution with any number of integers but the maximum value $<= k$, for example consider solution $\{1, 3, 5\}$ for $N = 9$ and $K = 3$, if we write each of the value as bunch of $1$'s we will get something shown in the figure below.

![[Pasted image 20240818181315.png | center]]

Hence choosing $k$ integers is same as generating a solution in which each value is $\leq k$  which is simple to solve with our state. Also we have to solve for `rec(n-k,k)` since we need to keep $k$ $1's$ separately since it might happen that in our solution none of the values is equal to $k$ in which case when distributing the answer into $k$ values we will get some of the values as $0$, hence we keep $k$ $1's$ separately to give to every item later.

```c++
int rec(int n, int k) {
	if(n == 0) return 1;
	if(n < 0 || k == 0) return 0;

	if(dp[n][k] != -1) return dp[n][k];

	int ans = (rec(n-k, k) + rec(n, k-1)) % mod;

	return dp[n][k] = ans;
}
```

### Rock Paper Scissors

**Problem**: Given a string $S$ of length $n$ that represents the choice of moves that Bob will make when playing rock, paper, scissors against you. Given you already know what $S$ is, generate a string of your moves such that it contains at most $k$ places where the previous move is not same as current move and the number of wins is maximum possible. If multiple solutions exist return the one which is lexicographically the smallest. Given input string contains character `R or P or S` representing the Bob's move. For output we need to print the maximum number of wins possible and lexicographically smallest string that gets us this answer.

**Solution:** We will use a dp state $rec(i, j, x)$ which gives the maximum number of wins in the suffix $[i, \dots, n-1]$ such that $j$ changes have been made and we have move $x$ at $ith$ position ($0 \leq x \leq 2$). For transition we can go to `rec(i+1, j, x) or rec(i+1, j+1, (x+1)%3) or rec(i+1, j+1, (x+2)%3)` to these we need to add $1$ in case win in this round. When generating the solution we choose the one which gives the maximum wins and in case of draw we take a choice with smallest move.

```c++
int dp[1010][1010][3];
int n, k;
string s;
string pattern = "RPS";

int result(int bobMove, int yourMove) {
	return yourMove == ((bobMove+1)%3);
}

int rec(int i, int changes, int curr) {
	if(i >= n) return 0;
	if(changes > k) return -inf;
	if(dp[i][changes][curr] != -1) return dp[i][changes][curr];
	int ans = 0;
	int bobMove = pattern.find(s[i]);
	int currResult = result(vivekMove, curr);
	for(int nextMove = 0; nextMove < 3; nextMove++) {
		if(nextMove == curr) ans = max(ans, rec(i+1, changes, nextMove));
		else ans = max(ans, rec(i+1, changes+1, nextMove));
	}
	ans += currResult;
	return dp[i][changes][curr] = ans;
}

string getMoves(int i, int changes, int curr) {
	if(i >= n) return "";
	int ans = rec(i, changes, curr);
	int vivekMove = pattern.find(s[i]);
	int currResult = result(vivekMove, curr);
	int ans1 = rec(i+1, changes, curr);
	int ans2 = rec(i+1, changes+1, (curr+1)%3);
	int ans3 = rec(i+1, changes+1, (curr+2)%3);
	string moves = "";
	if(curr == 0) {
		if(ans2+currResult == ans) {
			moves = getMoves(i+1, changes+1, (curr+1)%3);
		} else if(ans1+currResult == ans) {
			moves = getMoves(i+1, changes, curr);
		} else {
			moves = getMoves(i+1, changes+1, (curr+2)%3);
		}
	} else if(curr == 1) {
		if(ans1 + currResult == ans) {
			moves = getMoves(i+1, changes, curr);
		} else if(ans3+currResult == ans) {
			moves = getMoves(i+1, changes+1, (curr+2) % 3);
		} else {
			moves = getMoves(i+1, changes+1, (curr+1) % 3);
		}
	} else {
		if(ans3+currResult == ans) {
			moves = getMoves(i+1, changes+1, (curr+2)%3);
		} else if(ans2 + currResult == ans) {
			moves = getMoves(i+1, changes+1, (curr+1)%3);
		} else {
			moves = getMoves(i+1, changes, curr);
		}
	}
	
	return pattern[curr] + moves;
}

  

void solve(int Case) {
	cin >> n >> k;
	forn(i, 0, n) forn(j, 0, k+1) forn(x, 0, 3) dp[i][j][x] = -1;
	cin >> s;
	int ans = 0;
	ans = max(ans, rec(0, 0, 0));
	ans = max(ans, rec(0, 0, 1));
	ans = max(ans, rec(0, 0, 2));
	string moves = "";
	if(ans == rec(0, 0, 1)) {
		moves = getMoves(0, 0, 1);
	} else if(ans == rec(0, 0, 0)) {
		moves = getMoves(0, 0, 0);
	} else {
		moves = getMoves(0, 0, 2);
	}
	cout << ans << nline << moves << nline;
}
```