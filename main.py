import sig10
import c20004
import binascii

permition_list = [['00550073d712', '081100'],
                  ['001100596a7f', '182200']]

# sig10.write_key('101', permition_list)
c20004.write_key('444', permition_list)
# # Вывод файла в консоль
# file = open('_2.ki', 'rb')
# for line in file:
#     # print(line)
#     print(binascii.hexlify(line))

