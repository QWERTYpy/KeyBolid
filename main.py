import binascii
import binhex
import html
# import re
# import crc8bolid as crc
#
#
# line_cursor = 0
file = open('71/1.ki', 'rb')
# # file = open('53.ki', 'rt')
for line in file:
    print(line)
    # print(line.decode('cp1252'))
    # print(line.decode('ansi'))
    # print(html.escape(line.decode('ansi')))
    print(binhex.binhex(line))
    print(binascii.hexlify(line))

# # file = open(filepath, 'rb')
# cursor_str = False
# count_key = 0
# buffer_str = b''
# for line in file:
#     line_cursor += 1
#     print(line_cursor,'->',len(binascii.hexlify(line)), binascii.hexlify(line))
#     if len(binascii.hexlify(line)) == 48:
#         cursor_str = True
#         continue
#     if cursor_str:
#         buffer_str += line
#
#         if len(binascii.hexlify(buffer_str)) == 304 or len(binascii.hexlify(buffer_str)) == 262:
#             # print('--->',binascii.hexlify(buffer_str))
#             cursor_str = False
#
#             count_key +=1
#             file_key = crc.reverse_key(binascii.hexlify(buffer_str)[242:254])
#             file_perm = binascii.hexlify(buffer_str)[256:262]
#             buffer_str = b''
#             print(count_key, file_key, file_perm)
#
#         if len(binascii.hexlify(buffer_str)) == 346 or len(binascii.hexlify(buffer_str)) == 276:
#             # print('--->', len(binascii.hexlify(buffer_str)), binascii.hexlify(buffer_str))
#             cursor_str = False
#             count_key +=1
#             file_key = crc.reverse_key(binascii.hexlify(buffer_str)[214:226])
#             file_perm =binascii.hexlify(buffer_str)[228:234]
#             buffer_str = b''
#
#             # print(count_key, file_key, file_perm)
#
#
#
#
# file.close()
#
# import time
#
# print(time.strftime("%d%m%y_%H:%M", time.localtime()))
a= b'\x04\x00\x00\x00\x00\x00\x000\xf9\x19\x00\x00\x00\x00\x00\xb1\x02\x00\x00\x01\x00\x00\x00\n'
print(a.decode('ansi'))
print(a.decode('cp1252'))