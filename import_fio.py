from pathlib import Path
import saveloadini
from person import Person

# directory = 'key'
# pathlist = Path(directory).glob('*.txt')
# person_dict = {}
# for path in pathlist:
#     print(path)
#     file = open(path, 'r')
#     for line in file:
#         if len(line.split('\t'))==4:
#             fio, _, hex, _ = line.split('\t')
#
#             # print(fio, hex)
#         elif len(line.split('\t'))==3:
#             fio, hex, _ = line.split('\t')
#             # print(fio, hex)
#         if len(fio.split()) == 3:
#             _f, _i, _o = fio.split()
#             # print(_f.title() , _i.title(), _o.title(), hex)
#             # person_list.append([_f.title() , _i.title(), _o.title(), hex])
#             person_dict[hex]=[_f.title() , _i.title(), _o.title()]
#         # if len(fio.split()) != 3:
#         #     print(fio)
# ini_person_list = saveloadini.load_person_ini()
# for _ in ini_person_list:
#     if _.key in person_dict.keys():
#         _.name = person_dict[_.key][1]
#         _.surname = person_dict[_.key][0]
#         _.patronymic = person_dict[_.key][2]
#
# saveloadini.save_person_ini(ini_person_list)

#### ----- Новая
directory = 'key'
pathlist = Path(directory).glob('*.txt')
person_dict = {}
for path in pathlist:
    print(path)
    file = open(path, 'r')
    i = 0
    for line in file:
        i+=1
        if i == 1:
            # print(line.strip().title().split(), end=' ')
            list_fio = line.strip().title().split()
            if len(list_fio) == 3:
                _f, _i, _o = list_fio
            if len(list_fio) == 4:
                _f, _i, _o, _o2 = list_fio
                _o = _o+_o2
            if len(list_fio) == 2:
                _f, _i,  = list_fio
                _o = ''


            # print(_f, _i, _o)

            # i += 1
            continue
        if i == 2:
            hex = line.strip()
            # i += 1
            continue
        if i == 3:
            # i += 1
            continue
        if i == 4:
            person_dict[hex] = [_f.title(), _i.title(), _o.title()]
            i = 0
    # print(person_dict)
        # if len(line.split('\t'))==4:
        #     fio, _, hex, _ = line.split('\t')
        #
        #     # print(fio, hex)
        # elif len(line.split('\t'))==3:
        #     fio, hex, _ = line.split('\t')
        #     # print(fio, hex)
        # if len(fio.split()) == 3:
        #     _f, _i, _o = fio.split()
        #     # print(_f.title() , _i.title(), _o.title(), hex)
        #     # person_list.append([_f.title() , _i.title(), _o.title(), hex])
        #     person_dict[hex]=[_f.title() , _i.title(), _o.title()]
        # # if len(fio.split()) != 3:
        #     print(fio)
ini_person_list = saveloadini.load_person_ini()
for _ in ini_person_list:
    if _.key in person_dict.keys():
        _.name = person_dict[_.key][1]
        _.surname = person_dict[_.key][0]
        _.patronymic = person_dict[_.key][2]

saveloadini.save_person_ini(ini_person_list)
