var api_url = "http://127.0.0.1:5000/api/?url="

var currurl = window.location;
//alert(currurl);
var argu = api_url + currurl

function main(obj)
{
	
chrome.runtime.sendMessage(obj);
console.log(obj);

}
fetch(argu)
.then(res => res.json())
.then(data => main(data))

main();

