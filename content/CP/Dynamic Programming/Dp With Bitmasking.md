> Here we discuss various types of problems related to dp with bit-masking

## Form 1

The first form is where we have two sets and we need to match elements from one set two another set. For example consider the problem where we are given $n$ ranks and m students we need to assign the ranks to students, giving $ith$ rank to $jth$ student gives happiness score $happy[i][j]$, we need to assign ranks such that total happiness is maximized. Note that it might be that $n \lt m$, then all students can't be assigned unique ranks, so the students that don't get any rank save happiness score $0$. Here $1  \leq n \leq 15$ and $1 \leq m \leq 50$.

**Dp With Bitmasking Approach:** the idea here is to store mask of one set and iterate over other set, since $n$ is small we will keep mask of ranks that we have chosen and iterate over students. We will use the dp state $dp[chosen][indx]$ which returns maximum happiness for students from $[i, m]$ such that $chosen$ gives the bitmask of all the ranks that are already chosen. For transition we loop over all not taken ranks and if we choose a rank $i$ then we get total happiness as $rec(chosen|(1<<i), indx+1) + happiness[indx][i])$ The time complexity if $O(m \times 2^n)$, but actually it is less that that because a lot of the states are never visited. 

```c++
int n, m;
int happiness[50][50];
int dp[1<<15+1][50];
int maxHappiness(int chosen, int indx) {
	if(indx == m) {
		return 0;
	}
	if(dp[chosen][indx] != -1) return dp[chosen][indx];
	int ans = maxHappiness(chosen, indx+1); // not chosing any rank for curr student
	for(int i = 0; i < n; i++) {
		if(chosen&(1<<i)) continue; // rank already chosen
		ans = max(ans, maxHappiness(chosen|(1<<i), indx+1) + happiness[indx][i]);
	}
	return dp[chosen][indx] = ans;
}
```
  
*Similar Problem:* [T-Shirts](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/TSHIRTS?tab=statement)
## Form 2

In the type we have to generate the best permutation or count number of valid permutations based on the conditions given in the problem. Here the state is generally $dp(lastElement, mask)$ where $mask$ is of elements that already went into permutation and $lastElement$ is the last element that went into the permutation. Lets understand this with a famous problem.

**Hamiltonian Walk Problem:** given a graph, we need to count number of *hamiltonian* walks that start at node $1$ and end at node $n$ ($n \leq 20$). A hamiltonian walk is one in which every node is visited exactly once. For example look at the graph below, one of the possible hamiltonian walks are shown by orange path. 
![[Pasted image 20240827221809.png | center]]

**Approach:** Here a dp state $dp(node, mask)$ that returns the number of hamiltonian walks from $node$ to $n$, where $mask$ is of nodes that we have visited. For transition here we go over all adjacent nodes of $node$ and if they are unvisited we explore the path and add its returns value to our answer. Base case is when we reach node $n$, if at this point every node is visited then we return $1$ or else we return $0$. For easy implementation we change graph to $0$ base indexed i.e nodes are from $0$ to $n-1$.

**Time complexity** can be calculated considering the fact that this code is exploring all dfs paths from node $0$ and a dfs is $O(n+m)$ ($m$ is number of edges), so total time complexity is $O((n+m) \times 2^n)$, obviously actual time complexity is lower but it cannot be easily calculated, and this is a good upper bound.

```c++
vector<vector<int>> graph, dp;
int n;
int rec(int node, int visited) {
	if(node == n) {
		if(visited == ((1<<20)-1)) return 1; // if all nodes are visited
		else return 0; // otherwise we return 0
	}
	if(dp[node][visited] != -1) return dp[node][visited];
	int ans = 0;
	for(int adjNode : graph[node]) {
		if(visited&(1<<adjNode)) continue; // if node already visited continue
		ans += rec(adjNode, visited | (1<<adjNode));
	}
	return dp[node][visited] = ans;
}
```
  

*Similar Problem:* [Minimum Cost Array Permutation](https://leetcode.com/problems/find-the-minimum-cost-array-permutation/description/)

#### Some Variants Of Hamiltonian Walk Problem:
1. *Find min cost hamiltonian walk in a weighted graph,* here we can start from any node and end at any node. To solve this we can use the same dp state as the previous one, just that dp will now min cost path to visit all the nodes starting from current node such that $mask$ represents nodes that are already visited. Base case will be when mask has all bits set. We call the recursion multiple times by considering each node as starting point and our answer will be ${\underset{i=0}{\overset{n-1}{min}}}\hspace{3 mm} rec(i, (1<<i))$.
   Another way to do the same without calling recursion multiple times is to use a *dummy node* with edge of weight $0$ to every other node and we call $rec(dummyNode,\hspace{1 mm} (1<<dummyNode))$.
2. *Finding number of hamiltonian walks,* here we can start from any node and end at any node. Here the idea is same as above, we either call $rec(i, 1<<i)$ for every node $i$ and add them up, or use a dummy node.
3. *Find number of hamiltonian cycle.* Hamiltonian cycle is a path that start from a node and ends at the same node visiting all edges once. Here there is a nice trick, we can simply solve for number hamiltonian walks, just in the base case add extra condition if there is an edge from last visited node to first node.
4. *Finding number of Simple Paths in Undirected Graph:* a simple path is simple a path connecting $2$ nodes in which each node is visited only once. For solving this we use same approach as point $2$ the only difference we need to initialize our answer with $1$ instead of $0$ since every node is an ending of a path (note we only do this if there are at least $2$ nodes visited). Finally after calculating the answer we divide it by $2$ since every path will be counted twice.
#### Number of Cycles in an Undirected Graph
Finding every cycle is very difficult and needs multiple dfs. To uniquely identify a cycle and avoid over counting we will associate every cycle with its smallest node, then problem boils down to number of paths from node $i$ to $i$ such that all nodes in the path are $\gt i$. Here a dp state $dp(node, mask)$ works where $node$ is current node on which we are at and $mask$ is list of all nodes in the path. This dp will store the number of simple paths from node to smallest set bit in $mask$, clearly the smallest set bit will be the $start$ of the path and at every $node$ we will check if there is a direct edge from $node$ to $start$ so we check if $edge[node][start]$ exist we increment answer (*Note* we only do this if number of nodes visited are more than $2$). Then we will explore all possible paths from node. Only one caveat here is that the answer we count this way is 2 times actual answer, because for each path we discover from $i$ to $i$, the reverse path will also be discovered.

```c++
vector<vector<int>> graph, dp;
int n;
int rec(int node, int mask, int start) {
	if(dp[node][mask] != -1) return dp[node][mask];
	int ans = 0;
	int visitedNodes = __builtin_popcount(mask);
	// if there is edge from node to start
	if(graph[node][start] && visitedNodes >= 3) {
		ans++;
	}

	for(int adjNode = start+1; adjNode < n; adjNode++) {
		if(mask&(1<<adjNode)) continue; // if already visited continue;
		if(!graph[node][adjNode]) continue; // if no edge from node to adjNode
		ans += rec(adjNode, mask | (1<<adjNode), start);
	}

	return dp[node][mask] = ans;
}

void numberOfCycles() {
	int n, m; cin >> n >> m;
	graph.assign(n, vector<int>(n, 0));
	dp.assign(n, vector<int>(1<<n, -1));
	for(int i = 0; i < m; i++) {
		int u, v; cin >> u >> v;
		graph[u][v] = graph[v][u] = 1;
	}
	int ans = 0;
	for(int start = 0; start < n; start++) {
		ans += rec(start, 1<<start, start);
	}

	cout << ans / 2 << '\n';
}
```
  
## Form 3

In form 3 we have problems which have intraset matching, like consider problem where we have n chess boards and $2*n$ chess players, each player has a rating and we need to pair chess players. Pairing players i and j on board k gives happiness score of $k \times |rating[i] - rating[j]| \times gcd(rating[i], rating[j])$. Here a simple state $dp(mask)$ works where mask represents players already paired. From mask we can also get the board for which we need to choose next pair, look at the code below.

```c++
vector<vector<int>> dp;
vector<int> rating;
int n;
int rec(int mask) {
	int k = (__builtin_popcount(mask) / 2) + 1;
	if(k == n+1) return 0; // all chess boards assigned
	if(dp[mask] != -1) return dp[mask];
	int ans = 0;
	for(int i = 0; i < 2 * n; i++) {
		if(mask&(1<<i)) continue; // player i is used
		for(int j = i + 1; j < 2 * n; j++) {
			if(mask&(1<<j)) continue; // player j is used
			int pairScore = k * abs(rating[i] - rating[j]) * __gcd(rating[i], rating[j]); // can precalculate before 
			ans = max(ans, rec(mask | (1<<i) | (1<<j)) + pairScore);
		}
	}
	return dp[mask] = ans;
}
```

>[!Note]
> If lets say the board on which a pair sits does not matter then we can optimize the transition, where instead of trying pairs of all available players we can just pair the first available player with the rest of the players this will make transition from $O(n^2)$ to $O(n)$ and total complexity $O(n * 2^n)$ ($n$ is number of players and not boards).

## Form 4

Another form is where we need to delete some edges from a graph. Consider the problem where we are given a *directed graph* and we need to find the *minimum* number of edges that we need to delete such that the graph becomes *DAG*.

**Solution:** The solution lies in a property of DAG which is presence of topological sort of the nodes. So we will generate all possible topological sorts and then delete edges from graph such that the topological sort is valid. The idea is that in a DAG there is no edge from a node in topological sort to a previous node. For example if topo sort $4,3,5,2,1$, then there cannot be an edge from node $1$ to $2,3,4,5$ or from node $2$ to $3,4,5$ and so on. Here a dp state $dp(mask)$ works where mask represents the nodes that are already put in topo sort, then for transition we loop over the available nodes and lets say we choose to put node i next, then cost of putting node i will be number of back edges from i to nodes in mask.

```c++
vector<vector<int>> graph;
vector<int> dp;
int n;
int rec(int mask) {
	if(mask == (1<<n)-1) return 0;
	if(dp[mask] != -1) return dp[mask];
	int ans = inf;
	for(int node = 0; node < n; node++) {
		if(mask&(1<<node)) continue;
		int currCost = 0;
		for(int prevNode = 0; prevNode < n; prevNode++) {
			if(!(mask&(1<<prevNode))) continue; // if node not present, then not prev node
			currCost += graph[node][prevNode]; // increase cost if there is edge from node to prev node
		}
		ans = min(ans, currCost + rec(mask&(1<<node)));
	}
	return dp[mask] = ans;
}
```

## Form 5 (Profile Dp)

Consider a problem where there is an $n \times n$ grid and we need to tile this grid completely using $2\times1$ rectangular tiles, the tiles can be placed vertically or horizontally. We need to find number of ways to do this task.
**Approach** In such problems we can use profile dp with bitmask. Each tile we represent by its end and when we are at cell $(i,j)$ we choose to place end of a $2\times1$ tile here, if we place horizontally then the cell to left will also get filled and if we place vertically then cell above will also get filled, hence we need information about cell to left and cell above to know what ways we can place tile in current cell.

![[Pasted image 20240828000351.png | center | 700]]

**Dp State:** Here a bitmask where $0$ represents empty cell and $1$ represents filled cell can be used, we will store bitmask of cells starting from cell above to the cell to left of current cell this will require $n$ bits (as shown in the figure above, only part of square grid is shown and not the whole grid). Now since cell above is empty then we must put the tile vertically as that is the only way to fill that cell. If above cell is filled then we have two choice if cell to left is not filled then we can place tile horizontally or else we cannot place any tile (tile end) in this cell and continue. Moving to next state is simply left shifting the mask and adding configuration of current cell. Final sub problem will be when row is $n$ and $mask$ is $(1<<n)-1$ i.e we move out of grid and last row is completely filled.

```c++
vector<vector<int>> dp;
int n;
int rec(int cellNumber, int mask) {
	int row = cellNumber / n;
	int col = cellNumber % n;
	if(row == n) {
		if(mask == (1<<n)-1) return 1; // all cells are filled
		else return 0; // not all of the cells are filles
	}
	if(dp[cellNumber][mask] != -1) return dp[cellNumber][mask];
	int ans = 0;
	// if cell above is empty
	if((mask&(1<<(n-1))) == 0) {
		ans = rec(cellNumber+1, (mask<<1)|1);
	} else {
	    // if previous cell exist and is empty
		if(col > 0 && !(mask&1)) ans += rec(cellNumber+1, (mask<<1)|3);
		ans += rec(cellNumber+1, (mask << 1)); // leaving the cell empty
	}
	return dp[cellNumber][mask] = ans;
}
```

**Note:** Similarly we can solve problems where we need to fill $n\times m$ grid with $L$ shaped tile or some other shape.

## Form 6: (Submask Decomposition)

Some problems requires to form most groups among of elements of a set. For example consider a problem where we have $n$ students and we want to form teams. If student $i$ and $j$ are in the same team then their happiness increases by $happiness[i][j]$. We need to form teams such that maximum happiness is achieved.

Here $dp(mask)$ represents maximum happiness possible by making teams of the children available in mask. We will loop over all $submask$ of $mask$ and put all of those students in one team and then call for `dp(mask^submask)` which is mask of remaining students. Now happiness of putting all students represented by mask in one team can be pre-calculated. For calculating happiness of $mask$, we find happiness of first student (say $j$) with all other present students then we find happiness of remaining mask i.e $maskHappiness[mask] = \sum happiness[i][j] + maskHappiness[mask - (1<<j)]$. If we iterate over masks from $0$ to $2^n$ then the value of $mask-(1<<j)$ will be already calculated.

To iterate over all submasks efficiently there is a common algorithm, where we start with $submask = mask$ and run loop till $submask > 0$ and after each iteration we need to update $submask = ((submask-1)\& mask)$. To understand this first we consider our $mask = 15 = (1111)_2$ and lets we simply subtract $1$ from $mask$ in every iteration $mask$ we get are given below,
$$(1111)_2 \rightarrow (1110)_2 \rightarrow (1101)_2 \rightarrow (1100)_2 \rightarrow (1011)_2 \rightarrow (1010)_2 \rightarrow (1001)_2 \rightarrow (1000)_2 \rightarrow (111)_2 \rightarrow (110)_2 \rightarrow (101)_2 \rightarrow (100)_2 \rightarrow (11)_2 \rightarrow (10)_2 \rightarrow 1$$
We can see that this actually generated all the $submasks$ of $mask$. But this was only due to the fact that $mask$ had all bits set initially (without gaps). Now if $mask = 26 = (11010)_2$ then simply doing $mask-1$ every time introduces new set bits that were not part of original set. But if along with subtracting with $1$ we also do bitwise AND with $mask$ then all extra bits will automatically be removed. Doing so we get values of submask in each iteration as shown below,
$$(11010)_2 \rightarrow(11000)_2 \rightarrow(10010)_2 \rightarrow(10000)_2 \rightarrow(1010)_2 \rightarrow(1000)_2 \rightarrow(10)_2$$
This is similar to generating $submasks$ of $mask = 7 = (111)_2$ with extra zeroes in some places that always remain as $0$.

```c++
vector<vector<int>> happiness;
vector<int> dp, maskHappiness;
int n;
void preCalculateGroupHappiness() {
	int maskEnd = (1<<n);
	maskHappiness.assign(maskEnd, 0);
	for(int mask = 0; mask < maskEnd; mask++) {
		int i = __builtin_ffs(mask) - 1; // first set bit in mask, we can also use __builtin_ctz(mask)
		int currHappiness = maskHappiness[mask^(1<<i)];
		for(int j = i + 1; j < n; j++) {
			if(mask&(1<<j)) currHappiness += happiness[i][j];
		}
		maskHappiness[mask] = currHappiness;
	}
}

int rec(int mask) {
	if(mask == 0) {
		return 0; // all students are in some group
	}
	if(dp[mask] != -1) return dp[mask];
	int ans = 0;
	for(int submask = mask; submask > 0; submask = ((submask-1)&mask)) {
		ans = max(ans, rec(mask^submask) + maskHappiness[submask]);
	}
	return dp[mask] = ans;
}
```

## Some More Practice Problems

**Problem:** A sequence $b$ of size $n$ is considered good if for every element $i$ and $j$ of the sequence ($i \neq j$) we have $gcd(b_i, b_j) = 1$. Given a sequence $a$ of same size as $b$, find a sequence $b$ gives minimum value for expression $\sum |a_i - b_i|$. Constraints are $1 \leq n \leq 100$ and $1 \leq a_i \leq 30$.

**Solution:**

```c++
void solve()
{
	int maxb = 60;
	int inf = 1e9;
	cin >> n;
	vector<int> a;
	forn(i, 0, n) cin >> a[i];
	vector<int> pf(maxb+1);
	int primeIndex = 0;
	for(int i = 2; i <= maxb; i++)
	{
		if(pf[i]) continue;
		for(int j = i; j <= maxb; j += i)
			pf[j] |= (1<<primeIndex);
		primeIndex++;
	}
	int maskEnd = (1 << primeIndex);
	vector<vector<int>> dp(n+1, vector<int>(maskEnd));
	vector<vector<int> choice(n+1, vector<int>(maskEnd))
	for(int i = n-1; i >= 0; i--)
	{
		for(int j = 0; j < maskEnd; j++)
		{
			dp[i][j] = dp[i+1][j] + abs(a[i] - 1);
			choice[i][j] = 1;
			for(int b = 2; b < 2 * a[i]; b++)
			{
				if((pf[b] & j)) continue; // if b and j have common prime factors
				int curr = dp[i+1][j|pf[b]] + abs(a[i] - b);
				if(dp[i][j] > curr)
				{
					dp[i][j] = curr;
					choice[i][j] = b;
				}
			}
		}
	}
	vector<int> res;
	int j = 0;
	for(int i = 0; i < n; i++)
	{
		res.push_back(choice[i][j]);
		j |= pf[choice[i][j]];
	}
	for(auto val : res) cout << val << ' ';
	cout << '\n';
}
```

