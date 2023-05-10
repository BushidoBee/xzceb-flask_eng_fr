#Converting English to French Text, and French to English Text
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['LANGUAGE_TRANSLATOR_APIKEY']
url = os.environ['LANGUAGE_TRANSLATOR_URL']

def english_to_french(english_text):
    """Function translates English Text to French"""
    auth_key = IAMAuthenticator(apikey) #Create Authenticator Key w/ IAMAuthenticator
    lang_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=auth_key)
    lang_translator.set_service_url(url) #Target the Service URL
    french_translation = lang_translator.translate(text=english_text, model_id="en-fr").get_result()
    return french_translation['translations'][0]['translation']  #Return the 'translation' dictionary index

def french_to_english(french_text):
    """Function translates English Text to French"""
    auth_key = IAMAuthenticator(apikey) #Create Authenticator Key w/ IAMAuthenticator
    lang_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=auth_key)
    lang_translator.set_service_url(url) #Target the Service URL
    english_translation = lang_translator.translate(text=french_text, model_id="fr-en").get_result()
    return english_translation['translations'][0]['translation']  #Return the 'translation' dictionary index
