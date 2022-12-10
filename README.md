# python-requests-pytest
Conhecimentos de testes unitários de Requests do Python com cobertura de testes utilizando Pytest. 
Estes códigos têm por objetivo reforçar o aprendizado de testes unitários com Pytest aplicados ao conhecimento de Requests em um pequeno projeto de uma API de usuários fake. 

## Como executar o projeto

* Ter o Python Requests instalado
* Ter o Pytest instalado
* Ter um token válido na API de usuários [https://gorest.co.in/]
* Importante ter o Python 3 instalado (versão 3.11.0 ou superior)

### Instalar o Python Requests
'
 pip install requests
'

### Instalar o Python Requests
'
 pip install pytest
'

### Instalar o Pytest Coverage - para cobertura dos testes
'
pip install pytest-cov
'

### Executar todos os testes
'
python -m pytest
'

### Executar tag específica
'
python -m pytest -v -m nome_do_metodo_de_teste
'
