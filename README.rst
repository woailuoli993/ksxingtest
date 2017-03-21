+++++++++++++++++
头一次写rst
+++++++++++++++++

:Authers: vici
:Version: 1.0 of 2017/3/20
:dedication: README To my test 

My first paragraph writen by restructuredText
is awsome...

     Where is  `e` ? Yes. It's awesome.

原因
：看到了鄙视链，latex 鄙视 restructuredText， 
restructuredText 鄙视 markdown

1. 醉了的时候需要自己写序号

#. time is short

    I. 123

    #. 1231 

- hoho
- xixi

* a bullet point using "*"
    - a sub list using "- "
        + sub-sub using"+ "
    - another using "-"

define
    定义一个东西就是辣么简单

*how* : step1
    tab 就阔以了？

code example::

    printf("Hello World!");
    echo "hola"


+++++++++++++++++
title 1
+++++++++++++++++


title 1.1
================

title 1.2
================

+++++++++++++++++
title 2
+++++++++++++++++

.. image:: https://v2ex.assets.uxengine.net/avatar/3fcf/1a54/218410_large.png?m=1488435213
    
`use "\`"`

我的博客_   --》 `就是我的博客内部链接`__

.. _我的博客: http://blog.heyuhua.com

__ 我的博客_

`python hyperlink <http://www.python.org>`_

*斜体* **黑提**  我的 ``内嵌`` 文字

我的头像 |substitution references|

.. |substitution references| image:: http://blog.heyuhua.com/img/tu_ruiwen_dead.jpg

有些放到最底下的东西（猪脚）like [1]_.



.. [1] 我已经可以写书了

但是好像不是最下面

“”“\`233`\”“”


usage of dockertags_:

.. _dockertags: shlltest/dockertages

-h      command-line help
-r      tree recursion


+--------------------------+-----------------------------------------------+
| `dockertages ubuntu`     |       list all tags of ubuntu                 |  
+--------------------------+-----------------------------------------------+
| `dockertags ubuntu 16`   |       list all ubuntu tags containing '16'    |  
+--------------------------+-----------------------------------------------+


| 我不想让你
| 换行，
| 你就不能
| 换行。
|       我让你干啥～
|   我就干啥

block quotes：
    indented 段落，
        and suns

++++++++++++++++++++++++
 假装是个python终端(docunit)
++++++++++++++++++++++++

"``>>>``" print "Hello World." 
Hello World