#ex 1 (justificar)
def limpa_texto(texto):

    """
    Esta função limpa a string (remoção de carateres brancos).
    """
    texto_limpo = texto.strip()
    texto_separado = texto_limpo.split()
    texto_junto = ' '.join(texto_separado)
    return texto_junto

def corta_texto(texto, numero):

    """
    Esta função recebe uma string de texto limpo e um numero 
    e retorna 2 tuplos. O primeiro contem as palavres completas 
    (incluindo os espaços)desde o início até ao comprimento do 
    número (largura) e o segundo contem o resto da string.
    """
    str1= ""
    str2= ""
  
    if len(texto) <= numero:
        str1 = texto
        str2 = ""
        return(str1, str2)
    
    numero = numero - 1 #o indice começa a partir de 0
    if texto[numero] == " ":
        str1= texto[:numero]
        str2= texto[numero + 1:]
        return (str1, str2)
    
    elif texto[numero] != " ":
        while texto[numero] != " ": #processo até texto[numero]== " "
            str1 = texto[:numero -1]
            str2 = texto[numero:]
            numero = numero -1
        return (str1, str2)

def insere_espacos(texto, largura):

    """
    Esta função recebe uma string e um um inteiro(largura),
    caso a string tenha 2 ou mais palavras devolve uma string
    com comprimento = largura, adicionando espaços igualmente 
    entes as palavras.
    """

    if len(texto.split()) == 1: #caso para uma palavra
        str_final = texto.split()
        while len(str_final) != (largura - len(texto) + 1):
            str_final.append(" ") 
        return " ".join(str_final) 

    if len(texto.split()) != 1:
        if len(texto) == largura:
            return texto
        str_final = texto.split()
        while len((" ".join(str_final))) < largura:
            for i in range(len(str_final)-1):
                str_final.insert(i+1, " ")#add " " à lista das palavras
                x = str_final[i] + str_final[i + 1]#junto o 1º termo da lista + o 2º
                str_final.pop(i) #retiro o " " da lista de palavras
                str_final.pop(i) #retiro a palavra
                str_final.insert(i, x) #adiciono a palavra junta com o espaço na lista de palavras
                if (len((" ".join(str_final)))) == largura:
                    return " ".join(str_final)

def justifica_texto(texto, largura):

    """
    Esta função recebe uma string(texto) e um int(largura),
    e devolve um tuplo de strings justificadas(comprimento
    de cada string = largura).
    """
    if type(texto)!= str or type(largura) != int:
        raise ValueError ("justifica_texto: argumentos invalidos")
    if len(texto) == 0:
        raise ValueError ("justifica_texto: argumentos invalidos")
    if largura <= 0:
        raise ValueError ("justifica_texto: argumentos invalidos")
    
    texto = limpa_texto(texto)

    for word in texto.split():
        if len(word) > largura:
            raise ValueError ("justifica_texto: argumentos invalidos")

    t = corta_texto(texto, largura)
    
    if t[1] == "":           
        espacos = largura - len(t[0])
        str_espacos = (" " * espacos)
        frase_pequena = t[0] + str_espacos
        return (frase_pequena,)
    
    if len(t[1]) <= largura:
        x = insere_espacos(t[0], largura) 
        y = insere_espacos(t[1], largura)
        return tuple(x, y)
    
    i = 1  
    while len(t[i]) > largura:
        t2 = corta_texto(t[i], largura)
        t = t + t2 #ajustar os tuplos à largura pretendida
        i += 2
        
    Lista_final = []
    for e in range(0,len(t)-1,2):#juntar os tuplos com a largura certa
        Lista_final += (insere_espacos(t[e], largura),)#justificá-los
              
    espacos_extra = largura - len(t[-1])
    laststr = t[-1] + (" " * espacos_extra)
    Lista_final.append(laststr)#caso extra para a laststring
    
    return tuple(Lista_final)
#ex 2 (método de Hondt)
def calcula_quocientes(votos, dep):

    """
    Esta funcao recebe um dicionario com os votos num circulo 
    e um inteiro positivo representando o numero de deputados; e devolve
    o dicionario com as mesmas chaves do dicionario argumento (partidos)
    contendo a lista (comprimento = n de deputados) com os quocientes
    calculados com o metodo de Hondt ordenados em ordem decrescente.
    """
    new_votos = {}
    new_votos = votos.copy()
    for key in votos:
        lista = []
        for i in range(1,dep + 1):
            new_value = (votos[key] / i)
            lista += [new_value]
        new_votos[key] = lista #associar os quocientes ao partido
            
    return new_votos

def atribui_mandatos(votos,dep):

    """
    Esta funcao recebe um dicionario(votos) e um inteiro(deputados)
    e devolve a lista(len = dep) ordenada com os partidos(str) que
    obtiveram cada mandato. A primeira posição da lista corresponde
    ao partido que obteve o primeiro deputado, etc.
    """
    
    dict_quocientes = calcula_quocientes(votos, dep)
    key_list= list (dict_quocientes.keys())
    votos_val=list (votos.values())
    val_list = []
    
    for key in dict_quocientes:
        val_list += (dict_quocientes[key])#juntar todos os valores dos
                                          #partidos numa lista
    lista_quocientes = val_list.copy()    
    lista_quocientes.sort()
    for el in range(len(lista_quocientes)-1,-1,-1):
        if lista_quocientes[el] == lista_quocientes[el -1]:
            lista_quocientes.pop(el)#retirar os valores iguais da lista
    
    lista_quocientes.sort(reverse = True)#do maior para o menor
    lista_quocientes = lista_quocientes[0:dep]#tamanho da lista 
                                              #igual ao nº de dep
    lista_final = []
    i = 0
    
    while i < dep:
        if val_list.count(lista_quocientes[i]) == 1:
            for key in dict_quocientes:#caso para quando o valor do quociente é único
                if lista_quocientes[i] in dict_quocientes[key]:
                   lista_final.append(key)
            i += 1
            
        else:#caso para quando o valor do quociente se repete
            votos_val.sort()
            for el in votos_val:               
                for key in votos:
                    if el == votos[key]:
                        lowest_key = key#partido com menos votos
                        if lista_quocientes[i] in dict_quocientes[lowest_key]:
                            lista_final.append(key)
                            i+=1
                        if len(lista_final) == dep:
                            return lista_final
                         
    return lista_final

def obtem_partidos(circulos):

    """
    Esta função recebe um dicionário contendo
    vários circulos eleitorais e devolve uma 
    lista com todos os partidos que participaram,
    por ordem alfabética.
    """
    lista_final = []

    for key in circulos:#avançando no dicionário
        for i in circulos[key]:
            if isinstance(circulos[key][i], dict):
            #filtrar para vermos apenas os "votos", que são do tipo dicionário, ao contrário dos "deputados"
                for partido in circulos[key][i]:            
                    if partido not in lista_final:
                        lista_final.append(partido)

    lista_final.sort()     
    return lista_final

def obtem_resultado_eleicoes(circulos):

    """
    Esta função recebe um dicionário contendo vários circulos eleitorais
    e devolve a lista com os resultados da eleições(tamanho = nº d partidos).
    Cada elemento da lista é um tuplo, que contém o nome do partido, o num
    de deputados e o num de votos. A lista está ordenada de maneira decrescente.
    """

    if type(circulos) != dict:
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    
    if len(circulos) == 0:
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")

    for key in circulos:
        if type(key) != str:
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        verifica_votos_totais =0
        for i in circulos[key]:
            if "votos" not in circulos[key]:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
            if i == "votos":
                if type(circulos[key][i]) != dict:
                    raise ValueError("obtem_resultado_eleicoes: argumento invalido")
                for el in circulos[key][i]:
                    if type(circulos[key][i][el]) != int or circulos[key][i][el] < 0:
                        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
                    verifica_votos_totais += circulos[key][i][el]
                    if type(el) != str:
                        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
                if verifica_votos_totais == 0:
                    raise ValueError("obtem_resultado_eleicoes: argumento invalido")
            if "deputados" not in circulos[key]:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
            if i == "deputados":
                if type(circulos[key][i]) != int or circulos[key][i] == 0:
                    raise ValueError("obtem_resultado_eleicoes: argumento invalido")

    lista_obtem = obtem_partidos(circulos)
    votos = {}
    dep = 0
    l_partidos = []
    l_final = []
    t_resumido = ()
    l_final_tuplos = []
    
    for key in circulos:
        for i in circulos[key]:
            if isinstance(circulos[key][i], dict):
            #"separar" os dicionarios para obter as variáveis corretas para usar a função atribui_mandatos                  
                votos = circulos[key][i]                                         
            else:
                dep = circulos[key][i]
                
        l_partidos = atribui_mandatos(votos,dep)

        for partido in lista_obtem:
            if partido in l_partidos:#verificar se o partido estava na lista de partidos com deputados                                            
                count = 0 
                for el in l_partidos:
                    if partido == el:
                        count +=1                                        
            
                x = votos[partido]
                l_final += (partido, count, x)#lista com tudo sobre cada partido para encontrar 
                                              #o nº de deputados total de cada partido   
    for partido in lista_obtem:
        num_dep_partido = 0
        for dado in range(0,len(l_final),3):#andar de 3 em 3 uma vez que o partido aparecia de 3 em 3 posições na lista
            if partido == l_final[dado]:
                num_dep_partido += l_final[dado +1]

        num_votos_partido = 0                                            
        for key in circulos:
            for i in circulos[key]:
                if isinstance(circulos[key][i], dict):#calculos para obter o num votos total de cada partido
                    if partido in circulos[key][i]:
                        num_votos_partido += circulos[key][i][partido]
        
        t_resumido = (partido, num_dep_partido,num_votos_partido)#criando um tuplo com a informação final sobre cada partido
        l_final_tuplos += (t_resumido,)
    
    l_final_tuplos.sort(reverse = True, key = lambda x:(x[1], x[2]) )#ordenar a lista pela ordem pedida no enunciado
        
    return  l_final_tuplos

#ex 3 (método de jacobi)
def produto_interno(u,v):

    """
    Produto interno entre os 2 vetores iniciais (tuplos)
    retornando um real.
    """
    produto = 0
    for i in range(len(u)):
        produto += u[i] * v[i]                        
    return float(produto)

def verifica_convergencia(m,c,x,r): 
    
    """
    Recebe 3 tuplos e um numero real, representando
    a matriz, as constantes, a solução e a precisão, 
    respetivamente. Esta função retorna True se o valor 
    absoluto do erro de todas as equações for inferior à precisão.
    """                                                
    for linha in range(len(m)):
        if abs(produto_interno(m[linha],x)-c[linha]) > r:
            return False
    return True

def retira_zeros_diagonal(m,c):

    """
    Recebemos uma matriz com o seu vetor de constantes(tuplo de tuplos)
    e ocorre um processo de reordenação de linhas, de forma a não
    existirem zeros na diagonal da matriz, returnando a tal matriz
    mais o vetor de constantes, sem zeros nas diagonais.
    """
    m = list(m)
    c = list(c)
    for i in range(len(m)):
        count = 0                                                              
        while count < len(m):                                                  
            if m[i][i] == 0 and m[count][i] != 0 and m[i][count] != 0:
            #verificar se estamos perante a condição correta para fazer a troca de linha
                m[i] , m[count] = m[count], m[i]                               
                c[i] , c[count] = c[count], c[i]                               
                break 
            else: 
                count+= 1
    return (tuple(m), tuple(c))
    
     
def eh_diagonal_dominante(m):
    
    """
    Recebe um tuplo com a matriz returnando True se ela
    for diagonal dominante.
    """
    soma_diagonal = 0
    for i in range(len(m)): 
        soma_diagonal +=abs(m[i][i])#soma do valor da diagonal da matriz
    
    for i in range(len(m)):
        soma_linha = 0
        for el in range(len(m[i])): #ciclo for que faz a soma dos elementos de cada linha
            soma_linha += abs(m[i][el])             
        if (soma_linha) > (soma_diagonal):#verificação para confirmar se é uma matriz diagonal dominante
            return False
   
    return True

def resolve_sistema(m,c,r):

    """
    Esta função recebe um tuplo com a matriz, um tuplo com o vetor das constantes 
    e o valor da precisão pretendido. Recorrendo ao método de Jacobi, retorna um
    tuplo com a solução do sistema.
    """

    if not isinstance(m, tuple) or not isinstance(c,tuple) or not isinstance(r, (float)):  
        raise ValueError ("resolve_sistema: argumentos invalidos")
    
    for tuplo in range(len(m)):
        if type(m[tuplo]) != tuple:
            raise ValueError ("resolve_sistema: argumentos invalidos")
        for el in range(len(m[tuplo])):
            if not isinstance(m[tuplo][el], (int, float)):
                raise ValueError ("resolve_sistema: argumentos invalidos") 
    
    for i in range(len(m)-1):
        if len(m[i]) != len(m[i +1]) or len(m) != len(m[i]):                             
            raise ValueError ("resolve_sistema: argumentos invalidos")
   
    if len(m) == 0:
        raise ValueError ("resolve_sistema: argumentos invalidos")
    
    for constante in c:
        if not isinstance(constante, (int, float)):
            raise ValueError ("resolve_sistema: argumentos invalidos")
    
    if len(m) != len (c):                                                                
        raise ValueError ("resolve_sistema: argumentos invalidos")
    
    if len(c) == 0:
        raise ValueError ("resolve_sistema: argumentos invalidos")
    if r < 0:
        raise ValueError ("resolve_sistema: argumentos invalidos")
    
    n_m,n_c = retira_zeros_diagonal(m,c)
    
    if not eh_diagonal_dominante(n_m):
        raise ValueError ("resolve_sistema: matriz nao diagonal dominante")
    
    x = ()
    for i in range(len(m)):
        x += (0,)#tuplo incial das soluções
    while not verifica_convergencia(n_m,n_c,x,r):
        x_extra = ()
        for linha in range(len(x)):
             x_count = x[linha] + (n_c[linha] - produto_interno(n_m[linha],x))/n_m[linha][linha]
             x_extra += (x_count,)#juntando os resultados
        x = x_extra#no final do ciclo atualiza a solução
            
    return x




    




        

