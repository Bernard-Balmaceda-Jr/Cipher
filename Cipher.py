#!/usr/bin/env python2.7


class Cipher:
    def __init__(self):
        self._plain_text = 'plain_text'
        # self._keyword
        self._datagram = []
        self._rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def print_msg(self):
        print("cipher test")

        self._datagram = []
        new_row = []
        loop_count = len(self._rows)
        while loop_count != 0:
            for x in self._rows:
                new_row.append(x)
            self._datagram.append(new_row)
            loop_count -= 1
            new_row = []

        for x in self._datagram:
            print(x)

        print('finished')
