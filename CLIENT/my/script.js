var userinput = select(#userinput);
userinput.input(newText);
function newText()
{	chrome.tabs.getCurrrent(gotTab);
	function gotTab(tab)
	{
	var msg = userinput.value();
	chrome.tabs.sendMessage(msg);
	}
}