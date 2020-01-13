#!/usr/bin/python3

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
        # implement try catch
        return file

    def askRotation(self):
        rot = input("Rotation distance (0-25 or *)> ")
        if rot == "*":
            rot = 25
        rot = int(rot)
        while (rot > 25 and rot < 0):
            print("That is not a valid rotation!")
            rot = input("Rotation distance (0-25 or *)> ")
            if rot == "*":
                rot = 25
            rot = int(rot)
        return rot

    def printf(self):
        file = self.askFile()
        rot = self.askRotation()
        c = Cipher(file, rot)
        c.decode()

class Cipher:
    def __init__(self, file, rot):
        self.__file = file
        self.__rotations = rot

    def getRotations(self):
        return self.__rotations

    def getFile(self):
        return self.__file

    def decode(self):
        LOWER = "abcdefghijklmnopqrstuvwxyz"
        UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(f'Decoding {self.getFile()}...')

    def display(self):
        pass

def main():
    m = Menu()
    while True:
        m.prompt()
        m.run()

main()