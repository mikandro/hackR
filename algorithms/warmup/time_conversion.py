def timeConversion(s):
    # TODO if/else hell
    hh = int(s[0:2])
    mm = int(s[3:5])
    ss = int(s[6:8])
    m_s = s[2:8]
    if 'A' in s:
        if s == '12:00:00AM':
            return '00:00:00'
        else:
            if hh == 12 and (mm > 0 or ss > 0):
                return ''.join(['00', m_s])
            else:
                return s[0:8]
    else:
        if s == '12:00:00PM':
            return '12:00:00'
        else:
            if hh == 12 and (mm > 0 or ss > 0):
                return ''.join(['12', m_s])
            else:
                hh = str(int(s[0:2]) + 12)
                return ''.join([hh, m_s])


s = '12:21:00AM'
result = timeConversion(s)
print(result)
