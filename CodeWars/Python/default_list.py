class DefaultList(list):
    def __init__(self, array, def_value):
        super().__init__(array)
        self.def_value = def_value

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.def_value


lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

print(lst[1])        #should return 3
print(lst[333000])   #should return 'def'
lst.extend([3, 23, 'hello', 'lists', 'word', 344])

print(lst[9])       #should return 'lists'
print(lst[11])      # should return 344
print(lst[12])      # should return 'def'
lst.append(233344455)
print(lst[12])      # 233344455
print(lst[100])     # 'def'
lst.remove(2)
lst.remove(1)
lst.remove(3)

lst.insert(-3, 34.34)
print(lst[8])       # 'word'
print(lst[10])      # 233344455




