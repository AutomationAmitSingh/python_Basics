from selenium import webdriver
import time
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="D:\\Software\\Selenium_Python\\geckodriver-v0.24.0-win64\\geckodriver.exe")
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
time.sleep(2)
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
