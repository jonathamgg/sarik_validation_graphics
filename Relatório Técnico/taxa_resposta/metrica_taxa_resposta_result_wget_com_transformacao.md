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

O arquivo PDF fornecido ([Veja o PDF aqui](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/result/media_tr_wget_transformado.pdf)) foi processado usando expressões regulares para extração de dados. As métricas estatísticas extraídas incluem média, mediana, desvio-padrão, amplitude, mínimo, máximo, assimetria e curtose. A linguagem utilizada para esta análise foi o Python para processamento subsequente.

---

## Resultados

## Estatísticas Descritivas
Os dados extraídos são resumidos na tabela abaixo:
[Link para o arquivo CSV](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/result/media_tr_wget_transformado.csv)

> **Tabela Anexo**

| Group  | media    | LOG                 |
|--------|----------|---------------------|
| Group 1| 17.0501  | 2.8361560688149656  |
| Group 1| 2.15011  | 0.7655190036214983  |
| Group 1| 0.516774 | -0.6601496373768385 |
| Group 1| 1.78344  | 0.5785440835351864  |
| Group 1| 1.58345  | 0.4596060108744184  |
| Group 1| 0.516774 | -0.6601496373768385 |
| Group 1| 0.516781 | -0.6601360918954656 |
| Group 1| 0.416777 | -0.875203972407232  |
| Group 1| 0.483449 | -0.726809450520952  |
| Group 1| 0.516776 | -0.6601457672205808 |
| Group 2| 33.5501  | 3.5130398440391803  |
| Group 2| 33.6168  | 3.5150259420108094  |
| Group 2| 33.5834  | 3.514031897268375   |
| Group 2| 33.5834  | 3.514031897268375   |
| Group 2| 33.5834  | 3.514031897268375   |
| Group 2| 33.5834  | 3.514031897268375   |
| Group 2| 168.25   | 5.125450968524837   |
| Group 2| 166.917  | 5.117496682880317   |
| Group 2| 33.6168  | 3.5150259420108094  |


## Teste t para Amostras Independentes

Estatística t de Student: -15.0 (gl = 14.0, p < .001)

t de Welch: -17.1 (gl = 8.00, p < .001)

Teste de Levene para Homogeneidade de Variâncias: F = 40.0, gl1 = 1, gl2 = 14, p = 0.001

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
