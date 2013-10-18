#     _  _       _   _  _   _   _
#  |  _| _| |_| |_  |_   | |_| |_|
#  | |_  _|   |  _| |_|  | |_|  _|
#

# test_ocr.py

from ocr import ocr

def test_um():
    entrada = [" ", 
               "|",
               "|",
               " "]
    assert ocr(entrada) == 1

def test_dois():
    entrada = [" _ ",
               " _|",
               "|_ ",
               "   "]
    assert ocr(entrada) == 2

def test_tres():
    entrada = [" _ ",
               " _|",
               " _|",
               "   "]
    assert ocr(entrada) == 3

def test_quatro():
    entrada = ["   ",
               "|_|",
               "  |",
               "   "]
    assert ocr(entrada) == 4

def test_23():
    entrada = [ " _  _ ",
                " _| _|",
                "|_  _|",
                "      "]
    assert ocr(entrada) == 23

def test_22():
    entrada = [ " _  _ ",
                " _| _|",
                "|_ |_ ",
                "      "]
    assert ocr(entrada) == 22
    




