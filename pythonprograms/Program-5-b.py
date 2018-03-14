""" Program-5-b : To get a string from a given string where all occurrences of its first char have
been changed to '$', except the first char itself."""
def change_char(str1):
    char = str1[0]          # find the first later of the string
    length = len(str1)      # length of the string
    str1 = str1.replace(char, '$') # Replace the all the character of string which has str1
    str1 = char + str1[1:]         # Append first string with original char
    return str1

str = input("Enter the string ")
print(change_char(str))     # function call with argument