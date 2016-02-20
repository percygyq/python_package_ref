# python_package_ref
测试工程中Python不同包之前模块和函数的引用

## 文件结构为：
```
➜  package_ref  tree
.
├── module1
│   ├── __init__.py
│   ├── m11.py
│   ├── m12.py
│   └── module11
│       ├── __init__.py
│       └── m1_m11.py
├── module2
│   ├── __init__.py
│   └── m21.py
├── module3
│   ├── __init__.py
│   └── m31.py
└── m.py
```

具体的引用关系为：  
1. m21.py引用了m11,m12中的函数  
2. m31引用了m1_11中的函数  
3. m.py引用了m11,m12中的函数

## 文件内容
* m11.py
```python
#!/usr/bin/env python
# coding=utf-8

__author__ = 'junqiangshen'


def func1():
    print 'm11 func1'


def func2():
    print 'm11 func2'
```
* m12.py
```python
#!/usr/bin/env python
# coding=utf-8

__author__ = 'junqiangshen'


def func1():
    print 'm12 func1'


def func2():
    print 'm12 func2'
```
* m1_m11.py
```python
#!/usr/bin/env python
# coding=utf-8

__author__ = 'junqiangshen'


def func1():
    print 'm1_m11 func1'


def func2():
    print 'm1_m11 func2'
```
* m21.py
```python
#!/usr/bin/env python
# coding=utf-8
# from module1 import m11, m12
import sys

sys.path.append('..')

from module1 import m11, m12


__author__ = 'junqiangshen'


def func1():
    m11.func1()
    print 'm21 func1'


def func2():
    m12.func2()
    print 'm21 func2'


if __name__ == '__main__':
    func1()
    func2()
```
* m31.py
```python
#!/usr/bin/env python
# coding=utf-8
import sys

sys.path.append('..')

from module1.module11 import m1_m11

__author__ = 'junqiangshen'


def func1():
    m1_m11.func1()
    print 'm31 func1'


def func2():
    m1_m11.func2()
    print 'm31 func2'


if __name__ == '__main__':
    func1()
    func2()
```
* m.py
```python
#!/usr/bin/env python
# coding=utf-8
from module1 import m11, m12

__author__ = 'junqiangshen'


def func1():
    m11.func1()
    print 'm func1'


def func2():
    m12.func2()
    print 'm func2'

if __name__ == '__main__':
    func1()
    func2()
```
