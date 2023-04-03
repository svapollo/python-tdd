from scripts.bytebank import Funcionario


class TestClass:
    def test_quando_idade_receve_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Apollo_Sobrenome_deve_retornar_Sobrenome(self):
        entrada = ' Apollo Sobrenome '  # Given
        esperado = 'Sobrenome'

        sobrenome_teste = Funcionario(entrada, '02/02/1900', 11000)
        resultado = sobrenome_teste.sobrenome()  # When

        assert resultado == esperado  # Then

    def test_quando_reduzir_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '01/01/2000',
                                        entrada_salario)
        funcionario_teste.reduzir_salario()  # When
        resultado = funcionario_teste.salario

        assert resultado == esperado  # Then

    def test_quando_calcular_bonus_recebe_2000_deve_retornar_200(self):
        entrada_salario = 2000  # Given
        esperado = 200

        funcionario_teste = Funcionario('Tiago', '03/04/2003', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado  # Then
