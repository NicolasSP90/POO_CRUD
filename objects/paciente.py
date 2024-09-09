class Paciente:
    def __init__(self, nome:str = "", identificador:str = "")  -> None:
        self.__nome = nome
        self.__identificador = identificador

    def __repr__(self) -> str:
        return f"\nNome: {self.__nome}\nCPF: {self.__identificador}"
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def identificador(self) -> str:
        return self.__identificador
    
    @identificador.setter
    def identificador(self, novo_identificador):
        self.__identificador = novo_identificador
    
    @property
    def cpf(self):
        return self.__identificador
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__identificador = novo_cpf

    # Exportar valores em formato de dicionário
    @property
    def exportar(self) -> dict:
        return {self.__identificador:{"nome": self.__nome}}

    @property
    def importar(self) -> None:
        return None

    @importar.setter
    def importar(self, dicionario) -> None:
        self.__nome = dicionario["nome"]
