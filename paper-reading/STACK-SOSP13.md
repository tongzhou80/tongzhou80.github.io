# Towards Optimization-Safe Systems: Analyzing the Impact of Undefined Behavior

[Paper](https://people.csail.mit.edu/nickolai/papers/wang-stack.pdf)

Compilers can optimized assuming the programs have no certain UBs, such as assuming `*p` implies `p` will always be non-NULL, or assuming `i+1 < i` is always false. It's legal for the compiler to do so.

There are many categories of undefined behaviors. Some UB are erroneous behaviors like buffer overflow and deferencing NULL pointers. Some are non-portable constructs, like bitwise shift and integer overflow. To enforce a uniform behavior over erroneous and non-portable constructs, the compiler would have to do extra checks like Java does, but C language is designed for low-level programming and efficiency first, so it relies on the programmer to write correct code.

# Undefined behavior examples

- Dereferencing NULL pointers

- Integer overflow (including division)
  - `INT_MIN / -1` can overflow too

- Buffer index out of bound

- Unsequenced modification
  - Two operations are unsequenced and operate the same scalar variable. One of them has side effects (write to the scalar). 
  - This one is gradually defined.
  - `i = ++i` is defined in C++11.
  - `i = i++` is defined in C++17.

# Algorithm for finding the well-defined program assumption (WDA)
To put it a simpler way, it tries to analyze when a statement `e` is reached, can it exhit UB. Let `R(e)` be the Boolean condition that makes `e` reachable, and `U(e)` be the condition that makes `e` exhibit UB, if `R(e)` and `U(e)` are both true for an input, then the program contains UB. The WDA is that when `R(e)` is true, `U(e)` must not be true. 

## Eliminating unreachable code
Trying to answer if reaching a statement requires triggering UB. If so the statement must be unreachable.
```
if R(e) is UNSAT:
	Remove(e)  # trivially unreachable
else:
	if R(e) && !U(e) is UNSAT:
	Remove(e)  # unreachble due to WDA
```

If `R(e) && !U(e)` is unsatisfiable, it means it's impossible for `e` to be both reachable and not triggering the UB condition. The means when `e` is reached, `U(e)` must be true.

# Some more comments
Java code is inherently slower than C because its more strict language specification (more strict memory model, less undefined behaviors) prevents the compiler from doing certain optimizations, like reordering statements, removing index-out-of-bound checks etc. There are also GC safepoint checks, deoptimization checks. Pretty much the only undefined behavior is Java is incorrectly synchronized programs (DRF0 model). Therefore, a well-tuned Java program is going to be somewhat slower than a well-tuned equivalent C program (not considering dynamic compilation advantage).

# How to solve this problem eventually?
For sure the programmers need to be more aware of UBs and the compilers should also warn wherever possible. However...

Some UB maybe difficult to check statically (like involving pointer analysis etc). The paper only modeled a few simple statements that can trigger UBs (Figure 3).

It's not realistic to understand the entire C specification.

Rust?
