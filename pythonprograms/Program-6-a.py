""" Program-6-a : To compute the frequency of the words from the input. The output should
output after sorting the key alphanumerically."""

def word_count(str):
    counts = dict()
    words = str.split(" ")
   # sorted(list(set(words)))
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    sorted(list(set(counts)))
    return counts

print(word_count('the quit values for others values'))