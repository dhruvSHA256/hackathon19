
// var image =  document.getElementById("imageOne");

            // function changeColor()
            // {
                // if (image.getAttribute('src') == "button_on.png")
                // {
                    // image.src = "button_off.png";
                // }
                // else
                // {
                    // image.src = "button_on.png";
                // }
				
            // }
			
 chrome.extension.onMessage.addListener
 (
  function(msg, sender, sendResponse)
  { console.log("executed in script.js");
  console.log(msg);
  }
 )