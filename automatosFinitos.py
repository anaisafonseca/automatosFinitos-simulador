# 11811ECP012 - Anaísa Forti da Fonseca

n = input()                          # número de estados
sigma = input()                      # conjunto de símbolos terminais
F = input()                          # conjunto de estados de aceitação
nTransicoes = input()                # número de transições do autômato

t = []                               # lista de transições
while len(t) < int(nTransicoes):     # recebendo todas as transições
    transicao = input()
    transicao = transicao.split(' ')
    t.append(transicao)

c = input()                          # número de cadeias que serão avaliadas
cadeias = []                         # lista de cadeias a serem avaliadas
while len(cadeias) < int(c):         # recebendo todas as cadeias
    cad = input()
    cad = list(cad)
    cadeias.append(cad)

sigma = sigma.split(' ')             # separando os símbolos terminais
nSimbolos = sigma[0]                 # quantidade de símbolos terminais
simbolos = sigma[1:]                 # lista de símbolos terminais

F = F.split(' ')                     # separando os estados de aceitação
nEstados = F[0]                      # número de estados de aceitação
estados = F[1:]                      # lista de estados de aceitação

aceitacao = list(map(int,estados))   # transformando estados de aceitação em inteiros


# função recursiva para percorrer cada cadeia de entrada
# se parar em estado de aceitação: true, outro estado: false
def percorreCadeia(cadeiaAtual, estadoAtual):

    # analisa a cadeia vazia
    if(cadeiaAtual == ['-']):
        if(estadoAtual in aceitacao):
            return True
        return False

    # verifica se o estado final da cadeia é um de aceitação
    if(cadeiaAtual == []):
        if(estadoAtual in aceitacao):
            return True
        return False

    # compara o primeiro símbolo da cadeia com todas as transições possíveis
    simboloAtual = cadeiaAtual[0]
    for i in range(len(t)):
        transicaoAtual = t[i]
        estadoInicialT = int(transicaoAtual[0])
        simboloT = transicaoAtual[1]
        if((estadoInicialT == estadoAtual) and (simboloT == simboloAtual)):
            # muda o estado atual
            estado = int(transicaoAtual[2])            
            # passa para o próximo símbolo da cadeia
            cadeiaNova = cadeiaAtual[1:]               
            # recursividade (com próximo símbolo e novo estado atual)
            if(percorreCadeia(cadeiaNova,estado)):
                return True
    return False


# aceitação ou rejeição de cada cadeia de entrada
for j in range(int(c)):
    cadeiaAtual = cadeias[j]
    # percorre cada cadeia (o estado 0 é sempre o estado inicial)
    if(percorreCadeia(cadeiaAtual,0)):
        print("aceita")
    else:
        print("rejeita")