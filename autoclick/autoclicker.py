import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import random


# import threading
# import queue
SUCCESS = 1
INFO_ERROR = 999

driver = webdriver.Chrome("./chromedriver")
def open_page():
    try:

        driver.get("https://app.reef-education.com/#/login")
        driver.get(driver.getCurrentUrl())
        driver.refresh()
    except:
        driver.refresh()



def auto_login(email, password):
    try:
        time.sleep(5)
        while 1:
            try:
                if driver.find_element_by_id("userEmail") != 0:
                    break
            except:
                time.sleep(2)
                print("Waiting for Email Page...")#debug


        emailid = driver.find_element_by_id("userEmail")
        time.sleep(1)
        emailid.send_keys(email)

        time.sleep(1)

        passw = driver.find_element_by_id("userPassword")
        time.sleep(1)
        passw.send_keys(password)

        time.sleep(1)

        signin = driver.find_element_by_id("sign-in-button")
        signin.click()

        time.sleep(3)
        return SUCCESS
    except:
        print("email or password incorrect, please enter again")
        return INFO_ERROR

def select_join():
    #select the course
    while 1:
        try:
            if driver.find_element_by_css_selector('a[ng-click="routes.courseScreen(course.id)"]') != 0:
                break
        except:
            time.sleep(10)
            print("Waiting for Course List...")

    cpsc = driver.find_element_by_css_selector('a[ng-click="routes.courseScreen(course.id)"]')
    cpsc.click()

    time.sleep(7)

    while(not driver.find_element_by_css_selector('button[ng-click="controller.gestures.btnJoinSessionClicked()"]')):
        time.sleep(1)
        print("Waiting for Join button...")

    join = driver.find_element_by_css_selector('button[ng-click="controller.gestures.btnJoinSessionClicked()"]')
    join.click()

def multiple_choice():

    while 1:

        answer = ''
        choices = ['a','b','c','d','e']
        default = choices[random.randint(0,5) % 5]
        print(default)

        while 1:

            try:
                if driver.find_element_by_class_name('multiple-choice-buttons') != 0:
                    break
            except:
                time.sleep(5);
                #print("Waiting for New Clicker Question...")

#         answer = input("The answer for the clicker question is: ")
#         start_time = time.time();
#         while(answer == ''):
#             answer = input()
#             if(time.time() - start_time > 10):
#                 break


        if answer == '':
            answer = default #default value
        else:
            answer = answer[0].lower()

        if answer not in choices:
            answer = default



        selector_text = 'button[id="multiple-choice-%s"]'


        for i in choices:
            if(answer == i):
                choice = driver.find_element_by_css_selector(selector_text % i)
                choice.click()

        time.sleep(60)

    driver.quit()
    #q.join()


def main():
    email = input("Enter email: ")
    password = input("Enter password: ")
    open_page()
    auto_login(email, password)
    select_join()
    multiple_choice()

if __name__ == "__main__":
    main()
