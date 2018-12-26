#Write a simple Rectangle class. It should do the following:

    #Accepts length and width as parameters when creating a new instance
    #Has a perimeter method that returns the perimeter of the rectangle
    #Has an area method that returns the area of the rectangle
    #Don't worry about coordinates or negative values, etc.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle_1 = Rectangle(4,5)
print('Area of rectangle:', rectangle_1.area())
print('Perimeter of rectangle: ', rectangle_1.perimeter())

#Python provides several modules to allow you to easily extend some of the basic
#objects in the language. Among these modules are UserDict, UserList, and
#UserString. (Refer to the chart in Topic 10.3 to see what the methods you need
#to override look like. Also, since UserDict and UserList are part of the
#collection module, you can import them using from collections import UserDict
#and from collections import UserList.)

#Using the UserList module, create a class called Ulist, and override the
#__add__, append, and extend methods so that duplicate values will not be added
#to the list by any of these operations.

from collections import UserList

class Ulist(UserList):
    def __add__(self, value = []):
        for item in value:
            if item not in self.data:
                self.data = self.data + [item]
        return self.data

    def append(self, value = None):
        if value not in self.data:
            self.data.append(value)

    def extend(self, value = []):
        for item in value:
            if item not in self.data:
                self.data.extend([item])


my_list = Ulist([1,2,3])
my_list.__add__([2,8,1])
my_list.append(1)
my_list.append(9)
print('List after append:',my_list.data)
my_list.extend([2,10])
print('List after extend:',my_list.data)



#(Extra Credit) Using the UserDict module, create a class called Odict, which
#will be just like a dictionary but will "remember" the order in which key/value
#pairs are added to the dictionary.
#(Hint: Override the built-in __setitem__ method.)
#Create a new method for the Odict object called okeys, which will return the
#ordered keys.
#Create the dictionary. Add all the keys into a list as the key gets added into the
# dictionary.
from collections import UserDict

class Odict(UserDict):

    def __init__(self):
        super().__init__(self)
        self.keylist = []

    def __setitem__(self, key, value):
        self.data[key] = value
        self.keylist.append(key)

    def okeys(self):
        return self.keylist

my_dict = Odict()
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3
print('Dictionary:',my_dict.data)
print('Ordered Keys:',my_dict.okeys())
