#input two sentences
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

#split the sentences into words and create a set of unique words
words1 = set(sentence1.split())
words2 = set(sentence2.split())

#find common words (interaction)
common_words = words1 & words2

#find unique words in each sentence
unique_words = words1 ^ words2

print("set1 (words in sentence1): ", words1)
print("set2 (words in sentence2): ", words2)
print("Common words: ", common_words)
print("Unique words: ", unique_words) 