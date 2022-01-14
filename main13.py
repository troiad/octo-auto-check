from lib2to3.pgen2 import driver
import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telnetlib import EC
from selenium import webdriver
from pynput.keyboard import Controller
from pynput.keyboard import Key
import telnetlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time
import requests
from bs4 import BeautifulSoup

global filename
global response
global text
global result
global acc_id
global keyboard

keyboard = Controller()
path = os.path.abspath(os.getcwd())

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.9"
           }

id_octo = input("Введите ключевое слово для аккаунтов: ")
url = "https://app.octobrowser.net/api/v2/automation/profiles?search={}".format(id_octo)

payload = {}
headers_octo = {
    'X-Octo-Api-Token': '79556756b1b64c6e84d51d18570dac99'
}

data_uuid = {}

filename = "~x_test.mp3"
audioToTextDelay = 10
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'


def audioToText(mp3Path):
    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])

    driver.get(googleIBMLink)

    # Upload file
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[6]/button[2]").click()
    time.sleep(2)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # Audio to text is processing
    time.sleep(audioToTextDelay)

    text = driver.find_element(By.XPATH,
                               '//*[@id="root"]/div/div[7]/div/div').find_elements_by_tag_name(
        'span')
    result = " ".join([each.text for each in text])

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return result


def saveFile(content, filename):
    with open(create_dir_mp3() + '~x_test' + '.mp3', 'wb') as handle:
        for data in content.iter_content():
            handle.write(data)


response_octo = requests.request("GET", url, headers=headers_octo, data=payload)
data_uuid = response_octo.json()
uuid = data_uuid.get('data')
newuuid = dict()
for ud in uuid:
    newuuid[ud.pop('uuid')] = ud

octo = str(newuuid)
octo_str = octo.replace("}", '')
octo_str = octo_str.replace("{", '')
octo_str = octo_str.replace(" ", '')
octo_str = octo_str.replace(":", '')
octo_str = octo_str.replace("'", '')

octo_id = octo_str.split(",")
print(octo_id)

while len(octo_id) > 0:
    PROFILE_ID = octo_id.pop(0)
    CHROME_DRIVER = '/Users/mac/PycharmProjects/check_octo/1/chromedriver'
    LOCAL_API = 'http://localhost:58888/api/profiles'


    def create_dir():
        # Parent Directory path
        parent_dir = os.path.expanduser(
            "/Users/mac/~auto/")
        os.path.dirname(os.path.realpath(__file__))
        # Path
        return parent_dir

    def create_dir_mp3():
        # Parent Directory path
        parent_dir_mp3 = os.path.expanduser(
            "/Users/mac/~auto/")
        os.path.dirname(os.path.realpath(__file__))
        # Path
        return parent_dir_mp3


    img_data = requests.get(url="https://thispersondoesnotexist.com/image", headers=headers).content
    with open(create_dir() + '~~~person' + '.jpg', 'wb') as handler:
        handler.write(img_data)


    def get_webdriver(port):
        chrome_options = Options()
        chrome_options.add_experimental_option('debuggerAddress', f'127.0.0.1:{port}')
        # Change chrome driver path accordingly
        driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=chrome_options)
        return driver


    def get_debug_port(profile_id):
        data = requests.post(
            f'{LOCAL_API}/start', json={'uuid': profile_id, 'headless': False, 'debug_port': True}
        ).json()
        return data['debug_port']


    def main():
        global driver
        global response
        port = get_debug_port(PROFILE_ID)
        driver = get_webdriver(port)
        driver.get('https://www.facebook.com/checkpoint/1501092823525282/')
        time.sleep(2)

        # находим кнопку Продолжить, чтобы попасть на капчу
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"scrollview\"]/div/div/div[2]/div/div/div["
                                                            "1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div["
                                                            "3]/div/div/div"))).click()
            time.sleep(5)
        except Exception as e:
            print(e)

        try:
            # находим чекбокс с капчей, и пытаемся его нажать
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id=\"captcha-recaptcha\"]")))
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[1]/div/div/iframe")))
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))).click()
            time.sleep(3)
        except Exception as e:
            print(e)
        # пробуем пройти капчу просто по клику
        try:
            driver.switch_to.default_content()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"scrollview\"]/div/div"
                                                            "/div[2]/div/div/div["
                                                            "1]/div/div/div/div/div/div/div/div"
                                                            "/div/div/div["
                                                            "3]/div/div/div"))).click()
        except Exception as e:
            print(e)

        # если не получилось, ищем кнопку Звуковой капчи и кликаем
        try:
            driver.switch_to.default_content()
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id=\"captcha-recaptcha\"]")))
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[2]/div[4]/iframe")))
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"recaptcha-audio-button\"]"))).click()
            time.sleep(2)
        except Exception as e:
            print(e)
        # жмем Прослушать
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\":2\"]"))).click()
            time.sleep(2)
        except Exception as e:
            print(e)
        #пытаемся скачать звуковой файл капчи
        try:
            href = driver.find_element_by_xpath("//*[@id=\"audio-source\"]").get_attribute('src')
            response = requests.get(href, stream=True)
        except Exception as e:
            print(e)
        try:
            saveFile(response, filename)
        except Exception as e:
            print(e)
        try:
            response = audioToText(create_dir_mp3() + '/' + filename)
            print(response)
        except Exception as e:
            print(e)

        # получаем слова, которые были обнаружены в звуковом файле, и вставляем их
        try:
            driver.switch_to.default_content()
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id=\"captcha-recaptcha\"]")))
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[2]/div[4]/iframe")))
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"audio-response\"]"))).send_keys(response)
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"audio-response\"]"))).send_keys(Keys.ENTER)
        except Exception as e:
            print(e)
        # капча пройдена, ищем кнопку Продолжить
        try:
            time.sleep(5)
            driver.switch_to.default_content()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"scrollview\"]/div/div"
                                                            "/div[2]/div/div/div["
                                                            "1]/div/div/div/div/div/div/div/div"
                                                            "/div/div/div["
                                                            "3]/div/div/div"))).click()
            time.sleep(5)
        except Exception as e:
            print(e)

        # ищем кнопку Загрузить фото и загружаем фото
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "//*[@id=\"scrollview\"]/div/div/div["
                                                                              "2]/div/div/div["
                                                                              "1]/div/div/div/div/div/div/div/div/div"
                                                                              "/div/div["
                                                                              "2]/div/div/div/div/div/div/div/div/div"))).click()
            time.sleep(4)
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(10)
        except Exception as e:
            print(e)
        # фото загружено, ищем кнопку Продолжить
        try:
            driver.find_element_by_xpath(
                "//*[@id=\"scrollview\"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div["
                "3]/div/div/div").click()
            time.sleep(15)
            # чекпоинт пройден
            print("Success")
            driver.close()
        except Exception as e:
            print(e)
            driver.close()


    if __name__ == '__main__':
        main()

