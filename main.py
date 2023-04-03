from scripts.bytebank import Funcionario

# apollo = Funcionario('Apollo', '04/04/1200', 90000)

# print(apollo.idade())


def teste_idade():
    funcionario_teste = Funcionario('Teste', '10/02/2000', 4567)
    print(f'Teste = {funcionario_teste.idade()}')


teste_idade()
