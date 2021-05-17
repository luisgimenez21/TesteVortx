import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NavegacaoPage:

    def __init__(self, driver):
        self.driver = driver
        self.waitShort = WebDriverWait(self.driver, 15)

        self.btn_investidor = By.ID, "investidor"

        self.btn_fundos_investimentos = By.ID, "investidor4"

        self.img_fundos_investinento = By.XPATH, "//*[@id='__next']/div/section[1]/div[1]/div"

        self.detalhe_fundo_investimento = By.XPATH, "//*[@id='__next']/div/section[1]/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]"

        self.aba_documentos = By.ID, 2

        self.btn_cota = By.XPATH,"//*[@id='__next']/div/section[1]/section/section/div[1]/button"

    def clicar_sessao_investidor(self, context):
        self.waitShort.until(EC.presence_of_element_located((self.btn_investidor))).click()

    def selecionar_fundos_investimento(self, context):
        self.waitShort.until(EC.presence_of_element_located((self.btn_fundos_investimentos))).click()

    def validar_fundos_investimentos(self, context):
        try:
            self.waitShort.until(EC.presence_of_element_located((self.img_fundos_investinento)))
            self.driver.save_screenshot("report_images/pagina_fundos_investimentos.png")
        except:
            context.driver.quit()

    def clicar_detalhe_fundo_investimento(self, context):
        time.sleep(5)

        self.waitShort.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div/section[1]/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]"))).click()

    def valida_detalhe_fundo(self, context):
        time.sleep(5)

        gestor_result = self.driver.find_element(By.XPATH,
                                                 "//*[@id='__next']/div/section[1]/section/section[2]/div/div[1]/h4").text

        administrador_result = self.driver.find_element(By.XPATH,
                                                        "//*[@id='__next']/div/section[1]/section/section[2]/div/div[2]/h4").text

        custodiante_result = self.driver.find_element(By.XPATH,
                                                      "//*[@id='__next']/div/section[1]/section/section[2]/div/div[3]/h4").text

        auditor_result = self.driver.find_element(By.XPATH,
                                                  "//*[@id='__next']/div/section[1]/section/section[2]/div/div[4]/h4").text

        distribuidor_result = self.driver.find_element(By.XPATH,
                                                       "//*[@id='__next']/div/section[1]/section/section[2]/div/div[5]/h4").text

        verificadora_result = self.driver.find_element(By.XPATH,
                                                       "//*[@id='__next']/div/section[1]/section/section[2]/div/div[6]/h4").text

        patrimonio_liquido_result = self.driver.find_element(By.XPATH,
                                                             "//*[@id='__next']/div/section[1]/section/section[2]/div/div[7]/h4").text

        data_fundacao_result = self.driver.find_element(By.XPATH,
                                                        "//*[@id='__next']/div/section[1]/section/section[2]/div/div[8]/h4").text

        giin_result = self.driver.find_element(By.XPATH,
                                               "//*[@id='__next']/div/section[1]/section/section[2]/div/div[9]/h4").text

        email_result = self.driver.find_element(By.XPATH,
                                                "//*[@id='__next']/div/section[1]/section/section[2]/div/div[10]/h4").text

        site_ri_result = self.driver.find_element(By.XPATH,
                                                  "//*[@id='__next']/div/section[1]/section/section[2]/div/div[11]/h4/a").text

        dados_dashboard = {
            "gestor": gestor_result,
            "administrador": administrador_result,
            "custodiante": custodiante_result,
            "auditor": auditor_result,
            "distribuidor": distribuidor_result,
            "verificadora": verificadora_result,
            "patrimonio_liquido": patrimonio_liquido_result,
            "data_fundacao": data_fundacao_result,
            "giin": giin_result,
            "email": email_result,
            "site_ri_result": site_ri_result
        }

        with open('dados_dashboard.json', 'w') as f:
            json.dump(dados_dashboard, f)

    def clicar_aba_documentos(self, context):
        self.waitShort.until(EC.presence_of_element_located((self.aba_documentos))).click()

    def clicar_download(self, context):
        time.sleep(2)
        self.waitShort.until(EC.presence_of_element_located((By.ID, "Demonstração Financeira"))).click()
        time.sleep(0.2)
        try:
            self.waitShort.until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='doc-Demonstração Financeira']/a[1]"))).click()
        except:

            context.driver.quit()

    def valida_download(self, context):
        pass


