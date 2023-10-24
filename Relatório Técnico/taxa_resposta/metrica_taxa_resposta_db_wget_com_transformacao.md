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

O arquivo PDF fornecido ([Veja o PDF aqui](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/db/media_tr_wget_transformado.pdf)) foi processado usando expressões regulares para extração de dados. As métricas estatísticas extraídas incluem média, mediana, desvio-padrão, amplitude, mínimo, máximo, assimetria e curtose. A linguagem utilizada para esta análise foi o Python para processamento subsequente.

---

## Resultados

## Estatísticas Descritivas
Os dados extraídos são resumidos na tabela abaixo:
[Link para o arquivo CSV](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/db/media_tr_wget_transformado.csv)

> **Tabela Anexo**

| Group  | media    | LOG               |
|--------|----------|-------------------|
| Group 1| 2.25011  | 0.8109791039101948|
| Group 1| 0.516774 | -0.6601496373768385|
| Group 1| 0.483442 | -0.7268239299193541|
| Group 1| 0.21678  | -1.5288722645945332|
| Group 1| 1.81677  | 0.5970601991233404|
| Group 1| 0.516781 | -0.6601360918954656|
| Group 1| 0.516777 | -0.6601438321480688|
| Group 1| 1.85012  | 0.6152505018514639|
| Group 1| 0.516776 | -0.6601457672205808|
| Group 2| 33.6168  | 3.5150259420108094|
| Group 2| 33.5501  | 3.5130398440391803|
| Group 2| 33.5834  | 3.514031897268375|
| Group 2| 33.5834  | 3.514031897268375|
| Group 2| 33.6168  | 3.5150259420108094|
| Group 2| 33.5834  | 3.514031897268375|


## Teste t para Amostras Independentes

Estatística t de Student: -11.6 (gl = 13.0, p < .001)

t de Welch: -14.4 (gl = 8.00, p < .001)

Teste de Levene para Homogeneidade de Variâncias: F = 18.1, gl1 = 1, gl2 = 13, p = 0.001

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
