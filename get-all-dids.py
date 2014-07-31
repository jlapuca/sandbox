#!/usr/bin/python
#-*- coding: utf-8 -*-

# Доброе утро. Сейчас напитоним.

import ConfigParser
from collections import defaultdict

# Конфигурация
users_file_name = 'users.conf'
dids_file_name = 'extensions.conf'


def get_names(file_name):
    """
    Возвращает словарь {экстент: имя обладателя}

    :param file_name: Файл, который будет парситься
    :return dict:
    """

    def extract_name(section):
        """
        Имя может быть в параметре fullname или в callerid.

        :param section: имя секции (номер экстента)
        :return str: имя обладателя экстента
        """
        if not section in users.sections():
            return
        try:
            return users.get(section, 'fullname')
        except ConfigParser.NoOptionError:
            # параметр callerid имеет вид: Alex Browning <3213>
            return users.get(section, 'callerid').split('<')[0].strip().strip('"')

    users = ConfigParser.ConfigParser()
    users.read('users.conf')

    return {ext: extract_name(ext) for ext in users.sections()}


def get_dids(file_name):
    """
    Возвращает словарь {экстент: [соответствующие диды]}

    :param file_name: файл конфигурации
    :return dict:
    """
    dids = defaultdict(list)
    exts = open(file_name, 'r')
    for line in exts:
        if "internalq-calls" in line and not line.startswith(';'):
            fields = line.split(' ')[2].split(',')
            dids[fields[3]].append(fields[0])
    exts.close()
    return dids


if __name__ == "__main__":
    # получаем информацию из файлов
    names = get_names(users_file_name)
    dids = get_dids(dids_file_name)

    # объединяем экстенты из разных источников в один набор уникальных значений
    extents = set(names.keys() + dids.keys())

    # выясним максимальное количество номеров у одного экстента
    max_dids = max(len(d) for d in dids.values())

    # подготовим строку формата с подходящим количеством полей
    out_format = '%-20s\t%-10s' + '\t%-15s'*max_dids

    # отформатируем заголовок таблицы
    header = tuple(['Name', 'ext'] + ['DID'+str(x+1) for x in range(max_dids)])
    print out_format % header

    # проходим по всем экстентам
    for ext in sorted(list(extents)):
        # если у экстента меньше номеров, чем максимум - дополняем его
        # список номеров пустыми строками
        line = tuple([names.get(ext, "No name"), ext] +
                     dids.get(ext, []) + ['']*(max_dids - len(dids.get(ext, []))))
        print out_format % line