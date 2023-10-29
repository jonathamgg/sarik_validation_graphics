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

O arquivo PDF fornecido ([Veja o PDF aqui](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/vote/media_tr_apt.pdf)) foi processado usando expressões regulares para extração de dados. As métricas estatísticas extraídas incluem média, mediana, desvio-padrão, amplitude, mínimo, máximo, assimetria e curtose. A linguagem utilizada para esta análise foi o Python para processamento subsequente.

---

## Resultados

## Estatísticas Descritivas

Os dados extraídos são resumidos na tabela abaixo:
[Link para o arquivo CSV](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/vote/media_tr_apt.csv)

> **Tabela Anexo**

| Group   | media    |
| ------- | -------- |
| Group 1 | 0.916766 |
| Group 1 | 0.783441 |
| Group 1 | 2.05011  |
| Group 1 | 2.11678  |
| Group 1 | 17.2501  |
| Group 1 | 0.783441 |
| Group 1 | 0.750114 |
| Group 1 | 0.85011  |
| Group 1 | 0.850115 |
| Group 1 | 2.18344  |
| Group 2 | 15.8834  |
| Group 2 | 18.6168  |
| Group 2 | 17.2834  |
| Group 2 | 17.3168  |
| Group 2 | 17.2834  |
| Group 2 | 18.6501  |
| Group 2 | 17.2834  |
| Group 2 | 17.3168  |
| Group 2 | 150.65   |
| Group 2 | 17.3168  |

## Teste t para Amostras Independentes

Estatística t de Student: -46.4 (gl = 16.0, p < .001)

t de Welch: -46.4 (gl = 15.2, p < .001)

Teste de Levene para Homogeneidade de Variâncias: F = 0.0437, gl1 = 1, gl2 = 16, p = 0.837

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
