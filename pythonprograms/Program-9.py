""" Program-9 : To demonstrate use of Dictionary & related functions """
# How to create Dictionary
# empty dictionary
my_dict = {}
print("Empty Dictionary ",my_dict)

# Dictionary with integer keys
my_dict = {1:'apple', 2:'ball'}
print("Element in dictionary with integer keys ",my_dict)

# Dictionary with mixed keys
my_dict = {'name':'john',1:[1,2,3]}
print("Mixed key",my_dict)

# Use dict()
my_dict = dict({1:'apple',2:'ball'})
print("dict function ",my_dict)

# How to access element from dictionary
my_dict = {'name':'john',1:[1,2,3]}
print("Access of element in dictionary ",my_dict['name'])

""" how to change the element from dictionary
 Modify element of the dictionary
 """
my_dict = {'name':'John','age':26}
my_dict['age'] = 27
print("Modify element ",my_dict)

# add new element in dictionary
my_dict['address'] = 'Downtown'
print("Add element in dictionary",my_dict)

# How to delete element from the dictionary
# Remove perticular element
my_dict = {'name':'John','age':26,'address':'Downtown',1:4}
print("Delete particular element from dictionary ")
print(my_dict.pop('address')) 

# use of popitem
print(my_dict.popitem())

# delete an element
del my_dict['name']
print(my_dict)

# To clear all the element from dictionary
print(my_dict.clear())

# how to delete dictionary
del my_dict
print(my_dict)
