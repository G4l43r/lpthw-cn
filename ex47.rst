练习 47: 自动化测试
******************************

为了确认游戏的功能是否正常, 你需要一遍一遍地在你的游戏中输入命令. 这个过程是很
让人烦躁的. 如果能写一小段代码用来测试你的代码岂不是更好? 然后只要你对程序做了
任何修改, 或者添加了什么新东西, 你只要"跑一下你的测试", 而这些测试能确认程序依
然能正确运行. 这些自动测试不会抓到所有的bug, 但可以让你无需重复输入命令运行你的
代码, 从而为你节约很多时间.

从这一章开始, 以后的练习将不会有"你应该看到的结果"这一节, 取而代之的是一个"你应
该测试的东西"一节. 从现在开始, 你需要为自己写的所有代码写自动化测试, 而这将让你
成为一个更好的程序员.

我不会试图解释为什么你需要写自动化测试. 我要告诉你的是, 你想要成为一个程序员, 而
程序的作用是让无聊冗繁的工作自动化. 测试软件毫无疑问是无聊冗繁的, 所以你还是写点
代码让它为你测试的更好. 

这应该是你需要的所有的解释了. 因为*你*写单元测试的原因是让你的大脑更加强健. 你读
了这本书, 写了很多代码让它们实现一些事情. 现在你将更进一步, 写出懂得你写的其他
代码的代码. 这个写代码测试你写的其他代码的过程将*强迫*你清楚的理解你之前写的代码. 
这会让你更清晰地了解你写的代码实现的功能及其原理, 而且让你对细节的注意更上一个台阶.


撰写测试用例
===================

我们将拿一段非常简单的代码为例, 写一个简单的测试. 我们将
We're going to take a very simple piece of code and write one simple test.  We're
going to base this little test on a new project from your project skeleton.

First, make a ``ex47`` project from your project skeleton.  Make sure you
do it right and rename the module and get that first ``tests/ex47_tests.py`` test
file going right.  Also make sure nose runs this test file.  *IMPORTANT* make sure you
also delete ``tests/skel_tests.pyc`` if it's there.

Next, create a simple file ``ex47/game.py`` where you can put the code to test.
This will be a very silly little class that we want to test with this code
in it:

.. literalinclude:: ex/ex47.py
    :linenos:

Once you have that file, change unit test skeleton to this:

.. literalinclude:: ex/ex47_tests.py
    :linenos:

This file imports the ``Room`` class you made in the ``ex47.game``
module so that you can do tests on it.  There are then a set of tests that are functions
starting with ``test_``.  Inside each test case there's a bit of code that makes
a Room or a set of Rooms, and then makes sure the rooms work the way you expect them
to work.  It tests out the basic room features, then the paths, then tries out a whole
map.

The important functions here are ``assert_equal`` which makes sure that variables
you have set or paths you have built in a ``Room`` are actually what you think they are.
If you get the wrong result, then ``nosetests`` will print out an error message
so you can go figure it out.


Testing Guidelines
==================

Follow these general loose set of guidelines when making your tests:

1. Test files go in ``tests/`` and are named ``BLAH_tests.py`` otherwise ``nosetests``
   won't run them.  This also keeps your tests from clashing with your other code.
2. Write one test file for each module you make.
3. Keep your test cases (functions) short, but do not worry if they are a bit
   messy.  Test cases are usually kind of messy.
4. Even though test cases are messy, try to keep them clean and remove any repetitive
   code you can.  Create helper functions that get rid of duplicate code.  You will thank
   me later when you make a change and then have to change your tests.  Duplicated
   code will make changing your tests more difficult.
5. Finally, do not get too attached to your tests.  Sometimes, the best way to redesign
   something is to just delete it, the tests, and start over.


What You Should See
===================

.. literalinclude:: ex/ex47.txt

That's what you should see if everything is working right.  Try causing an error to see what
that looks like and then fix it.

Extra Credit
============


1. Go read about nosetests more, and also read about alternatives.
2. Learn about Python's "doc tests" and see if you like them better.
3. Make your Room more advanced, and then use it to rebuild your game yet again
   but this time, unit test as you go.

