Random-Letter-Detector
===========

**Random-Letter-Detector** evaluates whether input string is random letter sequence or not. This may be useful for detecting auto-generated e-mail accounts.

##How to run

###Train
```
rl = RandomLetter()
rl.train('train.dat', 'nonrandom.dat')
```

###Evaluate
```
rl.evaluate('your_text')
```

* True: Random
* False: Non-Random

##Example
```
$ python detect.py
non-random : the_electrode_contacts
non-random : steady_rate_in
non-random : ond_the_sequence
non-random : the_corresponding_current
non-random : al_as_the
non-random : creases_it_would
non-random : form_as_shown
non-random : crease_must_be
non-random : trode_tip_until
non-random : occur_so_fast
    random : f59fc80eee2a8b8
    random : 8ef9fd9d7fa89c2
    random : 8bd1a531a345f62
    random : f5c1a09796d75d0
    random : 5615b7d40d246bd
    random : 3788010d03d9f32
    random : 761355454f6084d
    random : 89b82946d0aa0e9
    random : 566d18845cfbb36
    random : 5qik37bzbfa364lqy1pe
    random : z8oa1swy7ugmqtrvumee
    random : m3yva7t7z37enbdz3uyb
    random : 1qbgx129oiw9b2506f1n
    random : shcqnaejk7o6fe797afx
    random : 7w01ghs2f7o739q5fg4s
    random : 1abe78cj0w8xvxkl8pei
    random : lgn2qvptlwto7hhjzcfo
    random : qdd2iv6ystyh1e71hyos
    random : o3wnxg8oyrhcefaqvikh
```

##How it works?
In training phase, bigrams of support-characters ('abcdefghijklmnopqrstuvwxyz0123456789') are extracted from standard documents, then, probability of each bigram is calculated. Generation probability of any letter sequence can be evaluated using the bigram probability based on Markov's assumption. Threshold value is derived by :

```
(min(probs of non-random samples) + max(probs of random samples)) / 2
```

Since this is a poor & simple manner, there are better fashions like using Fisher's linear discriminant.

In the case that a letter sequence generation probability is less than the threshold value, the sequence is classified as random, and vice versa.

