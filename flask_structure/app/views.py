from flask import (render_template, flash, redirect, 
                   request, Response, abort)
from app import app, db
from app.forms import *
from app.models import *

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html', title='Home') 

