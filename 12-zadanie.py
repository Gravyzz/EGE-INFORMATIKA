"""s = 146 * "5"
while "333" in s or "555" in s:
    if "555" in s:
        s = s.replace("555", "3", 1)
    else:
        s = s.replace("333", "5", 1)
print(s)"""

"""s = "1" + 80*"8"
while "18" in s or "288" in s or "3888" in s:
    if "18" in s:
        s = s.replace("18", "2", 1)
    elif "288" in s:
        s = s.replace("288", "3", 1)
    else:
        s = s.replace("3888", "1", 1)
print(s)"""

"""s = "8"*99+"1" 
while '133' in s or '881' in s:
    if '133' in s:
        s = s.replace('133', '81', 1)
    if '881' in s:
        s = s.replace('881', '13', 1)
print(s)"""

"""for i in range(201, 300):
    s = i*'1'
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    print(s, i) """


"""for n in range(1, 1000):
    s = '>' + '0' * 39 + n * '1' + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>',1)
        if '>2' in s:
            s = s.replace('>2', '2>',1)
        if '>0' in s:
            s = s.replace('>0', '1>',1)
    if (s.count('1') + s.count('2')*2)%3837==0:
        print( n)"""

"""for i in range(1,100):
    for j in range(1,100):
        for q in range(1,100):
            s = '0' + '1'*i+'2'*j+'3'*q+'0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(i,j,q, i+q+j+2)"""



"""s = 1000*'8'
while '999' in s or '888' in s:
    if '888' in s:
        s = s.replace('888','9',1)
    else:
        s = s.replace('999','8',1)
print(s)"""

"""s = '>' + 10*'1'+20*'2'+30*'3'
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print(s.count('1')+s.count('2')*2+s.count('3')*3)"""

"""for od in range(1, 50):
    for dv in range(1, 50):
        for tr in range(1, 50):
            s = '0' + od*'1'+dv*'2'+tr*'3'
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)
            if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
                print(od)"""

"""s = '1' + 98*'9'
while '19' in s or '299' in s or '3999' in s:
    s = s.replace('19', '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print(s)"""

"""s = 108*'7'
while '33333' in s or '777' in s:
    if '33333' in s:
        s = s.replace('33333', '7', 1)
    else:
        s = s.replace('777', '3', 1)
print(s)"""