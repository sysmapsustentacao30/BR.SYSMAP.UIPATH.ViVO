import sys
import os
import requests

def get_list(email, password):

    email = "uipath.api@sysmap.com.br"
    password = "UIPath2018"
    #Url para gerar o token
    url="http://apisanity.sysmap.com.br/api/ReleaseVivo/ListCenarios"   

    # Parametros
    param = {"email": email, "password": password}

    lista_cenarios = requests.get(url, params=param)

    return lista_cenarios.text


def update_cenario(email,password,cenario,executado,status,codRelease):

    email = "uipath.api@sysmap.com.br"
    password = "UIPath2018"

    url="http://apisanity.sysmap.com.br/api/ReleaseVivo/AtualizaCenario" 

    # Parametros
    param = {"email": email, "password": password,"cenario": cenario, "executado": executado, "status": status, "codRelease": codRelease} 

    update = requests.post(url, params=param)

    return update.text
