var api_url = "http://127.0.0.1:5000/api/?url="

var currurl = window.location;
//alert(currurl);
var argu = api_url + currurl

function main(obj)
{
	var checks = {"check1":1,"check2":1,"check3":1,"check4":1}//object['check1'];
chrome.runtime.sendMessage(checks);
console.log(obj);

}
fetch(argu)
.then(res => res.json())
.then(data => main(data))

main();

