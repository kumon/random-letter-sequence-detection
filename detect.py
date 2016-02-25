# -*- coding: utf-8 -*-
from random_letter import RandomLetter

rl = RandomLetter()
rl.train('train.dat', 'nonrandom.dat')
for line in open('examples.dat'):
    if rl.evaluate(line):
        print '    random : ' + line.strip()
    else:
        print 'non-random : ' + line.strip()

