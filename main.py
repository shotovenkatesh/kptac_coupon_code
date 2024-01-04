import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("operations@hadero.com")
password_field = driver.find_element(By.NAME, "password").send_keys(" welcome2023")
driver.find_element(By.NAME, "submit").click()
time.sleep(1)


# clciking on edit pen link
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[7]/div/div[2]/h4').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[7]/div/div[2]/div[1]/a/i').click()
time.sleep(2)

#clicking coupoun
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/ul/li[9]/a/p').click()


CODE = "SB"
value = 1
MIN_ORDER = 12
USAGE_LIMIT = 1
DISCOUNT_VALUE = 15
END_DATE = "01/31/2024 04:32 pm"



while value <= 250:
    print(value)
    padded_value = str(value).zfill(3)
    final_code = f"{CODE}{padded_value}"


    #click on products
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/a').click()
    time.sleep(1)


    #name field
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[1]/input').click()
    driver.find_element(By.NAME,'code').send_keys(final_code)

    #discount value type
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[2]/div[1]/div/div/button/div[1]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[2]/div[1]/div/div/div/div[3]/ul/li[2]/a').click()

    #discount value
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[2]/div[2]/div/input').click()
    driver.find_element(By.NAME,'discount_value').send_keys(DISCOUNT_VALUE)

    #min order value
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[3]/div[1]/div/input').click()
    driver.find_element(By.NAME,'min_order_value').send_keys(MIN_ORDER)

    #usage limit
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[4]/div[1]/div/input').click()
    driver.find_element(By.NAME,'usage_limit').send_keys(USAGE_LIMIT)

    #Free delivery
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[4]/div[2]/div/div/label/span/span').click()

    #start date
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[7]/div[1]/div/input').click()

    #end date
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[7]/div[2]/div/input').click()
    end_date_input = driver.find_element(By.ID, "id_end_date")
    end_date_input.clear()
    end_date_input.send_keys(END_DATE)

    #submit
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[8]/div/input').click()
    time.sleep(1)
    print(f"{final_code} coupoun code is created")
    value += 1