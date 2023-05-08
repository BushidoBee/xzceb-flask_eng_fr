```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    #Function translates English Text to French
    #Create Authenticator Key w/ IAMAuthenticator
    #Create Language Translator instance w/ LanguageTranslatorV3
    #Target the Service URL
    FRENCH_TRANSLATION = 0 #'translate' from English to French ('en-fr') & get the result
    return FRENCH_TRANSLATION #Return the 'translation' dictionary index

def frenchtoEnglish(frenchText):
    #Function translates French Text to English
    #Create Authenticator Key w/ IAMAuthenticator
    #Create Language Translator instance w/ LanguageTranslatorV3
    #Target the Service URL
    ENGLISH_TRANSLATION = 0 #'translate' from French to English ('fr-en') & get the result
    return ENGLISH_TRANSLATION #Return the 'translation' dictionary index
```