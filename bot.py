# Import Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Set the path to the ChromeDriver executable
webdriver_path = '/home/adnan/Downloads/chromedriver'  

# options
option = webdriver.ChromeOptions()
# option.add_argument("-incognito")
# option.add_argument("--headless")
# option.add_argument("disable-gpu")
option.binary_location = "/usr/bin/brave"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path, options=option)


# Open URL
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeyRnNmfhAHa4piOlBc-Hg4sHjz8kVl73UFQ6ofqOoicFKEow/viewform?usp=pp_url&entry.654267232=Classification+problems+with+multiple+classes&entry.1122298898=By+adding+a+penalty+term+to+the+loss+function+that+discourages+the+model+from+having+high+coefficients&entry.423845870=will+never+decrease+the+training+error.&entry.1420555353=Sigmoid&entry.698147537=minimizing+false+positive+and+maximizing+true+positive+is+in+focus.&entry.1289474642=0.40&entry.712938498=To+predict+the+probabilities+of+a+binary+outcome&entry.1518936156=To+compare+different+models&entry.537832320=Reduce+the+number+of+features+by+manually+selecting+some+features.&entry.537832320=Selecting+the+right+model+using+model+selection+algorithm.&entry.537832320=Keep+all+features+but+reduce+magnitude+of+parameters.&entry.123827720=0.116")

# wait for one second, until page gets fully loaded
time.sleep(1)

# Data
start = 2301
end = 2374
prefix = "2020UCM"

datas = [prefix + str(number) for number in range(start, end+1)]
random.shuffle(datas)

# Delete 5 random elements
indices_to_delete = random.sample(range(len(datas)), 5)
indices_to_delete.sort(reverse=True)  # Sort indices in descending order to avoid index shifting

for index in indices_to_delete:
    del datas[index]

# Delete specific elements
elements_to_delete = ["2020UCM2313", "2020UCM2372", "2020UCM2373"]

for element in elements_to_delete:
    if element in datas:
        datas.remove(element)

print(len(datas))

# Iterate through each data
for data in datas[:50]:
	# Initialize count is zero
    time.sleep(2)
    if data == "2020UCM2313" or data == "2020UCM2372" or data == "2020UCM2373":
        print(data)
        pass

    # fill the text boxes
    textbox = driver.find_element(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    textbox.send_keys(data)

	# click on submit button
    submit = driver.find_element(By.XPATH,
		'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    time.sleep(2)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeyRnNmfhAHa4piOlBc-Hg4sHjz8kVl73UFQ6ofqOoicFKEow/viewform?usp=pp_url&entry.654267232=Classification+problems+with+multiple+classes&entry.1122298898=By+adding+a+penalty+term+to+the+loss+function+that+discourages+the+model+from+having+high+coefficients&entry.423845870=will+never+decrease+the+training+error.&entry.1420555353=Sigmoid&entry.698147537=minimizing+false+positive+and+maximizing+true+positive+is+in+focus.&entry.1289474642=0.40&entry.712938498=To+predict+the+probabilities+of+a+binary+outcome&entry.1518936156=To+compare+different+models&entry.537832320=Reduce+the+number+of+features+by+manually+selecting+some+features.&entry.537832320=Selecting+the+right+model+using+model+selection+algorithm.&entry.537832320=Keep+all+features+but+reduce+magnitude+of+parameters.&entry.123827720=0.116")

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeyRnNmfhAHa4piOlBc-Hg4sHjz8kVl73UFQ6ofqOoicFKEow/viewform?usp=pp_url&entry.654267232=Classification+problems+with+multiple+classes&entry.1122298898=By+adding+a+penalty+term+to+the+loss+function+that+discourages+the+model+from+having+high+coefficients&entry.423845870=will+never+decrease+the+training+error.&entry.1420555353=Sigmoid&entry.698147537=minimizing+false+positive+and+maximizing+true+positive+is+in+focus.&entry.1289474642=0.40&entry.712938498=To+predict+the+probabilities+of+a+binary+outcome&entry.1518936156=To+calculate+the+standard+errors+of+the+coefficients&entry.537832320=Reduce+the+number+of+features+by+manually+selecting+some+features.&entry.537832320=Selecting+the+right+model+using+model+selection+algorithm.&entry.537832320=Keep+all+features+but+reduce+magnitude+of+parameters.&entry.123827720=0.912")

for data in datas[50:59]:
	# Initialize count is zero
    time.sleep(2)
    if data == "2020UCM2313" or data == "2020UCM2372" or data == "2020UCM2373":
        print(data)
        pass

    # fill the text boxes
    textbox = driver.find_element(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    textbox.send_keys(data)

	# click on submit button
    submit = driver.find_element(By.XPATH,
		'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    time.sleep(2)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeyRnNmfhAHa4piOlBc-Hg4sHjz8kVl73UFQ6ofqOoicFKEow/viewform?usp=pp_url&entry.654267232=Classification+problems+with+multiple+classes&entry.1122298898=By+adding+a+penalty+term+to+the+loss+function+that+discourages+the+model+from+having+high+coefficients&entry.423845870=will+never+decrease+the+training+error.&entry.1420555353=Sigmoid&entry.698147537=minimizing+false+positive+and+maximizing+true+positive+is+in+focus.&entry.1289474642=0.40&entry.712938498=To+predict+the+probabilities+of+a+binary+outcome&entry.1518936156=To+calculate+the+standard+errors+of+the+coefficients&entry.537832320=Reduce+the+number+of+features+by+manually+selecting+some+features.&entry.537832320=Selecting+the+right+model+using+model+selection+algorithm.&entry.537832320=Keep+all+features+but+reduce+magnitude+of+parameters.&entry.123827720=0.912")

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeyRnNmfhAHa4piOlBc-Hg4sHjz8kVl73UFQ6ofqOoicFKEow/viewform?usp=pp_url&entry.654267232=Classification+problems+with+multiple+classes&entry.1122298898=By+removing+some+of+the+independent+variables+from+the+model&entry.423845870=will+never+decrease+the+training+error.&entry.1420555353=Sigmoid&entry.698147537=minimizing+false+positive+and+maximizing+true+positive+is+in+focus.&entry.1289474642=0.40&entry.712938498=To+predict+the+probabilities+of+a+binary+outcome&entry.1518936156=To+calculate+the+standard+errors+of+the+coefficients&entry.537832320=Reduce+the+number+of+features+by+manually+selecting+some+features.&entry.537832320=Selecting+the+right+model+using+model+selection+algorithm.&entry.537832320=Keep+all+features+but+reduce+magnitude+of+parameters.&entry.123827720=0.652")

for data in datas[59:]:
	# Initialize count is zero
    time.sleep(2)
    if data == "2020UCM2313" or data == "2020UCM2372" or data == "2020UCM2373":
        print(data)
        pass

    # fill the text boxes
    textbox = driver.find_element(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    textbox.send_keys(data)

	# click on submit button
    submit = driver.find_element(By.XPATH,
		'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    time.sleep(2)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeyRnNmfhAHa4piOlBc-Hg4sHjz8kVl73UFQ6ofqOoicFKEow/viewform?usp=pp_url&entry.654267232=Classification+problems+with+multiple+classes&entry.1122298898=By+removing+some+of+the+independent+variables+from+the+model&entry.423845870=will+never+decrease+the+training+error.&entry.1420555353=Sigmoid&entry.698147537=minimizing+false+positive+and+maximizing+true+positive+is+in+focus.&entry.1289474642=0.40&entry.712938498=To+predict+the+probabilities+of+a+binary+outcome&entry.1518936156=To+calculate+the+standard+errors+of+the+coefficients&entry.537832320=Reduce+the+number+of+features+by+manually+selecting+some+features.&entry.537832320=Selecting+the+right+model+using+model+selection+algorithm.&entry.537832320=Keep+all+features+but+reduce+magnitude+of+parameters.&entry.123827720=0.652")

driver.close()

