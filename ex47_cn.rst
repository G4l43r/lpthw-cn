��ϰ 47: �Զ�������
******************************

Ϊ��ȷ����Ϸ�Ĺ����Ƿ�����, ����Ҫһ��һ����������Ϸ����������. ��������Ǻ�
���˷����. �����дһС�δ�������������Ĵ������Ǹ���? Ȼ��ֻҪ��Գ�������
�κ��޸�, ���������ʲô�¶���, ��ֻҪ"��һ����Ĳ���", ����Щ������ȷ�ϳ�����
Ȼ����ȷ����. ��Щ�Զ����Բ���ץ�����е�bug, ���������������ظ����������������
����, �Ӷ�Ϊ���Լ�ܶ�ʱ��.

����һ�¿�ʼ, �Ժ����ϰ��������"��Ӧ�ÿ����Ľ��"��һ��, ȡ����֮����һ��"��Ӧ
�ò��ԵĶ���"һ��. �����ڿ�ʼ, ����ҪΪ�Լ�д�����д���д�Զ�������, ���⽫����
��Ϊһ�����õĳ���Ա.

�Ҳ�����ͼ����Ϊʲô����Ҫд�Զ�������. ��Ҫ���������, ����Ҫ��Ϊһ������Ա, ��
������������������߷��Ĺ����Զ���. ����������������������߷���, �����㻹��д��
��������Ϊ����Եĸ���. 

��Ӧ��������Ҫ�����еĽ�����. ��Ϊ*��*д��Ԫ���Ե�ԭ��������Ĵ��Ը���ǿ��. ���
���Ȿ��, д�˺ܶ����������ʵ��һЩ����. �����㽫����һ��, д��������д������
����Ĵ���. ���д���������д����������Ĺ��̽�*ǿ��*������������֮ǰд�Ĵ���. 
���������������˽���д�Ĵ���ʵ�ֵĹ��ܼ���ԭ��, ���������ϸ�ڵ�ע�����һ��̨��.


׫д��������
===================

���ǽ���һ�ηǳ��򵥵Ĵ���Ϊ��, дһ���򵥵Ĳ���. ���ǽ�
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

