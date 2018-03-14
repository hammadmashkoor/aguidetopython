""" Program-7 :Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them
alphanumerically."""

s =input()
words = [word for word in s.split(" ")]  # Split the words that with whitespace
print(" ".join(sorted(list(set(words))))) # jion the words after sorting the by space