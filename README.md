# InstaBot
Shows you the people who don't follow you back. A bot based on Selenium.

Prequirements: 
-> Instagram account
-> Selenium - pip install selenium
-> Latest Chrome Browser located at C:\Program Files (x86)\Google\Chrome\Application\chrome.exe - modify the Path in __init__
-> Latest chromedriver.exe located in the same folder as the script

You will need to provide your username and password
This script does not save and export your credentials! It runs only locally and does not make a connection
to some external server.
To be sure of that take a look in the code.

This script works by simulating a user who clicks on the elements in the browser which causes the script to take some time.
Allow it up to 15 minutes depending on how many followers/following you have.
If you want it to run faster consider altering the sleep timers.

The script uses XPaths to locate to elements on the webpage. Instagram is a quite complex website which means that the
XPath might be different when you use it. If the script can't access an element it will ask you to provide the
correct XPath. Please inspect the named element and copy the XPath.

Have fun!
- Blank
