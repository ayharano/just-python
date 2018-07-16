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
<!-- TODO:

    Currently, there are two common tools for creating Python virtual environments:
    venv is available by default in Python 3.3 and later, and installs pip and setuptools into created virtual environments in Python 3.4 and later.

    https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments

 -->
<!-- TODO: Comentar que ao usar 3.4+ vem instalado com pip e setuptools -->
https://docs.python.org/3/library/venv.html
...



# Slides sobre TDD
<!-- TODO: Slides sobre TDD -->
<!-- TODO: falar sobre ler bem os erros -->
<!-- TODO: falar sobre abordagem bottom-up e top-down -->
<!-- TODO: baby steps para construir base -->
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
- https://packaging.python.org/guides/distributing-packages-using-setuptools/
- PyPA sample project: https://github.com/pypa/sampleproject
<!--
Note

Projects using setuptools 0.6.27+ have standard readme files (README.rst, README.txt, or README) included in source distributions by default. The built-in distutils library adopts this behavior beginning in Python 3.7. Additionally, setuptools 36.4.0+ will include a README.md if found. If you are using setuptools, you don’t need to list your readme file in MANIFEST.in. Otherwise, include it to be explicit.
-->



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
