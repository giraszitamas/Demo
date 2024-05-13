from bottle import route, run, request,get, post
from bottle import *
from difflib import SequenceMatcher
import pickle
from web3 import *

basic_dictionary = []

@route('/')
def asdf():
    site = ""
    for f in open("test.html","r",encoding="utf-8"):
        site+=f
    
    return site  

run(host='localhost', port=8080, debug=True)