import pandas as pd
import string
#import sys
import requests
#import facebook
import json
import nltk
import numpy as np
import os
import matplotlib.pyplot as plt
from flask import Flask, render_template, request,session, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField,StringField,SubmitField
from PIL import Image
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#from fbanalysis import fbanalysis

class AnalysisForm(FlaskForm):
    token = StringField('Token')
    page_id = StringField('Page_ID')
    submit = SubmitField('Run')

WORDCLOUD_FOLDER = os.path.join('static','wordcloud_photo')
app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = WORDCLOUD_FOLDER
app.config['SECRET_KEY'] = 'faithlimzx'


@app.route("/", methods=['GET', 'POST'])
def runanalysis():
    form = AnalysisForm()
    if form.is_submitted():
        return redirect(url_for('wcg'))
        #return render_template('data.html' ,result=result)   
    return render_template('runanalysis1.html', form=form)
    

@app.route('/wcg', methods=["POST","GET"])
def wcg():
    filename = os.path.join(app.config['UPLOAD_FOLDER'], 'wordcloud3.png')
    filename1 = os.path.join(app.config['UPLOAD_FOLDER'], 'chart.png')
    return render_template("wcg.html", user_image = filename, new_image=filename1)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
 