from flask import Flask, request, render_template, redirect, url_for,  send_from_directory, jsonify
from azure.storage.blob import BlobServiceClient
import os
from werkzeug.utils import secure_filename
from tabulate import tabulate
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path
from sqlalchemy.engine import URL
import pyodbc
import json

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return render_template('index.html')



if __name__ == "__main__":
    app.run()
