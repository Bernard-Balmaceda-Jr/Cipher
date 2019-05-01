#!/usr/bin/env python2.7

from Cipher import *
from CipherVigenere import *


def main():
    print('Vigenere Encrpytion Program - Initialised')

    my_cipher = CipherVigenere()
    my_cipher.cipher_matrix()

    my_cipher.msg_encryption('We are Anonymous')


if __name__ == '__main__':
    main()
