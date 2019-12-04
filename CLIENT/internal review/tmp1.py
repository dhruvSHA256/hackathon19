
import ssl
from sys import exit
from tld import get_tld
import flask
from flask import request , jsonify
from flask_cors import CORS


verified_doms  = ("com" , "org" , "in" , "co.in" , "au" , "us" , "ru" , "jp" , "edu") # examples of reputed top level domains



app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["DEBUG"] = True
CORS(app)

@app.route('/api/',methods=['GET'])
def api_id():
    if 'url' in request.args:
        url2 = request.args['url']

    else:
        return "Error: No url field provided. Please specify an id."



    ### CHECK FOR HTTP or HTTPS ###

    proto = url2[:5]

    
    if(proto=="https"):
        check1 = 1
        

    if(proto=="http:"):
        check1 = 0
         
   
    ### CHECK FOR TOP LEVEL DOMAIN ###
    
    _tld = get_tld(url2)
    
    for __tld in verified_doms:
        if(__tld==_tld):
            check2 = 1
        else:
            check2 = 0
            
    ### CHECK IF DOMAIN IS IP ADDRESS
    for i in url:
        if(i=<9 and i>=0 or i=='.')
        check3 = 0
        else:
        check3 = 1

    dict = { 'check1' : check1 , 'check2' : check2 , 'check3' : check3  }
    return dict
app.run()
 
 


    
