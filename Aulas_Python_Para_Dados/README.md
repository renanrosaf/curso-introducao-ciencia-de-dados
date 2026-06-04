# 💻 Códigos das Aulas

**Introdução e Python para Dados:** Repositório destinado ao armazenamento dos códigos, anotações e exemplos práticos desenvolvidos durante as aulas.

---

## 📝 Aulas 1 e 2: Primeiros Passos com Python

Nestas aulas introdutórias, focou-se na preparação do ambiente de desenvolvimento e nos comandos fundamentais da linguagem Python. Os tópicos abordados nos códigos destas aulas incluem:

* **Configuração do Ambiente:**
    * Instalação do Python.
    * Instalação e configuração do editor VS Code (Visual Studio Code).
* **Sintaxe e Estrutura Básica:**
    * Como realizar e utilizar comentários no código para documentação.
* **Entrada e Saída de Dados:**
    * `print()`: Comando inicial para exibição de mensagens no console (saída de dados).
    * `input()`: Comando para receber informações digitadas pelo usuário (entrada de dados).
* **Variáveis:**
    * Atribuição de valores.
    * Regras e boas práticas de como nomear variáveis corretamente.
* **Manipulação Inicial de Strings (Textos):**
    * Operações básicas com strings.
    * Concatenação (união de duas ou mais strings).
    * Como verificar o tamanho de uma string (quantidade de caracteres, via comando len()).

---

## 📝 Aula 3: Ambiente Virtual (VirtualENV) e Ecossistema Python

Nesta aula, exploramosexploru-se  o conceito de ambientes virtuais e as principais ferramentas que compõem o ecossistema de dados em Python.

### 📦 O que é um Ambiente Virtual?
Um ambiente virtual (VirtualENV) é um diretório isolado que contém uma instalação autônoma do Python, além de pacotes e bibliotecas específicas para um projeto. 
* **Por que usar?** Ele permite o uso de diferentes versões de bibliotecas em projetos distintos na mesma máquina, evitando conflitos de dependências. Facilita o gerenciamento do projeto e mantém a instalação global do Python limpa.
* **Nota:** Você pode criar quantos ambientes virtuais forem necessários (geralmente, cria-se um para cada novo projeto).

### ⚙️ Roteiro: Criação de um Ambiente Virtual
Abaixo está o passo a passo dos comandos utilizados no terminal (Bash/CMD) para criar e gerenciar seu ambiente:

```bash
# 1. Instalar a ferramenta virtualenv (caso ainda não tenha instalado)
pip install virtualenv

# 2. Criar o diretório para o seu novo projeto
mkdir primeiro_projeto_python

# 3. Navegar para dentro do diretório criado
cd primeiro_projeto_python

# 4. Criar o ambiente virtual (daremos o nome de 'venv')
virtualenv venv

# 5. Ativar o ambiente virtual (Comando para Windows)
venv\Scripts\activate 

# 6. Desativar o ambiente virtual (quando terminar de trabalhar no projeto)
deactivate
```


### 📚 Principais Bibliotecas e Ferramentas (Ecossistema de Dados)
Uma visão geral das bibliotecas e tecnologias essenciais apresentadas para a área de dados e desenvolvimento:

**Análise e Visualização de Dados**
* **NumPy:** Focada em computação numérica e manipulação eficiente de arrays/matrizes multidimensionais.
* **Pandas:** Essencial para a manipulação e análise de dados tabulares (utilizando a estrutura de DataFrames).
* **Matplotlib:** Biblioteca fundamental para a criação de gráficos e plotagens 2D.
* **Seaborn:** Interface de alto nível baseada no Matplotlib, focada na criação de gráficos estatísticos atraentes e informativos.

**Inteligência Artificial e Machine Learning**
* **Scikit-Learn:** Biblioteca principal para algoritmos clássicos de Machine Learning (como classificação, regressão e clusterização).
* **PyTorch e TensorFlow:** Frameworks avançados focados em Deep Learning e construção de redes neurais complexas.

**Extração, Interação e Banco de Dados**
* **Jupyter Notebook:** Aplicação web interativa que permite mesclar código Python em execução, textos formatados, equações e visualizações em um único documento.
* **Scrapy e BeautifulSoup:** Ferramentas poderosas para extração e raspagem de dados de páginas da web (Web Scraping).
* **SQLAlchemy:** Uma API/ORM (Object-Relational Mapping) em Python que facilita a integração e manipulação de bancos de dados SQL utilizando código Python.

**Versionamento de Código**
* **Git:** Sistema de controle de versão que registra o histórico de alterações do código e permite a ramificação (branches) do projeto.
* **GitHub:** Plataforma em nuvem baseada no Git para hospedagem de código, facilitando o portfólio e a colaboração em equipe.


## 📝 Aula 4: Estruturas de Dados, Módulos e Pacotes

Nesta aula, abordamos as principais estruturas de dados nativas do Python e como estruturar e organizar projetos utilizando módulos e pacotes.

### 🧱 Estruturas de Dados

* **Listas:** Coleções de itens utilizadas para armazenar múltiplos valores em uma única variável.
    * **Características:** São estruturas **mutáveis** (podem ser alteradas após a criação) e **ordenadas**, definidas utilizando colchetes `[]`.
    * **Conceitos:** Definição, criação e acesso de elementos via índice.
    * **Inserção:** Adição de elementos em posições específicas (`insert()`) ou ao final da lista (`append()`).
    * **Remoção:** Exclusão de elementos pelo valor (`remove()`) ou pelo índice/último elemento (`pop()`).

* **Tuplas:** Coleções de itens utilizadas para armazenar múltiplos valores, com funcionamento semelhante ao das listas.
    * **Características:** São estruturas **ordenadas**, porém **imutáveis** (seus elementos não podem ser alterados após a criação), definidas utilizando parênteses `()`.
    * **Conceitos:** Definição, criação, acesso de elementos via índice e criação de listas contendo tuplas.

* **Dicionários:** Estruturas que mapeiam pares de **Chave-Valor**, definidas utilizando chaves `{}`.
    * **Características:** Semelhantes a listas, mas os elementos não são acessados por índices numéricos, e sim por chaves únicas (que devem ser de um tipo imutável). Eles facilitam a busca, adição e remoção de itens de forma muito eficiente.
    * **Conceitos:** Definição de chave/valor, conversão de lista de tuplas para dicionário (usando a função `dict()`), acesso aos valores, além da adição e remoção referenciando a chave.

---

### 📦 Organização e Reutilização de Código

Mecanismos que permitem estruturar e reaproveitar o código de maneira eficiente:

* **Módulo:** Um arquivo Python (extensão `.py`) que contém definições de funções, classes e variáveis que possuem relação entre si.
* **Pacote:** Uma coleção de módulos organizados dentro de um diretório. Para que o Python reconheça esse diretório como um pacote, ele deve conter um arquivo chamado `__init__.py`.

**Sintaxe Básica de Importação (`import`):**

```python
# Importando um módulo inteiro
import meu_modulo

# Importando um módulo e atribuindo um "apelido" (alias)
import pandas as pd

# Importando apenas uma função específica de dentro de um módulo
from meu_modulo import minha_funcao

# Importando apenas um módulo específico de dentro de um pacote
import meu_pacote.meu_modulo

# Importando uma função específica de um módulo que está dentro de um pacote
from meu_pacote.meu_modulo import minha_funcao
```
