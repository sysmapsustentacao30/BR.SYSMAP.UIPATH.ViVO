import sys
import os
import requests

def get_list(codRelease, analista):

    #Url para gerar o token
    url="http://apisanity.sysmap.com.br/api/ReleaseVivo/ListCenarios"   

    # Parametros
    param = {"codRelease": codRelease , "analista": analista}

    lista_cenarios = requests.get(url, params=param)

    return lista_cenarios.text


def update_cenario(codRelease,numTeste,status,observacao):

    url="http://apisanity.sysmap.com.br/api/ReleaseVivo/AtualizaCenario" 

    # Parametros
    param = {"codRelease": codRelease, "numTeste":numTeste, "status":status,"observacao":observacao} 

    update = requests.post(url, params=param)

    return update.text
