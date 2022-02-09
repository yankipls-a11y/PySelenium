from selenium import webdriver

#browser exposes an executable file
#through the Selenium test we need to invoke the executable file, which invokes the actual broswer


#driver = webdriver.Chrome(executable_path="C:\\Users\Yani\PycharmProjects\pythonTesting\chromedriver.exe")
#using this to automate the complete browser
#needed all the time for test cases
#double slash after C:\\ to avoid unicode error fuck you

driver = webdriver.Firefox(executable_path="C:\\Users\Yani\PycharmProjects\pythonTesting\geckodriver.exe")

driver.maximize_window()
#makes the browser full screen

driver.get("https://www.selenium.dev/") #get method to hit URL on browser, so you should land on this page

print (driver.title)
#print (driver.)

print (driver.current_url)

driver.back()
#like the back button in the browser

driver.refresh()
#refreshes the page

driver.close()
#closes the browser