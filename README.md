# python-tdd
Aplicando TDD


## criar ambiente virtual desenvolvendo em python
python -m venv venv

# ativar ambiente virtual
source venv/bin/activate

# executar todos os testes com detalhes
pytest -v

# executar testes filtrando por palavra no nome do test
pytest -k PALAVRA

# executar testes com tag associada com @mark
pytest -v -m tag_associada

# verificar quais marks já existem
pytest --markers

# Atualizar requirements
 pip freeze > requirements.txt

# Analisar cobertura de testes
pytest --cov=PASTADOCODIGO PASTADETESTE/

# Identificar linha sem cobertura de testes
pytest --cov=PASTADOCODIGO PASTADETESTE/ --cov-report term-missing

# Relatório de cobertura de testes
pytest --cov=PASTADOCODIGO PASTADETESTE/ --cov-report html

# Relatorio de testes em xml
pytest --junitxml NOMEARQUIVO.xml

# Relatório de cobertura de testes em xml
pytest --cov-report xml