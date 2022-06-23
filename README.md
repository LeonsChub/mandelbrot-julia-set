# mandelbrot-julia-set

This is a Mandelbrot/Julia set explorer 

Both patterns can be computed via iterating the expression, (Z_(n+1) = (Z_(n))^2 + C) in the complex plane to the desired approximation. When Z's distance from the origin is bigger than 2, the expression has been proven to "shoot out" exponentially. When passing this threshold, we know that it will never return back to the bounds of the set, in which case we paint this infinitesimal region in a color appropriate to when it shot out. Otherwise we paint it black meaning it collapsed on a single value or is oscillating between values (such as Z_(1) = -1).

run the main.py program, to explore the Mandelbrot set via dragging the mouse, and scrolling in and out.
run the Julia-sets.py to generate Julia sets (duh) by clicking on any point on the screen and an appropriate Julia set will be drawn


usage:

example $python main.py -pallete


avilable palletes:
    fire
    green
    alternate
