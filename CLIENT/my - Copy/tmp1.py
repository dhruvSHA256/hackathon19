
import ssl
from sys import exit
from tld import get_tld
import flask
from flask import request , jsonify
from flask_cors import CORS

verified_doms  = ("com" , "org" , "in" , "co.in" , "au") # examples of reputed top level domains



app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["DEBUG"] = True
CORS(app)
# object = {domain,check1,check2,check4,check5}
# check1 = http/https ,check2 = check for special chars , check3 = serial, check4 = , check5 = 
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

    if(proto!= "http:" and proto!= "https"):
        print("unknown protocol of connection !!!")
        msg+="unknown protocol of connection !!!"
        flag2 = 0
    if(proto=="http:"):
        print("Site does not have a Secure Connection !!! Please be Careful !!! ")
        msg+="Site does not have a Secure Connection !!! Please be Careful !!!\n"
        flag2 = 0
### if program continues the url has https protocol

### check for domain ###
    if(proto=="https")
    dom = get_tld(url2)

    for d in verified_doms:
        if (d == dom) :
            flag = 1
            break
    if(flag!=1):
        print("Top level domain of site is not in our  database of safe domains !!! ")
        msg +="Top level domain of site is not in our  database of safe domains !!! \n"
        flag2 = 0
    if (flag2 == 1):
        msg = "all_good"
    dict = { '1' : msg }
    return dict
app.run()
 
 


    
