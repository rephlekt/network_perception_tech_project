# network_perception_tech_project
To interact with the "the-internet.herokuapp.com" website, I created a python program named “heroku_interact.py”. It can be found at the following address:
https://github.com/rephlekt/network_perception_tech_project
I mostly used the automation framework “Selenium” (documentation and full installation instructions for Selenium can be found here: https://www.selenium.dev/documentation/overview/) to perform the interactions. To install Selenium, use the following command on the Linux command line (this will install the current selenium version 4.1):
pip3 install selenium
Selenium also requires the use of a webdriver for the browser you wish to automate. I chose Firefox (version 95.0.1) as a browser, which requires the “geckodriver” webdriver. The latest geckodriver binary can be found here (I used version 0.30.0, in the archive “geckodriver-v0.30.0-linux64.tar.gz”):
https://github.com/mozilla/geckodriver/releases
If necessary, you can also download the Firefox web browser with the following command (this should install Firefox in /usr/bin/):
sudo apt install firefox
The downloaded webdriver will have to be extracted from the archive it came in, then must be included in your OS’s search path. I placed mine in the “/usr/bin/” folder (as this location is already within the search path), and changed its owner and permissions using the following commands:
tar xvzf ./geckodriver-v0.30.0-linux64.tar.gz (or whatever archive you downloaded)
sudo mv geckodriver /usr/bin/
sudo chown root:root /usr/bin/geckodriver
sudo chmod +x /usr/bin/geckodriver
As of at least July 2021, the Drag and Drop action in Selenium 4.1 is broken due to web driver issues (chromedriver, geckodriver, etc). See the following links for details:
https://github.com/SeleniumHQ/selenium/issues/10119
https://github.com/SeleniumHQ/selenium/issues/9878
https://github.com/SeleniumHQ/selenium/issues/9860
https://wpt.fyi/results/webdriver/tests/perform_actions/pointer.py
To be able to perform drag and drop interactions, I opted to use the “seletools” module, which was created to address this specific issue (you can find more information here: https://pypi.org/project/seletools/). To install the seletools module on Linux, use the following command:
pip3 install seletools
Once all dependencies have been installed, the program can be run using the following command:
python3 heroku_interact.py
This will start the program, which will open up the web browser associated with the webdriver you’ve downloaded. The program will then interact with the webpage at “the-internet.herokuapp.com”, specifically the “Drag and Drop”, “WYSIWYG Editor”, and “Challenging DOM” sub-pages.
