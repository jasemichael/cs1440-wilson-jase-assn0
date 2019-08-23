# CS 1440 Assignment 0 Instructions

## Description

![Caesar Cipher](doc/Caesar_substition_cipher.png)

> "The Caesar cipher is one of the earliest known and simplest ciphers. It is a
> type of substitution cipher in which each letter in the plaintext is
> 'shifted' a certain number of places down the alphabet. For example, with a
> shift of 1, A would be replaced by B, B would become C, and so on. The method
> is named after Julius Caesar, who apparently used it to communicate with his
> generals."
> 
> [Practical Cryptography](http://practicalcryptography.com/ciphers/caesar-cipher/%C2%A0)

The Wikipedia article on the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher/) offers more information about this simple cipher.

I introduce two pieces of Cryptography jargon to facilitate our discussion of your assignment:

-   **Plaintext**: The original, human-readable message
-   **Ciphertext**: The result of applying a cipher to a plaintext message

Observe the effect of the Caesar cipher of various rotation offsets upon the alphabet:

Rotation of 1 position (rot1)

	plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
	ciphertext: BCDEFGHIJKLMNOPQRSTUVWXYZA

Rotation of 5 positions (rot5)

	plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
	ciphertext: FGHIJKLMNOPQRSTUVWXYZABCDE

Rotating the rot5 ciphertext by 21 positions decrypts it

	ciphertext: FGHIJKLMNOPQRSTUVWXYZABCDE
	plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ


## Requirements

Submit your work in a git repository created by cloning this starter code.
Your repository must have at least **five (5)** commits in your name in
addition to the commits that I made to it.  Use the `git log` command to make
sure that you have enough.

Write a program which applies the Caesar Cipher to a text file of the user's
choice.

Present to the user a main menu with options to process a file or exit.  When
the user chooses to process a file they are prompted to input the name of a
file.  When the file does not exist or cannot be read print a message to this
effect and return to the main menu.  The main menu is repeated when the user
enters invalid input.

When the file is readable the user is prompted for a rotation distance to use
to decode the file.  The rotation distance must be an integer in the range [0,
25] The user may also instruct the program to perform all 26 possible rotations
by entering a special value of your choosing.

Print an error message when the user provides invalid input and return to the
main menu.

Before the program prints the deciphered text it prints a banner indicating the
rotation distance used.  When running through all possible rotations this
banner is repeated 26 times.  The user can scroll through the output to find
the plaintext; the banner will inform the user which one of the possible
rotations was the "key".

Rotate the text in the file by iterating over the file one character at a time.
When a letter is encountered turn it into a number, add the rotation distance,
convert it back into a letter, and print it.  There is a trick (which you must
discover for yourself) to employ when adding the rotation distance would take
you past the end of the alphabet.  The program must *not* modify non-alphabetic
characters, but print them out unchanged.

After the program performs the desired operation control returns to the main
menu.
