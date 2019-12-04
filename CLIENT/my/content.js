 //console.log(document.location.origin);
 //console.log(windows.location.hostname)
 chrome.runtime.onMessage.addListener(gotMessage);
 function gotMessage(message,sender,sendResponse)
 {
	 console.log(message.txt );
 } 