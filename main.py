import pyautogui #biblioteca para automação
import time
import pandas #gerenciador de banco

#automação para cadastrar produtos dentro de um site.
pyautogui.PAUSE = 0.5 #tempo de espera a cada linha de comando

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=1520, y=32)#click no button para maximizar a tela
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(4)#dando tempo para página carregar
pyautogui.click(x=1375, y=521)#pegando posição na tela no outro arquivo nomeado "posicaoMouse"
pyautogui.write('marlonzucolotto@gmail.com')
pyautogui.press('tab')
pyautogui.write('naruto321')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

tabela = pandas.read_csv('produtos.csv')#lendo tabela

for linha in tabela.index:
      pyautogui.click(x=1372, y=363)#clicando no primeiro  campo do form 
      pyautogui.write(str(tabela.loc[linha, "codigo"]))
      pyautogui.press('tab')
      pyautogui.write(str(tabela.loc[linha, "marca"]))
      pyautogui.press('tab')
      pyautogui.write(str(tabela.loc[linha, "tipo"]))
      pyautogui.press('tab')
      pyautogui.write(str(tabela.loc[linha, "categoria"]))
      pyautogui.press('tab')
      pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
      pyautogui.press('tab')
      pyautogui.write(str(tabela.loc[linha, "custo"]))
      pyautogui.press('tab')
      if not pandas.isna(tabela.loc[linha, "obs"]):
            pyautogui.write(str(tabela.loc[linha, "obs"]))
      pyautogui.press('tab')
      pyautogui.press('enter')
