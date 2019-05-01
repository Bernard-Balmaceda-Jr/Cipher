#!/usr/bin/env python2.7

from CipherVigenere import *


def main():
    print('Vigenere Encrpytion Program - Initialised\n')

    my_cipher = CipherVigenere()
    my_cipher.cipher_matrix()

    my_cipher.msg_encryption('We are Anonymous')
    my_cipher.msg_decryption(';ssGPF7UBWTWNBOG')


if __name__ == '__main__':
    main()
