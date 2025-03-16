def get_vowels(sentence):
    return set(sentence) & {'a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O' , 'U'}

#input
sentence = input("Enter a sentence: ")
print("Vowels in the sentence are: ", get_vowels(sentence))
