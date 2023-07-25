import unittest
from translator import fernchToEnglish, englishToFrench


class TestEnglishToFrench(unittest.TestCase):
    """
    This class is to test the englishToFrench Function
    """
    def test1(self):
        """ 
        Test cases to test english-french translator
        """
        self.assertEqual(englishToFrench('hello'), 'bonjour')
        self.assertEqual(englishToFrench('two'), 'deux')
        self.assertEqual(englishToFrench('book'), 'livre')


class TestFrenchToEnglish(unittest.TestCase):
    """
    This class is to test the frenchToEnglish Function
    """
    def test1(self):
        """ 
        Test cases to test french-english translator
        """
        self.assertEqual(fernchToEnglish('bonjour'), 'hello')
        self.assertEqual(fernchToEnglish('deux'), 'two')
        self.assertEqual(fernchToEnglish('livre'), 'book')

# running thr tests
unittest.main()