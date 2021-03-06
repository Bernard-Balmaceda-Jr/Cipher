#!/usr/bin/env python2.7

from CipherVigenere import *
from CipherEnigma import *
import unittest


def main():
    print('Vigenere Encrpytion Program - Initialised\n')
    my_cipher = CipherVigenere()
    my_cipher.cipher_matrix()
    print(my_cipher.msg_encryption('We are Anonymous. We do not forgive. We do not forget. Expect us.'))
    print(my_cipher.msg_decryption(';ssGPF7UBWTWNBOG9q?F7xCsTMU7zCZMGWr	8}KiEBeBWZiGBLuMZlRRDMIRlHM`'))

    # my_enigma = CipherEnigma()
    # my_enigma.cipher_matrix()

    # print('Enigma Cipher')
    # my_cipher = CipherEnigma()
    # my_cipher.test()

    unittest.main()


if __name__ == '__main__':
    main()
