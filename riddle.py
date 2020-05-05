#!/usr/bin/python3
from itertools import permutations 
import time
import os

liseis = list(list(x) for x in permutations([i for i in range(10)],4))
to_remove = []

## Implementing test

def check_1(l,c): #One number is correct but in wrong position
    f=False
    for i in c:
       if i in l:
           if l.index(i) != c.index(i):
               f = True

    if not f:
       to_remove.append(l)

    for i in c:
        if i in l:
            ni = c[:]
            ni.remove(i)
            for j in ni:
                if j in l:
                    if l not in to_remove:
                        to_remove.append(l)

def check_2(l,c): #Two numbers are correct but in wrong positions
    perm = permutations(c,2)
    f = False
    for i in list(perm):
        if i[0] in l and i[1] in l:
            ni = l[:]
            ni.remove(i[0])
            ni.remove(i[1])
            if ni[0] not in i and ni[1] not in i:
                if c.index(i[0]) != l.index(i[0]) and c.index(i[1]) != l.index(i[1]):
                    f = True

    if not f:
        to_remove.append(l)

def check_3(l,c): #One number is correct and in correct position
    f=False
    for i in c:
       if i in l:
           if l.index(i) == c.index(i):
               f = True

    if not f:
       to_remove.append(l)

    for i in c:
        if i in l:
            ni = c[:]
            ni.remove(i)
            for j in ni:
                if j in l:
                    if l not in to_remove:
                        to_remove.append(l)

def check_4(l,c): #No number is correct
    for i in l:
        if i in c:
            to_remove.append(l)

def check_5(l,c): #Two numbers are correct and in correct positions
    perm = permutations(c,2)
    f = False
    for i in list(perm):
        if i[0] in l and i[1] in l:
            ni = l[:]
            ni.remove(i[0])
            ni.remove(i[1])
            if ni[0] not in i and ni[1] not in i:
                if c.index(i[0]) == l.index(i[0]) and c.index(i[1]) == l.index(i[1]):
                    f = True

    if not f:
        to_remove.append(l)

def check_6(l,c): #At least one number is in correct position
    f = False
    for t, i in enumerate(l):
        if c[t] == i:
           f = True
    if not f:
       to_remove.append(l)

##Presenting pazzle:
print("""
Could you find my 4 digit PIN?
Take those hints:
    1. 9285 => "One number is correct, but in wrong position"
    2. 1937 => "Two numbers are correct, but in wrong positions"
    3. 5201 => "One number is correct and in correct position"
    4. 6507 => "No number is correct"
    5. 8524 => "Two numbers are correct, but in wrong position"

""")
input('Press "Enter" to reveal the answer')

## Running tests

print("Possible solutions:", len(liseis))

print("One number is correct in [9, 2, 8, 5] but in wrong position")
for lisi in liseis:
    check_1(lisi, [9,2,8,5])
for d in to_remove:
    try:
        liseis.remove(d)
    except ValueError:
        pass
print("Possible solutions:",len(liseis))

print("Two numbers are correct in [1, 9, 3, 7] but in wrong positions")
for lisi in liseis:
    check_2(lisi, [1,9,3,7])
for d in to_remove:
    try:
        liseis.remove(d)
    except ValueError:
        pass
print("Possible solutions:",len(liseis))

print("One number is correct in [5, 2, 0, 1] and in correct position")
for lisi in liseis:
    check_3(lisi, [5,2,0,1])
for d in to_remove:
    try:
        liseis.remove(d)
    except ValueError:
        pass
print("Possible solutions:",len(liseis))

print("No number is correct in [6, 5, 0, 7]")
for lisi in liseis:
    check_4(lisi, [6,5,0,7])
for d in to_remove:
    try:
        liseis.remove(d)
    except ValueError:
        pass
print("Possible solutions:",len(liseis))

print("Two numbers are correct in  [8, 5, 2, 4] but in wrong position")
for lisi in liseis:
    check_2(lisi, [8,5,2,4])
for d in to_remove:
    try:
        liseis.remove(d)
    except ValueError:
        pass
print("Possible solutions:",len(liseis))

for i in liseis:
    print(i)


