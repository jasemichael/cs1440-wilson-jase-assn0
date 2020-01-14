#!/usr/bin/python3
from unittest import TestCase

print("Pnrfne Pvcure!")

class Menu:
    def __init__(self):
        self.__command = None

    def display(self):
        print("""
P)rint a file
E)xit""")

    def prompt(self):
        self.display()
        command = input("?> ")
        command = command[0:1]
        while command not in ("E", "e", "p", "P"):
            print("That is not a valid command!")
            self.display()
            command = input("?> ")
            command = command[0:1]
        self.__command = command.casefold()

    def run(self):
        if self.__command == "p":
            self.printf()
        elif self.__command == "e":
            exit()
        self.__command = None

    def askFile(self):
        file = input("\nEnter the name of a file> ")
        try:
            fin = open(file,"r")
            fin.close()
        except:
            print("\nThere was an error opening your file!")
            return False
        return file

    def askRotation(self):
        rot = input("Rotation distance (0-25 or *)> ")
        if rot == "*":
            rot = 25
        rot = int(rot)
        while (rot > 25 or rot < 0):
            print("\nThat is not a valid rotation!")
            return False
        return rot

    def printf(self):
        file = self.askFile()
        if file:
            rot = self.askRotation()
            if rot or rot == 0:
                for r in range(rot+1):
                    print("\nRotation " + str(r) + ":")
                    c = Cipher(file, r)
                    c.decode()
                    c.display()
                    del c

class Cipher:
    def __init__(self, file, rot):
        self.__file = file
        self.__rotations = rot
        self.__text = ""

    def getRotations(self):
        return self.__rotations

    def getFile(self):
        return self.__file

    def openFile(self):
        fin = open(self.__file, "r")
        return fin

    def decode(self):
        LOWER = "abcdefghijklmnopqrstuvwxyz"
        UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print('Decoding...')
        char = " "
        file = self.openFile()
        while char != "":
            char = file.read(1)
            if char == "":
                break
            if char in LOWER: #char is lowercase
                index = LOWER.index(char)
                if (index + self.getRotations()) > 25: #reset index
                    index = (index + self.getRotations()) - 26
                else:
                    index += self.getRotations()
                self.__text += LOWER[index]
            elif char in UPPER: #char is uppercase
                index = UPPER.index(char)
                if (index + self.getRotations()) > 25: #reset index
                    index = (index + self.getRotations()) - 26
                else:
                    index += self.getRotations()
                self.__text += UPPER[index]
            else: #character is not alpha
                self.__text += char
        file.close()

    def display(self):
        print(self.__text)

def main():
    m = Menu()
    while True:
        m.prompt()
        m.run()

main()