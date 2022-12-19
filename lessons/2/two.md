not sure what to do in this lesson so just gonna write the code + explanations for drawing the backdrop and go from there.

## Non-scalar variables

*Non-scalar* refers to a variable's ability to hold multiple pieces of data at the same time. These are commonly known as lists or arrays.

In python there are 4 main types of non-scalar (iterable) variables.

- Lists

- Tuple

- Dictionary - stores key <-> value pairs

- Set - stores unique variables (least common)

We will focus on the first 2 - lists & tuples - as the others will not be used in this course, and are generally less commonly used. The differences between them are subtle, and, as a beginner, do not need to be memorised. However, their different properties do lead to some situations where certain types are preferable over others.

The differences between tuples and lists are:

- That tuples are **immutable** (cannot be changed) whereas lists are not. This means that once you create a tuple, you can neither add, remove nor change its elements. No similar limitation exists with lists.
  
  ```python
  a_list = [1, 2, 3, 4]
  a_list[0] = 10
  print(a_list)
  # >> [10, 2, 3, 4]
  
  a_tuple = (1, 2, 3, 4)
  a_tuple[0] = 10
  # Errors:
  # 'tuple' object does not support item assignment 
  ```
  
  You will receive similar errors if trying to add / delete elements.

- As shown above, the syntax for initialising tuples is also slightly different - tuples use round brackets (`()`) whereas lists use square brackets (`[]`). Both types can contain unlimited items, can contain items of any type and can contain elements with different types.

Every item an iterable type contains is known as an *element*. Elements can be accessed by *indexing* into the array. IMPORTANT! All iterables are *zero-indexed*, meaning that the first element has an index of 0, the second has an index of 1, ect. To generalise, the *n*-th element has an index of *n-1*.

The syntax is as follows:

```python
<variable>[<index>]
```

The index must be an integer (no decimal numbers).

```python
a_list = [1, "hey!"]
a_tuple = (False, 18, 34)
print(a_list[0]) # >> 1
print(a_list[1]) # >> hey!
print(a_tuple[0]) # >> False
print(a_tuple[2]) # >> 34
```

You can check if a non-scalar variable contains a value with the `in` and `not in` operators.

```python
a_list = ["fish", "waffle", "baguette", 100]

100 in a_list       # >> True
"cow" not in a_list # >> True
"fish" in a_list    # >> True
```

You also can loop non-scalar values with the `for .. in ..` syntax as mentioned earlier. For example:

```python
a_list = ["h", "e", "l", "l", "o", "!"]
for letter in a_list:
    print(letter)

# >> h
# >> e
# >> l
# >> l
# >> o
# >> !
```

The are some built-in functions to create lists for you - a common one is *range*. Range creates a list containing the numbers from `0` (inclusive) to `n` (exclusive).

```python
print(range(10))
# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

It is commonly used in `for` loops, like such:

```python
for number in range(3):
    print("Number is " + str(number)

# >> Number is 0
# >> Number is 1
# >> Number is 2
```

## Code

## Todo

- Destrucring

- `_` pattern in loops

- Code
