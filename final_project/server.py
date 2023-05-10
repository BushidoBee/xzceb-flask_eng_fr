from machinetranslation import translator
from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    FrenchVoice = translator.english_to_french(textToTranslate)#Use 'translator' file functions, translate text to French
    return FrenchVoice

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    EnglishVoice = translator.french_to_english(textToTranslate) #Use 'translator' file functions, translate text to English
    return EnglishVoice

@app.route("/")
def renderIndexPage():
    return render_template('index.html')#Render template 'index.html' 

#if __name__ == "__main__":
app.run(host="127.0.0.1", port=8080) #Point to 'localhost' on Port 8080
