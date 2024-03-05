from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# точнее options.add_argument("--headless=new")



service = Service('chromedriver\chromedriver.exe')
url = 'https://ajs.su/'
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def get_source(url):
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.delete_all_cookies()
        driver.get(url)
        
        
        
        # element = driver.find_element(By.XPATH, '/html/body/div/div[1]')
        # driver.execute_script(
        #     "arguments[0].click();", element)
        # time.sleep(5)
        div_to_frame = driver.find_element(By.XPATH, '//div[@id="carrotquest-messenger-collapsed-container"]/div/div/iframe')
        driver.switch_to.frame(div_to_frame)

        driver.find_element(By.XPATH, '/html/body/div/div[1]').click()
        time.sleep(5)
        
        driver.switch_to.default_content()
        
        frame2 = driver.find_element(By.ID, 'carrot-messenger-frame')
        driver.switch_to.frame(frame2)
        
        driver.find_element(By.XPATH, '//*[@id="carrotquest-messenger"]/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]/button').click()
        time.sleep(5)
        
        
        message_input = driver.find_element(By.ID, 'opened-textfield')
        message_input.send_keys('Добрый вечер')
        message_input.send_keys(Keys.ENTER)
        print('Сообщение отправлено')
        time.sleep(20)
        
    except Exception as e:
        print(e)
        
    finally:
        driver.close()
        driver.quit()

def main():
    get_source(url)

if __name__ == '__main__':
    main()