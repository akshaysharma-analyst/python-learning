# Project- Study Notes App
note = input("Write a study note: ")
path = "/Users/msd/Desktop/study_notes.txt"
with open(path, "w") as file:
    file.write(note)
with open(path, "r") as file:
    content = file.read()
print("Saved note:")
print(content)
