# TurtleCrossing
Turtle Crossing completed on 'Expert mode'

Tortor capstone project

So I have been trying to complete the 'capstone projects' [which round off all that one's learned in the relevant section] by myself without any sort of guidance. 
The first was the coffee machine, the second was the turtle crossing. I did the project only by downloading the starting code [which had a few classes set up, but
not much else otherwise], and viewing how the game should play out. Which was basically:

  1. Move turtle to starting position
  2. Spawn cars on right hand side of screen, which them move left
  3. When turtle reaches top of screen increment level number display, reset turtle to starting position, increase car speed
  4. Detect collision with cars and game over if so
  
I feel that I could have done it myself, although I would have had to spend a little extra time on a few things I wasn't 100% on [timer, turtle.tracer(0), turtle.update().
Although when I consider these things in a vaccuum they're quite easy to understand. 

At first I was clearing the cars everytime the player levelled up. This introduced a bug where a black square would sit in the middle of the screen on level up. And 
I could not find a way to deal with it! turtle.hide(), turtle.move(), turtle.color(), you name it. It was the only thing which made me feel the project hadn't yet
been completed. But as it turned out I didn't have to clear the cars on level up, just increase their speed. So I refactored the code a bit to increase their speed 
[they were retaining their old speed on level up so there was a mix of car speeds between level ups] and that was that.

I don't believe I'm an 'expert level coder', but I do try to do these projects on my own since I feel it's good practice and it really helps with understanding stuff.
