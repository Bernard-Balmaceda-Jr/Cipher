#!/usr/bin/env python2.7


class Cipher:
    def __init__(self):
        self._all_data_sets = []

    def print_msg(self):
        data_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        #   1. add data_set to all_data_sets
        self._all_data_sets.append(data_set[:])

        #   2. create data set matrix
        counter = 25
        while counter != 0:
            data_set.append(data_set.pop(data_set.index(data_set[0])))
            # print(data_set)
            self._all_data_sets.append(data_set[:])
            counter -= 1

        #   3. visual inspection of matrix
        for x in self._all_data_sets:
            print(x)

    def reorder_data_sets(self, args):
        result = args.append(args.pop(args.index(args[0])))
        return result

