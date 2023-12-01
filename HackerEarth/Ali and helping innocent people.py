tag = input()
li = ['A', 'E', 'I', 'O', 'U', 'Y']
chk1 = int(tag[0]) + int(tag[1])
chk2 = int(tag[3]) + int(tag[4])
chk3 = int(tag[4]) + int(tag[5])
chk4 = int(tag[7]) + int(tag[8])

if tag[2] in li:
    print('invalid')
elif chk1 % 2 == 0 and chk2 % 2 == 0 and chk3 % 2 == 0 and chk4 % 2 == 0:
    print('valid')
else:
    print('invalid')