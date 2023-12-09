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

## Day 4
Let's be honest, I could've used some regexs again, but regular ol' string comprehension is perfectly cromulent in this application. Nice and straightforward one today.

### Benchmarking
We got into a bit of a competition at work, so I updated with a max speedy version.

## Day 5
Part 1 🌞
Part 2 🌋

SO MANY SLICING ERRORS. I hate this. This was not good for my mental health.

Oh, Python3.12 is now the minimum required version due to use of `batched()` from itertools. 

## Day 6
What kinda rollercoaster are we on, this was nice and easy.

## Day 7
Not hard, but lot's of edge cases, and honestly it looks a bit ugly.

## Day 8
This was easy enough, but I'm annoyed by the supposedly smart shortcut one can take for part 2. I feel it's highly dependant on how the input data was engineered rather than being a general solution. So it's more enforced luck rather than algorithmic chops. It's not the first time they've had this sort of solution on AoC, but it just feels extra contrived this time.

## Day 9
Today was pretty trivial, even part 2 was only mildly tricksy.