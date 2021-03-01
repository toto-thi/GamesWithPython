"""
Homework Assignment #8: Input and Output (I/O)

Details:

Create a note-taking program. When a user starts it up, it should prompt them for a filename.

If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file.

Extra Credit:

Allow the user to select a 4th option:
D) Replace a single line

If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:

1) The line number they want to update.

2) The text that should replace that line.
"""

# BEGIN

count = 0
max = 5
notes = {}

while (count < max):
    FileName = str(input("Please enter file name: "))

    if FileName in notes.keys():
        print("This file is valid. \n")
        print("Please select an options: \n1. Read \n2. Delete & start over \n3. Append the file")
        option = int(input("Option: "))

        if option == 1:
            displayFile = open(FileName, "r")
            tempData = []

            for line in displayFile:
                tempTest = line.strip("\n").split()
                print(tempTest)
                tempData.append(tempTest)
            print(tempData)
            displayFile.close()
        elif option == 2:
            displayFile = open(FileName, "w")
            tempData = {}
            for t in range(1):
                tempNote = []
                date = input("Please enter date: ")
                tempNote.append(date)
                title = input("What title: ")
                tempNote.append(title)
                detail = input("Details: ")
                tempNote.append(detail)

                tempData = tempNote
            notes[FileName] = tempData

            for data in tempNote:
                displayFile.write(str(data))
                displayFile.write(", ")
            displayFile.write("\n")
            print(notes)
            displayFile.close()
        elif option == 3:
            displayFile = open(FileName, "a")

            text = str(input("Enter text to add to file: "))
            displayFile.write(text + ", ")
            print(notes)
            displayFile.close()

        else:
            print("Wrong entry, try again please.")

        count += 1
        print("Number of entries: ", count)
    else:
        # if no file excisted do here
        Noted = {}
        MakeNote = open(FileName, "w")
        for t in range(1):
            tempNote = []
            date = input("Please enter date: ")
            tempNote.append(date)
            title = input("What title: ")
            tempNote.append(title)
            detail = input("Details: ")
            tempNote.append(detail)

            Noted = tempNote

        notes[FileName] = Noted
        print(Noted)

        for data in Noted:
            MakeNote.write(str(data))
            MakeNote.write(", ")

        MakeNote.write("\n ")

        print(notes)
        MakeNote.close()
        count += 1
        print("Number of entries: ", count)
