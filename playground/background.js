 chrome.runtime.onMessage.addListener
 (
  function(msg, sender, sendResponse)
  { console.log("executed");
  console.log(msg);
	if(msg.check1==1)
	{
		 var options = 
{
	type:"basic",
	title:"A P T",
	message:"all good",
	iconUrl:"icon.png"
};
chrome.notifications.create(options);
 
	}
		if(msg.check1==0)
	{
		 var options = 
{
	type:"basic",
	title:"A P T",
	message:"all bad",
	iconUrl:"icon.png"
};
chrome.notifications.create(options);
 
	}
	
  }
										
);
 
 
 