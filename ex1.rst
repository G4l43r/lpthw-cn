Exercise 1: A Good First Program
********************************

Remember, you should have spent a good amount of time in Exercise 0 learning
how to install a text editor, run the text editor, run the Terminal, and
work with both of them.  If you haven't done that then don't go on, you'll
not have a good time.  This is the only time I'll start an exercise with a 
warning that you should not skip or get ahead of yourself.

.. literalinclude:: ex/ex1.py
    :linenos:

Take the above and type it into a single file named ``ex1.py``.  This is important
as python works best with files ending in ``.py``.

.. warning::

    Do not type the numbers on the far left of these lines.  Those are called
    "line numbers" and they're used by programmers to talk about what part of 
    a program is wrong.  Python will tell you errors related to these line numbers,
    but *you* do not type them in.


Then in Terminal you *run* the
file by typing:

.. code-block:: bash

    python ex1.py


If you did it right then you should see the same output I have below.  If not,
then you've done something wrong.  No, the computer is not wrong.

What You Should See
===================

.. literalinclude:: ex/ex1.txt

You may see the name of your directory before the ``$`` which is fine,
but if your output is not exactly the same, then find out why and fix it.

If you have an error it will look like this:

.. literalinclude:: ex/ex1.err
    :language: python
    :linenos:

It's important you be able to read these since you'll be making many of 
these mistakes.  Even I make many of these mistakes.  Let's look at this
line-by-line.

1. Here we ran our command in the terminal to run the ``ex1.py`` script.
2. Python then tells us that the file ``ex1.py`` has an error on line 3.
3. It then prints this line for us.
4. Then it puts a ``^`` (caret) character to point at where the problem is.
   Notice the missing ``"`` (double-quote) character?
5. Finally, it prints out a "SyntaxError" and tells us something about what might
   be the error.  Usually these are very cryptic, but if you copy that text into
   a search engine you'll find someone else who's had that error and you can probably
   figure out how to fix it.


Extra Credit
============

You will also have extra credit you should do to make sure you understand
each exercise.  For this exercise, try these things:

1. Make your script print another line.
2. Make your script print only one of the lines.
3. Put a '#' (octothorpe) character at the beginning of a line.  What did it do?
   Try to find out what this character does.

From now on, I won't explain how each exercise works unless an exercise is
different for some reason.  Each time there is code you should put in a new
file, the output you should see when you run the file in terminal, and 
extra credit you should do.


.. note::

    An 'octothorpe' is also called a 'pound', 'hash', 'mesh', or any number of names.  Pick the one that makes you chill out.
