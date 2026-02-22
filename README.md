# ProjetoGrupo5

# Guia de Execução do Projeto

## 1. Pré-requisitos

* Python 3.10 ou superior
* pip

---

## 2. Estrutura esperada do projeto

A pasta raiz deve possuir a seguinte organização:

```
ProjetoGrupo5/
│
├── main.py
├── aima/
├── agents/
│   ├── __init__.py
│   └── Program0.py
├── env/
│   ├── __init__.py
│   └── Environment0.py
├── problems/
│   ├── __init__.py
│   └── Problem0.py
```

Observação:
As pastas `agents`, `env` e `problems` precisam obrigatoriamente conter um arquivo vazio chamado `__init__.py`.
Sem isso, o Python não reconhece as pastas como pacotes e ocorrerá o erro:

```
ModuleNotFoundError: 'agents' is not a package
```

---

## 3. Criar ambiente virtual (recomendado)

Na raiz do projeto:

Linux/macOS:

```
python3 -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

---

## 4. Instalar dependências necessárias

O projeto depende de bibliotecas externas utilizadas pelo AIMA:

```
pip install numpy
pip install ipythonblocks
```

---

## 5. Configurar PYTHONPATH

Como o diretório `aima` está incluído localmente (não instalado via pip), é necessário informar ao Python onde encontrá-lo.

Linux/macOS:

```
export PYTHONPATH=$PYTHONPATH:$(pwd)/aima
```

Windows:

```
set PYTHONPATH=%PYTHONPATH%;%cd%\aima
```

Esse passo é obrigatório para evitar erros como:

```
ModuleNotFoundError: No module named 'utils'
```

---

## 6. Executar o projeto

Ainda na raiz do projeto:

```
python3 main.py
```


