'''
크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=

ljes=njak
6
'''

alpha = input()
cnt = len(alpha)
for i in range(len(alpha)):
    if i == 1:
        if alpha[i] == 'j':
            if alpha[i-1] == 'n' or alpha[i-1] == 'l':
                cnt -= 1

        elif alpha[i] == '-':
            if alpha[i-1] == 'c' or alpha[i-1] == 'd':
                cnt -= 1

        elif alpha[i] == '=':
            if alpha[i - 1] == 'z' or alpha[i-1] == 's' or alpha[i-1] == 'c':
                cnt -= 1

    elif i >= 2:
        if alpha[i] == 'j':
            if alpha[i-1] == 'n' or alpha[i-1] == 'l':
                cnt -= 1

        elif alpha[i] == '-':
            if alpha[i-1] == 'c' or alpha[i-1] == 'd':
                cnt -= 1

        elif alpha[i] == '=':
            if alpha[i-1] == 'z':
                if alpha[i-2] == 'd':
                    cnt -= 2
                else:
                    cnt -= 1
            elif alpha[i-1] == 's':
                cnt -= 1

            elif alpha[i-1] == 'c':
                cnt -= 1
print(cnt)
