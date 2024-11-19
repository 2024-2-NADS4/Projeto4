# Sistema de Recomendação de Cuidadores para Idosos

## Objetivo do Programa
O programa desenvolvido tem como objetivo recomendar cuidadores ideais para idosos com base em um conjunto de características e condições. Utilizando um algoritmo de aprendizado de máquina, o sistema analisa as necessidades e as condições dos idosos e escolhe o cuidador mais adequado, levando em consideração características como mobilidade, obesidade, deficiência, dificuldades visuais, auditivas e condições médicas.

O sistema também permite que o usuário escolha um idoso específico para o qual será feita a recomendação personalizada de um cuidador.

## Estrutura e Fluxo do Programa

### 1. Carregamento de Dados
O sistema começa carregando dados do banco de dados SQLite (`familycare.db`), onde estão armazenadas informações sobre os idosos e cuidadores. Essas informações incluem características relevantes, como:

- **Idosos**: Nome, mobilidade, obesidade, deficiência, dificuldades visuais, auditivas e condições médicas.
- **Cuidadores**: Nome, habilidades e características de cuidados em relação às mesmas condições dos idosos.

**Função**: `carregar_dados()`
- Carrega os dados das tabelas `Idosos` e `Cuidadores` do banco de dados e os converte em DataFrames do Pandas para processamento posterior.

### 2. Recomendação de Cuidador
Quando um idoso é selecionado, o programa utiliza um algoritmo de k-Nearest Neighbors (kNN) para encontrar o cuidador mais adequado, comparando as características do idoso com aquelas dos cuidadores.

**Função**: `recomendar_cuidador(idoso_dados, cuidadores_df)`
- Codifica as características dos cuidadores e do idoso selecionado em variáveis numéricas, usando a técnica de *one-hot encoding* (ou codificação binária).
- Aplica o algoritmo de kNN para encontrar o cuidador que mais se assemelha ao idoso, ou seja, o cuidador cujas características são mais próximas (no espaço vetorial) das do idoso.
- O kNN retorna o cuidador mais próximo baseado nas características codificadas.

### 3. Interface com o Usuário
Através de um menu interativo, o programa solicita que o usuário escolha um idoso do banco de dados. Após a escolha, o sistema recomenda o cuidador mais adequado, exibindo o nome do cuidador ideal para aquele idoso.

**Função**: `exibir_menu_de_idosos()`
- Exibe uma lista numerada de idosos cadastrados e pede ao usuário para selecionar um deles.
- Após a escolha, a recomendação do cuidador é feita com base nas características do idoso selecionado.

### 4. Execução do Programa
O programa principal é a função `realizar_matching()`, que orquestra o fluxo de carregamento dos dados, seleção do idoso e recomendação do cuidador.

## Como o Algoritmo Funciona

### 1. Codificação dos Dados
Para garantir que os dados possam ser processados pelo modelo de aprendizado de máquina, as variáveis categóricas (como "Sim" ou "Não") são convertidas em variáveis numéricas. A codificação é feita utilizando o `pd.get_dummies()`, uma técnica comum para transformar variáveis categóricas em uma forma numérica, onde cada categoria é representada por uma coluna separada, com valores binários (0 ou 1).

**Exemplo**:
- Se um idoso possui a condição de mobilidade, a coluna "mobilidade" será codificada como 1, caso contrário, será 0.

### 2. Algoritmo k-Nearest Neighbors (kNN)
O algoritmo escolhido para a recomendação dos cuidadores foi o k-Nearest Neighbors. Esse algoritmo funciona encontrando os vizinhos mais próximos de um ponto de dados em um espaço vetorial. No contexto deste sistema:
- Cada cuidador e idoso são representados como pontos em um espaço multidimensional, onde cada dimensão corresponde a uma característica (como mobilidade, deficiência, etc.).
- O kNN compara as distâncias entre o ponto representando o idoso e todos os pontos dos cuidadores. O cuidador mais próximo (com a menor distância) é o recomendado.

### Por que kNN foi escolhido?
O kNN é um algoritmo simples, eficaz e amplamente utilizado para problemas de recomendação e classificação. Ele é intuitivo e fácil de implementar, além de não exigir um treinamento complexo. Para o caso específico de recomendação de cuidadores para idosos, o kNN é uma escolha apropriada, pois os dados são relativamente pequenos e não exigem técnicas mais complexas, como redes neurais. Além disso, a ideia de encontrar o "vizinho mais próximo" (o cuidador mais adequado) faz sentido dentro do contexto de características semelhantes.

O kNN é especialmente útil quando não há uma relação linear clara entre as variáveis de entrada, como no caso de características como "mobilidade", "deficiência", "obesidade", etc. O algoritmo pode capturar essas complexidades de maneira eficaz.

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

# Sistema de Avaliação de Cuidadores

## Objetivo do Programa
O programa desenvolvido tem como objetivo construir um feedback textual do Idoso ao Cuidador, por meio de uma API dedicada, o sistema recebe as avaliações enviadas pelos familiares após o atendimento e a partir da IA classifica o feedback em categorias como Excelente, Bom, Mediano e Ruim. Esse sistema de classificação é sustentado por um modelo de aprendizado de máquina, treinado em uma base de dados com mais de 5.000 feedbacks variados. O modelo, ao identificar padrões nas palavras e expressões, aprimora continuamente sua capacidade de avaliar com precisão o tipo de experiência relatada. O sistema também permite que o usuário escolha um idoso específico para o qual será feita a recomendação personalizada de um cuidador.

## Estrutura e Fluxo do Programa

### 1. Carregamento de Dados
O sistema começa carregando dados do banco de dados SQLite (`familycare.db`), onde estão armazenadas informações sobre as avaliações. Essas informações incluem características relevantes, como:

- **Avaliações**: id idoso, id cuidador, email idoso, email cuidador, classificacao, feedback

**Função**: `train_model()`
- É responsavel pela leitura do csv `feedbacks.csv` aonde treina ainda mais o modelo de Machine Learning utilizado na aplicação, neste formato entregue o modelo já esta treinado.

### 2. Análise de Feedback
Para lidar com o feedback textual e extrair informações de forma eficiente, aplicamos NLP ao sistema. A partir de um endpoint desenvolvido em Flask, a aplicação recebe os feedbacks e, através do modelo SVM, classifica automaticamente a qualidade do atendimento. O sistema considera cada feedback textual como uma entrada, transformando-o em uma classificação que varia de Excelente a Ruim, com base nas expressões e palavras usadas pelo familiar ao relatar sua experiência.

**Função**: `avaliar_cuidador()`
- Recebe dados do idoso e do cuidador, incluindo identificadores (id_idoso, id_cuidador), emails e um feedback textual, através de uma requisição POST no formato JSON.
- Valida se todos os dados obrigatórios estão presentes na requisição.
- Transforma o texto do feedback em uma representação numérica utilizando um vectorizer (ex.: TF-IDF).
- Aplica um modelo de aprendizado de máquina para classificar o feedback em categorias como Excelente, Bom, Médio, Ruim ou Péssimo.
- Converte a classificação textual para uma escala numérica de 1 a 5, onde 5 representa "Excelente" e 1 representa "Péssimo".
- Armazena a avaliação, incluindo IDs, emails, classificação e o texto do feedback, na tabela Avaliacoes do banco de dados.
- Retorna uma resposta com status 200 indicando sucesso ou um erro específico em caso de falha (ex.: status 400 ou 500).

**Função**: `listar_cuidadores()`
- Realiza uma consulta no banco de dados para listar todos os cuidadores registrados, juntamente com suas avaliações médias.
- Utiliza a tabela Cuidadores e realiza um LEFT JOIN com a tabela Avaliacoes para calcular a média das classificações dos feedbacks associados a cada cuidador.
- Organiza os dados retornados em uma lista de dicionários com os campos:
- id: Identificador do cuidador.
- nome: Nome do cuidador.
- media_classificacao: Média das classificações (ou 0 caso o cuidador ainda não tenha avaliações).
- Retorna os dados no formato JSON, ordenados pela média de classificação em ordem decrescente.
- Em caso de erro durante a consulta ou processamento, retorna um erro com status 500 e a descrição da exceção.- Valida se todos os dados obrigatórios estão presentes na requisição.

### 4. Execução do Programa
O programa principal para a execução do sistemaa de avaliação é o arquivo `api.py`, que orquestra o fluxo de carregamento dos dados, criando uma API via flask, onde serão imbutidos os dados.

## Como o Algoritmo Funciona

### 1. Codificação dos Feedbacks
O sistema utiliza TF-IDF (Term Frequency-Inverse Document Frequency) para transformar os feedbacks dos usuários em representações numéricas. O TF-IDF é uma técnica amplamente usada em NLP (Natural Language Processing) para converter texto em uma matriz numérica, destacando as palavras mais importantes para cada feedback com base na frequência relativa das palavras.

**Como funciona o TF-IDF:**:
- Term Frequency (TF): Mede a frequência de uma palavra em um feedback específico.
- Inverse Document Frequency (IDF): Reduz a importância de palavras comuns em todos os feedbacks, como "o", "de", "e", que não ajudam na distinção.
- O produto TF-IDF dá maior peso às palavras que são importantes em um feedback específico, mas raras no conjunto total.

### 2. Modelo de Classificação
O modelo de aprendizado de máquina (por exemplo, Logistic Regression ou Random Forest) é treinado para identificar o sentimento por trás de um feedback, classificando-o em uma das seguintes categorias:
- Excelente
- Bom
- Mediano
- Ruim
- Péssimo

O treinamento do modelo é realizado utilizando feedbacks previamente rotulados, criando uma associação entre padrões de palavras e a classificação correspondente.

### 3. Fluxo do Sistema
Recebendo o Feedback:

O usuário (familiar) fornece um feedback textual sobre o cuidador no endpoint /avaliar_cuidador
O feedback é enviado para a API no formato JSON, junto com os identificadores do cuidador e do avaliador.
Pré-processamento do Feedback:

O texto é convertido em um vetor TF-IDF.
Essa representação numérica é usada para alimentar o modelo de aprendizado de máquina.

**Classificação:**
O modelo classifica o feedback em uma das categorias mencionadas acima.
A classificação é então mapeada para um valor numérico:
- Excelente: 5
- Bom: 4
- Mediano: 3
- Ruim: 2
- Péssimo: 1

**Armazenamento no Banco de Dados:**

O feedback e sua classificação numérica são salvos na tabela Avaliacoes, junto com os IDs do cuidador e do avaliador.
Consulta de Avaliações:

**Consulta de Avaliações:**

Os cuidadores podem ser consultados pelo endpoint /cuidadores, que retorna a média das classificações de cada cuidador, ordenados do melhor para o pior.


### Por que NLP foi escolhido?
A análise de linguagem natural (NLP - Natural Language Processing) foi escolhida como abordagem principal para este projeto devido à natureza dos dados envolvidos: feedbacks textuais escritos por familiares de idosos. O NLP permite extrair padrões e sentimentos contidos nos textos, transformando palavras em informações úteis para classificação e análise.

Ao invés de algoritmos baseados em distâncias como o kNN, o NLP utiliza modelos treinados para identificar automaticamente a classificação de um texto (como Excelente, Bom, Mediano, Ruim ou Péssimo). Isso torna o NLP mais adequado para problemas em que os dados de entrada são predominantemente textuais, como avaliações qualitativas.

## Por que o NLP é adequado?
O NLP é especialmente eficaz para análise de sentimentos e classificação de textos, sendo uma escolha ideal para este projeto.

## Escolha do Algoritmo
A Análise de Linguagem Natural (NLP) foi escolhida por algumas razões principais:
- **Adequação para textos não estruturados:**: O NLP é ideal para processar textos livres, como feedbacks de cuidadores, capturando o sentimento e classificando em categorias como Excelente, Bom, Mediano e Ruim.
- **Escalabilidade**: Com técnicas como TF-IDF e aprendizado de máquina, o modelo pode facilmente ser atualizado e adaptado conforme novos dados são adicionados.
- **Automatização e precisão**: O uso de NLP permite um processo eficiente e padronizado, eliminando subjetividades na análise manual.

## Considerações Finais
O sistema de análise de feedbacks com NLP foi projetado para oferecer uma solução prática e eficiente na classificação de opiniões de familiares sobre cuidadores. A escolha do uso de técnicas de NLP, aliada a um modelo de classificação como Logistic Regression, foi motivada pela simplicidade e eficácia para o problema atual, onde textos não estruturados precisam ser analisados de forma padronizada e precisa.

No futuro, o sistema pode ser aprimorado com a inclusão de mais dados, expansão do vocabulário analisado e adoção de técnicas mais avançadas, como redes neurais, para atender a volumes maiores de informações.

Apesar de sua simplicidade, este programa oferece uma base sólida para a automação e padronização da análise de sentimentos, otimizando a gestão da qualidade dos cuidadores com base nos feedbacks recebidos.
