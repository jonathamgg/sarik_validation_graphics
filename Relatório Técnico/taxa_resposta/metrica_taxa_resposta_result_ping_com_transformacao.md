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

O arquivo PDF fornecido ([Veja o PDF aqui](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/result/media_tr_ping_transformado.pdf)) foi processado usando expressões regulares para extração de dados. As métricas estatísticas extraídas incluem média, mediana, desvio-padrão, amplitude, mínimo, máximo, assimetria e curtose. A linguagem utilizada para esta análise foi o Python para processamento subsequente.

---

## Resultados

## Estatísticas Descritivas
Os dados extraídos são resumidos na tabela abaixo:
[Link para o arquivo CSV](https://github.com/jonathamgg/sarik_validation_graphics/blob/master/c%C3%A1lculo%20estat%C3%ADstico%20com%20jamovi/taxa_resposta/result/media_tr_ping_transformado.csv)

> **Tabela Anexo**

| Group  | media    | LOG               |
|--------|----------|-------------------|
| Group 1| 12.5501  | 2.5297286336735376|
| Group 1| 11.2501  | 2.420377017499812 |
| Group 1| 11.1834  | 2.414430535983676 |
| Group 1| 12.5834  | 2.5323784850261344|
| Group 1| 11.2168  | 2.4174126544247847|
| Group 1| 11.1834  | 2.414430535983676 |
| Group 1| 11.2168  | 2.4174126544247847|
| Group 1| 11.2501  | 2.420377017499812 |
| Group 1| 145.917  | 4.983037966904152 |
| Group 1| 12.5834  | 2.5323784850261344|
| Group 2| 163.583  | 5.097320506788983 |
| Group 2| 30.2168  | 3.4083980610988562|
| Group 2| 30.2168  | 3.4083980610988562|
| Group 2| 30.2168  | 3.4083980610988562|
| Group 2| 163.55   | 5.097118753984393 |
| Group 2| 31.5501  | 3.4515767585543067|
| Group 2| 164.917  | 5.105442317035362 |
| Group 2| 30.2501  | 3.4094994902565103|
| Group 2| 30.2168  | 3.4083980610988562|
| Group 2| 30.2168  | 3.4083980610988562|


## Teste t para Amostras Independentes

Estatística t de Student: -5.37 (gl = 17.0, p < .001)

Teste de Levene para Homogeneidade de Variâncias: F = 36.3, gl1 = 1, gl2 = 17, p = 0.001

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

Os dados apresentam características estatísticas significativamente diferentes entre os dois grupos. Enquanto o "Group 1" exibe maior variabilidade e assimetria, o "Group 2" é caracterizado por maior estabilidade em suas métricas. Essas informações são cruciais para qualquer análise subsequente que envolva esses grupos e devem ser consideradas no contexto do estudo em que esses dados são aplicados. Além disso, os dados sugerem diferenças substanciais entre os dois grupos em termos de média e outras estatísticas descritivas. O teste t também indica diferenças significativas, mas a violação do pressuposto de homogeneidade das variâncias sugere cautela na interpretação desses resultados. Após aplicação da transformação logarítmica não foi possível normalizar os dados. 

---

## Referências

- Jamovi Project. (2021). Jamovi. [https://www.jamovi.org](https://www.jamovi.org)
