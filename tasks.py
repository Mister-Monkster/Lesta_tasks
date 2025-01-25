#----------------------------Задание 1---------------------------------------------------------------------
def isEven(value):
    return value % 2


"""Плюсом этой реалицзации будет простота, понятность и эффективность.
   Минусом по сравнению с моей реализацией будет более медленная работ"""


def isEven_new(value):
    return (value & 1) == 0


"""Плюсом будет скорость и эффективность
Минусом - более трудный для понимания"""


#-------------------------------------------------------------------------------------------------------

#----------------------------Задание 2--------------------------------------------------------------------
class Queue:
    def __init__(self, len_: int):
        self.queue_ = []
        self.len_ = len_

    def add_element(self, element):  #метод добавления элементов
        if len(self.queue_) < self.len_: #O(1)
            return self.queue_.append(element)
        else:
            return print('Очередь заполнена')

    def get_element(self):  #метод получения и удаления элемента
        if len(self.queue_):
            element = self.queue_[0]  #O(1)
            del self.queue_[0]  #O(1)
            return self.queue_.append(element) #O(1)
        else:
            return None

    def extend(self, new_len: int):  #Расширение очереди
        if new_len > self.len_:
            self.len_ = new_len


"""Главным минусом подобной реализации будет меньшая производительность списков по сравнению со словарями
плюсом же будет простота реализации и то, что словари сами присваивают индексы элементам"""


class second_Queue:
    def __init__(self, len_: int):
        self.queue_ = {}
        self.len_ = len_
        self.index = 0
        self.index_for_get = 0

    def add_element(self, value):
        if len(self.queue_) < self.len_:  #O(1)
            self.queue_[self.index] = value  #O(1)
            self.index += 1

    def get_element(self):  #Получение элемента
        if len(self.queue_):
            element = self.queue_[self.index_for_get]  #O(1)
            del self.queue_[self.index_for_get]  #O(1)
            self.index_for_get += 1
            return element
        else:  # Если очередь пуста значит обнуляем индексы
            self.index_for_get = 0
            self.index = 0
            return None

    def extend(self, new_len: int):  #Расширение очереди
        if new_len > self.len_:
            self.len_ = new_len


"""Из плюсов: более просто получение индекса(ключа) и лучшая производительность словарей по сравнению со списками
Минусом будет большие затраты памяти для словарей и больший объем кода"""


#------------------------------------------------------------------------------------------------------------

#----------------------------Задание 3-----------------------------------------------------------------------

def sorting(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sorting(left) + middle + sorting(right)


"""Cтандартный алгоритм quicksort, он считается самым эффективным для сортировки"""