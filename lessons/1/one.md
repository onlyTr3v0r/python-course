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
One thing to note: in python, you can write comments to explain pieces of code! These are marked by a `#` and are ignored by the python interpreter (code runner), and are used to explain the code that you write.

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

## Types

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
string_type = type(a_string) # We can assign the type of a variable to another variable
print(string_type)
# >> <class 'str'>

an_int = 18
print(type(a_string))
# >> <class 'int'>
```

## Functions

In the example in the previous section, we use a *function*. Functions are fundamental aspects of programming. They allow the programmer to break the flow of the program and run code, or perform operations on variables (or program data).

For example: take this basic function example..

```python
def say_hello():
    print("Hello world!")

say_hello() # >> Hello, world!
```

When the python *interpreter* ('code runner') sees the line `say_hello()`, it jumps *execution* (the lines of code it is currently running) to the *function body* (`print("Hello, world!")`).

As you can see from the example above, functions are defined in the following manner:

```python
def <function name>(<arguments, if any>):
    <body>
```

First, you start with the `def` (short for 'define') keyword. This is followed by the function's name, which follows the same rules as variable names, as listed above. Then, you have a pair of parenthesises (`()`), which can optionally contain arguments. These will be covered in more detail in the next lesson, but, in short, arguments allow the user to pass variables into functions when that function is *called* (executed). The parenthesis are followed by a colon (`:`). And finally, there is a *function body*, which is the code that will be run when the function is called. Note: the code in the body is indented (usually by 4 spaces or 1 tab - which is used is preference but 4 spaces is considered the standard). This is a very important aspect of python: the scope (what part of code a *statement* belongs to) a *statement* (line of code) belongs to is controlled by how *indented* it is, or how many spaces there are before it.

This line of code (beginning with `def` and ending with the colon, `:`) is known as the function *signature*. It tells the programmer, or anyone reading the code what the function *is* and defines it - for example, it gives its name (`<function_name>`) and the different arguments (`<arguments, if any`).

For example: (you will learn about `if` and `!=` later on)

```python
print("Hello!") # Global scope (not indented)

def say_hello(name):
    print("Hello from function") # Indented once
    if name != "":
        print("Hello, " + name) # Indented twice
    else:
        print("Please pass in a name")
```

If you want code to be part of a function, it must be on the same level of indentation as other code in the function:

```python
def correct():
    print("This statement will be executed in a function")
    print("And so will this!")

def incorrect():
    print("This statement will be executed in a function")
print("But this won't")
```

Also note that only code in *global scope* (not indented) will be executed *unconditionally*^[2]^ (will always be executed) by the python interpreter.

^[2]^ This is technically not true (ex. calling `sys.exit()` stops execution) but is good enough for a basic understanding.

Functions are called by entering their name, followed again with parenthesis, containing any arguments.

```python
def hello_world():
    print("Hello, world")


def hello_person(name):
    print("Hello, " + name)

hello_world() # >> Hello, world
hello_person("Bobirty") # >> Hello, Bobirty
```

The number of arguments passed to a function must match the number of arguments declared in the function's signature. For example, the following snippet of code would error:

```python
def hello_person(name):
    print("Hello, " + name)

hello_person()
# Results in error:
# "hello_person() missing 1 required positional argument: 'name'"
```

Likewise, the following code would fail similarly:

```python
def hello_world():
    print("Hello, world")

hello_world("Bobirty")
# Results in error:
# "hello_world() takes 0 positional arguments but 1 was given"
```

Finally, functions can also *return* values. This will place the value returned by the function where it was called. For example:

```python
def generate_hello_message(name):
    return "Hello, " + name


msg = generate_hello_message("Bobirty")
print(msg)
```

Results in:

```python
msg = "Hello, Bobirty"
print(msg)
```

(This can obviously be shortened to: `print(generate_hello_message("Bobirty"))`)

Functions can return any type.

If the return statement has no value (`return` on it's own), or there is no return value in the function body, like in this example:

```python
def hello():
    print("Hello!")
    # Note there is no return statement in this function body
```

The function will implicitly return `None`.

## Control Flow

The final skill we will cover in this lesson is control flow. Control flow allows your program to perform different things based on the values of variables. The most basic form of control flow is `if`.

The `if` keyword was used briefly in an example above. The formal syntax is as follows:

```python
if <condition>:
    <body if true>
```

Note the indentation around `<body if true>` - this follows the same principle as functions, as described above. The `<body if true>` can be any collection of statements, again, the same as a function's body. This can be read in English as "if condition 1 is true, execute 'body if true'"

The condition, broadly speaking, can be any *expression* (code that evaluates to a value). If the expression *evaluates* (can be turned into) to `True`, or a value such that `bool(value)` is `True`, then the `<body>` will be executed. Examples of conditionals will be covered in greater depth later.

The `elif` keyword partners with `if` keyword. It is short for 'else if', and works in a predictable manner. The syntax is like follows:

```python
if <condition 1>:
    <body 1>
elif <condition 2>:
    <body 2>
```

The python interpreter will read the blocks line by line. One could read this, in English, as "if 'condition 1' is true, execute 'body 1'. If not (else if) 'condition 2' is true, execute 'body 2'".

Note: this means `<body 2>` will only execute if `<condition 2>` is True **and** `<condition 1>` if False - if `<condition 1>` was true, `<body 1>` would be executed before `<condition 2>` has as chance to be evaluated (and thus, if true, `<body 2>` executed). This property is known as *short-circuiting*^[4]^. If you want to avoid this behaviour, you can turn the `elif` keyword into an `if` keyword - then its corresponding condition and body will be evaluated and (if true) executed regardless if `<condition 1>` evaluates to `True` or not.

^[4]^ The term *short-circuiting* is normally used to describe a similar phenomena occurring with *logical operators*, as will be discussed later. However it is still applicable here.

You can chain `elif`s together, like so:

```python
if <condition 1>:
    <body 1>
elif <condition 2>:
    <body 2>
elif <condition 3>:
    <body 3>
[..]
```

This can go on indefinitely. When writing long `elif` chains, keep short-circuiting in mind, as it *may* result in unexpected behaviour.

Finally, there is the `else` keyword. The `else` keyword can optionally **follow** an `if` or a chain of `elif`s. `else` takes no `<condition>`, and is executed as a 'fallback' - only if all other `<condition>`s (of either `if` or `elif`) evaluate to `False`.

### Conditionals

Conditions are used widely in python (+ in other languages) - most commonly in `if` or `elif` statements. As explained above, they are *expressions* that *resolve* or *evaluate* to either `True` or `False`.

Variables always evaluate to `True` unless they are: ^[4]^

- A false boolean (`False`)

- An empty string (`""`)

- The integer or float 0 (`0`, `0.0`)

- An empty iterable - covered in a later lesson (`[]`, `{}`, `()`)

- The null type (`None`)

^[4]^ There are a few other cases where a variable evaluates to `False` - notably, any instance of a class whose `__bool__` or `__len__` methods (`__bool__` takes priority) return any value that evaluates to `False` (this is *recursive*). You can follow this rule for the above values; `"".__len__() == 0`, `0.__bool__() == False`, with `False` being the final evaluation. However, the above examples are the most important to remember.

Variables are evaluated to a boolean implicitly when used in *constructs* (statements) like `if` and `elif`, however this can be done manually by calling `bool(<variable>)`. 

Conditions can be combined with *logical operators*. The available logical operators are:

- `not <op1>` (reverses the boolean value of `<op1>` - ie. `True` -> `False` & `False` -> `True`)

- `<op1> and <op2>` (`True` if **both** `<op1>` and `<op2>` evaluate to `True`)

- `<op1> or <op2>` (`True` if at **least** one the *operands* evaluates to `True`)

Note: *short-circuiting* (discussed above) applies here too. In short, if `<op1>` evaluates to `True`, the python interpreter won't check if `<op2>` is `True`, and will evaluate the entire expression to `True`. While normally unimportant, this can lead to some difficult-to-track-down bugs, so is worth bearing in mind.

### Iteration

More advanced *iteration* (repeating things) will be covered later on during the course, but a basic understanding of looping is prerequisite to understanding the basic pygame code that will be introduced later on.

There are 2 types of looping: first is the `for` statement. The `for` keyword allows you to loop over the *elements* (values inside an iterable) of an *iterable* (a type of variable that contains multiple other variables, ex. lists). The syntax is as follows:

```python
for <variable name> in <iterable>:
    <body>
```

For every element in `<iterable>`, a variable named `<variable name>` will be created and assigned the value of the element. Then, body will be executed. (note: body is, again, indented), and the process will be repeated for all elements of `<iterable>`.

For example (again, lists will be covered later on, just know that `numbers` contains a list of numbers):

```python
numbers = [3, 5, 2, 7]
for num in numbers:
    print(num)

>> 3
>> 5
>> 2
>> 7
```

The next form of iteration is the `while` statement. The while statement repeats a block of code until a condition turns `False`. The syntax is as follows:

```python
while <condition>:
    <body>
```

If `<condition>` evaluates to `False` when the `while` statement is declared, the loop body will not be executed. 

Note: the opposite behaviour (the body is executed, then the condition is checked) is known as a `do-while` block in other languages, and can be emulated in python as follows:

```python
while True:
    <body>

    if <condition>:
        break
```

Note: since the constant value `True` will never change, and, of course, always evaluates to `True` and results in an infinite loop - this can only be exited with `break`, as shown above and explained below.

## Pygame

If you have gotten this far: congratulations! This has been a crash into python & programming basics, and we can now move onto utilising these skills to build our Snake game.

Create a new folder, and name it `main.py`. The first thing we need to is import the libraries we will be using. Add this to the top of the file:

```python
import pygame
```

You will learn more about `import` in the next lesson, but understand for now it brings variables and functions from other files of code into the code you are writing. For example, the second line brings the main pygame `module` into *scope*.

Next, we will make some *constant* variables (by naming them in UPPER_CASE) to hold some configuration data. Append the following lines to your file:

```python
WIDTH, HEIGHT = SCR_DIM = 800, 800
FPS = 5
```

The first line uses some variable declaration syntax which we have not yet covered (but we will, when we cover iterables). Just know it creates 2 variables name `WIDTH` and `HEIGHT`, both with the value `800` and another *tuple* (a type of list) containing the value `(800, 800)`.

Next, we are going to initialise pygame, and some pygame variables that we can use to open a window.

```python
pygame.init()
screen = pygame.display.set_mode(SCR_DIM)
pygame.display.set_name("Python Course")
clock = pygame.time.Clock()
```

This first line initialises pygame by calling an `init()` *function*, and is required by every pygame program. Next, we create a very important variable named `screen`. This creates our game's window, and is where we will draw our snake, and other game components. We also call a pygame function to change the name of the newly created window to something appropriate - feel free to choose another name! On the final line of this addition we create a `clock` variable - this will be used to control the *framerate* (how fast the game re-draws its screen) of the game.

If you run the code now, you might see a glimpse of a window, as it is created and subsequently (and very quickly) destroyed. This happens because the python interpreter runs code very fast,^[5]^ so as soon as the window is created by the `set_mode`call the program ends, and the window is closed again. To fix this, add the following lines of code:

^[5]^ ..ish

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

There's a lot to unpack now!

Firstly, we create a variable named `running`. This will store whether the game has ended or not (and thus, if it is still running). We then define a `while` loop, that will execute the code block beneath it until the variable `running` is set to `False`.

Inside the loop, we define a `for` loop. This exposes a fundamental concept of pygame - the event loop. Every time an *event* is registered by pygame, it is added to a list of all other events that have occurred since the last frame. An event is any action that has occurred since the last frame - for example, a key being pressed or the window being closed. We can access this list of events by calling `pygame.event.get()`, and loop over it with the `for event in pygame.event.get():` line shown above.

Next, we use an `if` check to check if the *type* of event is `pygame.QUIT`. You can use the `.` notation to access a *property* of a variable - which is basically a variable contained by another variable. We will discuss the in more depth later in the course. Also note that the `type` *attribute* (property) of an `Event` *doesn't* represent the type of the variable, in terms of what kind of data it holds. It simply tells us that the event is a message to say "The user has closed the window" (usually by clicking the `X` on the title bar). When we get this 'message', we set the `running` variable to `False` - as discussed above this stops the `while` loop from executed the loop's body, and thus will stop the program's execution. When the loop is broken out of, the `pygame.quit()` function will be called. Just as we initialised the pygame module, we must also quit it once we have stopped our game.

The final step to get our basic window up & running is to call add a few more function calls.

```python
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        [...]

    pygame.display.flip()
    clock.tick(FPS)
```

The first addition is `screen.fill()`. This function fills the screen with a given RGB colour value. This is used to 'reset' the screen back to a base value, so that the previous *frame* (image drawn to the screen) is cleared. The value we pass is a *tuple* (type of list) with 3 integer elements - they represent the colour to fill the screen with in RGB form. If you want to expirment with these colour codes, look at [this site](https://rgbacolorpicker.com/). Notice as how you move the dot around, the 3 colour values change. (note: you can ignore the *alpha value* - this refers to transparency and is not needed in this course). We fill our screen with `(255, 255, 255)` - pure white.

The next addition is `pygame.display.flip()`. This function pushes all changes made to the screen since it was last called to the visible window. Right now, this just paints it white, but later on this call will also paint everything else. Finally, we call `clock.tick(FPS)`. This pauses code execution for the right amount of time so that the game runs at the given `FPS` - for us that is `5` (the game will update 5 times every second).

Now, if you run the file, you will be able to see a blank, white window. If you click the `X` to close the window, the program will exit gracefully!

With this done, the first lesson of the course is concluded. This has covered the basics of python & programming, which we have used to make a window draw to the screen. We will expand on the concepts and code covered here in future lessons to build up our game!
