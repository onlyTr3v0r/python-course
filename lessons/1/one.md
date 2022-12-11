# Lesson 1

~ Variables, types & control flow

This lesson will cover variable declaration syntax, common types, `if`, `elif` and `else`

We will produce a blank window which will be the basis of our game.

## Variables

*Variables* are possibly the most important concept in programming. They are the building blocks of all programs.
Variables store data. This data has a specified *type*.

You can think of variables like digital boxes. A box is labelled and is used to store [TODO: better term] data. You can open a box and look at, or change^[1]^ its contents at any time. Boxes come in different shapes and sizes, each containing a different type of [TODO: As above] data.
Similarly, variables have a name, store data, have a type that matches the data they store and can be read from and written to.

^[1]^ Some variables cannot be changed - these variables are known as *immutable*. You can think of these variables as data in a display cabinet - although you can look at the data, you cannot change it!
A variable's ability to be changed (or not) is known as *mutability*. All variables in Python are mutable - however, by convention, Python variables named in UPPER_CASE should not be re-assigned to.
Other languages do feature immutable variables (often through keywords like `const` or `final`) that will crash if you *do* attempt to re-assign to them.

Let's write some code!

Variables in python are declared with the following syntax:

```python
<variable name> = <variable value>
```

There are various variable naming rules:

- They should be written in snake_case (ex. `variable`, `my_long_variable_name`)
- They should begin with a letter, a number or an underscore (_)
- They must only contain alphanumeric characters (no white-space)

This means variables like `10variable`, `variable-name` or `variable name` are all invalid.

Note:
Variables are *case sensitive*, meaning `myvariable`, `MyVariable` and `MYVARIABLE` are all different.

```python
full_name = "Bobirty Quandale"
likes_python = True
favourite_number = 18
```

Once a variable has been created, its value can be changed:

```python
knows_python = False
name = "You"
knows_python = True
```

.. And so can its type!

```python
x = "A string!"
x = 18
```

Every variable has a *type*. A variable's type is the kind of data it can hold.

Some common types are shown below:

```python
a_string = "Bobirty" # Holds text or characters, You can use single or double quotes ("text" or 'text')
an_integer = 18      # Holds whole numbers (no decimals). Can be of any size, and negative
a_float = 1.8        # Holds a number, with decimals
a_bool = True        # Holds a true or false value
none = None          # None is an exception - it represents the abscense of a value
```

Note, there are *hundreds* of types built-in to Python, and you can create your own, as will be discussed later in the course. However, these are the main ones you need to know.

You can get a variable's type with the `type()` function:

```python
a_string = "Hello!"
string_type = type(a_string)
print(string_type)
# >> <class 'str'>

an_int = 18
print(type(a_string))
# >> <class 'int'>
```

You will learn more about functions and printing later on!

## TODO

- `if` / `elif` / `else`
- `print()`
- basic functions
- pygame
- comment syntax
