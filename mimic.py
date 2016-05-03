#!/usr/bin/python3

"""Имитация текста

Прочитайте файл, указанный в командной строке.
Используйте str.split() (без аргументов) для получения всех слов в файле.
Вместо того, чтобы читать файл построчно, проще считать
его в одну гигантскую строку и применить к нему split() один раз.

Создайте "имитационный" словарь, который связывает каждое слово
со списком всех слов, которые непосредственно следуют за этим словом в файле.
Список слов может быть в любом порядке и должен включать дубликаты. 

Так, например, для текста "Привет, мир! Привет, Вселенная!" мы получим такой
имитационный словарь:
{'': ['Привет,'], 'Привет,': ['мир!', 'Вселенная!'], 'мир!': ['Привет,']}
Будем считать, в качестве ключа для первого слова в файле используется пустая строка.

С помощью имитационного словаря довольно просто генерировать случайные тексты, 
имитирующие оригинальный. Возьмите слово, посмотрите какие слова могут за ним, 
выберите одно из них наугад, выведите его и используйте это слово 
в следующей итерации.

Используйте пустую строку в качестве ключа для первого слова.
Если вы когда-нибудь застрянете на слове, которого нет в словаре,
вернетесь к пустой строке, чтобы продолжать генерацию текста.

Примечание: стандартный python-модуль random включает в себя метод 
random.choice(list), который выбирает случайный элемент из непустого списка.

"""

import random
import sys


def mimic_dict(filename):
    """Возвращает имитационный словарь, сопоставляющий каждое слово 
    со списом слов, которые непосредственно следуют за ним в тексте"""

    file = open(filename, 'r',encoding = "utf-8")
    mylist = file.read().split()
    mydict = {'':[mylist[0]]}
    elist = list(enumerate(mylist))
    for i in elist:
        ss = []
        for j in elist:
            if j[1]== i[1]:
                if (j[0]+1)<len(mylist):
                    ss.append(mylist[j[0]+1])
                else:
                    ss.append('')
        mydict.update({i[1]:ss})
    return (mydict)


def print_mimic(mimic_dict, word):

    """Принимает в качестве аргументов имитационный словарь и начальное слово,
    выводит 200 случайных слов."""

    res = []
    while len(res)<200:
        nextword = random.choice(mimic_dict[word]) 
        res.append(nextword)
        word = nextword
    print(' '.join(res))
    return


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')
    #sl=mimic_dict('example.txt')
    #for i in sl:
    #    print (i,sl[i])
    #print_mimic(sl,'')


if __name__ == '__main__':
    main()
