 chrome.runtime.onMessage.addListener
 (
  function(obj, sender, sendResponse)
  { console.log("executed");
  console.log(obj);
	if(obj.check_1==1)
	{
		 var options = 
{
	type:"basic",
	title:"Anti Phishing Toolkit",
	message:"THE SITE IS SECURE",
	iconUrl:"good.png"
};
chrome.notifications.create(options);
 
	}
		else
	{
		 var options = 
{
	type:"basic",
	title:"Anti Phishing Toolkit",
	message:"aBEWARE !! SONT ENTER YOUR CREDS ON THE SITE",
	iconUrl:"bad.png"
};
chrome.notifications.create(options);
 
	}
	
  }
										
);
 
 
 