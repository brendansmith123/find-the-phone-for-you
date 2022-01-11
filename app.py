from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Phones

app = Flask(__name__)

phones= db.phones

@app.route('/',)
def home():
    '''return homepage'''
    return render_template('home.html', phones=phones.find())

@app.route('/iphone',)
def iphone():
    '''return homepage'''
    return render_template('iphone.html', phones=phones.find())

@app.route('/samsung',)
def samsung():
    '''return homepage'''
    return render_template('samsung.html', phones=phones.find())

@app.route('/google',)
def google():
    '''return homepage'''
    return render_template('google.html', phones=phones.find())

@app.route('/cart',)
def cart():
    '''return homepage'''
    return render_template('cart.html', phones=phones.find())    
