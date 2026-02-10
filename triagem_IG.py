from tkinter import *
import datetime
from tkinter import ttk
from Triagem import preencherTriagem
import db
from tkinter import messagebox
import textwrap
import janelaTriagem




dataAtual = datetime.datetime.now()
tabelaTriagem = db.tabelaTriagem()
root = Tk()

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
    "cliente": "-",
    "defeitoAlegado": "-",
    "constatacaoTecnico": "-",
    "defeitoConstatado": "-",
    "testesRealizados": "-",
    "analise": "-",
    "conclusao": "-",
    "pecaEquipamentoFuncional": 0
}

def wrap(string, lenght=15):
    return '\n'.join(textwrap.wrap(string, lenght))

class Application():
    def __init__(self):
        self.root = root
        self.telaPrincipal()
        self.frame()

        self.frameAtual = self.frame2
        self.frame2.lift()
        self.ComponentesFrame2()
        self.ComponentesFrame3()
        self.ComponentesFrameDash()

        self.botoesLaterais()
        root.mainloop()

    def telaPrincipal(self):
        self.root.title("Daedalus Gestio")
        self.root.geometry("800x800")
        self.root.resizable(False,True)
        self.root.configure(background='#7ea0b1')


    def frame(self):
        
        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0.1 , rely=0, relheight=1 , relwidth=0.90)
        self.frame2.configure(bg="lightgrey")
        
        self.frame3 = Frame(self.root)
        self.frame3.place(relx=0.1 , rely=0, relheight=1 , relwidth=0.90)
        self.frame3.configure(bg="lightgrey")
        
        self.frameDash = Frame(self.root)
        self.frameDash.place(relx=0.1 , rely=0, relheight=1 , relwidth=0.90)
        self.frameDash.configure(bg="#f0f2f5")
        
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0 , rely=0, relheight=1 , relwidth=0.10)
        self.frame1.configure(background='#2c3e50')

    def ComponentesFrameDash(self):
        for widget in self.frameDash.winfo_children():
            widget.destroy()

        Label(self.frameDash, text="VISÃO GERAL", 
              bg="#f0f2f5", fg="#5e6d7a", font=("Segoe UI", 12, "bold"), anchor="w").place(relx=0.03, rely=0.04)

        try:
            
            mesAtual = dataAtual.month
            anoAtual = dataAtual.year
            totalMes = db.totalTriagensNoMes(mesAtual, anoAtual)
        
        except:
            totalMes = 0

        self.criarDashboard(
            framePai=self.frameDash,
            titulo="TOTAL DE TRIAGENS",
            valor=db.totalTriagens(),
            icone="📂",
            CorDestaque="#2980b9",
            relx=0.03, rely=0.12, relwidth=0.45, relheight=0.25
        )

        self.criarDashboard(
            framePai=self.frameDash,
            titulo=f"TRIAGENS MENSAL ({mesAtual}/{anoAtual})",
            valor=totalMes,
            icone="📅",
            CorDestaque="#27ae60",
            relx=0.50, rely=0.12, relwidth=0.45, relheight=0.25
        )

        self.criarDashboard(
            framePai=self.frameDash,
            titulo="PEÇAS/EQUIPAMENTOS FUNCIONAIS",
            valor=db.totalTriagensPecaFuncional(),
            icone="✅",
            CorDestaque="#16a085",
            relx=0.03, rely=0.42, relwidth=0.45, relheight=0.25
        )
        self.criarDashboard(
            framePai=self.frameDash,
            titulo="PEÇAS/EQUIPAMENTOS NÃO FUNCIONAIS",
            valor=db.totalTriagensPecaNaoFuncional(),
            icone="❌",
            CorDestaque="#c0392b",
            relx=0.50, rely=0.42, relwidth=0.45, relheight=0.25
        )

    def criarDashboard(self, framePai, titulo, valor, icone, CorDestaque, relx, rely, relwidth, relheight):
        card = Frame(framePai, bg="white", bd=0, highlightbackground="#d1d8dd", highlightthickness=1)
        card.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        Frame(card, bg=CorDestaque).place(relx=0, rely=0, relheight=1, width=6)
        Label(card, text=icone, bg="white", fg=CorDestaque, font=("Segoe UI Symbol", 28)).place(relx=0.82, rely=0.5, anchor=CENTER)
        Label(card, text=titulo, bg="white", fg="#7f8c8d", font=("Segoe UI", 9, "bold")).place(x=20, y=15)
        Label(card, text=str(valor), bg="white", fg="#2c3e50", font=("Segoe UI", 32, "bold")).place(x=20, rely=0.55, anchor="w")

  
    def ComponentesFrame3(self):

        self.frameBusca = Frame(self.frame3, bg="#d9e1e8", bd=1, relief=GROOVE)
        self.frameBusca.place(relx=0.02, rely=0.02, relwidth=0.96, height=135)

        opcoes = ["Data", "Ticket", "Técnico", "Analista Responsável", "Equipamento", "Cliente","N° Série","Peça/Equipamento Funcional"]
        self.opcoesPesquisa = ["Sim", "Não"]

        self.comboOpcoes = ttk.Combobox(self.frameBusca, values=opcoes, state='readonly')
        self.comboOpcoes.place(relx=0.02, rely=0.30)
        self.comboOpcoes.set("Ticket")

        Label(self.frameBusca, text="Seleciona a opção de Busca: ", bg="#d9e1e8", font=("Arial", 9, "bold")).place(relx=0.02, rely=0.1)
        self.entryBuscaOpcoes = Entry(self.frameBusca, font=("Arial", 10))
        self.entryBuscaOpcoes.place(relx=0.25, rely=0.30, width=200)

        Button(self.frameBusca, text="BUSCAR", bg="#6c8e9e", fg="white", font=("Arial", 8, "bold"), 
               command=self.buscarPorOpcao).place(relx=0.06, rely=0.55, width=300, height=25)
        
        Button(self.frameBusca, text="PESQUISAR TODAS", bg="#507080", fg="white", font=("Arial", 9, "bold"), 
               command=self.buscarTodas).place(relx=0.55, rely=0.25, width=120, height=40)
    
        Button(self.frameBusca, text="LIMPAR BUSCA", bg="#d65a5a", fg="white", font=("Arial", 9, "bold"), 
               command=self.limparPesquisa).place(relx=0.75, rely=0.25, width=120, height=40)
        
        Button(self.frameBusca, text="DELETAR TRIAGEM", bg="#760707", fg="white", font=("Arial", 9, "bold"), 
               command=self.deletarTriagem).place(relx=0.65, rely=0.65, width=120, height=40)
        
        self.comboOpcoes.bind("<<ComboboxSelected>>", self.itemSelecionado)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 10))
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        self.frameResultados = Frame(self.frame3, bg="#f0f2f5")
        self.frameResultados.place(relx=0.02, rely=0.20, relwidth=0.96, relheight=0.80)
        
        self.lblInstrucao = Label(self.frameResultados, text="", 
                                  bg="#f0f2f5", fg="#888", font=("Arial", 12))
        self.lblInstrucao.place(relx=0.5, rely=0.4, anchor=CENTER)


    def deletarTriagem(self):
        ticket = self.entryBuscaOpcoes.get().strip()
        if not ticket:
            self.mostrarAviso("Informe o Ticket para deletar.")
            return
        
        if messagebox.askyesno("Atenção","Deseja realmente Deletar?") == False:
                return
        else:
            db.deletarTriagem(ticket)
            self.limparPesquisa()
            self.mostrarAviso("Triagem do Ticket deletado.")

    def buscarPorOpcao(self):
        coluna = self.comboOpcoes.get().strip()
        if self.entryBuscaOpcoes.winfo_exists() == 0:
            valor = self.comboPesquisa.get().strip()
            if valor == "Sim":
                valor= '1'
            else:
                valor= '0'
        else:
            valor = self.entryBuscaOpcoes.get().strip()
        
        if not valor: return
        
        colunaMap = {
            "Data": "data",
            "Ticket": "ticket",
            "Técnico": "tecnico",
            "Analista Responsável": "analistaResponsavel",
            "Equipamento": "equipamento",
            "Cliente": "cliente",
            "N° Série": "NSerie",
            "Peça/Equipamento Funcional":"pecaEquipamentoFuncional"
        }
        
        colunaDB = colunaMap.get(coluna)
        if not colunaDB:
            self.mostrarAviso("Opção de busca inválida.")
            return
        
        lista = db.pesquisaTriagemOpcaoBusca(colunaDB, valor)
        self.processarListaResultados(lista)

    def buscarTodas(self):
        lista = db.pesquisarTodasTriagens()
        self.processarListaResultados(lista)
        if self.entryBuscaOpcoes.winfo_exists() == 0:
            self.comboOpcoes.set('Ticket')
            self.entryBuscaOpcoes = Entry(self.frameBusca, font=("Arial", 10))
            self.entryBuscaOpcoes.place(relx=0.25, rely=0.30, width=200)
            self.entryBuscaOpcoes.delete(0, END)
            self.entryBuscaOpcoes.delete(0, END)
        else:
            self.entryBuscaOpcoes.delete(0, END)
            self.entryBuscaOpcoes.delete(0, END)
            
    def voltarBusca(self):
        self.comboOpcoes.config(state='normal')
        if self.entryBuscaOpcoes.winfo_exists() == 0:
            self.comboPesquisa.config(state='normal')
        else:
            self.entryBuscaOpcoes.config(state='normal')
        valor = " "
        coluna = self.comboOpcoes.get().strip()
        if self.entryBuscaOpcoes.winfo_exists() == 0:
            valor = self.comboPesquisa.get().strip()
            if valor == "Sim":
                valor= '1'
            else:
                valor= '0'
        else:
            valor = self.entryBuscaOpcoes.get().strip()    
        
        colunaMap = {
            "Data": "data",
            "Ticket": "ticket",
            "Técnico": "tecnico",
            "Analista Responsável": "analistaResponsavel",
            "Equipamento": "equipamento",
            "Cliente": "cliente",
            "N° Série": "NSerie",
            "Peça/Equipamento Funcional":"pecaEquipamentoFuncional"
        }
        colunaDB = colunaMap.get(coluna)

        if not valor :
            self.buscarTodas()
        else:
            lista = db.pesquisaTriagemOpcaoBusca(colunaDB, valor)
            self.processarListaResultados(lista)

    def limparPesquisa(self):
        if self.entryBuscaOpcoes.winfo_exists() == 0:
            self.comboOpcoes.set('Ticket')
            self.entryBuscaOpcoes = Entry(self.frameBusca, font=("Arial", 10))
            self.entryBuscaOpcoes.place(relx=0.25, rely=0.30, width=200)
            self.entryBuscaOpcoes.delete(0, END)
            self.entryBuscaOpcoes.delete(0, END)
        else:
            self.entryBuscaOpcoes.delete(0, END)
            self.entryBuscaOpcoes.delete(0, END)

        for widget in self.frameResultados.winfo_children():
            widget.destroy()

    def mostrarAviso(self, msg):
        for widget in self.frameResultados.winfo_children(): widget.destroy()
        Label(self.frameResultados, text=msg, bg="#f0f2f5", fg="red", font=("Arial", 14)).place(relx=0.5, rely=0.4, anchor=CENTER)

    def processarListaResultados(self, lista):
        if not lista:
            self.mostrarAviso("Nenhum registro encontrado.")
            return
        self.exibirTabela(lista)

    def exibirTabela(self, listaDados):
        for widget in self.frameResultados.winfo_children(): widget.destroy()

        colunas = ("Data", "Ticket", "Técnico", "Equipamento", "PecaEquipamento")
        self.tree = ttk.Treeview(self.frameResultados, columns=colunas, show='headings')
        
        self.tree.heading("Data", text="Data")
        self.tree.heading("Ticket", text="Ticket")
        self.tree.heading("Técnico", text="Técnico")
        self.tree.heading("Equipamento", text="Equipamento")
        self.tree.heading("PecaEquipamento", text="Troca")

        self.tree.column("Data", minwidth=80, width=90, anchor="center")
        self.tree.column("Ticket", minwidth=80, width=90, anchor="center")
        self.tree.column("Técnico", minwidth=100, width=150, anchor="center")
        self.tree.column("Equipamento", minwidth=100, width=150, anchor="center")
        self.tree.column("PecaEquipamento", minwidth=150, width=150, anchor="center")

        scroolLista = Scrollbar(self.frameResultados, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=scroolLista.set)
        scroolLista.pack(side=RIGHT, fill=Y)
        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=5)

        for item in listaDados:
            self.tree.insert("", END, values=(item[1], item[3], item[4], item[7], wrap(item[10])))

        self.tree.bind("<Double-1>", self.aoClicarNaTabela)

    def aoClicarNaTabela(self, event):
        itemSelecionado = self.tree.selection()
        if not itemSelecionado: return
        
        valores = self.tree.item(itemSelecionado, "values")
        ticketSelecionado = valores[1]
        
        lista = db.pesquisarTriagem(ticketSelecionado)
        if lista:
            self.exibirDashboard(lista[0])

    def exibirDashboard(self, dados):
        for widget in self.frameResultados.winfo_children(): widget.destroy()

        Button(self.frameResultados, text="< Voltar para Lista", bg="#e0e0e0", relief=FLAT, 
               command=self.voltarBusca).place(relx=0.0, rely=0.0, height=25, width=120)
        
        Button(self.frameResultados, text="Expandir Triagem >", bg="#e0e0e0", relief=FLAT, 
                command= lambda:[janelaTriagem.Janela(ticket=dados[3])]).place(relx=0.83, rely=0.0, height=25, width=120)

        dadoTicket = dados[3]
        dadoTecnico = dados[4]
        dadoEquip = dados[7]
        dadoSerie = dados[9]
        dadoTroca = dados[10]
        dadoDefeitoAlegado = dados[11]
        dadoAnalise = dados[15]
        dadoConclusao = dados[16]

        frameTopo = Frame(self.frameResultados, bg="white", bd=1, relief=SOLID)
        frameTopo.place(relx=0.030, rely=0.05, relwidth=0.95, height=90)
        
        def itemTopo(frame, txtPrimeiro, dadoBuscado, x):
            Label(frame, text=txtPrimeiro, font=("Arial", 8, "bold"), fg="grey", bg="white").place(relx=x, rely=0.15, anchor=CENTER)
            Label(frame, text=dadoBuscado, font=("Arial", 12, "bold"), fg="#333", bg="white",wraplength=110).place(relx=x, rely=0.5, anchor=CENTER)

        itemTopo(frameTopo, "TICKET", str(dadoTicket), 0.10)
        itemTopo(frameTopo, "EQUIPAMENTO", str(dadoEquip), 0.35)
        itemTopo(frameTopo, "N° SÉRIE", str(dadoSerie), 0.60)
        itemTopo(frameTopo, "TÉCNICO", str(dadoTecnico), 0.85)

        pecaTrocada = Frame(self.frameResultados, bg="#e8f6f3")
        pecaTrocada.place(relx=0.030, rely=0.20, relwidth=0.95, height=35)
        Label(pecaTrocada, text="PEÇA TROCADA:", font=("Arial", 9, "bold"), fg="#0e6655", bg="#e8f6f3").place(relx=0.25, rely=0.2, anchor=CENTER)
        Label(pecaTrocada, text=dadoTroca, font=("Arial", 10), bg="#e8f6f3").place(relx=0.60, rely=0.2, anchor=CENTER)
        
        yPosicao = 0.27

        self.comboOpcoes.config(state='disable')
        if self.entryBuscaOpcoes.winfo_exists() == 0:
            self.comboPesquisa.config(state='disable')
        else:
            self.entryBuscaOpcoes.config(state='readonly')
            
        def blocoTexto(titulo, txt, cor, y):

            Frame(self.frameResultados, bg=cor).place(relx=0, rely=y, relwidth=0.01, relheight=0.18)
            Label(self.frameResultados, text=titulo, font=("Arial", 10, "bold"), fg="#555", bg="#f0f2f5").place(relx=0.02, rely=y)

            t = Text(self.frameResultados, height=5, bg="white", wrap=WORD, font=("Arial", 10), relief=FLAT)
            t.insert("1.0", str(txt))
            t.configure(state="disabled") 
            t.place(relx=0.02, rely=y+0.04, relwidth=0.96, relheight=0.13)
            return y + 0.19

        yPosicao = blocoTexto("DEFEITO ALEGADO", dadoDefeitoAlegado, "#e67e22", yPosicao)
        yPosicao = blocoTexto("ANÁLISE", dadoAnalise, "#3498db", yPosicao)
        yPosicao = blocoTexto("CONCLUSÃO", dadoConclusao, "#27ae60", yPosicao)

    def ComponentesFrame2(self):
        corFundo = "#f0f2f5"
        corBg = "#ffffff"
        corLbl = "#444444"
        corBtSalvar = "#2980b9"
        corBtLimpar = "#95a5a6"
        
        fonteLbl = ("Segoe UI", 9, "bold")
        fonteEntry = ("Segoe UI", 10)

        self.frame2.configure(bg=corFundo)

        Label(self.frame2, text="TRIAGEM TÉCNICA", bg=corFundo, fg="#2c3e50", 
              font=("Segoe UI", 14, "bold")).place(relx=0.03, rely=0.01)

        Label(self.frame2, text="Data", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.07)
        self.entryData = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1, justify="center")
        self.entryData.place(relx=0.03, rely=0.10, relwidth=0.12, height=28)
        self.entryData.insert(0, dataAtual.strftime('%d/%m/%Y'))

        Label(self.frame2, text="Nota Fiscal (NF)", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.17, rely=0.07)
        self.entryNF = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryNF.place(relx=0.17, rely=0.10, relwidth=0.12, height=28)

        Label(self.frame2, text="Nº Ticket", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.31, rely=0.07)
        self.entryTicket = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTicket.place(relx=0.31, rely=0.10, relwidth=0.15, height=28)

        Label(self.frame2, text="Região", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.48, rely=0.07)
        self.entryRegiao = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryRegiao.place(relx=0.48, rely=0.10, relwidth=0.20, height=28)

        Label(self.frame2, text="Técnico Responsável", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.15)
        self.entryTecnico = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTecnico.place(relx=0.03, rely=0.18, relwidth=0.30, height=28)

        Label(self.frame2, text="Analista Responsável", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.35, rely=0.15)
        self.entryAnalista = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryAnalista.place(relx=0.35, rely=0.18, relwidth=0.33, height=28)

        Label(self.frame2, text="Cliente", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.70, rely=0.15)
        self.entryCliente = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryCliente.place(relx=0.70, rely=0.18, relwidth=0.20, height=28)

        self.ckbox = Checkbutton(self.frame2, text="Peça/Equipamento Funcional", bg=corFundo, fg=corLbl, font=fonteLbl)
        self.ckbox.place(relx=0.70, rely=0.26)
        self.ckboxVar = IntVar()
        self.ckbox.configure(variable=self.ckboxVar)

        Label(self.frame2, text="Modelo do Equipamento", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.23)
        self.entryEquipamento = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryEquipamento.place(relx=0.03, rely=0.26, relwidth=0.45, height=28)

        Label(self.frame2, text="N° de Série (SN)", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.50, rely=0.23)
        self.entryNSerie = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryNSerie.place(relx=0.50, rely=0.26, relwidth=0.18, height=28)

        Label(self.frame2, text="Peça/Equipamento Trocado", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.31)
        self.entryTroca = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTroca.place(relx=0.03, rely=0.34, relwidth=0.65, height=28)

        Label(self.frame2, text="Defeito Alegado", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.39)
        self.textDefeito = Text(self.frame2, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1, wrap='word')
        self.textDefeito.place(relx=0.03, rely=0.42, relwidth=0.94, height=50)

        Label(self.frame2, text="Constatação do Técnico", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.50)
        self.textConstatacaoTec = Text(self.frame2, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1, wrap='word')
        self.textConstatacaoTec.place(relx=0.03, rely=0.53, relwidth=0.94, height=50)

        Label(self.frame2, text="Defeito Constatado (Resumo)", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.61)
        self.entryDefeitoConsta = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryDefeitoConsta.place(relx=0.03, rely=0.64, relwidth=0.45, height=28)

        Label(self.frame2, text="Testes Realizados", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.50, rely=0.61)
        self.entryTeste = Entry(self.frame2, bg=corBg, font=fonteEntry, relief="solid", bd=1)
        self.entryTeste.place(relx=0.50, rely=0.64, relwidth=0.47, height=28)

        Label(self.frame2, text="Análise do Equipamento/Peça", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.69)
        self.textAnalise = Text(self.frame2, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1, wrap="word")
        self.textAnalise.place(relx=0.03, rely=0.72, relwidth=0.94, height=50)

        Label(self.frame2, text="Conclusão Final", bg=corFundo, fg=corLbl, font=fonteLbl).place(relx=0.03, rely=0.80)
        self.textConclusao = Text(self.frame2, bg=corBg, font=("Segoe UI", 9), relief="solid", bd=1, wrap='word')
        self.textConclusao.place(relx=0.03, rely=0.83, relwidth=0.94, height=50)

        Button(self.frame2, text="SALVAR", bg=corBtSalvar, fg="white", 
                            font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2",
                            command=lambda: [self.getDados(dados),
                                ]).place(relx=0.72, rely=0.015, width=180, height=35)

        Button(self.frame2, text="LIMPAR", bg=corBtLimpar, fg="white",
                               font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2",
                               command=lambda: [
                                   self.limparCampos(self.frame2),
                                   self.entryData.insert(0,dataAtual.strftime('%d/%m/%Y')),
                                   self.entryNF.focus_set()       
                               ]).place(relx=0.72, rely=0.075, width=180, height=30)

    def getDados(self, dados):

        if self.entryTicket.get().strip() == "" or self.entryTicket.get().strip() == "-":
            messagebox.showwarning("Atenção", "O campo 'Ticket' é obrigatório.") 
        else: 
            if messagebox.askyesno("Atenção","Deseja realmente salvar?") == False:
                return
            else:
                dados["data"] = self.entryData.get()
                dados["NF"] = self.entryNF.get()
                dados["ticket"] = self.entryTicket.get()
                dados["tecnico"] = self.entryTecnico.get()
                dados["analistaResponsavel"] = self.entryAnalista.get()
                dados["regiao"] = self.entryRegiao.get()
                dados["cliente"] = self.entryCliente.get()
                dados["equipamento"] = self.entryEquipamento.get()
                dados["NSerie"] = self.entryNSerie.get()
                dados["pecaEquipamentoTrocado"] = self.entryTroca.get()
                dados["defeitoAlegado"] = self.textDefeito.get("1.0", END).strip()
                dados["constatacaoTecnico"] = self.textConstatacaoTec.get("1.0", END).strip()
                dados["defeitoConstatado"] = self.entryDefeitoConsta.get()
                dados["testesRealizados"] = self.entryTeste.get()
                dados["analise"] = self.textAnalise.get("1.0", END).strip()
                dados["conclusao"] = self.textConclusao.get("1.0", END).strip()
                dados["pecaEquipamentoFuncional"] = self.ckboxVar.get()

                self.setDadosDB(dados)
                
                preencherTriagem("TRIAGEM.docx",
                                    f"{dados.get('cliente','')}_{dados.get('equipamento','')}_{dados.get('ticket','')}_{(dados.get('pecaEquipamentoTrocado',''))}.docx",
                                    dados)
                
    def setDadosDB(self, Dados):
        db.inserirTriagem(dados["data"], dados["NF"], dados["ticket"], dados["tecnico"],
                                   dados["analistaResponsavel"], dados["regiao"], dados["equipamento"], dados["cliente"],
                                   dados["NSerie"], dados["pecaEquipamentoTrocado"], dados["defeitoAlegado"],
                                   dados["constatacaoTecnico"], dados["defeitoConstatado"],
                                   dados["testesRealizados"], dados["analise"], dados["conclusao"], dados["pecaEquipamentoFuncional"])
        
    def mostrarFrame(self, frameDesejado):
        frameDesejado.tkraise()

    def botoesLaterais(self):
        corBt = "#34495e"
        corTxt = "#ecf0f1"
        corHover = "#2980b9"
    
        Button(self.frame1, text='TRIAGEM', 
                            command=lambda: self.mostrarFrame(self.frame2), 
                            bg=corBt, fg=corTxt, wraplength=80,
                            activebackground=corHover, activeforeground="white",
                            font=("Segoe UI", 9, "bold"), relief="flat", bd=0, cursor="hand2").place(relx=0.05, rely=0.10, relheight=0.06, relwidth=0.9)

        Button(self.frame1, text='PESQUISAR', 
                            command=lambda: self.mostrarFrame(self.frame3),
                            bg=corBt, fg=corTxt,wraplength=80,
                            activebackground=corHover, activeforeground="white",
                            font=("Segoe UI", 9, "bold"), relief="flat", bd=0, cursor="hand2").place(relx=0.05, rely=0.18, relheight=0.06, relwidth=0.9)

        Button(self.frame1, text='DASHBOARD', 
                            command=lambda: [self.ComponentesFrameDash(), self.mostrarFrame(self.frameDash)],
                            bg=corBt, fg=corTxt, wraplength=80,
                            activebackground=corHover, activeforeground="white",
                            font=("Segoe UI", 8, "bold"), relief="flat", bd=0, cursor="hand2").place(relx=0.05, rely=0.26, relheight=0.06, relwidth=0.9)
                   
    def limparCampos(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, END)
            elif isinstance(widget, Text):
                widget.delete("1.0", END)
            elif isinstance(widget, ttk.Combobox):
                widget.set(0)
        self.ckboxVar.set(0)

    def itemSelecionado(self, event):
        itemSelecionado = self.comboOpcoes.get()
        if itemSelecionado == 'Peça/Equipamento Funcional':
            self.entryBuscaOpcoes.destroy()
            self.comboPesquisa = ttk.Combobox(self.frameBusca, values=self.opcoesPesquisa, state="readonly")
            self.comboPesquisa.place(relx=0.25, rely=0.30, width=200)
        else:
            self.entryBuscaOpcoes = Entry(self.frameBusca, font=("Arial", 10))
            self.entryBuscaOpcoes.place(relx=0.25, rely=0.30, width=200)
            self.comboPesquisa.destroy()


if __name__ == "__main__":
    Application()