# Sistema de Recomendação de Cuidadores para Idosos

## Objetivo do Programa
O programa desenvolvido tem como objetivo recomendar cuidadores ideais para idosos com base em um conjunto de características e condições. Utilizando um algoritmo de aprendizado de máquina, o sistema analisa as necessidades e as condições dos idosos e escolhe o cuidador mais adequado, levando em consideração características como mobilidade, obesidade, deficiência, dificuldades visuais, auditivas e condições médicas.

O sistema também permite que o usuário escolha um idoso específico para o qual será feita a recomendação personalizada de um cuidador.

## Execução do Programa 

<b> 1. Clone o repositório do GitHub para o seu computador utilizando o comando:  
```bash
git clone https://github.com/2024-2-NADS4/Projeto4.git
```
</b>

<b> 2. Navegue até a pasta **`Projeto4/src/Entrega 1`** e abra-a no Visual Studio Code. </b>

<b> 3. Instale a versão mais recente do Python através do link **`https://www.python.org/downloads/`** e executando o arquivo baixado. </b>

<b> 4. Instale as bibliotecas necessárias, executando o seguinte comando no terminal:
```bash
pip install pandas scikit-learn faker
```
</b>

<b> 5. Execute o arquivo inserirDados.py para popular o banco de dados com 10 registros aleatórios de idosos e 10 de cuidadores:
```bash
python inserirDados.py
```
</b>

<b> 6. Para adicionar registros manualmente, execute o arquivo inputs.py:
```bash
python inputs.py
```
</b>

<b> 7. Para visualizar todos os dados armazenados no banco e gerar um relatório em formato Excel, execute o arquivo verificacaoDados.py:
```bash
python verificacaoDados.py
```
</b>

<b> 8. O arquivo Excel será criado na pasta **`Projeto4/src/Entrega 1`** com o nome **`dados_familycare`**. Abra-o para revisar os dados do banco de dados, se necessário. </b>

<b> 9. Para determinar o cuidador ideal para cada idoso registrado no banco de dados, execute o arquivo algoritmoMatching.py:
```bash
python algoritmoMatching.py
```
</b>

<b> 10. Para selecionar um idoso e identificar o cuidador ideal para ele, execute o arquivo encontrarCuidadorIdeal.py:
```bash
python encontrarCuidadorIdeal.py
```
</b>

### Criptografia
Foi implementada no projeto criptografia MD5 (Message-Digest Algorithm 5), um algoritmo de criptografia que transforma um arquivo em uma sequência única de caracteres. Foi implementada no arquivo **`inputs.py`**, com o objetivo de tornar mais seguro o cadastro de senha de cuidadores e idosos no banco de dados.

## Como o Algoritmo Funciona

### 1. Codificação dos Dados
Para garantir que os dados possam ser processados pelo modelo de aprendizado de máquina, as variáveis categóricas (como "Sim" ou "Não") são convertidas em variáveis numéricas. A codificação é feita utilizando o `pd.get_dummies()`, uma técnica comum para transformar variáveis categóricas em uma forma numérica, onde cada categoria é representada por uma coluna separada, com valores binários (0 ou 1).

**Exemplo**:
- Se um idoso possui a condição de mobilidade, a coluna "mobilidade" será codificada como 1, caso contrário, será 0.

### 2. Algoritmo k-Nearest Neighbors (kNN)
O algoritmo escolhido para a recomendação dos cuidadores foi o k-Nearest Neighbors. Esse algoritmo funciona encontrando os vizinhos mais próximos de um ponto de dados em um espaço vetorial. No contexto deste sistema:
- Cada cuidador e idoso são representados como pontos em um espaço multidimensional, onde cada dimensão corresponde a uma característica (como mobilidade, deficiência, etc.).
- O kNN compara as distâncias entre o ponto representando o idoso e todos os pontos dos cuidadores. O cuidador mais próximo (com a menor distância) é o recomendado.

## Busca pelo Cuidador Ideal
Quando um idoso é selecionado, o sistema realiza a codificação de suas características, alinha os dados entre o idoso e os cuidadores (para garantir que ambos tenham o mesmo formato de dados) e, em seguida, utiliza o kNN para calcular a "distância" entre o idoso e todos os cuidadores. O cuidador com a menor distância é selecionado como a recomendação.

## Escolha do Algoritmo
O k-Nearest Neighbors (kNN) foi escolhido por algumas razões principais:
- **Simplicidade e Eficiência**: O kNN é fácil de entender e implementar. Como o programa não precisa de um modelo complexo, a escolha por um algoritmo simples e direto faz mais sentido.
- **Recomendação baseada em características**: O kNN é adequado para problemas de recomendação em que as variáveis podem ser tratadas como um vetor de características (como no caso de idosos e cuidadores).
- **Sem necessidade de treinamento prévio**: O kNN não requer treinamento, o que significa que o sistema pode ser atualizado facilmente com novos dados, sem a necessidade de retreinar o modelo.

Apesar de ser simples, o kNN é poderoso para encontrar padrões em conjuntos de dados pequenos e médios, como o conjunto de dados de cuidadores e idosos usado aqui. Caso o banco de dados cresça muito no futuro, seria possível explorar algoritmos mais avançados, como redes neurais ou árvores de decisão, mas o kNN ainda seria uma escolha viável para o problema atual.

## Considerações Finais
Este sistema de recomendação foi projetado para fornecer uma solução prática e simples para conectar idosos a cuidadores adequados. A escolha do algoritmo kNN foi motivada pela simplicidade e eficácia para o problema específico, onde as relações entre as variáveis não precisam ser modeladas de forma muito complexa.

No futuro, o sistema pode ser expandido para incluir mais variáveis de entrada, realizar análises mais profundas dos dados, ou até mesmo utilizar algoritmos mais avançados conforme o número de dados aumenta.

Este programa, embora simples, pode oferecer uma base robusta para o desenvolvimento de um sistema de recomendação de cuidadores, ajudando a otimizar a assistência aos idosos com base nas suas necessidades específicas.
