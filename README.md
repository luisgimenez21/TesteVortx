# TesteVortx

<br>
# Ferramentas necessarias para rodar a aplicação.
PYCHARM
<br>
PYTHON 3.7
<br>
install: selenium
<br>
pip install behave
<br>
pip install allure-behave
<br>
chromedriver -na versao atual do navegador

# Comando para rodar aplicação:
<br>
behave -f allure_behave.formatter:AllureFormatter -o testes-report features/test_vortx
<br>
testes configurados para rodar em headless

# Comando para gerar relatorio no servidor allure
<br>
allure serve C:\\TesteVortx\testes-report
<br>

![image](https://user-images.githubusercontent.com/83729219/118436321-04c19d00-b6b7-11eb-93be-c0582f719112.png)
