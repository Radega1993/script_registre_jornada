from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from datetime import datetime, date

import os 
import webbrowser
import time



def login(driver):
	load_dotenv()
		
	driver.get("https://app.evertime.es/pages/login")
	driver.find_element(By.ID, "ocode").send_keys(os.environ.get('codigo_centro'))
	driver.find_element(By.ID, "account").send_keys(os.environ.get('username'))
	driver.find_element(By.ID, "pass").send_keys(os.environ.get('password'))

	button = driver.find_element(By.ID, "blogin")
	button.click()
	time.sleep(5)

def inicio_jornada(driver):
	login(driver)
	
	button = driver.find_element(by=By.CSS_SELECTOR, value="button.buttonfichaje")
	button.click()
	time.sleep(5)
	driver.close();

def inicio_comida(driver):
	login(driver)

	button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-warning")
	button.click()
	time.sleep(5)
	submitLoginButton = driver.find_element(By.XPATH, '//i[text()="fastfood"]/ancestor::button')
	submitLoginButton.click()
	time.sleep(5)

def final_comida(driver):
	login(driver)

	button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-success")
	button.click()
	time.sleep(5)

def final_jornada(driver):
	login(driver)
	
	button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-danger")
	button.click()
	time.sleep(5)

def cargar_horario(today):
	load_dotenv()
	inicio_jornada = os.environ.get('inicio_'+str(today))
	inicio_comida = os.environ.get('inicioc_'+str(today))
	final_comida = os.environ.get('finalc_'+str(today))
	final_jornada = os.environ.get('final_'+str(today))
	return inicio_jornada, inicio_comida, final_comida, final_jornada

def main():
	#driver = webdriver.Chrome()
	#inicio_jornada(driver)
	#inicio_comida(driver)

	 
	if (datetime.today().weekday() != 5) and (datetime.today().weekday() != 6):
		today = datetime.today().weekday()
		inicio_jornada, inicio_comida, final_comida, final_jornada = cargar_horario(today)
		
		now = datetime.now()
		current_time = now.strftime("%H:%M")

		if str(inicio_jornada) != "no":
			if str(current_time) == str(inicio_jornada):
				driver = webdriver.Chrome()
				login(driver)
				inicio_jornada(driver)
		
		if str(inicio_jornada) != "no":
			if str(current_time) == str(inicio_jornada):
				driver = webdriver.Chrome()
				login(driver)
				inicio_comida(driver)

		if str(inicio_jornada) != "no":
			if str(current_time) == str(inicio_jornada):
				driver = webdriver.Chrome()
				login(driver)
				final_comida(driver)

		if str(inicio_jornada) != "no":
			if str(current_time) == str(inicio_jornada):
				driver = webdriver.Chrome()
				login(driver)
				final_jornada(driver)

while True:
	main()
	time.sleep(60)


