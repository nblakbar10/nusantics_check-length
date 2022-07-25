# from django.shortcuts import redirect, render
from urllib import response
# from django.shortcuts import redirect
# from cv2 import line
# from django.shortcuts import redirect
from flask import Flask, jsonify, redirect, render_template, send_file, url_for, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import gzip
from datetime import datetime
from Bio import SeqIO
from io import StringIO
import sys

# project_root = os.path.dirname(__file__)
# template_path = os.path.join(project_root, './')

# app = Flask(__name__, template_folder=template_path)
app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")




@app.route("/upload")
def upload():
    return render_template("upload_index.html")
    


@app.route("/check_length", methods = ['GET', 'POST'])
def check_length():
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
                        print(line, seq_length)
                        # return line, seq_length
                        return render_template("upload_index.html", value=(line, seq_length))
                        # return {'line': line, 'length': seq_length}
                        # return render_templatecheck_length()
                        # # return result

                    # else: # stop the program count equals to other numbers
                    #     break


                # for s in SeqIO.parse(StringIO(file.read()), 'fastq'):
                #     print(s.id)
                # print(file.content_type)
    # return 'OK', 200

    #     # date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        
    #     fs.save(secure_filename(fs.filename))
    #     # return fs.filename

        
    #     inputfile = fs.filename
        
    #     with gzip.open(inputfile, 'rb') as f: #Read a single .gz file
    #         count = 0
    #         for line in f:
    #             count=count+1
    #             if count==1: #1st line is not a sequence, so continue
    #                 continue
    #             if count==2: #2nd line is the sequence , so check length
    #                 line=line.rstrip()
    #                 seq_length= len(line)
    #                 return (line, str(seq_length))
    #                 # return result
    #             else: # stop the program count equals to other numbers
    #                 break

    #             # else: # stop the program count equals to other numbers
    #             #     breakCTCTTTT

    # # return "Thanks"


# @app.route("/A1_check_length.py", methods = ['POST'])
# def run_app():

#     filename = request.form['filename']

#     if not filename:
#         return render_template('index.html')
#     # else:
#     #     #execute the python script.