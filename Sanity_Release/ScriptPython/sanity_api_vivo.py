import sys
import os
import requests


def get_list_cenarios(email, password):

    #Url para gerar o token
    url="http://zeta.sysmap.com.br:9003/api/ReleaseVivo/ListCenarios"   

    # Parametros
    param = {"email": email, "password": password}

    lista_cenarios = requests.get(url, params=param)

    return lista_cenarios.text

def update_cenario(email,password,cenario,executado,status,codRelease):

    #Url para gerar o token
    url="http://zeta.sysmap.com.br:9003/api/ReleaseVivo/AtualizaCenario" 

    # Parametros
    param = {"email": email, "password": password,"cenario": cenario, "executado": executado, "status": status, "codRelease": codRelease} 

    update = requests.post(url, params=param)

    return update.text
