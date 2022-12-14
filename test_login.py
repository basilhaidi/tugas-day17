import pytest
from _pytest import mark
from _pytest.mark.structures import Mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

Salah =[
  ("basilhaidii","Qwerty123456!"), #Username salah pass benar
  ("basilhaidi","Qwerty1234567"), #Username benar pass salah
  ("basilhaidii","Qwerty1234567") #Username salah pass salah
]

@pytest.fixture
def setup():
  driver = webdriver.Chrome(options=options)
  driver.maximize_window()
  driver.get("https://demoqa.com/")
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
  
def test_login_page(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[6]").click()
  setup.find_element(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-0']").click()
  time.sleep(3)
  assert setup.find_element(By.XPATH, "//div[@class='main-header']").text == "Login"

def test_login_success(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[6]").click()
  setup.find_element(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-0']").click()
  time.sleep(3)
  setup.find_element(By.ID, "userName").send_keys("basilhaidi")
  setup.find_element(By.ID, "password").send_keys("Qwerty123456!")
  time.sleep(3)
  setup.find_element(By.ID, "login").click()
  time.sleep(3)
  assert setup.find_element(By.XPATH, "//label[@id='userName-value']").text == "basilhaidi"


@pytest.mark.parametrize('user,pw',Salah)
def test_login_failed(setup,user,pw):
  time.sleep(2)
  setup.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[6]").click()
  setup.find_element(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-0']").click()
  time.sleep(3)
  setup.find_element(By.ID, "userName").send_keys(user)
  setup.find_element(By.ID, "password").send_keys(pw)
  time.sleep(3)
  setup.find_element(By.ID, "login").click()
  time.sleep(3)
  assert setup.find_element(By.ID, "name").text == "Invalid username or password!"