from selenium import webdriver
# browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser
# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(executable_path="D:\\Software\\Selenium_Python\\chromedriver_win32\\chromedriver.exe",desired_capabilities = chromeOptions.to_capabilities())
# driver = webdriver.Firefox(executable_path = "D:\Software\Selenium_Python\geckodriver-v0.24.0-win64\geckodriver.exe")
driver = webdriver.Ie(executable_path = "D:\Software\Selenium_Python\IEDriverServer_x64_3.14.0\IEDriverServer.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  #get method to hit url on  browser

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()