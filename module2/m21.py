#!/usr/bin/env python
# coding=utf-8
# from module1 import m11, m12
import sys

sys.path.append('..')

from module1 import m11, m12


__author__ = 'junqiangshen'


def func1():
    m11.func1()
    print( 'm21 func1')


def func2():
    m12.func2()
    print( 'm21 func2')


if __name__ == '__main__':
    func1()
    func2()
