# Z-Function

Suppose we are given a string $s$  of length $n$ . The **Z-function** for this string is an array of length $n$  where the $i$ -th element is equal to the greatest number of characters starting from the position $i$  that coincide with the first characters of $s$ .

In other words, $z[i]$  is the length of the longest string that is, at the same time, a prefix of $s$  and a prefix of the suffix of $s$  starting at $i$ .

The first element of Z-function, $z[0]$​ , is generally not well defined. Here we will assume it is zero (although it doesn't change anything in the algorithm implementation).

**Implementation**

The trivial implementation with nested loop take $O(n^2)$ time to calculate the z function. But the efficient algorithm can do it in $O(n)$ time complexity.

The idea for efficient algorithm is that we will maintain a range $[l \dots r)$ which will be the right most explored range which is same as prefix i.e $s[l \dots r) = s[0 \dots r-l)$. Now there will be two cases for our current index $i$,

1. $i > r$, this is unexplored territory and we carry out comparision as usual like in trivial algorithm to calculate value of $z[i]$.
2. i <= r in this case we use the fact that $s[l \dots r) = s[0 \dots r-l)$, hence index $i$ in range $[l, r)$ corresponds to indes $i - l$ in range $[0, r - l)$ and we initialize value of $z[i]$ with $z[i-l]$. It might happen that value of $z[i-l]$ exceeds $r - i$ i.e goes beyond $r$. In that case we take $z[i] = min(z[i-l], r - i)$.

After processing index $i$, if $i + z[i] > r$ this means right most segment same as prefix is now $[i \dots i + z[i])$ so we update values of $l$ and $r$ accordingly.

It can be proved that this algorithm is $O(n)$ because every time the nested while loop runs the value of $r$ increases by $1$. Hence it only runs only $O(n)$ time.

```c++
vector<int> zfunction(string s)
{
    int n = s.length();
    vector<int> z(n);
    int l = 0, r = 0;
    for(int i = 1; i < n; i++)
    {
        if(i < r)
        {
            z[i] = min(r - i, z[i - l]);
        }
        while(i + z[i] < n && s[z[i]] == s[i+z[i]])
            z[i]++;
        if(i + z[i] > r)
        {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}
```

Applications of Z-Function is same as Prefix Function algorithm.

// Suffix Structure: This is a method to find a pattern of length m in a text in O(m) time by some preprocessing of text. The idea is to make a trie structure of all suffix sub strings in text and then checking for pattern is simply checking if that exist in the trie or not. All the sub strings will be present in the trie, so we start from the root and keep going down according to the pattern and if we are able to reach the end of the pattern this means that pattern exist in the string.