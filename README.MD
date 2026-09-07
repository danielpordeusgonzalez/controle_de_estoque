# Sistema de Controle de Estoque

Projeto simples desenvolvido em Python utilizando conceitos de **Programação Procedural** e organização inspirada no padrão **MVT (Model, Viewer e Template)**.

O sistema permite cadastrar produtos, consultar o estoque, realizar entradas e saídas e calcular o valor total dos produtos armazenados.

## Estrutura do projeto

```text
projeto_estoque/
│
├── main.py
├── model.py
├── viewer.py
├── template.py
└── README.md
```

### `model.py`

Representa o **Model** do projeto.

É responsável pelo armazenamento dos produtos em uma lista durante a execução do programa.

Cada produto possui:

* nome;
* preço;
* quantidade.

Os dados ficam armazenados apenas enquanto o programa estiver aberto, pois o projeto não utiliza banco de dados ou arquivos externos.

### `viewer.py`

Representa a parte responsável pelas **regras de negócio** do sistema.

Contém as principais funções:

* `cadastrar_produto()` — cadastra um novo produto com nome, preço e quantidade.
* `listar_produtos()` — apresenta todos os produtos cadastrados.
* `buscar_produto()` — procura um produto pelo nome.
* `entrada_estoque()` — adiciona determinada quantidade ao estoque de um produto.
* `saida_estoque()` — remove uma quantidade do estoque, desde que exista quantidade suficiente.
* `calcular_valor_estoque()` — calcula o valor de cada produto utilizando `preço × quantidade` e também o valor total do estoque.

O sistema também possui as funcionalidades adicionais de identificar:

* produto com maior quantidade;
* produto com menor quantidade;
* produto mais caro;
* produtos com estoque baixo, considerando menos de 5 unidades.

### `template.py`

Representa o **Template**.

É responsável pela parte visual exibida no terminal, como:

* menu principal;
* títulos;
* mensagens;
* formatação das informações dos produtos;
* apresentação dos resultados.

### `main.py`

É o arquivo principal do programa.

Ele inicia o sistema, apresenta o menu, recebe a opção escolhida pelo usuário e chama as funções correspondentes.

O menu continua sendo exibido até que seja escolhida a opção `0 - Sair`.

---

# Como executar o programa

Para iniciar o sistema, execute o arquivo:

```bash
python main.py
```

Também pode ser utilizado:

```bash
python3 main.py
```

dependendo da instalação do Python.

O arquivo que deve ser executado para testar o projeto é sempre o:

```text
main.py
```

---

# Fluxo básico de teste

Após executar `main.py`, o menu será apresentado:

```text
===== SISTEMA DE ESTOQUE =====

1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Entrada de estoque
5 - Saída de estoque
6 - Mostrar valor total do estoque
0 - Sair
```

Um fluxo simples para testar o sistema é:

### 1. Cadastrar um produto

Escolha:

```text
1
```

Exemplo:

```text
Nome: Teclado
Preço: 120
Quantidade: 10
```

### 2. Listar produtos

Escolha:

```text
2
```

Deve aparecer o produto cadastrado com preço e quantidade.

### 3. Buscar produto

Escolha:

```text
3
```

Digite:

```text
Teclado
```

O sistema deverá encontrar e apresentar os dados do produto.

### 4. Testar entrada de estoque

Escolha:

```text
4
```

Informe:

```text
Produto: Teclado
Quantidade de entrada: 10
```

Como existiam 10 unidades, o estoque deverá passar para:

```text
20 unidades
```

### 5. Testar saída de estoque

Escolha:

```text
5
```

Informe uma retirada de:

```text
5
```

O estoque deverá passar de 20 para:

```text
15 unidades
```

Também é importante tentar retirar uma quantidade maior do que a disponível.

Nesse caso o sistema deverá mostrar:

```text
Estoque insuficiente.
```

e não alterar a quantidade existente.

### 6. Calcular o valor do estoque

Escolha:

```text
6
```

O sistema deverá calcular:

```text
preço × quantidade
```

e apresentar o valor de cada produto e o valor total do estoque.

### 7. Encerrar

Escolha:

```text
0
```

O programa será finalizado.

---

## Conceitos utilizados

O projeto utiliza:

* funções;
* parâmetros;
* `return`;
* listas;
* estruturas condicionais;
* estruturas de repetição;
* menu interativo;
* Programação Procedural;
* separação de responsabilidades utilizando Model, Viewer e Template.

O projeto não utiliza banco de dados, orientação a objetos ou bibliotecas externas.
