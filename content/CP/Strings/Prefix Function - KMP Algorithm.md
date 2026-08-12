Knuth-Morris-Pratt Algorithm is a very famous algorithm for pattern searching.
## Prefix Function

You are given a string $s$  of length $n$ . The prefix function for this string is defined as an array $\pi$  of length $n$ , where $\pi[i]$  is the length of the longest proper prefix of the substring $s[0 \dots i]$  which is also a suffix of this substring. A proper prefix of a string is a prefix that is not equal to the string itself. By definition, $\pi[0] = 0$ .

Mathematically the definition of the prefix function can be written as follows:

$$\pi[i] = \max_ {k = 0 \dots i} \{k : s[0 \dots k-1] = s[i-(k-1) \dots i] \}$$

For example, prefix function of string "abcabcd" is $[0, 0, 0, 1, 2, 3, 0]$ , and prefix function of string "aabaaab" is $[0, 1, 0, 1, 2, 2, 3]$​ .

The trivial algorithm to compute this prefix function for a given string can be to simply go over every index and for it go over all possible proper prefixes and check if they are equal to suffix. This will take $O(n^3)$ time.

**Efficient Algorithm:**

This is based on the two facts,

1. $\pi[i+1] <= \pi[i] + 1$ this is obvious, since adding one character to substring $s[0 \dots i]$ can only increase $\pi[i+1]$ by $1$. Just doing this optimization changes the time complexity to $O(n^2)$. This is because now the value of $\pi$ can increase at most one time and decrease at most $n$ time, hence total number of comparisons are $O(n)$ and each comparison is $O(n)$.

2. The second optimisation is to remove the comparisons that we do and replace them with $O(1)$ operation.

   For this we use the fact that the first possible length for $\pi[i]$ is $\pi[i-1] + 1$. So we need to compare $s[i]$ with $s[(\pi[i-1]+1)-1] = s[\pi[i-1]]$. 

   If $s[i] \neq s[\pi[i-1]]$, then next possible value of $\pi[i]$ is $\pi[\pi[i-1]-1]+1$, and if this is also not the case then next check for $\pi[\pi[\pi[i-1]-1]-1] + 1$ and so on.

   >[!Note]
   >To check for a particular possible value of $\pi[i]$ we only need to compare two characters which is $O(1)$.

Proofs for both of these claims are nicely explained in CP-Algorithms Article.

Below is implementation of this algorithm.

```c++
vector<int> prefix_function(string s)
{
    int n = s.length();
    vector<int> pi(n);
    for(int i = 1; i < n; i++)
    {
        int j = pi[i-1];
        while(j > 0 && s[i] != s[j])
            j = pi[j-1];
       	if(s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}
```

## Applications Of KMP

1. **Finding all occurrences of string $s$ in $t$.**

   For this we will create a string $s + \# + t$ and create a prefix function of this string. Now for all indices in part of string $t$, if $pi[i] = n$ (where $n$ is the length of $s$) then $i$ is an end of an occurrence of $s$ in $t$. Keep in mind that $i$ is index in the concatenated string and not in $t$. Index $i$ in new string is $i - (n + 1)$ in string $t$. Also $i$ is the end of the occurrence of $s$ and not the start of it, so finally the starting index of occurrence of $s$ in $t$ is $i - (n + 1) - (n - 1) = i - 2n$.

   ```c++
   vector<int> occurrences(string s, string t)
   {
       int n = s.length();
       string S = s + '#' + t;
       vector<int> pi = prefix_function(S);
       vector<int> res;
       for(int i = n + 1; i < S.length(); i++)
       {
           if(pi[i] == n)
           {
               res.push_back(i - 2 * n);
           }
       }
       return pi;
   }
   ```

   **Note:** the space complexity of above algorithm is $O(n+m)$ but we can improve it to $O(n)$. We can use the fact that the value of $pi[i]$ will never cross $n$ (because of #). Hence we don't need store all values of $pi$ we only need the $pi$ values of $s + \#$. For computing $pi$ value of an index in $t$ we only need previous $pi$​ value.

2. **Counting number of occurrences of each prefix.**

   For this we first find all occurrences of $\pi[i]$ using the prefix_function. But this only counts the longest suffix ending at $i$ which is a prefix, but there might be other smaller prefixes that are also present. The next smaller suffix ending at $i$ which is also prefix will be of length $\pi[\pi[i-1]]$. Now for every occurrence of $\pi[i]$ there will be equal number of occurence of $\pi[\pi[i-1]]$ to we will add occurrences of $\pi[i]$ to it. Now if we do this process in decreasing length of prefixes then we don't need to worry the next smaller suffix after $\pi[\pi[i-1]]$ as when we reach $\pi[\pi[i-1]]$ we will add all of its occurrences to its next smaller suffix and so on.

   Lastly we need to add the count the prefix themselves (as they are not counted in $\pi$) which is basically increasing each count by 1.

   ```c++
   vector<int> prefix_occurrence(string s)
   {
       int n = s.length();
       vector<int> pi = prefix_function(s);
       vector<int> count(n+1);
       // count of pi[i]
       for(int i = 0; i < n; i++)
           count[pi[i]]++;
       // adding contribution of pi[i] to pi[pi[i-1]]
       for(int i = n; i > 0; i--)
           count[pi[i-1]] += count[i];
       // count the prefix themselves
       for(int i = 0; i <= n; i++)
           count[i]++;
     	return count;
   }
   ```

   **Note:** to get a number of occurrences of prefix $s[0 \dots i]$ the value is stored in $count[i+1]$​.

3. **Counting number of distinct substrings**

   We can solve this string iteratively. Lets say we have a string $s$ of length $n$ to which we add a new character $c$ at the end. We want to count the increase in number of distinct strings due to addition of this character. Clearly each extra distinct string that is formed will be suffix of $s + c$. To count them in $O(n)$ time we calculate the prefix function for string $c + rev(s)$ and from it we calculate $\pi_{max}$. This means all suffix of length $[1 \dots \pi_{max}]$ in $s + c$ were already present in $s$. Hence suffix of length $[(\pi_{max}+1) \dots (n+1)]$ are new distinct substring formed, and there count is $n + 1 - \pi_{max}$.

   This algorithm has time complexity $O(n^2)$.
   
   ```c++
   int max_prefix_function(string& s)
   {
       int n = s.length();
       vector<int> pi(n);
       int res = 0;
       for(int i = 1; i < n; i++)
       {
           int j = pi[i-1];
           while(j > 0 && s[i] != s[j])
               j = pi[j-1];
           if(s[i] == s[j])
               j++;
           pi[i] = j;
           res = max(p[i], res);
       }
       return res;
   }
   
   int distinct_strings(string& s)
   {
       int n = s.length();
       int res = 0;
       string curr = "";
       for(int i = n-1; i >= 0; i--)
       {
           curr = s[i] + curr;
           int pi_max = max_prefix_function(curr);
           res += (i + 1 - pi_max);
       }
       return res;
   }
   ```
   

Lets look at some interesting problems using Prefix-Function.

[Minimum Insertions In The Front To Make String Palindromic](https://practice.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/1)

**Statement:** Given string str of length N. The task is to find the minimum characters to be added at the front to make string palindrome.

**Solution:** the idea is that suppose we add $x$ elements in the start and now $x + s$ is palindromic. Lets say $x = 3$, which means that $x$ matches with last $3$ elements of $x$, this also means sub string from $s[0]$ to $s[s.length() - 3 - 1$] is palindromic in itself. Hence we need to find maximum length of prefix of $s$ which is palindromic, to find this in linear time we can use $lps$, first we reverse the string and add it to itself, then we simply calculate $lps$ array and find $lps$ for index $2 * n - 1$. Note if $lps[2*n-1]$ is more than n this means entire string is palindromic.

```c++
int minChar(string s)
{
    int n = s.length();
    string temp = s;
    reverse(temp.begin(), temp.end());
    s += temp;
    vector<int> pi(2*n);
    for(int i = 1; i < n; i++)
    {
        int j = pi[i-1];
        while(j > 0 && s[i] != s[j])
            j = pi[j-1];
        if(s[i] == s[j])
            j++;
        pi[i] = j;
    }
    
    int res = n - pi[2*n-1];
    return max(res, 0);
}
```