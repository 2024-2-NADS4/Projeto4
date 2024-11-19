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

### Execução do Programa

### 1. Instalar as Bibliotecas Necessárias
```bash
pip install Flask joblib scikit-learn pandas
```

### 2. Rodar o Servidor Flask

Com as dependências instaladas e o banco de dados configurado, você pode rodar o servidor Flask utilizando o seguinte comando no terminal:

```bash
python api.py
```

O servidor ficará disponível no endereço http://127.0.0.1:5000/.

### 3. Enviar Avaliação via Postman

Com o servidor Flask em execução, você pode enviar uma requisição POST para a rota /avaliar_cuidador utilizando o Postman.

Configuração do Postman:

Método HTTP: POST

URL: http://127.0.0.1:5000/avaliar_cuidador

Cabeçalhos (Headers):

Content-Type: application/json

Body:
{
    "id_idoso": 1,
    "id_cuidador": 2,
    "email_idoso": "idoso@example.com",
    "email_cuidador": "cuidador@example.com",
    "feedback": "O cuidador foi muito atencioso e prestativo."
}

Após enviar a requisição, o feedback será classificado automaticamente pelo modelo, e a avaliação será registrada no banco de dados

### 4. Consultar Cuidadores
Você pode consultar a lista de cuidadores e suas médias de avaliação enviando uma requisição GET para a rota /cuidadores.

Configuração do Postman:

Método HTTP: GET

URL: http://127.0.0.1:5000/cuidadores

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
