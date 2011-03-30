Exercise 5: More Variables And Printing
***************************************

Now we'll do even more typing of variables and printing them out.  This time
we'll use something called a "format string".  Every time you put ``"``
(double-quotes) around a piece of text you have been making a *string*.  A string
is how you make something that your program might give to a human.  You print
them, save them to files, send them to web servers, all sorts of things.

Strings are really handy, so in this exercise you will learn how to
make strings that have variables embedded in them.  You embed variables
inside a string by using specialized format sequences and then putting
the variables at the end with a special syntax that tells Python, "Hey,
this is a format string, put these variables in there."

As usual, just type this in even if you do not understand it and make it
exactly the same.

.. literalinclude:: ex/ex5.py
    :linenos:


What You Should See
===================

.. literalinclude:: ex/ex5.txt



Extra Credit
============

1. Change all the variables so there isn't the ``my_`` in front.  
   Make sure you change the name everywhere, not just where you used ``=`` to set them.
2. Try more format characters.  ``%r`` is a very useful one.  It's like saying "print this no matter what".
3. Search online for all of the Python format characters.
4. Try to write some variables that convert the inches and pounds to centimeters and kilos.
   Do not just type in the measurements. Work out the math in Python.


