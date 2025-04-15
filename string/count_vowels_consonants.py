def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in text if char in vowels)
    c_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return v_count, c_count

text = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(text)
print(f"🗣️ Vowels: {vowels}, 🧱 Consonants: {consonants}")
