from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys 

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing our custom file")
    except Exception as e:
        abs = CustomException(e, sys)
        logging.info(abc.error_message)
        return "Welcome to my Engineering ml project"


if __name__=="__main__":
    app.run(debug=True)