#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seletools.actions import drag_and_drop as dnd
import argparse
import time

def drag_and_drop():
    """Moves column A over to column b, then does it one more time

    Note: seletools function "drag_and_drop" (renamed to "dnd") used due to 
    Selenium drag and drop functionality being broken from drivers since at
    least July 2021. Selenium is used for all other functionality.
    """
    print("[*] drag_and_drop: automate moving column a over to column b," +\
        " and back again")
    # find "Drag and Drop" link and click
    driver.find_element(By.LINK_TEXT, "Drag and Drop").click()

    # find both column elements
    column_a = driver.find_element(By.ID, "column-a")
    column_b = driver.find_element(By.ID, "column-b")

    # use seletools drag_and_drop function (renamed here as dnd)
    # added sleeps to slow down the speed of the function
    time.sleep(2)
    dnd(driver, column_a, column_b)
    time.sleep(2) 
    dnd(driver, column_a, column_b)

    # return back to menu page
    # (refresh added to start at the top of the home page)
    time.sleep(3)
    driver.back()
    driver.refresh()

def WYSIWYG_editor():
    """Enters some text in the editor and makes it bold
    """

    print("[*] WYSIWYG_editor: type message into text editor, and make it bold")
    # click "WYSIWYG Editor" link
    driver.find_element(By.LINK_TEXT, "WYSIWYG Editor").click()

    # switch to inner frame with text box
    driver.switch_to.frame("mce_0_ifr")

    # find the text box and clear the text in it
    text_box = driver.find_element(By.ID, "tinymce")
    text_box.clear()

    # send text into text box
    text_box.send_keys("Hello Network Perception!")

    # find text element we just entered, and highlight select it
    text = driver.find_element(By.XPATH, '//body[@id="tinymce"]/p')
    webdriver.ActionChains(driver).double_click(text).key_down(Keys.CONTROL).\
        send_keys("a").perform()

    # switch back to default frame
    driver.switch_to.default_content()

    # find bold formatting button and click it
    driver.find_element(By.CSS_SELECTOR, '[title="Bold"]').click()

    # switch back to frame with text box, and deselect the text
    driver.switch_to.frame("mce_0_ifr")
    webdriver.ActionChains(driver).double_click(text).perform()

    # go back to menu page
    # (refresh added to start at the top of the home page)
    time.sleep(3)
    driver.back()
    driver.refresh()

def challenging_dom():
    """select and click buttons that have changing text and ids by using XPATH
    """

    print("[*] challenging_dom: click buttons with changing text " + 
          "and IDs by using XPATH")
    # find link "Challenging DOM" and click it
    driver.find_element(By.LINK_TEXT, "Challenging DOM").click()

    # find normal button via class name, get its text, and click the button
    normal_button = driver.find_element(By.XPATH, "//a[@class='button']")
    normal_button_text = normal_button.text
    normal_button.click()

    # print to command line the button text, it will change after the click
    print("[*] - clicked normal button when it was named: " + 
          normal_button_text)

    # find alert button, get its text, then click the button
    alert_button = driver.find_element(By.XPATH, "//a[@class='button alert']")
    alert_button_text = alert_button.text
    alert_button.click()

    # print to command line the button text, it will change after the click
    print("[*] - clicked alert button when it was named: " +
          alert_button_text)
    
    # find success button, get its text, then click the button
    success_button = driver.find_element(By.XPATH,\
        "//a[@class='button success']")
    success_button_text = success_button.text
    success_button.click()

    # print to command line the button text, it will change after the click
    print("[*] - clicked success button when it was named: " +
          success_button_text)
    
    time.sleep(3)
    driver.back()
    driver.refresh()

if __name__ == "__main__":

    # create program description that displays with "-h" argument
    parser = argparse.ArgumentParser(description=\
        "Selenium program that interacts with 3 subpages on " +
        "'the-internet.herokuapp.com': " +
        "'Drag and Drop', 'WYSIWYG Editor', and 'Challenging DOM'." +
        " Uses Firefox and the geckodriver webdriver for Selenium interaction.")
    args = parser.parse_args()

    # create firefox webdriver, then maximize the browser window
    driver = webdriver.Firefox()
    driver.maximize_window()

    # open browser to demo web app
    driver.get("http://the-internet.herokuapp.com/")
 
    # perform actions in 3 of the sub pages of the web app
    drag_and_drop()
    WYSIWYG_editor()
    challenging_dom()

    # close browser
    driver.close()

    #exit program
    print("[*] Thanks!")
    exit()