# **Bot de Carga de Productos desde CSV en WordPress**
# Autor: Ricardo Fernández
# Data Science-Data Analytics-Developer Python
# LinkedIn: [Perfil de LinkedIn](https://www.linkedin.com/in/ricardo-fern%C3%A1ndez00)
#
# Descripción:
# Este bot automatiza la carga de productos desde un archivo CSV en una instancia de WordPress con WooCommerce.
# Inicia sesión en WordPress, navega a la herramienta de importación de productos, sube el archivo CSV, 
# realiza selecciones y configuraciones necesarias y realiza la carga de productos.
# El código ha sido organizado y comentado para facilitar su comprensión y adaptación.
#
# Advertencia:
# El uso de este bot es responsabilidad del usuario. El autor no se hace responsable por problemas derivados de un uso indebido
# o mala ejecución del mismo.


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Define el encabezado para las solicitudes web
encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

# Obtén la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo CSV a importar (usando la ruta del directorio actual)
csv_file_path = os.path.join(current_dir, 'productos.csv')

# Iniciar el navegador
driver = webdriver.Chrome()

try:
    # Navegar a la página de inicio de sesión de WordPress
    driver.get('tu link de productos')

    # Ingresar el nombre de usuario y la contraseña
    username = driver.find_element(By.CSS_SELECTOR, 'input#user_login')
    username.send_keys('tu empresa')
    password = driver.find_element(By.CSS_SELECTOR, 'input#user_pass')
    password.send_keys('clave')
    password.send_keys(Keys.RETURN)

    # Esperar a que se cargue la página de inicio de WordPress
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains('wp-admin'))

    # Navegar a la página de importación de productos de WooCommerce
    driver.get('link product_importer')

    # Esperar a que se cargue la página de importación de productos
    wait.until(EC.url_contains('product_importer'))

    # Seleccionar el archivo CSV a importar
    import_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#upload')))
    import_button.send_keys(csv_file_path)

    # Esperar a que se complete la carga del archivo
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div#uploading-message')))

    # Obtener el contenido HTML de la página actual
    html = driver.page_source

    # Crear un objeto BeautifulSoup a partir del contenido HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Cliquear el botón para tildar
    boton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']"))
    )
    boton.click()

    # Hacer clic en el botón de siguiente
    next_button = driver.find_element(By.CSS_SELECTOR, 'button.button.button-primary.button-next')
    next_button.click()

    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div#processing-message')))
    
    # Continuar con el resto del proceso
    
finally:
    # Cierra el navegador al finalizar
    driver.quit()

print("Actualización de Lista Exitosa")

