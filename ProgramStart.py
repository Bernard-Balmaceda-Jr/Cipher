#!/usr/bin/env python2.7

from CipherVigenere import *
from CipherEnigma import *


def main():
    print('Vigenere Encrpytion Program - Initialised\n')

    my_cipher = CipherVigenere()
    my_cipher.cipher_matrix()

    my_cipher.msg_encryption('We are Anonymous')
    my_cipher.msg_decryption(';ssGPF7UBWTWNBOG')

    # my_enigma = CipherEnigma()
    # my_enigma.cipher_matrix()

    print('Enigma Cipher')
    my_cipher = CipherEnigma()
    my_cipher.test()


if __name__ == '__main__':
    main()
