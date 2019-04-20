#!/usr/bin/env python2.7


class Cipher:
    def __init__(self):
        self._all_data_sets = []
        self._data_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self._keyword_data_set = []
        self._keyword = 'keyword'

    def create_cipher(self):
        data_set = self._data_set[:]

        #   1. add data_set to all_data_sets
        self._all_data_sets.append(data_set[:])

        #   2. create data set matrix
        # counter = 25
        counter = len(data_set)-1
        while counter != 0:
            data_set.append(data_set.pop(data_set.index(data_set[0])))
            # print(data_set)
            self._all_data_sets.append(data_set[:])
            counter -= 1

        #   3. visual inspection of matrix
        # for x in self._all_data_sets:
        #     print(x)

    def create_keyword_dataset(self):
        data_sets = self._data_set[:]
        keyword = self._keyword[:]
        self._keyword_data_set = []

        #   1. create keyword dataset
        data_set_counter = len(data_sets)
        keyword_counter = 0

        while data_set_counter != 0:
            if keyword_counter > -1 and keyword_counter < 6:
                self._keyword_data_set.append(keyword[keyword_counter])
                data_set_counter -= 1
                keyword_counter += 1
            elif keyword_counter >= 6:
                self._keyword_data_set.append(keyword[keyword_counter])
                data_set_counter -= 1
                keyword_counter -= 6

    def encode_text_msg(self, args):
        #   1. local variables
        local_columns = self._data_set
        local_msg = args
        local_cipher = self._all_data_sets[:]
        local_keyword = self._keyword[:]
        local_keyword_dataset = self._keyword_data_set[:]
        encoded_msg = []

        print(local_msg)
        print(local_keyword)
        print(local_columns)
        # print(local_cipher)
        print(local_keyword_dataset)

        #   2. transcribe to correct dataset
        # counter = 0
        # while counter != len(local_msg):
        #     print(local_msg[counter])
        #     counter += 1

        # test = 'p'
        # for x in local_cipher:
        #     if x[0] == test:
        #         print(x)

        counter = 0
        keyword_counter = 0
        while counter != len(local_msg):
            for x in local_cipher:
                if x[0] == local_msg[counter]:
                    print(x)

                    #   1. find keyword index
                    for y in local_columns:
                        if y == local_keyword[keyword_counter]:
                            print(y)

                    #   2. encrypt with keyword

            if keyword_counter < 6:
                keyword_counter += 1
            elif keyword_counter >= 6:
                keyword_counter -= 6
            counter += 1




        # for x in local_msg:



        #   3. translate to correct letter

