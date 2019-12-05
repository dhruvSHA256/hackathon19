import ssl
import socket
import hashlib
import flask
from flask import request , jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["DEBUG"] = True
CORS(app)

@app.route('/api',methods=['GET'])
def api_id():
    if 'url' in request.args:
        url = request.args['url']
    else:
        return "error"
    #1 
    #checking connection protocol
    if url[0:5] == "https":
        #score += 1
        
        count += 1
        check1 = 1
    else:
        
        check1 = 0
    

    #2
    #checking usage of @ symbol
    if url.find != "@":
        
        count += 1
        check2 = 1
        
    else:
        
        check2 = 0

 
 
 #check3
 
    try:
        from urllib.request import Request, urlopen, ssl, socket
        from urllib.error import URLError, HTTPError
        import json
        # some site without http/https in the path
        host = (url.split("https://"))[1].split("/")[0]
        port = '443'
        

        hostname = host
        context = ssl.create_default_context()

        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                
                data = json.dumps(ssock.getpeercert())
      

        s_no = (data.split('"serialNumber": "'))[1].split('",')[0]
        count += 1
        check3=1

        expiry = (data.split('"notAfter": "'))[1].split('",')[0]
        count += 1
        check4=1
        #return expiry,s_no
    except:
        #return 0
        check3=0
        check4=0
    
#check 4

    try:
        host = (url.split("https://"))[1].split("/")[0]

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        wrappedSocket = ssl.wrap_socket(sock)

        try:
            wrappedSocket.connect((host, 443))
        except:
            response = False
        else:
            der_cert_bin = wrappedSocket.getpeercert(True)
            pem_cert = ssl.DER_cert_to_PEM_cert(wrappedSocket.getpeercert(True))
            

        
        hash_sha1 = hashlib.sha1(der_cert_bin).hexdigest()
        hash_sha256 = hashlib.sha256(der_cert_bin).hexdigest()
        res1 = ':'.join(hash_sha1[i:i + 2] for i in range(0, len(hash_sha1), 2))
        res256 = ':'.join(hash_sha256[i:i + 2] for i in range(0, len(hash_sha256), 2))
        check5 = 1
        #return res1,res256
    except:
        #return 0
        check5 = 0


#check 6
    try:
        hostname = (url.split("https://"))[1].split("/")[0]
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
        s.connect((hostname, 443))
        cert = s.getpeercert()

        subject = dict(x[0] for x in cert['subject'])
        issued_to = subject['commonName']
        issuer = dict(x[0] for x in cert['issuer'])
        issued_by = issuer['commonName']
        issue_date = cert['notBefore']
        ca_issuer = cert['caIssuers']
        #return issued_to, issued_by, issue_date
        check6,check7,check8=1,1,1
    except:
        check6,check7,check8=0,0,0



    import re 

    text = "рaytm.com"
    has_cyrillic(text)
        
        
    if has_cyrillic(url) is True:
        check9 = 1
    else:
        check9 = 0 



    check_dict = {'check_1': check1, 'check_2': check2, 'check_3': check3, 'check_4': check4, 'check_5': check5, 'check_6': check6, 'check_7': check7, 'check_8': check8, 'check_9': check9, 'check_10': check10,}
    info_dict = {'issued_date': issue_date, 'expiry_date': expiry, 'serial_number':(data.split('"serialNumber": "'))[1].split('",')[0]
, 'sha1': hash_sha1, 'sha256': hash_sha256, 'issuer': issued_by, 'issued_to': issued_to}
    
    
    check_dict.update(info_dict)
    return check_dict
app.run()
