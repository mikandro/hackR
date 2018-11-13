from collections import Counter
magazine = ['two', 'times', 'two', 'is', 'not', 'four']
note = ['two', 'times', 'two', 'is', 'four']

#
def checkMagazine(magazine, note):
    m_count = Counter(magazine)
    n_count = Counter(note)
    for key in n_count:
        if m_count.has_key(key) == False:
            print 'No'
            return
        if n_count[key] > m_count[key]:
            print 'No'
            return
    print 'Yes'
    return




checkMagazine(magazine, note)