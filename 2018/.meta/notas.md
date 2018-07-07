# Slides sobre o objetivo da apresentação
<!-- TODO: Slides sobre o objetivo da apresentação -->
...



# Slides sobre o projeto e sua motivação
<!-- TODO: Slides sobre o projeto e sua motivação -->
<!-- TODO: módulos importáveis: focar em usabilidade para quem for usar; fornecer documentação para quem quiser mais detalhes; prover mecanismos de testes para quem for contribuir em desenvolvimento -->
...



# Criação de diretório
<!-- TODO: Explicar cada parte -->
``` shell
$ mkdir PROJETO
$ cd PROJETO
$ touch .gitignore
$ echo '.venv'       >> .gitignore
$ echo '*.py[doc]'   >> .gitignore
$ echo '__pycache__' >> .gitignore
$ git init
$ python3 -m venv .venv        # https://docs.python.org/3/library/venv.html
$ source ./.venv/bin/activate  # https://docs.python.org/3/library/venv.html
```



# Slide sobre venv
<!-- TODO: Mostrar tabelinha de ativação -->
<!-- TODO: Comentar que ao usar 3.4+ vem instalado com pip e setuptools -->
https://docs.python.org/3/library/venv.html
...



# Slides sobre TDD
<!-- TODO: Slides sobre TDD -->
...



# Slides sobre unittest
<!-- TODO: Slides sobre unittest -->
...



# Slides sobre Exception
<!-- TODO: Slides sobre Exception -->
...



# Slides sobre documentação
<!-- TODO: Slides sobre documentação -->
<!-- TODO: incluir sobre estilo: pep8 e google python style guide -->
...



# Slides sobre doctest
<!-- TODO: Slides sobre doctest -->
<!-- TODO: Comentar sobre diferenças entre doctest e unittest - documetaçaão para usuário do módulo, teste para desenvolver o módulo -->
...



# Slides sobre logging
<!-- Slides sobre logging -->
...



# Slide sobre pacotes de distribuição
<!-- TODO: Comentar sobre estrutura e arquivos mínimos -->
- https://docs.python.org/3/tutorial/modules.html#packages
- https://packaging.python.org/tutorials/packaging-projects/
...



# Apêndice


## Módulos utilizados da biblioteca padrão do Python
- venv https://docs.python.org/3/library/venv.html


## Gerência de múltiplas versões de python
https://github.com/pyenv/pyenv


## Template de diretórios/arquivos, incluise para projetos Python
https://github.com/audreyr/cookiecutter


## Gerência de dependências, virtual env automático e uso de Pipfile
https://github.com/pypa/pipenv


## Gerência de dependência, empacotamento facilitado e uso de pyproject.toml
https://github.com/sdispater/poetry


<!-- TODO: incluir sobre cobertura: coverage -->
<!-- TODO: incluir sobre outros frameworks de testes: pytest -->
<!-- TODO: incluir sobre estilo: pep8 e google python style guide -->
<!-- TODO: incluir sobre linting: pylint e flake8 -->
<!-- TODO: incluir sobre formatação: black -->
