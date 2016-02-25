# -*- coding: utf-8 -*-
import math
import hashlib
import random

class RandomLetter:
    """Random Letter Detector"""

    support_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    initial_freq = 100 # works like prior

    def __init__(self):
        self.__thresh = 0
        self.__prob = {}

    def getFilteredLetters(self, text):
        return [c for c in text.lower() if c in RandomLetter.support_chars]

    def getProb(self, text):
        try:
            fl = self.getFilteredLetters(text)
            p = sum([self.__prob[fl[c]][fl[c+1]] for c in xrange(len(fl)-1)]) # sum of log probability
            return math.exp(p / len(fl)) # geometric mean
        except:
            return 0

    def train(self, train_data, nonrandom_data):
        # bigram freq
        freq = {c0: {c1:RandomLetter.initial_freq for c1 in RandomLetter.support_chars} for c0 in RandomLetter.support_chars}
        for line in open(train_data):
            fl = self.getFilteredLetters(line)
            for c in xrange(len(fl)-1):
                freq[fl[c]][fl[c+1]] += 1

        # bigram freq to log probability
        for k0,v0 in freq.items():
            s = float(sum(v0.values()))
            self.__prob[k0] = {k1:math.log(v1/s) for k1,v1 in v0.items()}

        # threshold value calculation
        nr = []
        r = []
        for line in open(nonrandom_data):
            nr.append(self.getProb(line))
            r.append(self.getProb(hashlib.md5(line).hexdigest()))
            r.append(self.getProb("".join([random.choice(RandomLetter.support_chars) for x in xrange(len(line))])))
        self.__thresh = (min(nr) + max(r)) / 2 # poor manner.. (There are some better fashions like Fisher's linear discriminant)

    def evaluate(self, text):
        return self.__thresh > self.getProb(text)

