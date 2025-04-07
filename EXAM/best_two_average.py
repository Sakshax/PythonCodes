# Program to calculate the average of the best two test marks out of three

# Accept three test marks from the user
mark1 = float(input("Enter test mark 1: "))
mark2 = float(input("Enter test mark 2: "))
mark3 = float(input("Enter test mark 3: "))

# Store the marks in a list
marks = [mark1, mark2, mark3]

# Sort the list in descending order so the best marks come first
marks.sort(reverse=True)

# Calculate the average of the two highest marks
best_two_average = (marks[0] + marks[1]) / 2

# Display the result
print("Average of the best two test marks:", best_two_average)
