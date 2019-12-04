
import ssl
from sys import exit
from tld import get_tld
import flask
from flask import request , jsonify
from flask_cors import CORS

url1 = "https://www.google.com/"
verified_doms  = ("com" , "org" , "in" , "co.in" , "au") # examples of reputed top level domains



app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["DEBUG"] = True
CORS(app)

@app.route('/api/',methods=['GET'])
def api_id():
    flag = 0
    flag2 = 1
    msg = ""
    if 'url' in request.args:
        url2 = request.args['url']

    else:
        return "Error: No url field provided. Please specify an id."



    ### CHECK FOR HTTP or HTTPS ###

    proto = url2[:5]

    
    if(proto=="https"):
        flag2 = 2
        
### check for domain ###
    if(proto=="https"):
        flag2 = 1
         
   
    dict = { '1' : flag2 }
    return dict
app.run()
 
 


    
