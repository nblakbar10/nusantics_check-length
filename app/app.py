from flask import Flask, jsonify, redirect, render_template, send_file, url_for, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import gzip
from datetime import datetime
from Bio import SeqIO
from io import StringIO
import sys

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload_index.html")
    
@app.route("/result", methods = ['POST'])
def result():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return 'Error', 500
        file = request.files['file']

        if file.filename == '':
            print('No selected file')
            return 'Error', 500
        if file:
            with gzip.open(file, 'rb') as f: #Read a single .gz file
                count = 0
                for line in f:
                    count=count+1
                    if count==1: #1st line is not a sequence, so continue
                        continue
                    if count==2: #2nd line is the sequence , so check length
                        line=line.rstrip()
                        seq_length= len(line)
                        # print(line, seq_length)
                        result = line, seq_length
                        # return line, seq_length
                    return render_template("result.html", data=result)