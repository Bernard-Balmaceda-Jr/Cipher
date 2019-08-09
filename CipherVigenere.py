#!/usr/bin/env python2.7
import string
import unittest


class CipherVigenere:
    def __init__(self):
        self._cipher_matrix = []
        self._data_set_length = 0

    def cipher_matrix(self, args=None):
        data_set = []

        #   1. pass cipher characters
        if args is None:
            for x in string.printable:
                data_set.append(x)
        elif args is not None:
            for x in args:
                data_set.append(x)

        #   2. create cipher matrix first row
        self._cipher_matrix.append(data_set[:])
        self._data_set_length = len(self._cipher_matrix[0])

        #   3. create all rows with shift
        counter = len(data_set)-1
        while counter != 0:
            data_set.append(data_set.pop(data_set.index(data_set[0])))
            self._cipher_matrix.append(data_set[:])
            counter -= 1

        #   4. verify cipher matrix
        # for x in self._cipher_matrix:
        #     print(x)

    def msg_encryption(self, args):
        cipher_matrix = self._cipher_matrix[:]
        columns = self._cipher_matrix[0][:]
        msg = args
        keyword = 'keyword'
        encrypted_msg = []

        msg_counter = 0
        keyword_counter = 0

        #   1. todo: comments to reflect algorithm
        while msg_counter != len(msg):
            for x in cipher_matrix:
                if x[0] == msg[msg_counter]:
                    for y in columns:
                        if y == keyword[keyword_counter]:
                            encrypted_msg.append(x[columns.index(y)])

            if keyword_counter < len(keyword) - 1:
                keyword_counter += 1
            elif keyword_counter >= len(keyword) - 1:
                keyword_counter -= len(keyword) -1

            msg_counter += 1

        s = ""
        s = s.join(encrypted_msg)
        # print(s)
        return s

    def msg_decryption(self, args):
        cipher_matrix = self._cipher_matrix[:]
        columns = self._cipher_matrix[0][:]
        msg = r'' + args
        keyword = 'keyword'
        decrypted_msg = []

        msg_counter = 0
        keyword_counter = 0

        #   1. todo: comments to reflect algorithm
        while msg_counter != len(msg):
            for x in cipher_matrix:
                if x[0] == keyword[keyword_counter]:
                    for y in x:
                        if y == args[msg_counter]:
                            decrypted_msg.append(columns[x.index(y)])

            if keyword_counter < len(keyword) - 1:
                keyword_counter += 1
            elif keyword_counter >= len(keyword) - 1:
                keyword_counter -= len(keyword) -1

            msg_counter += 1

        s = ""
        s = s.join(decrypted_msg)
        # print(s)
        return s

class TestCipherVigenere(unittest.TestCase):
    def test_msg_encryption(self):
        plain_msg = "We are Anonymous."
        encoded_msg = ';ssGPF7UBWTWNBOG9'

        cv = CipherVigenere()
        cv.cipher_matrix()
        self.assertEquals(cv.msg_encryption(plain_msg), encoded_msg)

    def test_msg_decryption(self):
        plain_msg = 'We are Anonymous.'
        encoded_msg = ';ssGPF7UBWTWNBOG9'

        cv = CipherVigenere()
        cv.cipher_matrix()
        a=cv.msg_decryption(encoded_msg)
        self.assertEquals(a, plain_msg)

