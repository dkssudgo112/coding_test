a = input()

a = a.lower()

ls = []
di = {}

ls.append(a.count('a'))
ls.append(a.count('b'))
ls.append(a.count('c'))
ls.append(a.count('d'))
ls.append(a.count('e'))
ls.append(a.count('f'))
ls.append(a.count('g'))
ls.append(a.count('h'))
ls.append(a.count('i'))
ls.append(a.count('j'))
ls.append(a.count('k'))
ls.append(a.count('l'))
ls.append(a.count('m'))
ls.append(a.count('n'))
ls.append(a.count('o'))
ls.append(a.count('p'))
ls.append(a.count('q'))
ls.append(a.count('r'))
ls.append(a.count('s'))
ls.append(a.count('t'))
ls.append(a.count('u'))
ls.append(a.count('v'))
ls.append(a.count('w'))
ls.append(a.count('x'))
ls.append(a.count('y'))
ls.append(a.count('z'))

di[str(a.count('a'))] = 'a'
di[str(a.count('b'))] = 'b'
di[str(a.count('c'))] = 'c'
di[str(a.count('d'))] = 'd'
di[str(a.count('e'))] = 'e'
di[str(a.count('f'))] = 'f'
di[str(a.count('g'))] = 'g'
di[str(a.count('h'))] = 'h'
di[str(a.count('i'))] = 'i'
di[str(a.count('j'))] = 'j'
di[str(a.count('k'))] = 'k'
di[str(a.count('l'))] = 'l'
di[str(a.count('m'))] = 'm'
di[str(a.count('n'))] = 'n'
di[str(a.count('o'))] = 'o'
di[str(a.count('p'))] = 'p'
di[str(a.count('q'))] = 'q'
di[str(a.count('r'))] = 'r'
di[str(a.count('s'))] = 's'
di[str(a.count('t'))] = 't'
di[str(a.count('u'))] = 'u'
di[str(a.count('v'))] = 'v'
di[str(a.count('w'))] = 'w'
di[str(a.count('x'))] = 'x'
di[str(a.count('y'))] = 'y'
di[str(a.count('z'))] = 'z'


ls.sort(reverse=True)


if(ls[0] == ls[1]): print('?')
else: print(di[str(ls[0])].upper())