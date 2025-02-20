---
date: 01-09-2024
tags:
  - masters
  - learning analytics
  - educational data mining
  - ENEM
---

# Utilização dos Dados do ENEM em Learning Analytics

## Introdução

Learning analytics e educational data mining são campos emergentes que utilizam dados educacionais para melhorar
processos de ensino e aprendizagem. No Brasil, o ENEM (Exame Nacional do Ensino Médio) oferece um rico conjunto de dados
que pode ser explorado para diversos fins analíticos, contribuindo significativamente para a compreensão e aprimoramento
do sistema educacional brasileiro.

## Categorias de Estudo

### 1. Análise de Desempenho

Estudos nessa categoria focam na avaliação do desempenho dos estudantes em diferentes contextos, explorando variáveis
como localização geográfica, condições socioeconômicas e perfil demográfico.

**Exemplo de Artigo:**

- **Título:** [A Data Mining Approach Applied to the High School National Examination: Analysis of Aspects of Candidates
  to Brazilian Universities]

- **Descrição:**

O artigo analisa microdados do ENEM, com um banco de dados contendo 8.627.367 registros e 166 atributos, utilizando a
arquitetura Spark para processar grandes volumes de dados. O objetivo é aplicar algoritmos de data mining para prever o
perfil dos inscritos no ENEM e identificar padrões que influenciam o desempenho dos candidatos.

**Hipóteses Avaliadas**:

- A relação entre a renda familiar, o acesso à informação, a profissão e o histórico acadêmico dos pais com o desempenho
  dos candidatos no ENEM.
- Identificação de padrões específicos em diferentes regiões do Brasil que podem influenciar a aprovação ou reprovação
  dos candidatos.

**Métodos Utilizados**:

- **Algoritmos de Classificação**: Para analisar como os fatores socioeconômicos e acadêmicos dos pais impactam o
  desempenho dos candidatos.
- **Indução de Regras**: Para identificar padrões regionais, destacando características comuns entre candidatos
  aprovados ou reprovados e fatores essenciais, como disciplinas e características regionais.

O estudo demonstra como o uso de algoritmos de data mining pode revelar insights valiosos sobre os fatores que
influenciam o sucesso dos candidatos, permitindo a análise de grandes volumes de dados de forma eficiente.

### 2. Predição de Desempenho

Pesquisas que desenvolvem modelos preditivos para antecipar o desempenho dos alunos em avaliações futuras, baseadas nos
dados históricos do ENEM.

**Exemplo de Artigo:**

- **Título:** [Educational Data Mining to Forecast Essay Score: A Case Study About ENEM]

- **Descrição:**

O artigo explora a previsão de notas de redação no ENEM, utilizando algoritmos de _machine learning_ para avaliar a
eficácia das predições. O objetivo central é entender quais configurações de características são mais úteis para prever
as notas das redações e como essas previsões podem ser utilizadas para melhorar os resultados dos estudantes.

**Hipóteses Avaliadas:**

- A eficácia de diferentes algoritmos de _machine learning_ (Random Forest, Neural Network, KNN Regressor, Linear
  Regression) na previsão de notas de redação.
- Comparação entre a previsão de notas de redação e a previsão de notas em disciplinas objetivas, considerando as
  diferentes habilidades exigidas para cada tipo de avaliação.

**Métodos Utilizados:**

- **Algoritmos de Machine Learning:** Foram testados diversos algoritmos, incluindo Random Forest, Neural Network, KNN
  Regressor e Linear Regression, para prever as notas de redação com base em diferentes configurações de características
  dos candidatos.
- **Erro Absoluto Médio (MAE):** Utilizado como métrica para avaliar o desempenho dos algoritmos, onde Random Forest
  apresentou o melhor resultado, seguido por Neural Network. Algoritmos como KNN Regressor e Linear Regression
  mostraram-se menos eficazes.
- **Comparação de Desempenho:** A comparação entre a previsão de notas de redação e disciplinas objetivas revela que a
  previsão de redação é mais desafiadora, devido às habilidades argumentativas necessárias, sugerindo que a previsão de
  desempenho nas redações pode ser utilizada como uma ferramenta para identificar e melhorar desempenhos fracos.

O estudo demonstra como _machine learning_ pode ser aplicado na previsão de desempenho em redações, oferecendo insights
sobre a utilidade de diferentes algoritmos e contribuindo para a melhoria do processo educacional.

### 3. Políticas Públicas

Esta categoria investiga o impacto de políticas públicas educacionais usando os resultados do ENEM, analisando como
diferentes políticas influenciam o desempenho e a equidade educacional.

**Exemplo de Artigo:**

- **Título:** [Analyzing the Equity of the Brazilian National High School Exam by Validating the Item Response Theory's
  Invariance]

- **Descrição:**

O artigo analisa a edição de 2019 do ENEM para avaliar se o pressuposto de invariância da Teoria de Resposta ao Item
(IRT) é mantido entre diferentes subgrupos definidos por características de gênero, raça e nível de renda. A premissa da
IRT é que a probabilidade de um participante responder corretamente a uma pergunta deve ser consistente
independentemente do subgrupo ao qual ele pertence. Este estudo investiga se essa premissa se sustenta no ENEM,
examinando se certas perguntas favorecem grupos específicos.

**Hipóteses Avaliadas:**

- A premissa de que a função de probabilidade de resposta correta, segundo a IRT, é invariável entre subgrupos de
  diferentes características (gênero, raça, e renda).
- Avaliação de se as perguntas do ENEM 2019 apresentam um viés que favorece um determinado grupo em detrimento de
  outros, levando a uma desigualdade nas notas atribuídas.

**Métodos Utilizados:**

- **Curvas Características dos Itens (ICCs):** As ICCs são utilizadas para modelar a probabilidade de um participante
  responder corretamente a uma pergunta, dado seu nível de habilidade. O estudo compara a área sob a curva (AUC) para
  diferentes subgrupos (por exemplo, homens e mulheres) para verificar se existe uma discrepância significativa.
- **Teste de Classificação Não Paramétrico:** Após a análise das ICCs, o estudo aplica um teste não paramétrico para
  verificar se as diferenças observadas são estatisticamente consistentes em todo o exame. Esse método é usado para
  avaliar se as perguntas consistentemente favorecem um grupo específico ao longo do teste.
- **Análise Estatística:** O estudo realiza uma análise estatística robusta para determinar se as ICCs, conforme
  estimadas pela IRT, favorecem certos grupos, sugerindo que a metodologia de pontuação do ENEM pode não ser
  completamente equitativa.

Este artigo contribui para o campo de _learning analytics_ ao questionar a equidade da metodologia de pontuação do ENEM,
oferecendo insights sobre como a IRT pode, inadvertidamente, beneficiar ou prejudicar subgrupos específicos.

### 4. Análise Socioeconômica

Os estudos nesta categoria se concentram na relação entre desempenho no ENEM e fatores socioeconômicos, buscando
entender as desigualdades educacionais e suas implicações na educação.

**Exemplo de Artigo:**

- **Título:** [Educational Data Mining: A Study on Socioeconomic Indicators in Education in INEP Database]

- **Descrição:**

O artigo explora como variáveis socioeconômicas influenciam as notas dos estudantes no ENEM 2016, utilizando uma base de
dados fornecida pelo INEP. O objetivo principal é identificar e explicar melhor quais fatores socioeconômicos impactam o
desempenho dos alunos no exame.

**Hipóteses Avaliadas:**

- A influência de variáveis socioeconômicas, como renda familiar, escolaridade dos pais e tipo de escola, no desempenho
  dos estudantes no ENEM 2016.
- A relação entre esses fatores e as notas obtidas, buscando entender como diferentes contextos socioeconômicos afetam o
  aprendizado e o sucesso acadêmico.

**Métodos Utilizados:**

- **Análise de Componentes Principais (PCA):** Esta técnica foi aplicada para reduzir a dimensionalidade dos dados,
  permitindo identificar os fatores mais influentes de forma mais clara e concisa. A PCA ajuda a extrair as principais
  variáveis socioeconômicas que explicam a maior parte da variação no desempenho dos alunos.
- **Redes Bayesianas:** Foram geradas redes bayesianas para modelar as relações probabilísticas entre as variáveis
  socioeconômicas e o desempenho dos estudantes. Essas redes permitem uma análise mais detalhada das dependências e
  interações entre os fatores, ajudando a prever como mudanças em uma variável podem impactar as notas dos alunos.

Os resultados mostram que fatores como renda, escolaridade dos pais e tipo de escola (pública ou privada) são fortes
influenciadores das notas dos estudantes. Este estudo contribui para o entendimento de como variáveis socioeconômicas
impactam o desempenho acadêmico e fornece insights valiosos para a formulação de políticas educacionais mais
equitativas.

### 5. Avaliação de Ensino

Nesta categoria, são realizadas avaliações da qualidade do ensino em diferentes escolas ou regiões utilizando os dados
do ENEM, visando identificar pontos fortes e áreas de melhoria no sistema educacional.

**Exemplo de Artigo:**

- **Título:** [Data Mining Solution for Assessing Brazilian Secondary School Quality]

- **Descrição:**

O artigo aborda os desafios do ensino médio brasileiro, com foco especial no papel dos Institutos Federais (IFs) na
oferta de educação técnica integrada ao ensino médio. O objetivo é desenvolver uma solução de _data mining_ que auxilie
os gestores dos IFs na tomada de decisões e na avaliação da qualidade dos serviços oferecidos, além de prever o
desempenho dos alunos e explicar os fatores que o influenciam.

**Hipóteses Avaliadas:**

- A eficácia dos Institutos Federais em melhorar a qualidade da educação técnica integrada ao ensino médio.
- Identificação dos fatores e nichos que influenciam o desempenho dos alunos no ensino médio técnico, com base nos dados
  coletados.

**Métodos Utilizados:**

- **Regressão Logística:** Utilizada para modelar a probabilidade de determinados resultados (como desempenho acadêmico)
  com base em variáveis independentes, ajudando a identificar quais fatores são mais determinantes no desempenho dos
  estudantes.
- **Árvores de Decisão:** Aplicadas para segmentar os dados em grupos com base nas características que mais influenciam
  o desempenho dos alunos, facilitando a interpretação dos padrões e a tomada de decisões informadas.
- **Indução de Regras de Classificação:** Técnica usada para extrair conhecimento e validar os resultados, fornecendo
  regras explícitas que explicam como diferentes fatores afetam o desempenho dos estudantes nos IFs.

O estudo emprega uma abordagem de _Domain-Driven Data Mining (D3M)_ para garantir que as técnicas de _data mining_ sejam
aplicadas de maneira relevante ao contexto educacional dos IFs. Esta abordagem permite aos gestores entender melhor os
fatores que afetam o desempenho dos alunos e tomar decisões mais informadas para melhorar a qualidade do ensino
oferecido.

## Conclusão

As análises dos dados do ENEM frequentemente se concentram em fatores socioeconômicos, como renda familiar, escolaridade
dos pais e tipo de escola, devido à sua influência significativa no desempenho dos estudantes. Estudos mostram que essas
variáveis impactam diretamente as notas dos alunos, como demonstrado pelo uso de técnicas de _data mining_ e redes
bayesianas para modelar essas relações [1], [2]. A análise de curvas características de itens (ICCs) para avaliar a
equidade também reforça que certas questões podem favorecer grupos específicos, revelando a importância de uma avaliação
justa entre diferentes subgrupo [3].

Embora essas abordagens sejam eficazes para entender as desigualdades educacionais e orientar políticas públicas, elas
indicam uma dependência dos dados socioeconômicos como principais preditores de desempenho. Isso pode limitar a
compreensão de outros fatores igualmente importantes, como características pedagógicas ou psicológicas dos estudantes.
No entanto, o uso de técnicas de _machine learning_ e _domain-driven data mining_ proporciona insights valiosos para
gestores educacionais, permitindo-lhes melhorar a qualidade do ensino e a equidade educacional de forma mais holística e
informada [5], [2].

## Referências

- [1]
  [A Data Mining Approach Applied to the High School National Examination: Analysis of Aspects of Candidates to Brazilian Universities](https://link.springer.com/chapter/10.1007/978-3-030-30241-2_1)
- [2]
  [Educational Data Mining to Forecast Essay Score: A Case Study About ENEM](https://link.springer.com/chapter/10.1007/978-3-031-33261-6_12)
- [3]
  [Analyzing the Equity of the Brazilian National High School Exam by Validating the Item Response Theory's Invariance](https://educationaldatamining.org/edm2022/proceedings/2022.EDM-posters.64/index.html)
- [4]
  [Educational Data Mining: A Study on Socioeconomic Indicators in Education in INEP Database](https://link.springer.com/chapter/10.1007/978-981-15-0978-0_5)
- [5]
  [Data Mining Solution for Assessing Brazilian Secondary School Quality](https://ieeexplore.ieee.org/document/8923965)