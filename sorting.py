#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input
which controls how the elements of the list
should be compared against each other:
If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.
'''


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    ixs = 0
    iys = 0
    ret = []
    while ixs < len(xs) and iys < len(ys):
        if cmp(xs[ixs], ys[iys]) == -1:
            ret.append(xs[ixs])
            ixs += 1
        else:
            ret.append(ys[iys])
            iys += 1

    while ixs < len(xs):
        ret.append(xs[ixs])
        ixs += 1

    while iys < len(ys):
        ret.append(ys[iys])
        iys += 1

    return ret


def merge_sorted(xs, cmp=cmp_standard):
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        left = xs[mid:]
        right = xs[:mid]
        left_sorted = merge_sorted(left, cmp=cmp)
        right_sorted = merge_sorted(right, cmp=cmp)
        return _merged(left_sorted, right_sorted, cmp=cmp)


def quick_sorted(xs, cmp=cmp_standard):
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        pivot = xs[mid]
        xs_lt = [x for x in xs if cmp(x, pivot) == -1]
        xs_gt = [x for x in xs if cmp(x, pivot) == 1]
        xs_eq = [x for x in xs if cmp(x, pivot) == 0]
        xs_lt = quick_sorted(xs_lt, cmp=cmp)
        xs_gt = quick_sorted(xs_gt, cmp=cmp)
        return xs_lt + xs_eq + xs_gt
