#language:pt
Funcionalidade: Desafio - Laboratório Automação

  Contexto: Validações Vortx
    Dado que esteja home page da Vortx

  @cenario1
  Cenario: Acessar Fundos de Investimento
    Quando eu clicar na sessao do investidor
    E selecionar fundos de investimento
    Então o sistema deve exibir pagina carregando fundos disponiveis

  @cenario2
  Cenario: Acessar detalhe de um Fundo de Investimento
    Dado que eu esteja na pagina de Fundos de investimento
    Quando eu clicar no detalhe de um fundo
    Então o sistema deve exibir  carregando do fundo selecionado

  @cenario3
  Cenario: Download aquivo
    Dado que eu esteja no detalhe de um investimento
    Quando eu clicar na aba documentos
    E clicar em download do pdf
    Então o sistema deve realizar download

