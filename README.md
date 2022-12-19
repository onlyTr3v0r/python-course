# Python Course

A python course where participants build a clone of snake

WIP, README and repo will be updated as I write the course!

## Todo

- Consider removing exceptions and returning a boolean from `Player.update` as its a very minor use of exceptions so could prove more confusing than helpful
  On the flipside, error handling is a very important and fundemental aspect of programming, so it would be nice to mention it. Verdict: Retain the excpetion
  and decide whether to keep it whilst writing!

- When getting the last player tile in `Player.update`, mention that negative indexing
  (`iterable[-n]`) is equivalent to `iterable[len(iterable) - n]`

- Consider making the player less than (0.8) the width of the tiles for visual distinction & flair

- Add basic stuff like concatenation, arithmetic operators, ect

- Casting (to & from `int` primarily)
