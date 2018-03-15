""" Program-10 : To demonstrate use of tuple, set& related functions """
# Creating a tuple
my_tuple= () 
print("empty tuple ",my_tuple)

# Tuple having integer
my_tuple = (1,2,3,4)
print("Tuple of integer",my_tuple)

# Tuple containing mix value
my_tuple = (1,'hello',4.6)
print("Tuple of containing mix values ",my_tuple)

# Neasted tuple
my_tuple = ("mouse",(8,7,9),[4,6,8,9])
print("Neasted tuple ",my_tuple)

# Tuple packing
my_tuple = 3,4.6,"cat"
print("Tuple packing ",my_tuple)

# Tuple unpacking
a, b, c = my_tuple
print(a)
print(b)
print(c)

# Accessing Tuple element
my_tuple = 'p','q','r','s','t','u','v' 
print(my_tuple[0])
print(my_tuple[6])

# Neasted tuple Accessing
my_tuple = ("mouse",(8,7,9),[4,6,8,9])
print(my_tuple[0][3])
print(my_tuple[1][1])

# Deleting in truple
my_tuple = 'p','q','r','s','t','u','v'
del my_tuple
my_tuple