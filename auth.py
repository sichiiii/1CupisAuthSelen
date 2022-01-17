from selenium.webdriver.common.by import By
from time import sleep
import undetected_chromedriver.v2 as uc

option = uc.ChromeOptions()
option.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=option)
driver.get('https://wallet.1cupis.ru/auth')

sleep(3)
driver.find_element(By.ID, "form_login_phone").send_keys("952*******")
driver.find_element(By.XPATH, '//*[@id="form_login"]/div[1]/div[2]/input').send_keys("***")
driver.find_element(By.XPATH, '//*[@id="btn_authorization_enter"]').click()
sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/h2/a').click()

sleep(60)