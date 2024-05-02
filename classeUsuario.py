'''
Desafio
Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

Entrada
Nome do usuário, número de telefone e plano.

Saída
Mensagem indicando que o usuário foi criado com sucesso.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Ana
(11) 91111-1111
Plano Essencial Fibra

Usuário Ana criado com sucesso.

Sofia
(22) 92222-2222
Plano Prata Fibra	Usuário Sofia criado com sucesso.
Pedro
(33) 93333-3333
Plano Premium Fibra

Usuário Pedro criado com sucesso.
'''

# Criação da classe 'UsuarioTelefone':

class UsuarioTelefone:
    
    # Método especial __init__ que inicializa os atributos da classe:
    def __init__(self, nome, telefone, plano):
        
        # Atributos da classe:
        self.__nome = nome
        self.__telefone = telefone
        self.__plano = plano
        
    # Método que retorna uma mensagem indicando que o usuário foi criado com sucesso:
    def criar_usuario(self):
        return f"Usuário {self.__nome} criado com sucesso."
    
# Solicita ao usuário que insira o nome, número de telefone e plano do usuário e armazena os valores fornecidos nas variáveis 'nome', 'telefone' e 'plano':

nome = input()

telefone = input()

plano = input()

# Cria um objeto 'usuario' da classe 'UsuarioTelefone' com os valores fornecidos e armazena na variável 'usuario':

usuario = UsuarioTelefone(nome, telefone, plano)

# Chama o método 'criar_usuario()' do objeto 'usuario' e armazena a mensagem retornada na variável 'mensagem':

mensagem = usuario.criar_usuario()

# Imprime a mensagem:

print(mensagem)

