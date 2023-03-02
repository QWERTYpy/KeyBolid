from pathlib import Path
import  saveloadini
from person import Person

directory = 'key'
pathlist = Path(directory).glob('*.txt')
person_dict = {}
for path in pathlist:
    print(path)
    file = open(path, 'r')
    for line in file:
        if len(line.split('\t'))==4:
            fio, _, hex, _ = line.split('\t')

            # print(fio, hex)
        elif len(line.split('\t'))==3:
            fio, hex, _ = line.split('\t')
            # print(fio, hex)
        if len(fio.split()) == 3:
            _f, _i, _o = fio.split()
            # print(_f.title() , _i.title(), _o.title(), hex)
            # person_list.append([_f.title() , _i.title(), _o.title(), hex])
            person_dict[hex]=[_f.title() , _i.title(), _o.title()]
        # if len(fio.split()) != 3:
        #     print(fio)
ini_person_list = saveloadini.load_person_ini()
for _ in ini_person_list:
    if _.key in person_dict.keys():
        _.name = person_dict[_.key][1]
        _.surname = person_dict[_.key][0]
        _.patronymic = person_dict[_.key][2]

saveloadini.save_person_ini(ini_person_list)
