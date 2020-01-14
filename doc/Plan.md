# 1. Requirements
Create a program that applies a Caesar Cipher to text file of user's choice. 
* Create a main menu that governs the process of the Caesar Cipher. 
* The user can input how much the text is rotated (0-25 or 26 with *). 
* Displays, depending on rotations, a banner of rotations.
* User can scroll through and find deciphered plaintext with given key.
* Rotates text in file one char at a time until text is decoded then returns to menu.

# 2. Design
## main()
This function encompasses the classes and functions used to build the Caesar Cipher.
main() will regulate the flow and control of the program. 
## Menu
The menu will be created as the Menu class. The menu acts as a terminal.
* Data Members:
    * command holds the user's selected command. The command resets to None after execution.
* Methods:
    * A display method will be used to show the user options and essentially act as the user's guide.
    * A prompt method will be used to capture user's input.
    * A run method will run the user's desired command.
    * An askFile and askRotation will be used to receive input for filename and the amount of rotations. 
    * A printf method instantiates the Cipher class and runs the decode.
## Cipher
 The Cipher class will be used to decode messages.
 * Data Members:
    * rotations holds an int of the amount of rotations.
    * file holds a string value of the name of the file that will be used to decode.
    * text holds the decoded string text.
 * Methods:
    * A constructor which initializes data members.
    * A getRotations method will prompt for the number of rotations.
    * A getFile method will prompt the user for file input.
    * A openFile method will manage opening the user's files and returning the opened file.
    * A decode method will decode the message.
    * A display method will show the decoded results.
# 3. Implementation 
# 4. Validation
## Unit Tests
This idea of validation allows the process to be automated.
> Tests include:
>* validating the methods
>* validating output based on input
## Logging
* Display statement/expression output using print().
## Brute Force
This idea of validation requires plugging and checking if errors occur.
* Input of non-alphabetic characters into console.
* Multiple times tested.
