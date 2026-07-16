# Algorithms & Data Structures Log

🔗 **Live Demo:** [algorithms-log demo](https://apega-tech.github.io/algorithms-log/) — runs the actual Python solutions in your browser via Pyodide

A running collection of classic algorithm and data structure problems,
solved in both Python and Java, with short write-ups on the approach and
complexity. Built to demonstrate core CS fundamentals — the kind of
problems that come up in technical interviews and in coursework (Data
Structures & Algorithms, OOP).

## Python (`/python`)
| Problem | Concept | Time | Space |
|---|---|---|---|
| `two_sum.py` | Hash map lookup | O(n) | O(n) |
| `valid_parentheses.py` | Stack | O(n) | O(n) |
| `binary_search.py` | Divide and conquer | O(log n) | O(1) |
| `max_subarray.py` | Kadane's algorithm (DP) | O(n) | O(1) |
| `reverse_linked_list.py` | Linked list pointer manipulation | O(n) | O(1) |

Run any file directly, e.g.:
```bash
python two_sum.py
```
Each file includes inline assertions that double as tests — "All tests
passed." means it works.

## Java (`/java`)
| Problem | Concept |
|---|---|
| `FizzBuzz.java` | Control flow / modulo logic |
| `BubbleSort.java` | Sorting, O(n²) with early-exit optimization |
| `BinarySearchTree.java` | Recursion, OOP, tree structures |

Compile and run, e.g.:
```bash
javac BinarySearchTree.java
java BinarySearchTree
```

## Why this repo
This is meant to be an ongoing log, not a one-time submission — I'll add
new problems here as I work through more of the Data Structures &
Algorithms coursework in my CS program. It's also meant to show range:
Python for quick, readable solutions; Java for practicing stricter OOP
structure.

## Possible next steps
- Add more problems (recursion, dynamic programming, graphs)
- Add a difficulty tag and a short "what I'd optimize next" note per file
- Set up a GitHub Action to auto-run the Python tests on push
