from flask import Flask, render_template

app = Flask(__name__)

# please insert " from app import routes " after linting here
from app import routes

