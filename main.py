import sig10

permition_list = [['00550073d712', '030000'],
                  ['001100596a7f', '000300']]

# sig10.write_key('101', permition_list)
file = open('test.ki', 'rb')
for line in file:
    print(line)
    # print(binascii.hexlify(line))

