The Setup
*********

This exercise has no code.  It is simply the exercise you complete in order
to get your computer setup to run Python.  Because this is a simple book
we'll assume you're using a Mac OSX computer.  Later versions of this book
will have instructions for Windows and Linux computers.

To complete this exercise you have to finish the following tasks:

1. Go to http://learningpythonthehardway.org/wiki/ExerciseZero with your browser and get
   the ``gedit`` text editor.
2. Put gedit (your editor) in your Dock so you can reach it easily.
3. Find your "Terminal" program.  Search for it.  You'll find it.
4. Put your Terminal in your Dock as well.
5. Run your Terminal program.  It won't look like much.
6. In your Terminal program, run ``python``.  You run
   things in Terminal by just typing their name and hitting RETURN.
7. Hit CTRL-D (^D) and get out of python.
8. You should be back at a prompt similar to what you had before you typed ``python``.  If not find out why.
9. Learn how to make a directory in the Terminal.  Search online for help.
10. Learn how to change into a directory in the Terminal.  Again search online.
11. Use your editor to create a file in this directory.  Typically you
    will make the file and then "Save" or "Save As.." and pick this directory.
12. Go back to Terminal using just the keyboard to switch windows.  Look it
    up if you can't figure it out.
13. Back in Terminal see if you can list the directory to see your 
    newly created file.  Search online for how to list a directory.

You're done with this exercise.  This exercise could actually be hard for you
depending on your familiarity with your computer.  If it is difficult, then
take the time to read and study and get through it, because until you can do
these very basic things you'll find it difficult to get much programming done.


What You Should See
===================

Here's me doing the above on my computer in Terminal.  Your computer would be
different, so see if you can figure out all the differences between what I did
and what you should do.  Notice I use a text editor called ``vim``.  You shouldn't
use it, it's too hard to use for you right now.

.. code-block:: bash
    
    Last login: Sat Apr 24 00:56:54 on ttys001
    ~ $ python
    Python 2.5.1 (r251:54863, Feb  6 2009, 19:02:12) 
    [GCC 4.0.1 (Apple Inc. build 5465)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> ^D
    ~ $ mkdir mystuff
    ~ $ cd mystuff
    mystuff $ ls
    mystuff $ vim test.txt
    mystuff $ ls
    test.txt
    mystuff $ 


If a programmer tells you to use ``vim`` or ``emacs`` tell them no.  These
editors are for when you are a better programmer.  All you need right now
is an editor that lets you put text into a file.

