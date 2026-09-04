# Nested Lists & List Methods

student = [
    "Jagadeesh",
    22,
    ["Python", "AI", "LLMs", "Git"]
]

print(student)

# Access Nested List
print(student[2])

print(student[2][0])
print(student[2][1])

# Slicing
print(student[2][:2])

# Update Nested List
student[2][2] = "Machine Learning"

print(student)

# Append
student[2].append("Agentic AI")

# Insert
student[2].insert(1, "GitHub")

# Extend
student[2].extend(["Prompt Engineering", "RAG"])

print(student)

# Count
print(student[2].count("Python"))

# Index
print(student[2].index("Agentic AI"))

# Copy
courses = student[2].copy()

print(courses)

# Sort Example
numbers = [45, 12, 67, 8, 22]

numbers.sort()

print(numbers)

numbers.reverse()

print(numbers)
