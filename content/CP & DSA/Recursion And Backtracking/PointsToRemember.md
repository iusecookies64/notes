### Points To Remember

1. In n queens problem if we want to check whether the queens at x,y attack queen at a, b, then first we check whether they have the same row or column by doing `x==a || y==b`, if not then we check for diagonal attack, for this we can check `abs(x - a) == abs(y - b)` because if they attack diagonally then they are ends of a square and in square sides are equal.

2. Recursive code for tower of hanoi with n disc i.e tower_hanoi(int n, int source, int target, int auxiliary) is first we transfer n-1 discs to auxiliary using target as auxiliary and then transfer these n-1 discs from auxiliary to target.

```c++
void tower_hanoi(int n, int source, int target, int auxiliary)
{
  if(n == 0) return;
  tower_hanoi(n-1, source, auxiliary, target)
  cout << "Move Disc " << n << " from " << source << " to " << target << endl;
  tower_hanoi(n-1, auxiliary, target, source);
}
```

3. Code to generate all subsequences of an array.

```c++
int n; // size of array
int arr[n];
int currSubsequence[n]; // will be used as a stack
int currTop = -1; // index for currTop

void generateSubsequences(int indx)
{
    if(indx == n)
    {
        // the stack has the subsequence
        for(int i = 0; i <= currTop; i++)
            cout << currSubsequence[i] << ' ';
        cout << '\n';
    }

    // case for not choosing arr[indx]
    generateSubsequences(indx+1);

    // case for choosing arr[indx]
    currTop++;  // adding arr[indx] to stack
    currSubsequence[currTop] = arr[indx];
    // generating subsequences again with arr[indx] included
    generateSubsequences(indx+1);
    currTop--;  // removing arr[indx] from stack
}

```

4. To generate all unique permutations of elements of a given array (may contain duplicate elements) we use a map of frequency of each element and recursion. In a given level of recursion we go over all possibilities of which element to put in this level, lets say we chose x, then we will decrease the frequency of x from map and insert it in current permutation array and then call for next level, then when recursion returns we will remove x from current permutation and increase its frequency again.

5. In tower of hanoi the recurrence relation if `t(n) = 2*t(n-1) + 1`, if we calculate the number of moves then we prove that `t(n) = 2^(n) - 1`. To prove this we observe a pattern, that if put value of t(n-1) we will get `t(n) = 2*(2*t(n-2) + 1) + 1 = 2^2 * t(n-2) + 2 + 1` i.e `t(n) = 2^k _ t(n-k) + 2^k-1 + 2^k-2 + ... + 2^0`. In this if we put k = n-1 we will get`t(n) = 2^n-1 _ t(1) + 2^n-2 + ... + 2^0`, now since `t(1) = 1` we get `t(n) = 2^n-1 + 2^n-2 + ... + 2^0 = 2^n - 1`.
