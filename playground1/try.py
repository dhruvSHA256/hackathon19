import ssl
import socket
import hashlib
import flask
from flask import request , jsonify
from flask_cors import CORS
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json
import re


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["DEBUG"] = True
CORS(app)

@app.route('/api/',methods=['GET'])
def api_id():
    if 'url' in request.args:
        url = request.args['url']
       
        _url = ["paytm.com", "www.paypal.com" , "www.icicibank.com" , "www.hdfcbank.com" , "www.pnbindia.in" , "www.phonepay.com" ]
    else:
        return "Error: No url field provided. Please specify an id."
        
    # try:
       
        #some site without http/https in the path
        # host = (url.split("https://"))[1].split("/")[0]
        # port = '443'
        

        # hostname = host
        # context = ssl.create_default_context()

        # with socket.create_connection((hostname, port)) as sock:
            # with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                
                # data = json.dumps(ssock.getpeercert())
                

        # s_no = (data.split('"serialNumber": "'))[1].split('",')[0]
        


        # expiry = (data.split('"notAfter": "'))[1].split('",')[0]
        
    # except:
        # s_no = 0
        # expiry = 0
        
        
    
        # host = (url.split("https://"))[1].split("/")[0]

        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.settimeout(1)
        # wrappedSocket = ssl.wrap_socket(sock)

        # try:
            # wrappedSocket.connect((host, 443))
        # except:
            # response = False
        # else:
            # der_cert_bin = wrappedSocket.getpeercert(True)
            # pem_cert = ssl.DER_cert_to_PEM_cert(wrappedSocket.getpeercert(True))
            

        
        # hash_sha1 = hashlib.sha1(der_cert_bin).hexdigest()
        # hash_sha256 = hashlib.sha256(der_cert_bin).hexdigest()
        # res1 = ':'.join(hash_sha1[i:i + 2] for i in range(0, len(hash_sha1), 2))
        # res256 = ':'.join(hash_sha256[i:i + 2] for i in range(0, len(hash_sha256), 2))
       
        
        
    # hostname = (url.split("https://"))[1].split("/")[0]
    # ctx = ssl.create_default_context()
    # s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
    # s.connect((hostname, 443))
    # cert = s.getpeercert()

    # subject = dict(x[0] for x in cert['subject'])
    # issued_to = subject['commonName']
    # issuer = dict(x[0] for x in cert['issuer'])
    # issued_by = issuer['commonName']
    # issue_date = cert['notBefore']
    # ca_issuer = cert['caIssuers']
    
   
    
    check0 = 0
        
    if url[0:5] == "https":             #### check1 = https / http 
        check1 = 1
    else:
         check1 = 0
        
    if url.find != "@":                 ### special characters
        

        check3 = 1
        
    else:
        
        check3 = 0
    

        
    for url1 in _url:
        if url == url1 :
            url2 = url1 
            if url == url2:
             check2 = 1
        else:
            check2 = 0
        
      
            
        
    check_dict = { 'check_1': check1, 'check_2': check2, 'check_3': check3}

    ##info_dict = {'issued_date': issue_date, 'expiry_date': expiry, 'serial_number': s_no, 'sha1': res1, 'sha256': res256, 'issuer': issued_by, 'issued_to': ca_issuer}
    

    #info_dict.update(check_dict)
    return check_dict
 
app.run()