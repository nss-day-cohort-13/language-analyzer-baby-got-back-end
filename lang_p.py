from language_analyzer import *

phrase = input('Enter the phrase you would like to analyze: ')

lang = LanguageAnalyzer(phrase)

lang.lang_run_all()
