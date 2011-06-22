Exercise 0: The Setup
*********************

This exercise has no code.  It is simply the exercise you complete
to get your computer setup to run Python.   You should follow these instructions
as exactly as possible.  For example, Mac OSX computers already have Python 2, so
do not install Python 3 (or any Python).


Mac OSX
=======

To complete this exercise, complete the following tasks:

1. Go to http://learnpythonthehardway.org/exercise0.html with your browser, get
   the ``gedit`` text editor, and install it.
2. Put gedit (your editor) in your Dock so you can reach
   it easily.

   a. Run gedit so we can fix some stupid defaults it has.
   b. Open ``Preferences`` from the ``gedit menu`` and select the ``Editor`` tab.
   c. Change ``Tab width:`` to 4.
   d. Select (make sure a check mark is in) ``Insert spaces instead of tabs``.
   e. Turn on "Automatic indentation" as well.
   f. Open the ``View`` tab and turn on "Display line numbers".

3. Find your "Terminal" program.  Search for it.  You will find it.
4. Put your Terminal in your Dock as well.
5. Run your Terminal program.  It won't look like much.
6. In your Terminal program, run ``python``.  You run
   things in Terminal by just typing their name and hitting RETURN.
7. Hit CTRL-D (^D) and get out of python.
8. You should be back at a prompt similar to what you had before you typed ``python``.  If not find out why.
9. Learn how to make a directory in the Terminal.  Search online for help.
10. Learn how to change into a directory in the Terminal.  Again search online.
11. Use your editor to create a file in this directory.  You
    will make the file, "Save" or "Save As...", and pick this directory.
12. Go back to Terminal using just the keyboard to switch windows.  Look it
    up if you can't figure it out.
13. Back in Terminal, see if you can list the directory to see your 
    newly created file.  Search online for how to list a directory.


.. note::

    If you have problems with gedit, which is possible with non-English
    keyboard layouts, then I suggest you try Textwrangler found
    at http://www.barebones.com/products/textwrangler/ instead.


OSX: What You Should See
------------------------

Here's me doing the above on my computer in Terminal.  Your computer would be
different, so see if you can figure out all the differences between what I did
and what you should do.

.. code-block:: console
    
    Last login: Sat Apr 24 00:56:54 on ttys001
    ~ $ python
    Python 2.5.1 (r251:54863, Feb  6 2009, 19:02:12) 
    [GCC 4.0.1 (Apple Inc. build 5465)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> ^D
    ~ $ mkdir mystuff
    ~ $ cd mystuff
    mystuff $ ls
    # ... Use Gedit here to edit test.txt....
    mystuff $ ls
    test.txt
    mystuff $ 

Windows
=======

.. note:: Contributed by zhmark.

1. Go to http://learnpythonthehardway.org/wiki/ExerciseZero with your browser, get
   the ``gedit`` text editor, and install it. You do not need to be administrator to do this.
2. Make sure you can get to ``gedit`` easily by putting it on your desktop and/or in
   ``Quick Launch``. Both options are available during setup.

   a. Run gedit so we can fix some stupid defaults it has.
   b. Open ``Edit->Preferences`` select the ``Editor`` tab.
   c. Change ``Tab width:`` to 4.
   d. Select (make sure a check mark is in) ``Insert spaces instead of tabs``.
   e. Turn on "Automatic indentation" as well.
   f. Open the ``View`` tab turn on "Display line numbers".

3. Find your "Terminal" program.  It's called ``Command Prompt``. Alternatively just run ``cmd``. 
4. Make a shortcut to it on your desktop and/or ``Quick Launch`` for your convenience.
5. Run your Terminal program.  It won't look like much.
6. In your Terminal program, run ``python``.  You run things in Terminal by just typing their 
   name and hitting RETURN.

   a. If you run ``python`` and it's not there (``python is not recognized..``).  Install it from http://python.org/download 
   b. *Make sure you install Python 2 not Python 3.*
   c. You may be better off with ActiveState Python especially when you miss Administrative rights

7. Hit CTRL-Z (^Z), ``Enter`` and get out of ``python``.
8. You should be back at a prompt similar to what you had before you typed ``python``.  If not find out why.
9. Learn how to make a directory in the Terminal.  Search online for help.
10. Learn how to change into a directory in the Terminal.  Again search online.
11. Use your editor to create a file in this directory.  Make the file, "Save" or "Save As...", and pick this directory.
12. Go back to Terminal using just the keyboard to switch windows.  Look it
    up if you can't figure it out.
13. Back in Terminal, see if you can list the directory to see your 
    newly created file.  Search online for how to list a directory.


.. warning::

    Windows is a big problem for Python.  Sometimes you install Python and one
    computer will have no problems, and another computer will be missing important
    features.  If you have problems, please visit: http://docs.python.org/faq/windows.html

Windows: What You Should See
----------------------------


.. code-block:: bat

    C:\Documents and Settings\you>python
    ActivePython 2.6.5.12 (ActiveState Software Inc.) based on
    Python 2.6.5 (r265:79063, Mar 20 2010, 14:22:52) [MSC v.1500 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> ^Z


    C:\Documents and Settings\you>mkdir mystuff

    C:\Documents and Settings\you>cd mystuff

    ... Here you would use gedit to make test.txt in mystuff ...

    C:\Documents and Settings\you\mystuff>
       <bunch of unimportant errors if you istalled it as non-admin - ignore them - hit Enter>
    C:\Documents and Settings\you\mystuff>dir
     Volume in drive C is
     Volume Serial Number is 085C-7E02

     Directory of C:\Documents and Settings\you\mystuff

    04.05.2010  23:32    <DIR>          .
    04.05.2010  23:32    <DIR>          ..
    04.05.2010  23:32                 6 test.txt
                   1 File(s)              6 bytes
                   2 Dir(s)  14 804 623 360 bytes free

    C:\Documents and Settings\you\mystuff> 

You will probably see a very different prompt, Python information, and other stuff but this is
the general idea.  If your system is different let us know at http://learnpythonthehardway.org
and we'll fix it.


Linux
=====

Linux is a varied operating system with a bunch of different ways to install software.
I'm assuming if you are running Linux then you know how to install packages so here are
your instructions:

1. Go to http://learnpythonthehardway.org/wiki/ExerciseZero with your browser, get
   the ``gedit`` text editor, and install it.
2. Make sure you can get to ``gedit`` easily
   by putting it in your window manager's menu.

   a. Run gedit so we can fix some stupid defaults it has.
   b. Open ``Preferences`` select the ``Editor`` tab.
   c. Change ``Tab width:`` to 4.
   d. Select (make sure a check mark is in) ``Insert spaces instead of tabs``.
   e. Turn on "Automatic indentation" as well.
   f. Open the ``View`` tab turn on "Display line numbers".

3. Find your "Terminal" program.  It could be called ``GNOME Terminal``, ``Konsole``, or ``xterm``.
4. Put your Terminal in your Dock as well.
5. Run your Terminal program.  It won't look like much.
6. In your Terminal program, run ``python``.  You run
   things in Terminal by just typing their name and hitting RETURN.

   a. If you run ``python`` and it's not there, install it.  *Make sure you install Python 2 not Python 3.*

7. Hit CTRL-D (^D) and get out of ``python``.
8. You should be back at a prompt similar to what you had before you typed ``python``.  If not find out why.
9. Learn how to make a directory in the Terminal.  Search online for help.
10. Learn how to change into a directory in the Terminal.  Again search online.
11. Use your editor to create a file in this directory.  Typically you
    will make the file, "Save" or "Save As..", and pick this directory.
12. Go back to Terminal using just the keyboard to switch windows.  Look it
    up if you can't figure it out.
13. Back in Terminal see if you can list the directory to see your 
    newly created file.  Search online for how to list a directory.


Linux: What You Should See
--------------------------


.. code-block:: console

    [~]$ python
    Python 2.6.5 (r265:79063, Apr  1 2010, 05:28:39)
    [GCC 4.4.3 20100316 (prerelease)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    [~]$ mkdir mystuff
    [~]$ cd mystuff
    # ... Use gedit here to edit test.txt ...
    [mystuff]$ ls
    test.txt
    [mystuff]$ 

You will probably see a very different prompt, Python information, and other stuff but this is
the general idea.


Warnings For Beginners
======================

You are done with this exercise.  This exercise might be hard for you
depending on your familiarity with your computer.  If it is difficult,
take the time to read and study and get through it, because until you can do
these very basic things you will find it difficult to get much programming done.

If a programmer tells you to use ``vim`` or ``emacs``, tell them, "No."  These
editors are for when you are a better programmer.  All you need right now
is an editor that lets you put text into a file.  We will use ``gedit`` because
it is simple and the same on all computers.  Professional programmers use
``gedit`` so it's good enough for you starting out.

A programmer may try to get you to install Python 3 and learn that.  You
should tell them, "When all of the python code on your computer is Python 3,
then I'll try to learn it."  That should keep them busy for about 10 years.

A programmer will eventually tell you to use Mac OSX or Linux.  If the programmer
likes fonts and typography, they'll tell you to get a Mac OSX computer.  If they
like control and have a huge beard, they'll tell you to install Linux.  Again,
use whatever computer you have right now that works.  All you need is ``gedit``,
a Terminal, and ``python``.

Finally the purpose of this setup is so you can do three things very reliably
while you work on the exercises:

1. *Write* exercises using ``gedit``.
2. *Run* the exercises you wrote.
3. *Fix* them when they are broken.
4. Repeat.

Anything else will only confuse you, so stick to the plan.

