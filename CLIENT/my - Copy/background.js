 console.log("background_script");
chrome.browserAction.onClicked.addListener(buttonClicked)
function buttonClicked(tab)
{	let msg = {
    txt: "hi" } 
	chrome.tabs.sendMessage(tab.id,msg)
}