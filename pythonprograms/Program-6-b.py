"""Program-6-b : Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically."""

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]  # It is finding the words seprated with ,
print(",".join(sorted(list(set(words)))))    # Now sort the list and print