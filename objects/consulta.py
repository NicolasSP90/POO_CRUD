class Consulta:
    def __init__(self, numero = "", instituicao = "", medico = "", paciente = "", sintomas = "", descricao = "", enfermidade = "", prescricao = "") -> None:
        self.__identificador = numero
        self.__instituicao = instituicao
        self.__medico = medico
        self.__paciente = paciente
        self.__sintomas = sintomas
        self.__descricao = descricao
        self.__enfermidade = enfermidade
        self.__prescricao = prescricao
        
    def __repr__(self) -> str:
        return f"\nIdentificador:{self.__identificador}\nInstituição: {self.__instituicao}\nMédico: {self.__medico}\nPaciente: {self.__paciente}\nSintomas: {self.__sintomas}\nDescrição: {self.__descricao}\nEnfermidade: {self.__enfermidade}\nPrescrição: {self.__prescricao}"
    
    @property
    def identificador(self):
        return self.__identificador
    
    @identificador.setter
    def identificador(self, novo_identificador):
        self.__identificador = novo_identificador

    @property
    def instituicao(self) -> str:
        return self.__instituicao
    
    @instituicao.setter
    def instituicao(self, nova_instituicao) -> None:
        self.__instituicao = nova_instituicao

    @property
    def cnpj(self) -> str:
        return self.__instituicao
    
    @cnpj.setter
    def cnpj(self, novo_cnpj) -> None:
        self.__instituicao = novo_cnpj

    @property
    def medico(self) -> str:
        return self.__medico
    
    @medico.setter
    def medico(self, novo_medico) -> None:
        self.medico = novo_medico

    @property
    def crm(self) -> str:
        return self.__paciente

    @crm.setter
    def medico(self, novo_crm) -> None:
        self.medico = novo_crm

    @property
    def paciente(self) -> str:
        return self.__paciente
    
    @paciente.setter
    def paciente(self, nova_paciente) -> None:
        self.__paciente = nova_paciente

    @property
    def cpf(self) -> str:
        return self.__paciente
    
    @cpf.setter
    def cpf(self, novo_cpf) -> None:
        self.__paciente = novo_cpf

    @property
    def sintomas(self) -> str:
        return self.__sintomas
    
    @sintomas.setter
    def sintomas(self, nova_sintomas) -> None:
        self.__sintomas = nova_sintomas

    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_descricao) -> None:
        self.__descricao = nova_descricao

    @property
    def enfermidade(self) -> str:
        return self.__enfermidade
    
    @enfermidade.setter
    def enfermidade(self, nova_enfermidade) -> None:
        self.__enfermidade = nova_enfermidade

    @property
    def prescricao(self) -> str:
        return self.__prescricao
    
    @prescricao.setter
    def prescricao(self, nova_prescricao) -> None:
        self.__prescricao = nova_prescricao

    # Exportar valores em formato de dicionário
    @property
    def exportar(self) -> dict:
        return {self.__identificador:{"instituicao":self.__instituicao,
                                      "medico":self.__medico,
                                      "paciente":self.__paciente,
                                      "sintomas":self.__sintomas,
                                      "descricao":self.__descricao,
                                      "enfermidade":self.__enfermidade,
                                      "prescricao":self.__prescricao}}

    
    @property
    def importar(self) -> None:
        return {"instituicao":self.__instituicao,
                "medico":self.__medico,
                "paciente":self.__paciente,
                "sintomas":self.__sintomas,
                "descricao":self.__descricao,
                "enfermidade":self.__enfermidade,
                "prescricao":self.__prescricao}

    @importar.setter
    def importar(self, novo_dicionario:dict) -> None:
        self.__instituicao = novo_dicionario["instituicao"]
        self.__medico = novo_dicionario["medico"]
        self.__paciente = novo_dicionario["paciente"]
        self.__sintomas = novo_dicionario["sintomas"]
        self.__descricao = novo_dicionario["descricao"]
        self.__enfermidade = novo_dicionario["enfermidade"]
        self.__prescricao = novo_dicionario["prescricao"]
