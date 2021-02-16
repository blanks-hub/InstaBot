from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

#INSTRUCTIONS
# Prequirements: Selenium - pip install selenium

# ----This Bot prints all the Instagram Accounts who don't follow you back----

# You will need to provide your username and password
# This script does not save and export your credentials! It runs only locally and does not make a connection
# to some external server.
# To be sure of that take a look in the code.

# This script works by simulating a user who clicks on the buttons in the browser. This means that the script takes some
# time to finish. Allow it up to 15 minutes depending on how many followers/following you have.
# If you want it to run faster consider altering the sleep timers.

# The script uses XPaths to locate to elements on the webpage. Instagram is a quite complex website which means that the
# XPath might be different when you use it. If the script can't access an element it will ask you to provide the
# correct XPath. Please inspect the named element and copy the XPath.

user = "INSERT YOUR USERNAME HERE"
pw = "INSERT YOUR PASSWORD HERE"

class InstaBot:
    def __init__(self, user, pw):

        self.user = user
        self.pw = pw

        WINDOW_SIZE = "1920,1080"
        CHROME_PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        chrome_opt = Options()
        #chrome_opt.add_argument("--headless")
        chrome_opt.add_argument("--windows-size=%s" % WINDOW_SIZE)
        chrome_opt.binary_location = CHROME_PATH

        self.driver = webdriver.Chrome(options=chrome_opt)
        self.driver.get("https://instagram.com")
        sleep(3)

        # If cookies need to be accepted
        if len(self.driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")) == 1:
            # then click accept cookies button
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()


        # If Instagram opens on the register site switch to login
        if len(self.driver.find_elements_by_xpath("//a[contains(text(), 'Log in')]")) == 1:
            self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
            sleep(2)

        # Login
        user_field = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")\
        .send_keys(user)
        pw_field = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input") \
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)

        # If Instagram asks for Notifications
        if len(self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")) == 1:
            self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
            sleep(0.5)

    # Scrolls the followers/following scrollbox to the bottom and extracts all the names
    @property
    def _get_names(self):

        sleep(1)
        # If scrollbox is open
        scroll_box_xpath = "/html/body/div[4]/div/div/div[2]"
        while len(self.driver.find_elements_by_xpath(scroll_box_xpath)) != 1:
            print("The scrollbox could'nt be found! Please provide the correct XPath!")
            print("To do this, inspect the scrollbox element and right click on the source code to copy the Xpath.")
            scroll_box_xpath = input("Paste it in here:")

        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        #close button
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
        .click()

        return names

    def get_unfollowers(self):

        sleep(3)
        # If user xpath is correct
        user_xpath = "//a[contains(@href,'{}')]".format(self.user)
        while len(self.driver.find_elements_by_xpath(user_xpath)) < 1:
            print("The user XPath could'nt be found! Please provide the correct XPath!")
            print("To do this, inspect the user button element and right click on the source code to copy the Xpath.")
            user_xpath = input("Paste it in here:")
        self.driver.find_element_by_xpath(user_xpath).click()
        sleep(2)

        # If following xpath is correct
        following_xpath = "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a"
        while len(self.driver.find_elements_by_xpath(following_xpath)) != 1:
            print("The following XPath could'nt be found! Please provide the correct XPath!")
            print("To do this, inspect the following button element and right click on the source code to copy the Xpath.")
            following_xpath = input("Paste it in here:")
        self.driver.find_element_by_xpath(following_xpath).click()
        following = self._get_names

        # If followers xpath is correct
        followers_xpath = "//*[@id='react-root']/section/main/div/header/section/ul/li[2]"
        while len(self.driver.find_elements_by_xpath(followers_xpath)) != 1:
            print("The followers XPath could'nt be found! Please provide the correct XPath!")
            print("To do this, inspect the followers button element and right click on the source code to copy the Xpath.")
            followers_xpath = input("Paste it in here:")
        self.driver.find_element_by_xpath(followers_xpath).click()
        followers = self._get_names

        dont_follow_back = [user for user in following if user not in followers]
        print("---Users who don't follow you back---")
        for user in dont_follow_back:
            print(user)


# Main
my_bot = InstaBot(user,pw)
my_bot.get_unfollowers()