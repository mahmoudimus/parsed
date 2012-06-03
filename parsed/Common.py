#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Denis Zalevskiy
# Licensed under MIT License

from cor import const, nth

nomatch = const('nomatch')
empty = const('empty')
end = const('end')

def ignore(*x): return empty
def value(x): return x
def first(x): return x[0]
second = nth(1)
third = nth(2)
def list2str(x): return ''.join(x)

def is_str(c):
    return isinstance(c, str) or c == nomatch