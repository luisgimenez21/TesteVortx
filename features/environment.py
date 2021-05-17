from selenium import webdriver

from features.pages.NavegacaoPage import NavegacaoPage


def before_all(context):
    # Configurações do driver
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument("headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--enable-webgl")
    chrome_options.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)

    # URL UTILIZAVEIS
    context.url = "https://vortx.com.br/"
    context.url_fundo_investimento = "https://vortx.com.br/investidor/fundos-investimento"
    context.url_fundo_investimento_detalhe ="https://vortx.com.br/investidor/fundos-investimento/operacao?cnpj=26.502.794/0001-85"

    context.vortx = NavegacaoPage(context.driver)


def after_all(context):
    context.driver.quit()
