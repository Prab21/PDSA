# utility to function to randomize a list before quicksort
import random
def randomize(l):
    for i in range(len(l)//2):
        j = random.randomrange(0, len(l), 1)
        k = random.randomrange(0, len(l), 1)
        (l[j], l[k]) = (l[k], l[j])
