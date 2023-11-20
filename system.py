import tkinter as tk
from tkinter import ttk
import datetime as dt
import pandas as pd

lista_tipos = ["Galão", "Caixa", "Saco", "unidade"]
list_codigos = []

janela = tk.Tk()

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_Selecionar_tipo.get()
    quantidade = entry_quantidade.get()
    data_criacao = dt.datetime.now().strftime("%d/%m/%Y %H:%M")  # Correção no formato da data
    codigo = len(list_codigos) + 1
    codigo_str = "COD-{}".format(codigo)
    list_codigos.append((codigo_str, descricao, tipo, quantidade, data_criacao))
    atualizar_planilha()

def atualizar_planilha():
    # Criar DataFrame com os dados coletados
    df = pd.DataFrame(list_codigos, columns=['Código', 'Descrição', 'Tipo', 'Quantidade', 'Data de Criação'])
    
    # Salvar o DataFrame em um arquivo Excel
    df.to_excel('dados_materiais.xlsx', index=False)
    
    print("Dados salvos em 'dados_materiais.xlsx'")

janela.title('Ferramenta de cadastro de materiais')

label_descricao = tk.Label(text='Descrição do Material')
label_descricao.grid (row=1, column=0, padx= 10, pady=10, sticky='nswe', columnspan =4) #posicionamento do label

entry_descricao = tk.Entry()
entry_descricao.grid (row=2, column=0, padx= 10, pady=10, sticky='nswe', columnspan = 4) #Criação da inserção de dados

label_tipo_unidade = tk.Label(text='tipo da unidade material')
label_tipo_unidade.grid (row=3, column=0, padx= 10, pady=10, sticky='nswe', columnspan = 2)

combobox_Selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_Selecionar_tipo.grid(row= 3, column=2, padx=10, pady=10, sticky='nswe', columnspan= 2) #criação do combo box

label_quantidade = tk.Label(text='Quantidade na unidade de material')
label_quantidade.grid (row=4, column=0, padx= 10, pady=10, sticky='nswe', columnspan = 2)

entry_quantidade = tk.Entry()
entry_quantidade.grid (row=4, column=2, padx= 10, pady=10, sticky='nswe', columnspan = 2)

botao_criar_codigo = tk.Button(text="Criar codigo", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx= 10, pady=10, sticky='nswe', columnspan = 4)



janela.mainloop()

janela.mainloop()
