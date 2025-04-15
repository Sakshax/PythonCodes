def all_substrings(text):
    substrings = []
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            substrings.append(text[i:j])
    return substrings

text = input("Enter a string: ")
print("🔎 Substrings:")
for s in all_substrings(text):
    print(s)
