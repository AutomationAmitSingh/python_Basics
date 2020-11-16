from selenium import webdriver
validateText = "Option3"
driver = webdriver.Firefox(executable_path="D:\\Software\\Selenium_Python\\geckodriver-v0.24.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()