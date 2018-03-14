""" Program-8 : To demonstrate use of list & related functions"""

fish = ['apple', 'white', 'logic', 'math'] # Defining the list with initial value 
# append function in list
fish.append('develop')      # Adding element at the end of the list
print(fish)

# Insert function in list
fish.insert(1,'computer')
print(fish)

# Extend function in list
more_fish = ['goby', 'herring','ide']
fish.extend(more_fish)
print(fish)

# Remove function in list
fish.remove('math')
print(fish)