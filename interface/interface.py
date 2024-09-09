# Objetos
from objects.instituicao import Instituicao
from objects.medico import Medico
from objects.paciente import Paciente
from objects.consulta import Consulta
from manager.manager import cadastrar, carregar, carregar_entradas, editar, deletar

# Biblioteca
import os

# A interface foi tratada como objeto para que tenha atributos atribuidos a ela
# Dessa forma o estado dela dita a sequencia ou não do programa
# Além de exibir o menu de acordo com os próprios atributos
class Interface:
    def __init__(self, status:bool = True, login:bool = False, menu:str = "raiz", nome:str = "MENU", cnpj:str = ""):
        self.__status = status
        self.__login = login
        self.__menu = menu
        self.__nome = nome
        self.__cnpj = cnpj
    
    def __repr__(self) -> str:
        return f"{self.__status}, {self.__login}, {self.__menu}, {self.__nome}, {self.__cnpj}"

    # Seleção do menu de exibição e ações de acordo com cada um
    def selecao_menu(self, tipo_menu:str = "raiz"):

        # Função para verificar se o numero do input(menu) está dentro das opções disponíveis (referencia)
        # Também retorna o status da interface. O retorno define se o programa deve continuar
        @staticmethod
        def loop_escolha(menu, referencia):
            escolha = input("Digite a opção desejada: ")
            while escolha not in referencia:
                escolha = input("Digite uma opção válida: ")

            if (escolha == "0") and (menu == "raiz"):
                return escolha, False
            else:
                return escolha, True

        # Função para validar o formato do CNPJ no formato utilizado
        @staticmethod
        def validar_cnpj():
            cnpj_login = input("Digite o CNJP da instituição (formato: 11.111.111/1111-11): ")
            if cnpj_login == "":
                return ""
            while (len(cnpj_login) != 18) or (cnpj_login.count(".") != 2) or (cnpj_login.count("/") != 1) or cnpj_login.count("-") != 1:
                cnpj_login = input("Digite o CNJP da instituição (formato: 11.111.111/1111-11): ")
                if cnpj_login == "":
                    return ""
            a, b, x = cnpj_login.upper().split(".")
            c, y = x.split("/")
            d, e = y.split("-")
            if not (a.isalnum() and b.isalnum() and c.isalnum() and d.isalnum() and e.isnumeric()):
                print("CNPJ inválido.")
                return ""
            return cnpj_login
        
        # Função para validar o CPF no formato utilizado
        @staticmethod
        def validar_cpf():
            cpf = input("Digite o CPF (formato: 111.111.111-11): ")
            if cpf == "":
                return ""
            while (len(cpf) != 14) or (cpf.count(".") != 2) or (cpf.count("-") != 1):
                cpf = input("Digite o CPF (formato: 111.111.111-11): ")
                if cpf == "":
                    return ""
            a, b, x = cpf.upper().split(".")
            c, d = x.split("-")
            if not (a.isnumeric() and b.isnumeric() and c.isnumeric() and d.isnumeric()):
                print("CPF inválido.")
                return ""
            return cpf
        
        # Função para validar o CRM do médico
        @staticmethod
        def validar_crm():
            crm = input("Digite o CRM (formato: 11111): ")
            if crm == "":
                return ""
            while (len(crm) != 5) or not crm.isnumeric():
                crm = input("Digite o CRM (formato: 11111): ")
                if crm == "":
                    return ""
            return crm
        
        # Função para validar o numero informado
        @staticmethod
        def validar_numero():
            num = input(f"Digite o número da consulta: ")
            while not (num.isnumeric() or (num == "")):
                num = input(f"Digite o número da consulta: ")
            return num

        # Menu Raiz
        if tipo_menu == "raiz":
            print(f"""
                ============={self.__nome}=============
                1-Definir instituicao atual
                2-Pesquisar instituição
                3-Pesquisar médico
                4-Pesquisar paciente
                0-Sair
                ============={self.__nome}=============
                """)
        
            opcao, self.status = loop_escolha(tipo_menu, "01234")
            
            # Opção para fazer o login.
            if opcao == "1":
                cnpj_login = validar_cnpj()

                objeto_login = Instituicao(cnpj=cnpj_login)

                # Tenta carregar o objeto com os dados do banco de dados
                # Se conseguir atribui os valores na interface
                try:
                    carregar(objeto_login, cnpj_login)
                    print(objeto_login)
                    self.login = True
                    self.nome = objeto_login.nome
                    self.cnpj = objeto_login.identificador
                    os.system("cls")
                    return "logado"
                
                # Se não conseguir carregar,informa e mantém no menu raiz
                except:
                    os.system("cls")
                    print(f"{cnpj_login} não consta na base de dados.")
                    self.login = False
                    return "raiz"
            
            elif opcao == "2":
                return "pesquisar_instituicao"
            
            elif opcao == "3":
                return "pesquisar_medico"
            
            elif opcao == "4":
                return "pesquisar_paciente"

            # Em tese não ocorre. Está aqui para não gerar erro.
            else:
                return "raiz"
        
        # Menu após login
        elif tipo_menu == "logado":
            print(f"""
                  ============={self.__nome}=============
                  1-Menu instituição
                  2-Menu consulta
                  3-Menu médico
                  4-Menu paciente
                  0-Logoff
                  ============={self.__nome}=============
                  """)
            
            opcao, self.status = loop_escolha(tipo_menu, "01234")

            # Encaminha para os menus dos objetos
            if opcao == "1":
                return "menu_instituicao"
            
            elif opcao == "2":
                return "menu_consulta"
            
            elif opcao == "3":
                return "menu_medico"
            
            elif opcao == "4":
                return "menu_paciente"
            
            # Retorna para o menu raiz
            else:
                os.system("cls")
                self.__login = False
                self.__nome = "MENU"
                return "raiz"
        
        # Menu Genérico dos objetos.
        elif "menu_" in tipo_menu:
            os.system("cls")
            _, tipo = tipo_menu.split("_")
            print(f"""
                  ============={self.__nome}=============
                  1-Cadastrar {tipo}
                  2-Pesquisar {tipo}
                  3-Editar {tipo}
                  4-Deletar {tipo}
                  0-Voltar
                  ============={self.__nome}=============
                  """)
            
            opcao, self.status = loop_escolha(tipo_menu, "01234")

            # Definição das ações a serem tomadas
            if opcao == "1":
                return f"cadastrar_{tipo}"
            
            elif opcao == "2":
                return f"pesquisar_{tipo}"

            elif opcao == "3":
                return f"editar_{tipo}"

            elif opcao == "4":
                return f"deletar_{tipo}"
            
            else:
                os.system("cls")
                return "logado"


        # Opção de cadastrar e cada uma das opções
        elif "cadastrar_" in tipo_menu:
            _, tipo = tipo_menu.split("_")
            dicionario_update = {}
            
            # Cadastro de instituição
            if tipo == "instituicao":
                # validar_cnpj retorna um valor vazio ou um cnpj
                chave_primaria = validar_cnpj()
                
                # Identificador não pode ser vazio
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Não foi informado um valor válido <--")
                    return "logado"
                
                else:
                    # Verifica se o CNPJ já está cadastrado
                    objeto = Instituicao(cnpj=chave_primaria)
                    verificacao_objeto = carregar(objeto, chave_primaria)

                    # Se não estiver, é feito o cadastro
                    if verificacao_objeto == None:
                        
                        # Valor do nome informado não pode ser vazio
                        nome = input("Informe o nome da instituição: ")
                        if nome == "":
                            os.system("cls")
                            print("--> Não foi informado um valor válido <--")
                            return "logado"
                        
                        # Cadastro da instituição
                        else:
                            dicionario_update = {"nome": nome}

                            # Valores do dicionario importados para o objeto
                            objeto.importar = dicionario_update
                            
                            # Cadastro no banco de dados
                            cadastrar(objeto)
                            os.system("cls")
                            print("--> Instituição foi cadastrada <--")
                    
                    else:
                        os.system("cls")
                        print("--> Instituição já cadastrada <--")
                

            elif tipo == "consulta":
                # Objeto Consulta
                objeto = Consulta()

                # Verifica o número de consultas no banco de dados
                # Armazena o próximo valor
                lista_consultas = carregar_entradas(objeto)
                objeto.identificador = str(max([int(x) for x in lista_consultas]) + 1)
                
                # Atualiza o objeto com a chave primária
                dicionario_update = {objeto.identificador:{}}

                # Validar e informar o médico que deve ser adicionado
                consulta_medico = validar_crm()

                if carregar(Medico(), consulta_medico) == None:
                    os.system("cls")
                    print("--> Não consta no banco de dados <--")
                    return "logado"
                
                # Validar e informar o paciente que deve ser adicionado
                consulta_paciente = validar_cpf()

                if carregar(Paciente(), consulta_paciente) == None:
                    os.system("cls")
                    print("--> Não consta no banco de dados <--")
                    return "logado"

                # Adicionar itens da consulta
                sintomas = input("Detalhe os sintomas: ")

                descricao = input("Detalhe a descrição do caso: ")

                enfermidade = input("Diagnóstico da enfermindade: ")

                prescricao = input("Detalhe a prescrição: ")
                
                # Importar itens para o objeto
                dicionario_update[objeto.identificador] = {"instituicao": self.__cnpj,
                                                             "medico": consulta_medico,
                                                             "paciente": consulta_paciente,
                                                             "sintomas": sintomas,
                                                             "descricao": descricao,
                                                             "enfermidade": enfermidade,
                                                             "prescricao": prescricao}
                
                objeto.importar = dicionario_update[objeto.identificador]

                # Cadastrar objeto no banco de dados
                cadastrar(objeto)
                os.system("cls")
                print("--> Consulta foi cadastrada <--")

            # Cadastro de médico
            elif tipo == "medico":

                # Identificador não pode ser vazio
                chave_primaria = validar_crm()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Não foi informado um valor válido <--")
                    return "logado"
                
                else:
                    # Verifica se o médico já está cadastrado
                    objeto = Medico(registro_profissional=chave_primaria)
                    verificacao_objeto = carregar(objeto, chave_primaria)
                    
                    # Se não estiver, é feito o cadastro
                    if verificacao_objeto == None:

                        # Valor do nome informado não pode ser vazio
                        nome = input("Informe o nome do médico: ")
                        if nome == "":
                            os.system("cls")
                            print("--> Não foi informado um valor válido <--")
                            return "logado"
                        
                        # Cadastro do médico
                        else:
                            dicionario_update = {"nome": nome}

                            # Valores do dicionario importados para o objeto
                            objeto.importar = dicionario_update

                            # Cadastro no banco de dados
                            cadastrar(objeto)
                            os.system("cls")
                            print("--> Médico foi cadastrado <--")
                    
                    else:
                        os.system("cls")
                        print("--> Médico já cadastrado <--")

            # Cadastro de [paciente]
            elif tipo == "paciente":

                # Identificador não pode ser vazio
                chave_primaria = validar_cpf()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Não foi informado um valor válido <--")
                    return "logado"
                
                else:
                    # Verifica se o paciente já está cadastrado
                    objeto = Paciente(identificador = chave_primaria)
                    verificacao_objeto = carregar(objeto, chave_primaria)

                    # Se não estiver, é feito o cadastro
                    if verificacao_objeto == None:

                        # Valor do nome informado não pode ser vazio
                        nome = input("Informe o nome do médico: ")
                        if nome == "":
                            os.system("cls")
                            print("--> Não foi informado um valor válido <--")
                            return "logado"
                        
                        # Cadastro do paciente
                        else:
                            dicionario_update = {"nome": nome}

                            # Valores do dicionario importados para o objeto
                            objeto.importar = dicionario_update

                            # Cadastro no banco de dados
                            cadastrar(objeto)
                            os.system("cls")
                            print("--> Paciente foi cadastrado <--")
                        
                    else:
                        os.system("cls")
                        print("--> Paciente já cadastrado <--")
            
            return "logado"
        
        # Opção de pesquisar e cada uma das opções
        elif "pesquisar_" in tipo_menu:
            _, tipo = tipo_menu.split("_")
            
            # Validacão de cada uma das chaves primárias
            # Objeto instanciado com as chaves primarias
            if tipo == "instituicao":
                chave_primaria = validar_cnpj()
                objeto = Instituicao(cnpj=chave_primaria)

            elif tipo == "consulta":
                chave_primaria = validar_numero()
                objeto = Consulta(numero=chave_primaria)

            elif tipo == "medico":
                chave_primaria = validar_crm()
                objeto = Medico(registro_profissional=chave_primaria)

            elif tipo == "paciente":
                chave_primaria = validar_cpf()
                objeto = Paciente(identificador = chave_primaria)
            
            # Se não for vazia realiza a pesquisa e imprime na tela o resultado
            if chave_primaria != "":
                objeto = carregar(objeto, chave_primaria)
            
                if objeto == None:
                    os.system("cls")
                    print("--> Não está cadastrado no banco de dados <--")
                else:
                    os.system("cls")
                    print(objeto)
            
            # Se a chave primária for vazia, retorna todos os itens cadastrados daquele objeto no banco de dados
            else:
                chaves = carregar_entradas(objeto)
                os.system("cls")
                
                for i in chaves:
                    objeto = carregar(objeto, i)
                    print(objeto)
            
            if self.login == True:
                return "logado"
            else:
                return "raiz"
        
        # Opção de editar e cada uma das ações
        elif "editar_" in tipo_menu:
            _, tipo = tipo_menu.split("_")
            
            # Editar instituicao
            if tipo == "instituicao":
                chave_primaria = validar_cnpj()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Não consta no banco de dados <--")
                    return "logado"
                
                else:
                    objeto = carregar(Instituicao(cnpj=chave_primaria), chave_primaria)
                    
                    # Verifica se está no banco de dados
                    if carregar(objeto, chave_primaria) == None:
                        os.system("cls")
                        print("--> Não consta no banco de dados <--")
                    
                    # Para cada valor, informar um novo valor ou deixar em branco para manter o mesmo
                    else:
                        os.system("cls")
                        print("--> Informe os novos valores ou deixe em branco para não alterar <--")

                        nova_chave = validar_cnpj()
                        novo_nome = input("Informe o nome da instituição: ")
                        
                        if nova_chave == "":
                            nova_chave = chave_primaria
                        
                        dicionario_editar = {nova_chave:{}}
                        
                        if novo_nome == "":
                            novo_nome = objeto.nome
                        
                        # Dicionário de atributos
                        dicionario_editar[nova_chave] = {"nome": novo_nome}

                        # Verificar se é necessário alterar o título                    
                        alt_titulo = objeto.nome == self.__nome

                        # Editar o Objeto
                        editar(objeto, dicionario_editar)
                        
                        if alt_titulo:
                            self.__nome = objeto.nome
                        
                        os.system("cls")
                        
                        print("--> Registro alterado <--")

            # Editar consulta
            elif tipo == "consulta":
                chave_primaria = validar_numero()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Não consta no banco de dados <--")
                    return "logado"
                
                else:
                    objeto = Consulta(numero=chave_primaria)
                    
                    # Verifica se está no banco de dados
                    if carregar(objeto, chave_primaria) == None:
                        print("--> Não consta no banco de dados <--")

                    # Para cada valor, informar um novo valor ou deixar em branco para manter o mesmo

                    # Nesse caso, Deve ser verificado se os valores de chave primária de outros objetos consta no banco de dados. Se não constar, cancela a operação
                    else:
                        os.system("cls")
                        print("--> Informe os novos valores ou deixe em branco para não alterar <--")

                        dicionario_editar = {chave_primaria:{}}

                        novo_medico = validar_crm()
                        if novo_medico == "":
                            novo_medico = objeto.medico
                        elif carregar(Medico(registro_profissional=novo_medico), novo_medico) == None:
                            os.system("cls")
                            print("--> Não consta no banco de dados <--")
                            return "logado"
                        
                        novo_paciente =  validar_cpf()
                        if novo_paciente == "":
                            novo_paciente = objeto.paciente
                        elif carregar(Paciente(identificador=novo_paciente), novo_paciente) == None:
                            os.system("cls")
                            print("--> Não consta no banco de dados <--")
                            return "logado"
                        
                        novos_sintomas = input("Descreva os sintomas de forma detalhada e atualizada")
                        if novos_sintomas == "":
                            novos_sintomas = objeto.sintomas

                        nova_descricao = input("Descreva o caso de forma detalhada e atualizada")
                        if nova_descricao == "":
                            nova_descricao = objeto.descricao

                        nova_enfermidade =  input("Descreva a enfermidade atualizada")
                        if nova_enfermidade == "":
                            nova_enfermidade = objeto.enfermidade

                        nova_prescricao =  input("Descreva a prescrição de forma detalhada e atualizada")
                        if nova_prescricao == "":
                            nova_prescricao = objeto.prescricao

                        # Dicionário de atributos
                        dicionario_editar[chave_primaria] = {"instituicao": self.__cnpj,
                                                            "medico": novo_medico,
                                                            "paciente": novo_paciente,
                                                            "sintomas": novos_sintomas,
                                                            "descricao": nova_descricao,
                                                            "enfermidade": nova_enfermidade,
                                                            "prescricao": nova_prescricao}

                        # Editar o Objeto
                        editar(objeto, dicionario_editar)
                        os.system("cls")
                        print("--> Registro alterado <--")

            # Editar Médico
            elif tipo == "medico":
                chave_primaria = validar_crm()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Não consta no banco de dados <--")
                    return "logado"
                
                else:
                    objeto = Medico(registro_profissional=chave_primaria)

                    # Verifica se está no banco de dados
                    if carregar(objeto, chave_primaria) == None:
                        print("Não consta no banco de dados.")

                    # Para cada valor, informar um novo valor ou deixar em branco para manter o mesmo
                    else:
                        os.system("cls")
                        print("-->Informe os novos valores ou deixe em branco para não alterar. <--")

                        nova_chave = validar_crm()
                        novo_nome = input("Informe o nome do médico: ")

                        if nova_chave == "":
                            nova_chave = chave_primaria
                        
                        dicionario_editar = {nova_chave:{}}
                        
                        if novo_nome == "":
                            novo_nome = objeto.nome
                        
                        # Dicionário de atributos
                        dicionario_editar[nova_chave] = {"nome": novo_nome}

                        # Editar o Objeto
                        editar(objeto, dicionario_editar)
                        os.system("cls")
                        print("--> Registro alterado <--")

            # Editar Paciente
            elif tipo == "paciente":
                chave_primaria = validar_cpf()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Não consta no banco de dados <--")
                    return "logado"
                
                else:
                    objeto = Paciente(identificador = chave_primaria)
                    
                    # Verifica se está no banco de dados
                    if carregar(objeto, chave_primaria) == None:
                        print("Não consta no banco de dados.")

                    # Para cada valor, informar um novo valor ou deixar em branco para manter o mesmo
                    else:
                        os.system("cls")
                        print("-->Informe os novos valores ou deixe em branco para não alterar. <--")

                        nova_chave = validar_crm()
                        novo_nome = input("Informe o nome do paciente: ")

                        if nova_chave == "":
                            nova_chave = chave_primaria
                        
                        dicionario_editar = {nova_chave:{}}
                        
                        if novo_nome == "":
                            novo_nome = objeto.nome

                        # Dicionário de atributos
                        dicionario_editar[nova_chave] = {"nome": novo_nome}

                        # Editar o Objeto
                        editar(objeto, dicionario_editar)
                        os.system("cls")
                        print("--> Registro alterado <--")
            
            return "logado"
        
        # Opção de deletar e cada uma das ações
        elif "deletar_" in tipo_menu:
            
            # Método para deletar o objeto baseado na chave primaria
            # Retorna se o objeto foi removido ou se não consta no banco de dados
            @staticmethod
            def deletar_objetos(objeto, chave_primaria):
                if carregar(objeto, chave_primaria) == None:
                    os.system("cls")
                    print("--> Não consta no banco de dados <--")
                        
                else:
                    os.system("cls")
                    deletar(objeto, chave_primaria)
                    print("--> Registro removido <--")
            
            _, tipo = tipo_menu.split("_")
            
            # Para cada objeto, verifica se a chave é vazia (cancela operação)
            # Se não for, deleta o objeto do banco de dados se constar
            if tipo == "instituicao":
                chave_primaria = validar_cnpj()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Operação Cancelada <--")
                    return "logado"
                
                else:
                    if chave_primaria == self.cnpj:
                        os.system("cls")
                        print("--> Operação Cancelada. <--")
                        print("--> Tentativa de deletar a própria instituição <--")
                        return "logado"

                    else:
                        objeto = Instituicao(cnpj=chave_primaria)
                        deletar_objetos(objeto, chave_primaria)

            elif tipo == "consulta":
                chave_primaria = validar_numero()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Operação Cancelada <--")
                    return "logado"
                
                else:
                    objeto = Consulta(numero=chave_primaria)
                    deletar_objetos(objeto, chave_primaria)

            elif tipo == "medico":
                chave_primaria = validar_crm()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Operação Cancelada <--")
                    return "logado"
                
                else:
                    objeto = Medico(registro_profissional=chave_primaria)
                    deletar_objetos(objeto, chave_primaria)

            elif tipo == "paciente":
                chave_primaria = validar_cpf()
                if chave_primaria == "":
                    os.system("cls")
                    print("--> Operação Cancelada <--")
                    return "logado"
                
                else:
                    objeto = Paciente(identificador = chave_primaria)
                    deletar_objetos(objeto, chave_primaria)
        
        return "logado"
    

    @property
    def status(self) -> bool:
        return self.__status
    
    @status.setter
    def status(self, condicao:bool) -> None:
        self.__status = condicao

    @property
    def login(self) -> str:
        return self.__login
    
    @login.setter
    def login(self, condicao:bool) -> None:
        self.__login = condicao
    
    @property
    def menu(self) -> str:
        return self.__menu
    
    @menu.setter
    def menu(self, tipo_menu) -> None:
        self.__menu = tipo_menu

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_titulo) -> None:
        self.__nome = novo_titulo

    @property
    def cnpj(self) -> str:
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, novo_cnpj) -> None:
        self.__cnpj = novo_cnpj