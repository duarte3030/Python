# Automacao de Tarefas
import matplotlib.pyplot
import pyautogui
import pyperclip
import time
import pandas as pd
import displayfunction


# entrar no sistema

pyautogui.PAUSE = 1
pyautogui.hotkey('ctrl', 't')
link = ''
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#navegar no sistema
time.sleep(5)
pyautogui.click(x=478, y=317, clicks = 2)

# fazer o download, cliques

# calcular faturamento com o Pandas no Excel
table = pd.read_excel(r"C:\\...Vendas - Dez.xlsx")
faturamento = table["Valor Final"].sum()
quantidade = table["Quantidade"].sum()
displayfunction.display(table)

#enviar email


