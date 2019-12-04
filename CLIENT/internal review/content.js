var api_url = "http://127.0.0.1:5000/api/?url="

var currurl = window.location.href;
//alert(currurl);
var argu = api_url + currurl

function main(object)
{
		
		//msg = ""
		//if(object['check1'] != "https")
			//msg += "This Site <" + object['domain_name']+ "> is Not Secure !!!\n"
		//if(object['check4']==1)
			//msg+= "This could be a phising attempt\n"
		//if(object['check2']!=1)
			//msg+= "domain of this site is not in our list of verified domains bE cAREFULL \n"
		
		//msg+="rank of this site is "	+ object['check3'] + " out of 10 "
		//ssalert(msg)
		alert(object["1"])
		if(object["1"]==1)
			// https

		
		if(object["1"]==1)
			// http

}
fetch(argu)
.then(res => res.json())
.then(data => main(data))