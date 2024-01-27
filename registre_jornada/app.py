from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
import os
import time
import logging
from datetime import datetime, date
from dotenv import load_dotenv
import pytz

# Carga las variables de entorno
load_dotenv()

# Configuración del logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler("auto_registre_jornada.log"),
                              logging.StreamHandler()])

# Registro de acciones ejecutadas
executed_actions = {}

def get_driver():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        logging.info("WebDriver initiated")
        return driver
    except Exception as e:
        logging.error(f"Error initiating WebDriver: {e}")
        return None

def login(driver):
    try:
        driver.get("https://app.evertime.es/pages/login")
        driver.find_element(By.ID, "ocode").send_keys(os.getenv('codigo_centro'))
        driver.find_element(By.ID, "account").send_keys(os.getenv('username'))
        driver.find_element(By.ID, "pass").send_keys(os.getenv('password'))

        button = driver.find_element(By.ID, "blogin")
        button.click()
        time.sleep(5)
        logging.info('Login successful')
    except WebDriverException as e:
        logging.error(f"Error during login: {e}")

def perform_action(driver, button_selector, action_name):
    if driver is None:
        logging.error(f"Driver not initialized, cannot perform {action_name}")
        return

    try:
        login(driver)
        button = driver.find_element(by=By.CSS_SELECTOR, value=button_selector)
        button.click()
        time.sleep(5)
        logging.info(f"{action_name} executed successfully")
    except WebDriverException as e:
        logging.error(f"Error during {action_name}: {e}")
    finally:
        driver.quit()

def inicio_comida(driver):
    login(driver)

    button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-warning")
    button.click()
    time.sleep(5)

    # Realizar el segundo clic
    try:
        submitLoginButton = driver.find_element(By.XPATH, '//i[text()="fastfood"]/ancestor::button')
        submitLoginButton.click()
        time.sleep(5)
        logging.info("Inicio comida ok")
    except WebDriverException as e:
        logging.error(f"Error during inicio comida (second click): {e}")

def cargar_horario(today):
    return (
        os.getenv(f'inicio_{today}'),
        os.getenv(f'inicioc_{today}'),
        os.getenv(f'finalc_{today}'),
        os.getenv(f'final_{today}')
    )

def convert_to_minutes(hora_str):
    if hora_str and hora_str != "no":
        h, m = map(int, hora_str.split(":"))
        return h * 60 + m
    return None

def main():
    madrid_timezone = pytz.timezone('Europe/Madrid')

    weekday = datetime.today().weekday()
    logging.info(f"Today is {weekday}, which corresponds to {date.today().strftime('%A')}")
    inicio_jornada_hora, inicio_comida_hora, final_comida_hora, final_jornada_hora = cargar_horario(weekday)
    current_time = datetime.now(madrid_timezone).strftime("%H:%M")    
    current_minutes = convert_to_minutes(current_time)

    logging.info(f"Current time is {current_time}")

    actions = [
        (convert_to_minutes(inicio_comida_hora), "button.btn-warning", "inicio_comida"),  # Pausa para comer
        (convert_to_minutes(inicio_jornada_hora), "button.buttonfichaje", "inicio_jornada"),  # Inicio de jornada
        (convert_to_minutes(final_comida_hora), "button.btn-success", "final_comida"),  # Fin de la pausa para comer
        (convert_to_minutes(final_jornada_hora), "button.btn-danger", "final_jornada")  # Fin de la jornada
    ]

    for hora_minutes, selector, action_key in actions:
        action_name = action_key.replace('_', ' ').capitalize()
        if hora_minutes and current_minutes >= hora_minutes:
            if executed_actions.get(action_key) != weekday:
                logging.info(f"Attempting to perform {action_name} at {current_time}")
                driver = get_driver()
                if action_key == "inicio_comida":
                    inicio_comida(driver)
                else:
                    perform_action(driver, selector, action_name)
                executed_actions[action_key] = weekday
            else:
                logging.info(f"Action {action_name} already executed for today")
        
if __name__ == "__main__":
    logging.info("Starting Auto Registre Jornada script")
    while True:
        main()
        time.sleep(30)
