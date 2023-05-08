from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    #Use 'translator' file functions, translate text to French
    return FrenchVoice

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    #Use 'translator' file functions, translate text to English
    return EnglishVoice

@app.route("/")
def renderIndexPage():
    #Render template 'index.html' 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) #Point to 'localhost' on Port 8080
