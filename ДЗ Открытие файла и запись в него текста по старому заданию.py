from pprint import pprint

name = 'openfail.txt'
#file = open(name, 'r')
#pprint(file.read())
file = open(name, 'a')
file.write(
    '\n My soul is dark - Oh! quickly string, '
    '\nThe harp I yet can brook to hear, '
    '\nAnd let thy gentle fingers fling, '
    '\nIts melting murmurs oer mine ear. '
    '\nIf in this heart a hope be dear, '
    '\nThat sound shall charm it forth again: '
    '\nIf in these eyes there lurk a tear, '
    '\nTwill flow, and cease to burn my brain. '
    '\nBut bid the strain be wild and deep, '
    '\nNor let thy notes of joy be first: '
    '\nI tell thee, minstrel, I must weep, '
    '\nOr else this heavy heart will burst; '
    '\nFor it hath been by sorrow nursed, '
    '\nAnd ached in sleepless silence, long; '
    '\nAnd now tis doomed to know the worst, '
    '\nAnd break at once - or yield to song.')
file.close()
file = open(name, 'r')
pprint(file.read())
file.close()