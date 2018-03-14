""" Program-5-a : To add 'ing' at the end of a given string (length should be at least 3). If the
given string already ends with 'ing' then add 'ly' instead. If the string length of
the given string is less than 3, leave it unchanged."""

a = input("Please enter the string  ")
str1, str2 = 'ly', 'ing'
if len(a) >= 3:
    slic = a[-3:]    # slicing from the end of the string
    print(slic)
    if (slic == "ing"):
        a += str1    # Adding string in last 'ly'
    else:
        a +=str2     # Adding string in last 'ing' 

print(a)