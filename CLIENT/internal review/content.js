 var api_url = "http://127.0.0.1:5000/api/?url=";
 var currurl = window.location;
var argu = api_url + currurl;
function main(object)
{	
	console.log(object);
		if(object["check1"]==0)
		msg +="";
		if()
		msg +="";
		if()
		msg +="";
		
}
fetch(argu)
.then(res => res.json())
.then(data => main(data))