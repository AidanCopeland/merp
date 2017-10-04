import random
import os
import trace_log as trace

def randomize():
    rand_seed = os.urandom(256)
    random.seed(rand_seed)

def d100():
    roll = random.randint(1,100)
    trace.detail("Roll was %d" % roll)
    return roll

def d1000():
    roll = random.randint(1,1000)
    trace.detail("Roll was %d" % roll)
    return roll