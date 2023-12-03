# Advent of Code 2023
Once more unto the breach.

Another year, and Python again!

## Day 1
No easy start this year, had a heck of a time catching the overlapping strings. I assumed that once a word-digit is detected those characters are invalidated for potentially overlapping words. That was not the case.

### Regex
I also decided to see if I could use regex to solve this, I cheated a little by using a third party regex lib, but then again I have better things to do with my life that figure out lookahead logic with regex.

## Day 2
Is it premature to break out some classes for this? This was a nice and easy one, or at least I was lucky enough with my initial approach that it was a trivial addition to get part 2.

## Day 3
Wow this is ugly, I tried being lazy by not splitting it up into an array, and now I pay for my hubris. Sub-substring matches are a pain. First submission is sphaghet, I'll see if I can make it prettier some time

### Regex Redux
Again it really feels like Regexs are the way to go. I've cleaned up a bit without changing my original approach, I don't *think* I can eliminate more for loops, but I don't want to spend more time on this now