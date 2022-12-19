# Python Course

## Targets

Must include:

[X] Variables & types
[X] Control flow
[X] Functions
[X] Basic (ish) OOP

[X] Modules / code splitting

[ ] I/O or user input

It should be:

- Non-trivial
- Simple enough for beginners to learn in 5/6 hours
- Decently fun & engaging
- Something tangible as an end result

## Stages

| Lesson | Concept                         | Result                                                                                       | Explanation                                                                                                                                                                                                                                             |
| ------ | ------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | Variables / types, control flow | Basic pygame boilerplate, a visible window                                                   | Foundational python concepts - an understanding of variables and control flow                                                                                                                                                                           |
| 2      | Functions, modules              | A better understanding of modules & how to use functions, arguments                          | Beginning to use `pygame.Surface.blit` and `pygame.draw.rect` to display things on the screen                                                                                                                                                           |
| 3      | Lists, Looping & Apples         | Tiles being drawn to the screen (including FX, ie. stripes). Apples being randomly generated | This lesson focuses on iterables, and looping over them. Perhaps introduce dicts, sets and tuples (not used in course)?                                                                                                                                 |
| 4      | N/A                             | Player                                                                                       | This lesson does not teach new concepts, and instead consolidates concepts taught in previous lessons. They will code the player, including player movement. Note: the player is purely procedural, and segments are represented by tuples of positions |
| 5      | OOP & Code splitting            | Apples grow the snake. Finished product.                                                     | OOP skils are introduced by refactoring the previous code to demonstrate the advantages of OOP. Notably the player will be changed such that player segments are given classes, and the snake is given the colour effect.                               |

## Todo

- Consider removing exceptions and returning a boolean from `Player.update` as its a very minor use of exceptions so could prove more confusing than helpful
  On the flipside, error handling is a very important and fundemental aspect of programming, so it would be nice to mention it. Verdict: Retain the excpetion
  and decide whether to keep it whilst writing!

- When getting the last player tile in `Player.update`, mention that negative indexing
  (`iterable[-n]`) is equivalent to `iterable[len(iterable) - n]`

- Consider making the player less than (0.8) the width of the tiles for visual distinction & flair
