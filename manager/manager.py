# Biliotecas
import json
import os

# Objetos
from objects.consulta import Consulta

# Variáveis
from env import path_current, path_data

# Cria a pasta Data e os arquivos .json caso não existam
def inicializar_db():
    if "data" not in os.listdir(path_current):
        os.makedirs("data")
    dicionarios = os.listdir(path_data)
    for dicionario in ["consulta.json", "instituicao.json", "medico.json", "paciente.json"]:
        if dicionario not in dicionarios:
            with open(os.path.join(path_data, dicionario), "w", encoding="utf-8") as file:
                file.write(json.dumps(dict()))
            if dicionario == "instituicao.json":
                with open(os.path.join(path_data, dicionario), "w", encoding="utf-8") as file:
                    file.write(json.dumps(dict({"00.000.000/0000-00": {"nome": "Admin"}})))
                    os.system("cls")
                    print("--> Banco de dados inicializado <--")
                    print("--> Faça login como admin - CNPJ: 00.000.000/0000-00 <--")
                    

# A partir de um objeto, cadastra ele no banco de dados
def cadastrar(objeto):
    nome = str(type(objeto).__name__).lower()+".json" # retorna o nome da classe em minúsculo
    with open(os.path.join(path_data, nome), "r", encoding="utf-8") as file: # Carrega os dados
        dados = json.load(file)
    dados.update(objeto.exportar)
    with open(os.path.join(path_data, nome), "w", encoding="utf-8") as file: # Registra os dados
        file.write(json.dumps(dados, indent=4, ensure_ascii=False))


# A partir de um objeto e uma chave primária, carrega os dados do banco de dados no objeto
def carregar(objeto, chave_primaria) -> object:
    nome = str(type(objeto).__name__).lower()+".json"# retorna o nome da classe em minúsculo
    with open(os.path.join(path_data, nome), "r", encoding="utf-8") as file:
        dados = json.load(file)
    if len(dados) != 0:
        if chave_primaria != "":
            if chave_primaria in dados:
                objeto.identificador = chave_primaria
                objeto.importar = dados[chave_primaria]
                return objeto
    return None


# A partir de um objeto, verifica quantos registros existem no banco de dados
def carregar_entradas(objeto) -> int:
    nome = str(type(objeto).__name__).lower()+".json" # retorna o nome da classe em minúsculo
    with open(os.path.join(path_data, nome), "r", encoding="utf-8") as file:
        dados = json.load(file)
    if len(dados) != 0:
        return list(dados.keys())


# A partir de um objeto, edita o registro dele no banco de dados com os valores de um dicionário
def editar(objeto, dicionario) -> object:
    nome = str(type(objeto).__name__).lower()+".json"# retorna o nome da classe em minúsculo
    
    # Armazena a chave original para o caso de ser necessário atualizar os dados de consulta
    if nome != "consulta.json":
        chave_original = objeto.identificador
    deletar(objeto, objeto.identificador)
    objeto.identificador = list(dicionario.keys())[0]
    objeto.importar = dicionario[objeto.identificador]
    cadastrar(objeto)

    if nome != "consulta.json":
        with open(os.path.join(path_data, "consulta.json"), "r", encoding="utf-8") as file:
            dados = json.load(file)
        for chave in dados:
            if dados[chave][nome[:-5]] == chave_original:
                dados[chave][nome[:-5]] = objeto.identificador
        with open(os.path.join(path_data, "consulta.json"), "w", encoding="utf-8") as file: # Registra os dados
            file.write(json.dumps(dados, indent=4, ensure_ascii=False))
    return objeto


# Deleta um objeto específico a partir de uma chave primária
def deletar(objeto, chave_primaria):
    nome = str(type(objeto).__name__).lower()+".json" # retorna o nome da classe em minúsculo
    with open(os.path.join(path_data, nome), "r", encoding="utf-8") as file:
        dados = json.load(file)
    dados.pop(chave_primaria)
    with open(os.path.join(path_data, nome), "w", encoding="utf-8") as file:
        file.write(json.dumps(dados, indent=4, ensure_ascii=False))