#!/usr/bin/env python2.7
import string


class CipherEnigma:
    def __init__(self):
        """
        Commercial Enigma Cipher lol
        """
        #   Ref:
        #   A,  B,  C,  D,  E,  F,  G,  H,  I,  J,  K,  L,  M,  N,  O,  P,  Q,  R,  S,  T,  U,  V,  W,  X,  Y,  Z
        #   0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25

        #   1. Steckerverbindungen:
        #   Plugboard input
        self._plugboard = [
            {'P', 'O'},
            {'M', 'L'},
            {'I', 'U'},
            {'K', 'J'},
            {'N', 'H'},
            {'Y', 'T'},
            {'G', 'B'},
            {'V', 'F'},
            {'R', 'E'},
            {'A', 'C'}
        ]    # PO ML IU KJ NH YT GB VF RE AC

        #   2. Ringstellung:
        #   Rotor wiring
        self._rotor_i = 2
        self._rotor_ii = 15
        self._rotor_iii = 6
        self._reflector = 0

        #   TODO: Turn over notch
        self._rotor_i_notch = 'Q'
        self._rotor_ii_notch = 'E'
        self._rotor_iii_notch = 'V'

        #   3. TODO: Umkehrwalze: Reflector

        #   4. TODO: rotor shift

        #   5. Python initialisation
        self._ref_chars = []
        self._cipher_matrix = []
        self.cipher_matrix()
        self._enigma_cipher = []

    def steckerverbindungen(self, list):
        """     Plug-Ubersetzungen anwenden     """
        temp_data_set = list[:]

        for x, y in self._plugboard:
            a, b = temp_data_set.index(x), temp_data_set.index(y)
            temp_data_set[b], temp_data_set[a] = temp_data_set[a], temp_data_set[b]

        return temp_data_set

    def cipher_matrix(self):
        """     creates cipher matrix      """
        for char in string.ascii_uppercase:
            self._ref_chars.append(char)

        data_set = self._ref_chars[:]
        # data_set = list[:]
        temp_data_set = [data_set[:]]

        counter = len(data_set)-1

        while counter != 0:
            data_set.append(data_set.pop(data_set.index(data_set[0])))
            temp_data_set.append(data_set[:])
            counter -= 1

        self._cipher_matrix = temp_data_set[:]

    def ringstellung(self, pos):
        """     Ringposition anwenden       """
        return self._cipher_matrix[pos]


    def reflecktor(self):
        pass

    def test(self):
        #   1. plain text
        plain_text = ['A', 'N', 'O', 'N', 'Y', 'M', 'O', 'U', 'S']
        self._enigma_cipher.append(self._ref_chars[:])

        #   2. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[0]))

        #   3. ringstellung III
        self._enigma_cipher.append(self.ringstellung(self._rotor_iii))

        #   4. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   5. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   6. ringstellung II
        self._enigma_cipher.append(self.ringstellung(self._rotor_ii))

        #   7. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   8. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   9. ringstellung I
        self._enigma_cipher.append(self.ringstellung(self._rotor_i))

        #   10. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   11. Todo: Reflektor

        #   12. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   13. ringstellung I
        self._enigma_cipher.append(self.ringstellung(self._rotor_i))

        #   14. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   15. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   16. ringstellung I
        self._enigma_cipher.append(self.ringstellung(self._rotor_ii))

        #   17. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   18. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        #   19. ringstellung I
        self._enigma_cipher.append(self.ringstellung(self._rotor_ii))

        #   20. Steckerverbindungen
        self._enigma_cipher.append(self.steckerverbindungen(self._enigma_cipher[-1]))

        for x in self._enigma_cipher:
            print(x)

        print(plain_text)
        for x in plain_text:
            print(self._enigma_cipher[0].index(x))
            print(self._enigma_cipher[-1][self._enigma_cipher[0].index(x)])