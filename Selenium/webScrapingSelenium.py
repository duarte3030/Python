# 1- Entrar na Internet, pegar a cotacao.
# 2- Pegar cotacao do dolar, euro e ouro.
# 3- Importar excel, atualizar, exportar

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

# dolar
navegador.get("http://www.google.com")
navegador.find_element_by_xpath(r"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotacao do dolar")
navegador.find_element_by_xpath(r"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[3]/td[1]/input').get_attribute('value')
print(cotacao_dolar)
# euro
navegador.get("http://www.google.com")
navegador.find_element_by_xpath(r"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotacao do euro")
navegador.find_element_by_xpath(r"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[3]/td[1]/input').get_attribute('value')
print(cotacao_euro)
# ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value').replace(',', '.')
print(cotacao_ouro)

navegador.quit()

# importar excel
tabela = pd.read_excel('Produtos.xlsx')
# atualizar cotacao, preco de compra e venda
tabela.loc[tabela["Moeda"] == "Dolar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
tabela["Preço de Compra"] = tabela["Preço Base Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
# tabela["Preço Final"].map("{:.2f}").format
tabela.to_excel("Produtos Novo.xlsx", index=False)
