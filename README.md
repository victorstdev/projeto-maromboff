# projeto-maromboff
 Application to manage banoff expenses, invoicing and sales records

## Problema
Minha irmã resolveu vender banoffs até o final de 2023 para conseguir uma renda extra para ajudar a pagar seu casamento. Até aí tudo bem, ela fez a sua primeira produção, porém não teve um controle dos gastos e do possível faturamento pra se calcular o lucro.

## Solução proposta
E se fizéssemos um aplicativo que ajudasse todo esse controle pra ela? Tanto na parte de registrar compra de matéria prima, quanto as vendas e o lucro obtido ao final de cada período?
Pra isso, pensei em um webapp em Django onde ela pudesse realizar todo esse gerenciamento de forma mais simples e que retornasse pra ela uma análise financeira.
Estou pensando em hospedar online pra que ela consiga acessar via celular.

## MVP Inicial
Vamos começar com o básico, uma planilha em excel que tenha três abas:
- Registro de compra de matéria prima
  - Data da compra, material e preço 
- Registro de vendas
  - Data da venda, valor pago
- Análise de gasto, faturamento e lucro
  - Gasto: Soma de preço da matéria prima
  - Faturamento: Soma de valor pago da venda
  - Lucro: Faturamento - Gasto
Com essa planilha, iremos até poder identificar outros indicadores que não estamos pensando inicialmente mas que poderão surgir.

## Possíveis melhorias
- Previsão de faturamento
- Previsão de tempo e quantidade de vendas para atingir a meta monetária
