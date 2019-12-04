 //console.log(document.location.origin);
 //console.log(windows.location.hostname)
 //chrome.runtime.onMessage.addListener(gotMessage);
 //function gotMessage(message,sender,sendResponse)
 //{
//	 console.log(message.txt);
 //} 
 var api_url = "http://127.0.0.1:5000/api/?url=";
 var currurl = window.location;
var argu = api_url + currurl;
function main(object)
{
		console.log(object);
}
fetch(argu)
.then(res => res.json())
.then(data => main(data))


