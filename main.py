import binascii
import re
import crc8bolid as crc


line_cursor = 0
file = open('71_2.ki', 'rb')
# file = open('53.ki', 'rb')
# for line in file:
#     # print(line)
#     print(binascii.hexlify(line))
# file = open(filepath, 'rb')
cursor_str = False
count_key = 0
buffer_str = b''
for line in file:
    line_cursor += 1
    # print(line_cursor,'->',len(binascii.hexlify(line)), binascii.hexlify(line))
    if len(binascii.hexlify(line)) == 48:
        cursor_str = True
        continue
    if cursor_str:
        buffer_str += line

        if len(binascii.hexlify(buffer_str)) == 304 or len(binascii.hexlify(buffer_str)) == 262:
            # print('--->',binascii.hexlify(buffer_str))
            cursor_str = False

            count_key +=1
            file_key = crc.reverse_key(binascii.hexlify(buffer_str)[242:254])
            file_perm = binascii.hexlify(buffer_str)[256:262]
            buffer_str = b''
            print(count_key, file_key, file_perm)

        if len(binascii.hexlify(buffer_str)) == 346 or len(binascii.hexlify(buffer_str)) == 276:
            # print('--->', len(binascii.hexlify(buffer_str)), binascii.hexlify(buffer_str))
            cursor_str = False
            count_key +=1
            file_key = crc.reverse_key(binascii.hexlify(buffer_str)[214:226])
            file_perm =binascii.hexlify(buffer_str)[228:234]
            buffer_str = b''

            print(count_key, file_key, file_perm)




file.close()

