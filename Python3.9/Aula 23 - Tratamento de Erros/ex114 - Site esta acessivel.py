import cores
import urllib.request

# site.read() consegue acessar o html do site

try:
    urllib.request.urlopen('http://www.pudim.com.br')
    print(f'{cores.verde}Consegui acessar o site do Pudim!{cores.clear}')
except:
    print(f'{cores.red}O site do Pudim não está acessível no momento. {cores.clear}')
