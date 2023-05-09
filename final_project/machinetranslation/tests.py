import unittest
import translator
import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        #Test values for successful English to French Translation
        self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french("hello"),"Bonjour")
        self.assertEqual(english_to_french("welcome"),"Bienvenue")
        self.assertEqual(english_to_french("love"),"Amour")

class Testfrench_to_english(unittest.TestCase):
    def test2(self):
        #Test values for successful French to English Translation
        self.assertEqual(french_to_english(""),"")
        self.assertEqual(french_to_english("bonjour"),"Hello")
        self.assertEqual(french_to_english("bienvenue"),"Welcome")
        self.assertEqual(french_to_english("amour"),"Love")

unittest.main()