class ListManager(object):
    def __init__(self, _list):
        self.__sum = None
        self.__list = _list

    def add_values(self):
        self.__sum = sum(self.__list)

    def get_sum(self):
        return self.__sum


my_list = [1, 2, 3, 4]
manager = ListManager(my_list)
manager.add_values()

print(manager.get_sum())
