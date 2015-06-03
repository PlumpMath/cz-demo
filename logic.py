from __future__ import division

import random
import math

def dot(i):
    return {'rgb': [random.random() for _ in range(3)],
            'x': random.random(),
            'y': random.random(),
            'r': random.random(),
            'key': i}

def makeDots():
    return [dot(i) for i in range(random.randint(3, 20))]

def makeStack(n):
    return [{'rgb': [0, 0, 0],
             'x': i / n,
             'y': i / n,
             'r': 0.1,
             'key': i} for i in range(n)]

def makeBlink(inPlace):
    '''
    Fixed array of dots, with keyed position, but presence/absence is randomised.
    inPlace=True to key by location; inPlace=False to key by presence.
    '''
    result = []
    keyCounter = 0
    for n in range(9 * 9):
        x = 0.5 - 0.4 + (n % 9) * 0.1
        y = 0.5 - 0.4 + (n // 9) * 0.1
        if random.random() > 0.5:
            if inPlace:
                k = n
            else:
                k = keyCounter
                keyCounter = keyCounter + 1
            result.append({'rgb': [0, 0, 0],
                           'x': x,
                           'y': y,
                           'r': 0.5,
                           'key': k})
    return result

NUM_SPINS = 20
spinColours = [[random.random() for _ in range(3)] for _ in range(NUM_SPINS)]

def makeSpin(counter):
    result = []
    for n in range(NUM_SPINS):
        angle = math.pi * 2 * n / NUM_SPINS - counter / 2
        x = 0.5 + (0.4 * math.sin(angle))
        y = 0.5 + (0.4 * math.cos(angle))
        result.append({'rgb': spinColours[n],
                       'x': x,
                       'y': y,
                       'r': 0.5,
                       'key': n})
    return result
