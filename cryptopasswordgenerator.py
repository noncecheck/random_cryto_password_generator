#Author: ARUN MOOTHEDATH
#Email: curtissoflow@gmail.com
#Date: 06/16/2022
#Description - A simple script to create random crypto passwords
import string
import secrets

def GenerateCryptoPassword(plength):
    characters = string.digits+string.ascii_letters+string.punctuation+string.octdigits
    new_random_password = ''.join(secrets.choice(characters) for i in range(plength))
    return new_random_password

def main():
    plength = input("Please enter the password length: ")
    plength = int(plength)
    print("New Passowrd: ", GenerateCryptoPassword(plength))
main()