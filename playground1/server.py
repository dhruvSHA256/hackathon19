
    #4
    #checking issued date
 

    #5
    #checking expiry date of url
    
    
    #6
    #checking serial number of
    
    #7
    #checking sha1 of url
    try:
        if cert_hash(url)[0] == cert_hash(url1)[0]:
            
            count += 1
            check7 = 1
        else:
            
            check7 = 0
            None
    except:
        
        check7 = 0
        None
    
    
    #8
    #checking sha256 of url
    try:
        if cert_hash(url)[1] == cert_hash(url1)[1]:
            
            count += 1
            check8 = 1
            None
        else:
           
            check8 = 0
            None
    except:
          
        check8 = 0
        None


    #9
    #checking which certificate provider provided the ssl certificate
    try:
        if str(certi(url)[1]) == str(certi(url1)[1]):
            
            count += 1
            check9 = 1
        else:
            
            check9 = 0
            None
    except:
        
        check9 = 0
        None
    

    #10
    #checking which domain was exactly issued this particular certificate
    try:
        if str(certi(url)[0]) == str(certi(url1)[0]):
            
            count += 1
            check10 = 1
        else:
           
            check10 = 0
            None
    except:
        
        check10 = 0
        None



    