import sqlite3

con = sqlite3.connect('triagem.db')
cur = con.cursor()

def tabelaTriagem():
    cur.execute(''' CREATE TABLE IF NOT EXISTS triagem (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data Date NOT NULL,
        NF INTEGER,
                ticket TEXT,
                tecnico TEXT,
                analistaResponsavel TEXT,
                regiao TEXT,
                equipamento TEXT,
                cliente TEXT,
                NSerie TEXT,    
                pecaEquipamentoTrocado TEXT,
                defeitoAlegado TEXT,
                constatacaoTecnico TEXT,
                defeitoConstatado TEXT,
                testesRealizados TEXT,
                analise TEXT,
                conclusao TEXT
    )''')

def inserirTriagem(data, NF, ticket, tecnico, analistaResponsavel, regiao, equipamento, cliente,NSerie, pecaEquipamentoTrocado, defeitoAlegado, constatacaoTecnico, defeitoConstatado, testesRealizados, analise, conclusao):
    cur.execute(''' INSERT INTO triagem (
    data, NF, ticket, tecnico, analistaResponsavel, regiao, equipamento, cliente, NSerie, pecaEquipamentoTrocado, defeitoAlegado, constatacaoTecnico, defeitoConstatado, testesRealizados, analise, conclusao
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ''', (
        data, NF, ticket, tecnico, analistaResponsavel, regiao, equipamento, cliente, NSerie, pecaEquipamentoTrocado, defeitoAlegado, constatacaoTecnico, defeitoConstatado, testesRealizados, analise, conclusao
        ))
    con.commit()

def pesquisarTriagem(ticket):
    cur.execute(''' SELECT * FROM triagem WHERE ticket = ? ''', (ticket,))
    return cur.fetchall()
    
def pesquisarTodasTriagens():
    cur.execute(''' SELECT * FROM triagem ''')
    return cur.fetchall()

def deletarTriagem(ticket):
    cur.execute(''' DELETE FROM triagem WHERE ticket = ? ''', (ticket,))
    con.commit()

def pesquisarTriagensTecnicos(tecnico):
    cur.execute(''' SELECT * FROM triagem WHERE tecnico = ? ''', (tecnico,))
    return cur.fetchall()
    
if __name__ == "__main__":
    tabelaTriagem()