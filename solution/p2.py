import binascii
from itertools import combinations
import re
import sys


def read_cipher_file(filename):
    """
    Read in a hex filename and return a list of ints
        :param filename: (str)
        :return: (list)
    """
    ct = open(filename, "r")
    cipher_list = []
    for line in ct:
        reg_match = re.match('0x(.*)\\n', line)
        if reg_match:
            cipher_list.append(int(reg_match.group(1), 16))
    return cipher_list


def xor_cipher_lists(cipher_list_1, cipher_list_2):
    """
    Return the xor of two lists of ints
        :param cipher_list_1: (list)
        :param cipher_list_2: (list)
        :return: (list)
    """
    xor_list = []
    index = 0
    for int1 in cipher_list_1:
        xor = (int1 ^ cipher_list_2[index])
        xor_list.append(xor)
        index += 1
    return xor_list


def xor_word(xor_list, crib_text, off_set):
    """
    Xor a crib against a list with an off_set
        :param xor_list: (list)
        :param crib_text: (str)
        :param off_set: (int)
        :return: (list)
    """
    xor_word_list = []
    crib_list = []
    for s in crib_text:
        crib_list.append(ord(s))
    index = 0
    counter = 0

    for val in xor_list:
        if off_set > index:
            xor = 32
        else:
            xor = (val ^ crib_list[counter])
            counter += 1
            if counter >= len(crib_list):
                counter = 0
        index += 1
        xor_word_list.append(xor)
    return xor_word_list


def xor_word_index(xor_list, crib_text):
    """
    xor a crib at every index of the list
        :param xor_list: (list)
        :param crib_text: (str)
        :return: (list)
    """
    xor_crib_list = []
    crib_list = []
    for s in crib_text:
        crib_list.append(ord(s))
    index = 0
    counter = 0
    for i in range(0, len(xor_list)-len(crib_list)):
        temp_xor = []
        for val in crib_list:
            xor = (xor_list[i] ^ val)
            i += 1
            temp_xor.append(xor)
        xor_crib_list.append(list_to_str(temp_xor))
    print_list(xor_crib_list)
    return xor_crib_list


def list_to_str(hex_list):
    """
    Convert list of ints to str
        :param hex_list: (list)
        :return: (str)
    """
    hex_str = ""
    for h in hex_list:
        hex_str += chr(h)
    return hex_str


def interpreter_xor(xor_list, crib_text, off_set):
    """
    Return a list of chrs collided with a crib with an off set
        :param xor_list: (list)
        :param crib_text: (str)
        :off_set: (int)
        :return: (list)
    """
    xor_word_list = xor_word(xor_list, crib_text, off_set)
    xor_str = list_to_str(xor_word_list)
    new_list = split_by_index(xor_str, len(crib_text))
    for i in new_list:
        print i
    return new_list


def split_by_index(old_List, index):
    """
    Split a list at an index
        :param old_list: (list)
        :param index: (int)
        :return: (list)
    """
    new_list = [old_List[i:i+index] for i in range(0, len(old_List), index)]
    return new_list


def print_list(xor_list):
    counter = 0
    for i in xor_list:
        print("%03d" % counter + ": " + i)
        counter += 1
