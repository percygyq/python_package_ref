#!/usr/bin/env python
# coding=utf-8
import sys

sys.path.append('..')

from module1.module11 import m1_m11

__author__ = 'junqiangshen'


def func1():
    m1_m11.func1()
    print( 'm31 func1')


def func2():
    m1_m11.func2()
    print( 'm31 func2')


if __name__ == '__main__':
    func1()
    func2()
