import youtube_dl
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def puxe(x):
    if x['status'] == 'finalizado':
        print('Concluido o download,agora convertendo...')

parametros ={
    'format': 'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
     'progress_hooks' : [puxe],
    
}

search = input(str("Digite o nome da musica ==> "))
print("Processando...")

option = Options()
option.headless = True
driver = webdriver.Chrome('c:\Users\felly\OneDrive\Área de Trabalho\Codigos\pYoutubeMp3')
#driver.maximize_window()
driver.get('https://www.youtube.com/')
print("PESQUISANDO MUSICA...")
input_box = driver.find_element_by_class_name("style-scope ytd-searchbox")

time.sleep(1)

input_box.send_keys(search)
input_box.send_keys(Keys.ENTER)
time.sleep(3)
#input_box = driver.find_element_by_id("video-title").click()
input_box = driver.find_element_by_id("video-title").click()
url_mp3 = driver.current_url

driver.refresh()
driver.quit()
print('Concluido o download de '+ url_mp3  +',agora convertendo...')
youtube = youtube_dl.YoutubeDL(parametros)

youtube.download([url_mp3])



