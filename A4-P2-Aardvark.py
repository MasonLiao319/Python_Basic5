#Program 2 – The Itsy Bitsy Aardvark
#Description: Design and develop a program that presents the user with a “Mad Libs” type game, where a random 
# choice of words are read from a file, then interjected into a story read from another file.

#Student #: w0424837    
#Student Name:  Mason Liao

# YOUR CODE STARTS HERE, each line must be indented (one tab)
def readStoryFromFile(p_fileName):
    """Read data from the specified file path"""
    with open(p_fileName, "r") as myFile:
        content = myFile.read()
    return content


def readDataFromCSVFile(p_fileName):
    '''Reads data from the specified file path, into a 2d list,which is returned'''
    my2DList = []
    with open(p_fileName,"r") as dndFile:
        import csv
        fileData = csv.reader(dndFile)
        for row in fileData:
            my2DList.append(row)

    return my2DList


def getValidChoice():
    """Get a valid multiple-choice answer from the user."""
    validChoices = ["a", "b", "c", "d", "e"]
    while True:
        userInput = input("Enter your choice (a-e): ").lower()
        if userInput in validChoices:
            return userInput
        else:
            print("Invalid choice. Please enter a-e.")


def main():
    # Print the title of the story
    print("The Isty Bitsy Aardvark")

    # Read the choices from the CSV file
    choicesList = readDataFromCSVFile("the_choices_file.csv")

    # Collect user choices
    userChoices = []
    for describe in range(len(choicesList)):
        print("\nPlease choose {0}:".format(choicesList[describe][0]))   
        index = 0

        # Display choices with corresponding letters (a-e)
        for choice in range(1,len(choicesList[describe])):    
                letter = chr(index + 97)
                print("{0}) {1}".format(letter,choicesList[describe][choice]))
                index += 1
        userChoice = getValidChoice()
        userChoices.append(userChoice)  # Store user choices in userChoices list
                
    # Read the story from the file
    story = readStoryFromFile("the_story_file.txt")
    index = 1
    for describe in range(len(choicesList)):
        userChoice = userChoices[describe]
        placeholder = "_{0}_".format(index)

        # Replace placeholders in the story with user choices
        story = story.replace(placeholder, choicesList[describe][ord(userChoice) - 97 + 1].upper()) 
        index += 1


    # Display the completed story
    print("\nYour Completed Story:\n")
    print(story)




    # YOUR CODE ENDS HERE

main()