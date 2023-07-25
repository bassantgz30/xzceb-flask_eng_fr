import unittest
from translator import frenchToEnglish, englishToFrench


class TestEnglishToFrench(unittest.TestCase):
    """
    This class is to test the englishToFrench Function
    """
    def test1(self):
        """ 
        Test cases to test english-french translator
        """
        self.assertEqual(englishToFrench('hello'), 'bonjour')
        self.assertEqual(englishToFrench('two'), 'deux' )
        self.assertEqual(englishToFrench('book'), 'livre')
        self.assertNotEqual(englishToFrench('one'), 'deux' )


class TestFrenchToEnglish(unittest.TestCase):
    """
    This class is to test the frenchToEnglish Function
    """
    def test1(self):
        """ 
        Test cases to test french-english translator
        """
        self.assertEqual(frenchToEnglish('bonjour'), 'hello')
        self.assertEqual(frenchToEnglish('deux'), 'two')
        self.assertEqual(frenchToEnglish('livre'), 'book' )
        self.assertNotEqual(frenchToEnglish('pomme'), 'car' )


# running thr tests
unittest.main()
