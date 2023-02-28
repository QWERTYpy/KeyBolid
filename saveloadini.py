import configparser
from person import Person
from object import ObjectBolid

def load_person_ini():
    # Загружаем объекты из файла
    config = configparser.ConfigParser()
    config.read('person2.ini', encoding='utf-8')
    list_person = []
    for hex_key in config.sections():
        pers = Person()
        pers.name = config[hex_key]['name']
        pers.surname = config[hex_key]['surname']
        pers.patronymic = config[hex_key]['patronymic']
        # pers.key = bytes(hex_key, 'ascii')
        pers.key = hex_key
        for _ in config[hex_key]['permission'].split(';'):
            if _:
                id_obj, num_obj, xo_obj, perm_obj = map(str.strip, _.split(','))
                pers.permission[id_obj] = [num_obj, xo_obj, perm_obj]
        list_person.append(pers)
    return list_person

def save_person_ini(list_person):
    # Сохраняем созданные объекты в файл
    config = configparser.ConfigParser()
    for _ in list_person:
        str_permission = ''
        for _perm in _.permission:
            str_permission += f"{_perm}, {_.permission[_perm][0]}, {_.permission[_perm][1]}, {_.permission[_perm][2]};"
        config[f"{_.key}"] = {'name': _.name,
                              'surname': _.surname,
                              'patronymic': _.patronymic,
                              'permission': str_permission}



    # shutil.copy('example.ini', 'example_tmp.ini')
    with open('person2.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


def load_object_ini():
    # Загружаем объекты из файла
    config = configparser.ConfigParser()
    config.read('object.ini', encoding='utf-8')
    list_obj = []
    for id_obj in config.sections():
        obj = ObjectBolid()
        obj.id = id_obj
        obj.num = config[id_obj]['num']
        obj.name = config[id_obj]['name']
        obj.type = config[id_obj]['type']
        obj.ver = config[id_obj]['ver']
        obj.comment = config[id_obj]['comment']
        # pers.show()
        list_obj.append(obj)
    return list_obj

if __name__ == '__main__':
    aa =load_person_ini()
    for _ in aa:
        print(_.permission)
    # print(list_person_table(aa))
