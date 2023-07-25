from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):

    frenchText = MyMemoryTranslator(source='en-US', target='fr-FR').translate(englishText)  

    return frenchText


def frenchToEnglish(frenchText):

    englishText = MyMemoryTranslator(source='fr-FR', target='en-US').translate(frenchText)  

    return englishText
