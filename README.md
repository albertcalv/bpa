# BPA Algorithms

Implementation of Best Position Algorithms in python 3.5

## Fagin's Algorithm  
Compute the aggregated rank of k items

PRE:
+ List of list of tuples <tag, value>.
+ Lists of same lenght
+ k num of items in the solution, if k is not specified it's done by Naïve Algorithm (All tuples are ranked).

```
List = List 1 + List 2 + ... + List M
      Every list consist on <tag, value>
```

POST:
+ List of scoring

```
List = <tag, score> ... <tag _k, score_k>

```

## Future Work  

```
- Add dataframes to improve performance

```



## References
The implementation is based on the following paper:

[1] Reza Akbarinia, Esther Pacitti, Patrick Valduriez. Best Position Algorithms for Top-k Queries.
ACM. International Conference on Very Large Data Bases (VLDB), Aug 2007, Vienna, Austria.
ACM, pp.495-506, 2007. <inria-00378836>
