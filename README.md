# Project setup:

## Create venv in current directory:
`python3 -m venv ./venv`

## Activate venv:
`source venv/bin/activate`

# functional-programming

## Functional vs Procedural Programming vs OOP
### Procedural programming
Procedural programming is the most basic form of coding. 
Code is structured hierarchically into blocks (such as if statements, loops, and functions). 
It is arguably the simplest form of coding. 
However, it can be difficult to write and maintain large and complex software due to its lack 
of enforced structure.

### Functional programming
Functional programming (FP) uses functions as the main building blocks. 
Unlike procedural programming, the functional paradigm treats functions as 
objects that can be passed as parameters, allowing new functions to be 
built dynamically as the program executes.
Functional programming tends to be more declarative than imperative – 
your code defines what you want to happen, rather than stating exactly how 
the code should do it. Some FP languages don’t even contain constructs, such as 
loops or if statements. However, Python is more general-purpose and allows you to 
mix programming styles very easily.

### OOP
Object-oriented programming (OOP) structures code into objects. 
An object typically represents a real item in the program, such as a file or a
window on the screen, and it groups all the data and code associated with that 
item within a single software structure. Software is structured according to the 
relationships and interactions between different objects. Since objects are encapsulated, 
with well-defined behavior, and capable of being tested independently, 
it is much easier to write complex systems using OOP.

## Advantages of FP
- FP often creates less code
- Intent of the code is clearer
- There are often fewer bugs
- Code is potentially mathematically provable
- Multiprocessing can be applied easily


## FP vs OOP
### Disadvantages of FP
- Not all functions can be pure
- FP has a learning curve
- FP can be inefficient

### Advantages of OOP
- OOP is easier to understand
- OOP is easier to maintain
- OOP is easier to extend
- OOP is easier to debug
- OOP is easier to reuse
- OOP is easier to test

### Disadvantages of OOP
- OOP is slower
- OOP is more difficult to learn
- OOP is more difficult to design

# TO DO:
# ======
- The goal is to complete the exercises under folder `exercises`.
  1. `fibonacci` folder contains script `fibonacci_v1.py` which calculates fibonacci 
  of each number which is in list. The task is to create `fibonacci_v2.py` script witch would be more efficient.
  The basic problem in `fibonacci_v1.py` is that we are calling fibonacci function multiple times, with the same argument. 
  So, each time we are calculating the same value all over again.
  The goal is to use dictionary as a cache to store already calculated values. 
  Dictionary key would be the function argument. 
  2. `reverse_string` folder contains script `reverse_string_v1.py` which reverses string using while loop.
  The task is to create `reverse_string_v2.py` script which would do the same only using recursion instead of while loop.
  3. `remove_duplicated_chars` folder contains script `remove_duplicated_chars_v1.py` which removes duplicates from string using for each.
  The task is to create `remove_duplicated_chars_v2.py` script which would do the same only using recursion instead of for each.