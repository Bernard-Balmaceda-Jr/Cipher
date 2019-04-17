#!/usr/bin/env python2.7


class Cipher:
    def __init__(self):
        self._plain_text = 'plain_text'
        self._keyword = 'keyword'
        self._datagram = 'datagram'

    def print_msg(self):
        print("cipher test")
        print(self._plain_text)
        print(self._keyword)
        print(self._datagram)

