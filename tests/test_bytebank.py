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
