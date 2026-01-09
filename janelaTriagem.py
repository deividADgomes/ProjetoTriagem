from tkinter import *
from tkinter import ttk
from Triagem import preencherTriagem
import datetime
import db
from tkinter import messagebox

dataAtual = datetime.datetime.now()
tabelaTriagem = db.tabelaTriagem()


dados = {
    "data": "00/00/0000",
    "NF": "-",
    "ticket": "-",
    "tecnico": "-",
    "analistaResponsavel": "-",
    "regiao": "-",
    "equipamento": "-",
    "NSerie": "-",
    "pecaEquipamentoTrocado": "-",
    "defeitoAlegado": "-",
    "constatacaoTecnico": "-",
    "defeitoConstatado": "-",
    "testesRealizados": "-",
    "analise": "-",
    "conclusao": "-"
}
 
class Janela(object):
    def __init__(self, ticket):
        self.janela = Toplevel()
        self.JanelaTriagem()
        self.ComponentesJL(ticket)

    def JanelaTriagem(self):
        self.janela.title("Triagem")
        self.janela.geometry("800x800")
        self.janela.resizable(False,False)
        self.janela.configure(background='#7ea0b1')

    def ComponentesJL(self, ticket):

        lista = db.pesquisarTriagem(ticket)
        listaDados =[]
        for item in lista:
            listaDados= item

        self.jlTriagem = Frame(self.janela)
        self.jlTriagem.place(relheight=1, relwidth=1)
        self.jlTriagem.configure(bg='#7ea0b1')
        
        corFundo = "#f0f2f5"
        corBg = "#ffffff"
        corLbl = "#444444"
        corBtSalvar = "#2980b9"
        fonteLbl = ("Segoe UI", 9, "bold")
        fonteEntry = ("Segoe UI", 10)

        self.jlTriagem.configure(bg=corFundo)

        Label(self.jlTriagem, text="TRIAGEM TÉCNICA", bg=corFundo, fg="#2c3e50", 
              font=("Segoe UI", 14, "bold")).place(relx=0.03, rely=0.01)

        self.lblData = Label(self.jlTriagem, text="Data", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblData.place(relx=0.03, rely=0.07)
        self.entryData = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1, justify="center")
        self.entryData.place(relx=0.03, rely=0.10, relwidth=0.12, height=28)
        self.entryData.insert(0, listaDados[1])
        self.entryData.configure(state=DISABLED)

        self.lblNF = Label(self.jlTriagem, text="Nota Fiscal (NF)", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblNF.place(relx=0.17, rely=0.07)
        self.entryNF = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryNF.place(relx=0.17, rely=0.10, relwidth=0.12, height=28)
        self.entryNF.insert(0, listaDados[2])

        self.lblTicket = Label(self.jlTriagem, text="Nº Ticket", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblTicket.place(relx=0.31, rely=0.07)
        self.entryTicket = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTicket.place(relx=0.31, rely=0.10, relwidth=0.15, height=28)
        self.entryTicket.insert(0, listaDados[3])

        self.lblRegiao = Label(self.jlTriagem, text="Região", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblRegiao.place(relx=0.48, rely=0.07)
        self.entryRegiao = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryRegiao.place(relx=0.48, rely=0.10, relwidth=0.20, height=28)

        self.lblTecnico = Label(self.jlTriagem, text="Técnico Responsável", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblTecnico.place(relx=0.03, rely=0.15)
        self.entryTecnico = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTecnico.place(relx=0.03, rely=0.18, relwidth=0.30, height=28)

        self.lblAnalista = Label(self.jlTriagem, text="Analista Responsável", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblAnalista.place(relx=0.35, rely=0.15)
        self.entryAnalista = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryAnalista.place(relx=0.35, rely=0.18, relwidth=0.33, height=28)

        self.lblCliente = Label(self.jlTriagem, text="Cliente", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblCliente.place(relx=0.70, rely=0.15)
        self.entryCliente = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryCliente.place(relx=0.70, rely=0.18, relwidth=0.20, height=28)

        self.lblEquipamento = Label(self.jlTriagem, text="Modelo do Equipamento", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblEquipamento.place(relx=0.03, rely=0.23)
        self.entryEquipamento = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryEquipamento.place(relx=0.03, rely=0.26, relwidth=0.45, height=28)

        self.lblNserie = Label(self.jlTriagem, text="N° de Série (SN)", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblNserie.place(relx=0.50, rely=0.23)
        self.entryNSerie = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryNSerie.place(relx=0.50, rely=0.26, relwidth=0.18, height=28)

        self.lblTroca = Label(self.jlTriagem, text="Peça/Equipamento Trocado", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblTroca.place(relx=0.03, rely=0.31)
        self.entryTroca = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTroca.place(relx=0.03, rely=0.34, relwidth=0.65, height=28)

        self.lblDefeito = Label(self.jlTriagem, text="Defeito Alegado", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblDefeito.place(relx=0.03, rely=0.39)
        self.textDefeito = Text(self.jlTriagem, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1)
        self.textDefeito.place(relx=0.03, rely=0.42, relwidth=0.94, height=50)

        self.lblConstatacaoTec = Label(self.jlTriagem, text="Constatação do Técnico", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblConstatacaoTec.place(relx=0.03, rely=0.50)
        self.textConstatacaoTec = Text(self.jlTriagem, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1)
        self.textConstatacaoTec.place(relx=0.03, rely=0.53, relwidth=0.94, height=50)

        self.lblDefeitoConsta = Label(self.jlTriagem, text="Defeito Constatado (Resumo)", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblDefeitoConsta.place(relx=0.03, rely=0.61)
        self.entryDefeitoConsta = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryDefeitoConsta.place(relx=0.03, rely=0.64, relwidth=0.45, height=28)

        self.lblTeste = Label(self.jlTriagem, text="Testes Realizados", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblTeste.place(relx=0.50, rely=0.61)
        self.entryTeste = Entry(self.jlTriagem, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTeste.place(relx=0.50, rely=0.64, relwidth=0.47, height=28)

        self.lblAnalise = Label(self.jlTriagem, text="Análise do Equipamento/Peça", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblAnalise.place(relx=0.03, rely=0.69)
        self.textAnalise = Text(self.jlTriagem, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1)
        self.textAnalise.place(relx=0.03, rely=0.72, relwidth=0.94, height=50)

        self.lblConclusao = Label(self.jlTriagem, text="Conclusão Final", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.lblConclusao.place(relx=0.03, rely=0.80)
        self.textConclusao = Text(self.jlTriagem, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1)
        self.textConclusao.place(relx=0.03, rely=0.83, relwidth=0.94, height=50)

        self.btSalvar = Button(self.jlTriagem, text="SALVAR", bg=corBtSalvar, fg="white", 
                               font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2")
                              
        self.btSalvar.place(relx=0.72, rely=0.015, width=180, height=35)

      

if __name__== "__main__": 
    Janela("28216360")