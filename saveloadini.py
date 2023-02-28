import configparser
from person import Person
from object import ObjectBolid

def load_person_ini():
    # Загружаем объекты из файла
    config = configparser.ConfigParser()
    config.read('person.ini', encoding='utf-8')
    list_person = []
    for hex_key in config.sections():
        pers = Person()
        pers.name = config[hex_key]['name']
        pers.surname = config[hex_key]['surname']
        pers.patronymic = config[hex_key]['patronymic']
        # pers.key = bytes(hex_key, 'ascii')
        pers.key = hex_key
        if ';' in config[hex_key]['permission']:
            for _ in config[hex_key]['permission'].split(';'):
                num_obj, id_obj, xo_obj, perm_obj = map(str.strip, _.split(','))
                pers.permission[id_obj] = [num_obj, xo_obj, perm_obj]
        else:
            num_obj, id_obj, xo_obj, perm_obj = map(str.strip, config[hex_key]['permission'].split(','))
            pers.permission[id_obj] = [num_obj, xo_obj, perm_obj]
        # pers.show()
        list_person.append(pers)
    return list_person


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
