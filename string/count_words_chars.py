def count_words_and_characters(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    return word_count, char_count

text = input("Enter a sentence: ")
words, chars = count_words_and_characters(text)
print(f"📝 Words: {words}")
print(f"🔡 Characters: {chars}")
