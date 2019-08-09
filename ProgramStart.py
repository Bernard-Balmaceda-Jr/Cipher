#!/usr/bin/env python3.7

from CipherVigenere import *
from CipherEnigma import *


def main():
    print('Vigenere Encrpytion Program - Initialised\n')

    my_cipher = CipherVigenere()
    my_cipher.cipher_matrix()


    my_cipher.msg_encryption('We are Anonymous. We do not forgive. We do not forget. Expect us.')
    my_cipher.msg_decryption(';ssGPF7UBWTWNBOG9q?F7xCsTMU7zCZMGWr	8}KiEBeBWZiGBLuMZlRRDMIRlHM`')

    # text = input("Enter text to encrypt")
    # my_cipher.msg_encryption(text .format(r''))
    # my_cipher.msg_decryption("e+MqySreoVULZzII!qUF7uFMqJFtCCV")


    my_enigma = CipherEnigma()
    my_enigma.cipher_matrix()

    # print('Enigma Cipher')
    # my_cipher = CipherEnigma()
    # my_cipher.test()


if __name__ == '__main__':
    main()
