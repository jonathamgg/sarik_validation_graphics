# Relatório Técnico sobre Análise de Estatísticas Descritivas

## Sumário

- [Introdução](#introdução)
- [Metodologia](#metodologia)
- [Resultados](#resultados)
    - [Estatísticas Descritivas](#estatísticas-descritivas)
    - [Teste t para Amostras Independentes](#teste-t-para-amostras-independentes)
- [Discussão](#discussão)
- [Conclusão](#conclusão)
- [Referências](#referências)

---

## Introdução

O presente relatório tem como objetivo avaliar e interpretar os resultados estatísticos descritivos do teste t para amostras independentes gerados pelo software Jamovi para dois grupos distintos, referidos como "Group 1" e "Group 2". Essas estatísticas podem ser fundamentais para compreender a distribuição e as características dos dados em cada grupo.

---

## Metodologia

O arquivo PDF fornecido ([Veja o PDF aqui](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/redis/media_tr_wget_transformado.pdf)) foi processado usando expressões regulares para extração de dados. As métricas estatísticas extraídas incluem média, mediana, desvio-padrão, amplitude, mínimo, máximo, assimetria e curtose. A linguagem utilizada para esta análise foi o Python para processamento subsequente.

---

## Resultados

## Estatísticas Descritivas
Os dados extraídos são resumidos na tabela abaixo:
[Link para o arquivo CSV](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/redis/media_tr_wget_transformado.csv)

> **Tabela Anexo**

| Group  | media    | LOG                 |
|--------|----------|---------------------|
| Group 1| 4.93343  | 1.5960344865045828  |
| Group 1| 0.916775 | -0.08689320215436885|
| Group 1| 0.516774 | -0.6601496373768385 |
| Group 1| 0.583442 | -0.5388102323674304 |
| Group 1| 7.95011  | 2.0731857650485046  |
| Group 1| 0.550108 | -0.5976406563960721 |
| Group 1| 0.550115 | -0.597627931702987  |
| Group 1| 0.55011  | -0.5976370207529542 |
| Group 1| 0.516782 | -0.6601341568416761 |
| Group 1| 0.516776 | -0.6601457672205808 |
| Group 2| 9.28344  | 2.228232167764846   |
| Group 2| 9.25011  | 2.2246354433455178  |
| Group 2| 9.28344  | 2.228232167764846   |
| Group 2| 7.95011  | 2.0731857650485046  |
| Group 2| 9.31677  | 2.2318160021058384  |
| Group 2| 7.91678  | 2.0689845574995442  |
| Group 2| 7.98344  | 2.077369396268657   |
| Group 2| 9.28345  | 2.2282332449511704  |
| Group 2| 7.95011  | 2.0731857650485046  |


## Teste t para Amostras Independentes

Estatística t de Student: -80.0 (gl = 14.0, p < .001)

t de Welch: -85.7 (gl = 13.00, p < .001)

Teste de Levene para Homogeneidade de Variâncias: F = 23.5, gl1 = 1, gl2 = 14, p = 0.001

---

## Discussão

### Média e Mediana
O "Group 1" possui uma média e mediana significativamente menores em comparação com o "Group 2", o que pode sugerir diferentes escalas ou unidades de medida.

### Desvio-Padrão
O "Group 1" apresenta maior variabilidade nos dados, como indicado pelo maior desvio-padrão.

### Amplitude
A amplitude para o "Group 1" também é maior, corroborando a maior variabilidade nos dados deste grupo.

### Assimetria
O "Group 1" apresenta uma assimetria significativamente maior, indicando uma distribuição inclinada para a direita.

### Curtose
O "Group 1" apresenta uma curtose positiva, indicando uma distribuição mais "pontiaguda" em relação a uma distribuição normal, enquanto o "Group 2" tem curtose negativa, sugerindo uma distribuição mais "achatada".

A análise das estatísticas descritivas e do teste t para amostras independentes sugere diferenças significativas entre os dois grupos. O Teste de Levene foi significativo (p < 0.05), indicando a violação do pressuposto de homogeneidade das variâncias.

---

## Conclusão

Os dados apresentam características estatísticas significativamente diferentes entre os dois grupos. Enquanto o "Group 1" exibe maior variabilidade e assimetria, o "Group 2" é caracterizado por maior estabilidade em suas métricas. Essas informações são cruciais para qualquer análise subsequente que envolva esses grupos e devem ser consideradas no contexto do estudo em que esses dados são aplicados. Além disso, os dados sugerem diferenças substanciais entre os dois grupos em termos de média e outras estatísticas descritivas. O teste t também indica diferenças significativas, mas a violação do pressuposto de homogeneidade das variâncias sugere cautela na interpretação desses resultados.

---

## Referências

- Jamovi Project. (2021). Jamovi. [https://www.jamovi.org](https://www.jamovi.org)
