from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from datetime import datetime, date

import os
import webbrowser
import time
import logging


def login(driver):
	load_dotenv()

	driver.get("https://app.evertime.es/pages/login")
	driver.find_element(By.ID, "ocode").send_keys(os.environ.get('codigo_centro'))
	driver.find_element(By.ID, "account").send_keys(os.environ.get('username'))
	driver.find_element(By.ID, "pass").send_keys(os.environ.get('password'))

	button = driver.find_element(By.ID, "blogin")
	button.click()
	time.sleep(5)
	logging.warning('Login ok')

def inicio_jornada(driver):
	login(driver)

	button = driver.find_element(by=By.CSS_SELECTOR, value="button.buttonfichaje")
	button.click()
	time.sleep(5)
	driver.close();
	logging.warning("Inicio jornada ok")

def inicio_comida(driver):
	login(driver)

	button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-warning")
	button.click()
	time.sleep(5)
	submitLoginButton = driver.find_element(By.XPATH, '//i[text()="fastfood"]/ancestor::button')
	submitLoginButton.click()
	time.sleep(5)
	logging.warning("Inicio comida ok")

def final_comida(driver):
	login(driver)

	button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-success")
	button.click()
	time.sleep(5)
	logging.warning("Final comida ok")

def final_jornada(driver):
	login(driver)

	button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-danger")
	button.click()
	time.sleep(5)
	logging.warning("Final jornada ok")

def cargar_horario(today):
	load_dotenv()
	inicio_jornada = os.environ.get('inicio_'+str(today))
	inicio_comida = os.environ.get('inicioc_'+str(today))
	final_comida = os.environ.get('finalc_'+str(today))
	final_jornada = os.environ.get('final_'+str(today))
	hora_test = "15:29"
	return inicio_jornada, inicio_comida, final_comida, final_jornada, hora_test


def main():

	if (datetime.today().weekday() != 5) and (datetime.today().weekday() != 6):
		today = datetime.today().weekday()
		inicio_jornada, inicio_comida, final_comida, final_jornada, hora_test = cargar_horario(today)
		now = datetime.now()
		current_time = now.strftime("%H:%M")

		if str(hora_test) != "no":
			if str(current_time) == str(hora_test):
				logging.warning('ENTRA OK')
				driver = webdriver.Chrome()
				login(driver)

		if str(inicio_jornada) != "no":
			if str(current_time) == str(inicio_jornada):
				driver = webdriver.Chrome()
				login(driver)
				inicio_jornada(driver)

		if str(inicio_comida) != "no":
			if str(current_time) == str(inicio_comida):
				driver = webdriver.Chrome()
				login(driver)
				inicio_comida(driver)

		if str(final_comida) != "no":
			if str(current_time) == str(final_comida):
				driver = webdriver.Chrome()
				login(driver)
				final_comida(driver)

		if str(final_jornada) != "no":
			if str(current_time) == str(final_jornada):
				driver = webdriver.Chrome()
				login(driver)
				final_jornada(driver)

while True:
	main()
	time.sleep(60)
