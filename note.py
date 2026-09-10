import os

print("=== Study Notes Organizer ===")

science_notes = [
    "Science: Photosynthesis is the process by which plants make food.",
    "Science: Plants need sunlight, water, and carbon dioxide.",
    "Science: The human body has 206 bones."
]

maths_notes = [
    "Maths: A triangle has three sides.",
    "Maths: The area of a rectangle is length multiplied by width.",
    "Maths: A right angle is 90 degrees."
]

with open("science-notes.txt", "w") as f:
    for note in science_notes:
        f.write(note + "\n")

with open("maths-notes.txt", "w") as f:
    for note in maths_notes:
        f.write(note + "\n")

print("Two subject notes files created.")



print("\n=== Science Notes ===")

with open("science-notes.txt", "r") as f:
    science_content = f.read()
    print(science_content)


print("=== Maths Notes ===")

with open("maths-notes.txt", "r") as f:
    maths_content = f.read()
    print(maths_content)




print("=== Word Count ===")

science_words = science_content.split()
maths_words = maths_content.split()

print("Science:", len(science_words), "words")
print("Maths:", len(maths_words), "words")
merged_file = "study-notes.txt"

if os.path.exists(merged_file):
    print("\nMerged file already exists.")

    os.remove(merged_file)
    print("Old merged file removed.")
else:
    print("\nNo old merged file found.")

with open(merged_file, "w") as output:

    output.write("========== STUDY NOTES ==========\n\n")

    output.write("========== SCIENCE ==========\n")

    with open("science-notes.txt", "r") as f:
        for line in f:
            output.write(line)

    output.write("\n========== MATHS ==========\n")

    with open("maths-notes.txt", "r") as f:
        for line in f:
            output.write(line)


print("\nStudy notes successfully merged!")

print("\n=== Final Study Notes ===")

with open(merged_file, "r") as f:
    print(f.read())
