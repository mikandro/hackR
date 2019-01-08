a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

def make_anagram(w1, w2):
    total = 0
    word_diff = list(set(w1) ^ set(w2))
    word_intersection = list(set(w1) & set(w2))
    print word_intersection
 #   for letter in 'abcdefghijklmnopqrstuvxyzw':
    difs = sum([w1.count(letter) + w2.count(letter) for letter in word_diff])
    interesections = sum([abs(w1.count(letter) - w2.count(letter)) for letter in word_intersection])
    print interesections

    return difs + interesections
res = make_anagram(a, b)
print res
