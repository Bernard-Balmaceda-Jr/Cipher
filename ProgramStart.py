#!/usr/bin/env python2.7

from Cipher import *


def main():
    print('Program Starting:')
    my_cipher = Cipher()
    my_cipher.create_cipher()
    my_cipher.create_keyword_dataset()

    my_cipher.encode_text_msg('programming')


if __name__ == '__main__':
    main()
