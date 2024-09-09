class Instituicao:
    def __init__(self, nome = "", cnpj = "") -> None:
        self.__nome = nome
        self.__identificador = cnpj

    def __repr__(self) -> str:
        return f"\nNome: {self.__nome}\nCNPJ: {self.__identificador}"

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome) -> None:
        self.__nome = novo_nome

    @property
    def identificador(self) -> str:
        return self.__identificador
    
    @identificador.setter
    def identificador(self, novo_identificador):
        self.__identificador = novo_identificador

    @property
    def cnpj(self) -> str:
        self.__identificador
    
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__identificador = novo_cnpj

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
    

    

