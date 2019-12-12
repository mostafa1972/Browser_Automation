###https://medium.com/better-programming/lets-create-an-instagram-bot-to-show-you-the-power-of-selenium-349d7a6744f7

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self, user, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('./driver/chromedriver.exe', options=self.browserProfile)
        self.user= user
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        user_box = self.browser.find_element_by_name("username")
        user_box.send_keys(self.user)
        pass_box = self.browser.find_element_by_name("password")
        pass_box.send_keys(self.password)
        pass_box.send_keys(Keys.ENTER)
        time.sleep(5)

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")
    
    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")
    
    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers

    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()


#bot = InstagramBot('youremail', 'yourpassword')
#bot.signIn()
#bot.followWithUsername('therock')
#bot.unfollowWithUsername('therock')

#def main():
user = "siddiquimostafa"
password = "siddi@123"
insta = InstagramBot(user, password)
insta.signIn()
insta.followWithUsername('therock')
insta.unfollowWithUsername('therock')

#if __name__ == "__main__":
#    main()
