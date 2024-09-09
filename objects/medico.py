class Medico:
    def __init__(self, nome:str = "", registro_profissional:str = "") -> None:
        self.__nome = nome
        self.__identificador = registro_profissional

    def __repr__(self) -> str:
        return f"\nNome: {self.__nome}\nCRM: {self.__identificador}"
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome) -> str:
        self.__nome = novo_nome
   
    @property
    def identificador(self) -> str:
        return self.__identificador
    
    @identificador.setter
    def identificador(self, novo_identificador) -> str:
        self.__identificador = novo_identificador

    @property
    def crm(self) -> str:
        return self.__identificador
    
    @crm.setter
    def crm(self, novo_crm) -> str:
        self.__identificador = novo_crm

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