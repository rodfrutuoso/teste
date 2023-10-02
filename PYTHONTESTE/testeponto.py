#pip install selnium, pip install numpy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import json
import os
# servico = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = servico)
CAMINHO = 'C:\\Users\\ECOELETRICA\\Documents\\Downloads PYPY'


options = webdriver.ChromeOptions()
#ESSE APP STATE É PARA AJUSTAR AS CONFIGS DE BAIXAR PDF POR MEIO DO SCRIPT  "execute_script("window.print();")" QUE BASICAMENTE EXECUTA CTRL+P
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}


prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
         'savefile.default_directory':CAMINHO,
         'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'plugins.always_open_pdf_externally': True,
         'download.default_directory' : CAMINHO}
options.add_experimental_option("prefs",prefs)
options.add_argument('--kiosk-printing')
# options.add_argument('--disable-print-preview')
# options.add_argument('--disable-printer-selection')
# options.add_argument('--disable-popup-blocking')
# options.add_argument('--disable-infobars')
#chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print(os.path.join(os.getcwd(),"chromedriver.exe"))
chrome = webdriver.Chrome(service=Service(executable_path="PYTHONTESTE\\chromedriver.exe"), options=options)



def teste_ai(dia):
    try:
        
        chrome.get('https://script.google.com/a/macros/ecoeletrica.com.br/s/AKfycbyZUJxKW_LunbZqYFJLHBo7YWxQBNmFUClSJ4iFdlkFrUXtHReZJd9yTdxyXQNtbOK1yQ/exec') #COLOCA O LINK E COMECE 

        chrome.switch_to.default_content()
        WebDriverWait(chrome, 200).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'sandboxFrame')))
        WebDriverWait(chrome, 200).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'userHtmlFrame')))
        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf"]')))
        chrome.find_element('xpath', '//*[@id="cpf"]').send_keys("07439759524")
        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="senha"]')))
        chrome.find_element('xpath', '//*[@id="senha"]').send_keys("9524")
        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-validation-cpf"]/button')))
        chrome.find_element('xpath', '//*[@id="screen-validation-cpf"]/button').click()

        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-validation-info-for-user"]/div/button[2]')))
        chrome.find_element('xpath', '//*[@id="modal-validation-info-for-user"]/div/button[2]').click()

        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-options-for-administrador"]/button[1]')))
        chrome.find_element('xpath', '//*[@id="modal-options-for-administrador"]/button[1]').click()

        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select-coordenation"]/option[6]')))
        chrome.find_element('xpath', '//*[@id="select-coordenation"]/option[6]').click()
        chrome.find_element('xpath', '//*[@id="data-compensatory"]').send_keys(dia)
        chrome.find_element('xpath', '//*[@id="entrada-time"]').send_keys("0700")
        chrome.find_element('xpath', '//*[@id="almoco-time"]').send_keys("1200")
        chrome.find_element('xpath', '//*[@id="pos-almoco-time"]').send_keys("1300")
        chrome.find_element('xpath', '//*[@id="saida-time"]').send_keys("1700")
        chrome.find_element('xpath', '//*[@id="icon-for-add"]/button').click()
        chrome.find_element('xpath', '//*[@id="extra-entrada-time"]').send_keys("1900")
        chrome.find_element('xpath', '//*[@id="extra-saida-time"]').send_keys("2000")
        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="motivo-hora-extra"]')))
        chrome.find_element('xpath', '//*[@id="motivo-hora-extra"]').send_keys("tacando a cobra no ponto de joão")
        WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="screen-compensatory"]/button')))

        print('passou da espera, vou clicar em')
        chrome.find_element('xpath', '//*[@id="screen-compensatory"]/button').click()

        while True:
            try:
                chrome.find_element('xpath', '//*[@id="modal-confirm-before-send"]/div/button[2]').click()
                break
            except: 
                chrome.find_element('xpath', '//*[@id="screen-compensatory"]/button').click()


        # WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-confirm-before-send"]/div/button[2]')))
        # chrome.find_element('xpath', '//*[@id="modal-confirm-before-send"]/div/button[2]').click()
        
        #input('Wait')# USO ESSE COMANDO APENAS PARA PARAR O SELENIUM E IMPEDIR QUE ELE FECHE AO DAR ERRO


        return True
    except:
        return False
    
for x in range (5,30):

    if teste_ai(f"{x}092023"):
        print("passou")
    else:
        print("falhou")