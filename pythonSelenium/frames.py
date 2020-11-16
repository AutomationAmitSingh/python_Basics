
from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="D:\\Software\\Selenium_Python\\geckodriver-v0.24.0-win64\\geckodriver.exe")
driver.maximize_window()
# iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")
# frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
