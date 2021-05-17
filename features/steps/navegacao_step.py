# coding=utf-8
from behave import *


@given(u'que esteja home page da Vortx')
def step_impl(context):
    context.driver.get(context.url)


@when(u'eu clicar na sessao do investidor')
def step_impl(context):
    context.vortx.clicar_sessao_investidor(context)


@when(u'selecionar fundos de investimento')
def step_impl(context):
    context.vortx.selecionar_fundos_investimento(context)


@then(u'o sistema deve exibir pagina carregando fundos disponiveis')
def step_impl(context):
    context.vortx.validar_fundos_investimentos(context)


# cenario2
@given(u'que eu esteja na pagina de Fundos de investimento')
def step_impl(context):
    context.driver.get(context.url_fundo_investimento)


@when(u'eu clicar no detalhe de um fundo')
def step_impl(context):
    context.vortx.clicar_detalhe_fundo_investimento(context)


@then(u'o sistema deve exibir  carregando do fundo selecionado')
def step_impl(context):
    context.vortx.valida_detalhe_fundo(context)

#cenario 3
@given(u'que eu esteja no detalhe de um investimento')
def step_impl(context):
    context.driver.get(context.url_fundo_investimento_detalhe)


@when(u'eu clicar na aba documentos')
def step_impl(context):
    context.vortx.clicar_aba_documentos(context)


@when(u'clicar em download do pdf')
def step_impl(context):
    context.vortx.clicar_download(context)


@then(u'o sistema deve realizar download')
def step_impl(context):
    context.vortx.valida_download(context)

