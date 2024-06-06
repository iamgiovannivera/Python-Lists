# 2. Advanced List Methods and Identity Operators 



# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]

# both_submitted_and_attended = list(set(submitted) & set(attended))
# print("Students who both submitted their assignments and attended the class:", both_submitted_and_attended)

# print("-----------------------")

# are_identical = set(submitted) == set(attended)
# print("Are the two lists identical regardless of order?", are_identical)

# print("-----------------------")

# attended = [student for student in attended if student in submitted]
# print("Attended list after removing those who did not submit their assignment:", attended)