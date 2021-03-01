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
