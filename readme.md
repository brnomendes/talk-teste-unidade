
# Lightning Talk - Teste de Unidade em Python

### Ferramentas para Teste de Unidade em Python
- Ferramentas na biblioteca padrão:
  - [Doctest](https://docs.python.org/3/library/doctest.html)
  - [Unittest](https://docs.python.org/3/library/unittest.html)
- Ferramentas externas:
  - [Pytest](https://docs.pytest.org/en/latest/)
  - [Nose](http://nose.readthedocs.io/en/latest/)


### Como executar
```bash
$ git clone https://github.com/brnomendes/talk-teste-unidade.git
$ cd talk-teste-unidade

$ sudo pip install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate

$ pip install pytest

$ python unitDoctest.py
$ python unitUnittest.py
$ pytest unitPytest.py
```

Mais dicas sobre por que testar em [Testing Your Code - Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/tests/)
