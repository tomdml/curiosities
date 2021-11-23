while 1: 
    h='#';o='o';b = 'xo';g=p=q=[h]*9;i=input;f=print
    while not p in[*b]:p=i('x or o > ')
    while q:
        c=-1
        while not c in range(9):c=int(i('1-9 > '))-1;
        if not g[c]in[*b]: 
            g[c]=p;f('{6}|{7}|{8}\n{3}|{4}|{5}\n{0}|{1}|{2}'.format(*g))
            if[*p*3]in[g[x:y:z]for x,y,z in[[0,3,1],[3,6,1],[6,9,1],[0,7,3],[1,8,3],[2,9,3],[0,9,4],[2,7,2]]]:f(p+' wins!');q=0
            elif not h in g:f('Draw');q=0
            p='x'if p==o else o
    if not i('Replay > ')=='y':break