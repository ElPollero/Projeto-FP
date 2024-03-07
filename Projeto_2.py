#TAD gerador
def cria_gerador(b,s):#construtor
    """
    A representação interna que escolhi para o TAD gerador foi o tipo 
    "dict", tendo o dicionário apenas 2 elementos. A primeira key, "bits"
    tem como valor o nº de bits (32 ou 64) e a segunda key, "seed" tem
    como valor o estado inicial.

    int x int -> gerador
    Recebe um inteiro (b) correspondente ao número de bits e um 
    inteiro(s) correspondente à seed e devolve o gerador correspondente.
    """
    if type(b) != int or type(s) != int:
        raise ValueError("cria_gerador: argumentos invalidos")
    if s <= 0:
        raise ValueError("cria_gerador: argumentos invalidos")
    if b != 32 and b !=64:
        raise ValueError("cria_gerador: argumentos invalidos")
    if b == 32 and s > 2**32:
         raise ValueError("cria_gerador: argumentos invalidos")
    if b == 64 and s > 2**64:
         raise ValueError("cria_gerador: argumentos invalidos")

    return {"bits":b, "seed":s}

def cria_copia_gerador(g):#construtor
    """
    gerador -> gerador
    Recebe um gerador e devolve uma nova cópia do gerador.
    """
    x = g.copy()
    return x

def obtem_estado(g):#seletor
    """
    gerador -> int
    Recebe um gerador e devolve a sua seed.
    """
    return g["seed"]

def define_estado(g,s):#modificador
    """
    gerador x int -> int
    Recebe um gerador(g) e um inteiro(s) e define o novo estado do 
    gerador g como s, devolvendo s.
    """
    g["seed"] = s
    
    return obtem_estado(g)

def atualiza_estado(g):#modificador
    """
    gerador -> int
    Recebe um gerador(g), atualiza o estado do mesmo de acordo com
    o algoritmo "xorshift" e devolve o novo estado.
    """
    s = g["seed"] 
    if g["bits"] == 32:
        s ^= ( s << 13 ) & 0xFFFFFFFF
        s ^= ( s >> 17 ) & 0xFFFFFFFF
        s ^= ( s << 5 ) & 0xFFFFFFFF
    elif g["bits"] == 64:
        s ^= ( s << 13 ) & 0xFFFFFFFFFFFFFFFF
        s ^= ( s >> 7 ) & 0xFFFFFFFFFFFFFFFF
        s ^= ( s << 17 ) & 0xFFFFFFFFFFFFFFFF
    
    define_estado(g,s)
    return g["seed"]

def eh_gerador(arg):#reconhecedor
    """
    universal -> booleano
    Recebe qualquer argumento e devolve "True" caso esse 
    argumento seja um TAD gerador e "False" caso contrário.
    """
    if type(arg) != dict or len(arg) != 2 or 'bits' not in arg or 'seed' not in arg:
        return False
    return True

def geradores_iguais(g1,g2):#teste
    """
    gerador x gerador -> booleano
    Recebe um gerador(g1) e um gerador(g2) e 
    devolve "True" se ambos forem iguais.
    """
    return g1["bits"] == g2["bits"] and g1["seed"] == g2["seed"]

def gerador_para_str(g):#transformador
    """
    gerador -> str
    Recebe um gerador e devolve a cadeira de caracteres que o representa.
    """
    return "xorshift" + str(g["bits"]) + "(s=" + str(g["seed"]) + ")"

def gera_numero_aleatorio(g,n):#alto nível
    """
    gerador x int -> int
    Recebe um gerador(g) e um inteiro(n), atualiza o estado de g 
    e devolve um número aleatório no intervalo [1, n]. Este número 
    é obtido a partir do novo estado de g (s), seguindo o algoritmo
    1 + ( s % n ).
    """
    atualiza_estado(g)
    return 1 + (obtem_estado(g) % n )

def gera_carater_aleatorio(g,c):#alto nível
    """
    gerador x str -> str
    Recebe um gerador(g) e uma string(c), atualiza o estado de g 
    e devolve um carater aleatório no intervalo entre "A" e o 
    carater maiúsculo "c". Este carater é obtido a partir do novo 
    estado de g seguindo um algoritmo específico.
    """
    atualiza_estado(g)
    l = (ord(c) - ord("A")) + 1 #distância entre "A" e o carater maiúsculo "c"
    return chr(65 + (obtem_estado(g) % l))

#TAD coordenada
def cria_coordenada(col, lin):#construtor
    """
    A representação interna que escolhi para o TAD coordenada foi o 
    tipo "tuple", tendo o tuplo apenas 2 elementos. O primeiro elemento
    é uma string correspondente à coluna do campo e o segundo elemento é
    um inteiro correspondente à linha do campo.

    str x int -> coordenada
    Recebe uma string(col) correspondente à coluna e um inteiro(lin)
    correspondente à linha, devolvendo a coordenada correspondente.
    """
    if type(col) != str or type(lin) != int:
        raise ValueError ("cria_coordenada: argumentos invalidos")
    if len(col) != 1:
        raise ValueError ("cria_coordenada: argumentos invalidos")
    if col < chr(65) or col > chr(90):
        raise ValueError ("cria_coordenada: argumentos invalidos")
    if not 1 <= lin <= 99:
        raise ValueError ("cria_coordenada: argumentos invalidos")
    return (col, lin)

def obtem_coluna(c):#seletor
    """
    coordenada -> str
    Recebe uma coordenada (c) e devolve a coluna(col) da mesma.
    """
    return c[0]

def obtem_linha(c):#seletor
    """
    coordenada -> int
    Recebe uma coordenada (c) e devolve a linha(lin) da mesma.
    """
    return c[1]

def eh_coordenada(arg):#reconhecedor
    """
    universal -> booleano
    Recebe qualquer argumento e devolve "True" caso esse 
    argumento seja uma TAD coordenada e "False" caso contrário.
    """
    if type(arg) != tuple or len(arg) != 2 or type(arg[0]) != str or type(arg[1]) != int or \
        len(arg[0]) != 1: 
        return False
    if arg[0] < chr(65) or arg[0] > chr(90) or arg[1] < 1 or arg[1] > 99:
        return False
    return True

def coordenadas_iguais(c1,c2):#teste
    """
    coordenada x coordenada -> booleano
    Recebe uma coordenada(c1) e uma coordenada(g2) 
    e devolve "True" se ambas forem iguais.
    """
    return c1[0] == c2[0] and c1[1] == c2[1]

def coordenada_para_str(c):#transformador
    """
    coordenada -> str
    Recebe uma coordenada(c) e devolve a cadeia de 
    carateres que a representa.
    """
    if c[1] < 10: #quando a linha é menor que 10
        return c[0] + "0" + str(c[1])
    else:
        return c[0] + str(c[1])

def str_para_coordenada(s):#transformador
    """
    str -> coordenada
    Recebe uma str(s) e devolve a 
    coordenada que a representa.
    """
    return cria_coordenada(s[0], int(s[1:]))

def obtem_coordenadas_vizinhas(c):#alto nível
    """
    coordenada -> tuplo
    Recebe uma coordenada(c) e devolve um tuplo com 
    as coordenadas vizinhas à coordenada c, começando
    pela coordenada diagonal acima-esquerda e seguindo
    no sentido horário.
    """
    tuplo_final = ()
    #verificar se cada coordenada vizinha de c se encontrava  
    #dentro dos limites do campo pela ordem pedida
    if chr(65) <= chr(ord(obtem_coluna(c)) - 1) <= chr(90) and 1 <= (obtem_linha(c)- 1) <= 99:
        tuplo_final+= (cria_coordenada(chr(ord(obtem_coluna(c)) - 1),obtem_linha(c)- 1),)

    if chr(65) <= obtem_coluna(c) <= chr(90) and 1 <= (obtem_linha(c)- 1) <= 99:
        tuplo_final+= (cria_coordenada(obtem_coluna(c),obtem_linha(c)- 1),)
    
    if chr(65) <= chr(ord(obtem_coluna(c)) + 1) <= chr(90) and 1 <= (obtem_linha(c)- 1) <= 99:
        tuplo_final+= (cria_coordenada(chr(ord(obtem_coluna(c)) + 1),obtem_linha(c)- 1),)
    
    if chr(65) <= chr(ord(obtem_coluna(c)) + 1) <= chr(90) and 1 <= obtem_linha(c) <= 99:
        tuplo_final+= (cria_coordenada(chr(ord(obtem_coluna(c)) + 1),obtem_linha(c)),)
    
    if chr(65) <= chr(ord(obtem_coluna(c)) + 1) <= chr(90) and 1 <= (obtem_linha(c) + 1) <= 99:
        tuplo_final+= (cria_coordenada(chr(ord(obtem_coluna(c)) + 1),obtem_linha(c) + 1),)
    
    if chr(65) <= obtem_coluna(c) <= chr(90) and 1 <= (obtem_linha(c)+ 1) <= 99:
        tuplo_final+= (cria_coordenada(obtem_coluna(c),obtem_linha(c)+ 1),)
    
    if chr(65) <= chr(ord(obtem_coluna(c)) - 1) <= chr(90) and 1 <= (obtem_linha(c)+ 1) <= 99:
        tuplo_final+= (cria_coordenada(chr(ord(obtem_coluna(c)) - 1),obtem_linha(c)+ 1),)
    
    if chr(65) <= chr(ord(obtem_coluna(c)) - 1) <= chr(90) and 1 <= obtem_linha(c) <= 99:
        tuplo_final+= (cria_coordenada(chr(ord(obtem_coluna(c)) - 1),obtem_linha(c)),)
    
    return tuplo_final

def obtem_coordenada_aleatoria(c,g):#alto nível
    """
    coordenada x gerador -> coordenada
    Recebe uma coordenada(c) e um TAD gerador(g) e
    devolve uma coordenada gerada aleatoriamente, onde
    c define a maior coluna e a maior linha possíveis.
    
    """
    col = gera_carater_aleatorio(g,obtem_coluna(c))
    lin = gera_numero_aleatorio(g,obtem_linha(c))
    return cria_coordenada(col,lin)

#TAD parcela
def cria_parcela():#construtor
    """
    A representação interna que escolhi para o TAD parcela foi o tipo "dict",
    tendo o dicionário apenas 2 elementos. A primeira key, "estado" tem como
    valor o estado da parcela("tapada", "marcada" ou "limpa") e a segunda key, 
    "mina" tem como valor "sim" se a parcela estiver minada ou "não" caso contrário.

    {} -> parcela
    Devolve uma parcela tapada sem mina.
    """
    return {"estado":"tapada", "mina": "não"}

def cria_copia_parcela(p):#construtor
    """
    parcela -> parcela
    Recebe uma parcela e devolve uma nova cópia da parcela.
    """
    nova_p = p.copy()
    return nova_p

def limpa_parcela(p):#modificadores
    """
    parcela -> parcela
    Recebe uma parcela, modifica destrutivamente o seu 
    estado para limpa e devolve a própria parcela.
    """
    p["estado"] = "limpa"
    return p

def marca_parcela(p):#modificaodor
    """
    parcela -> parcela
    Recebe uma parcela, modifica destrutivamente o seu 
    estado para marcada e devolve a própria parcela.
    """
    p["estado"] = "marcada"
    return p

def desmarca_parcela(p):#modificador
    """
    parcela -> parcela
    Recebe uma parcela, modifica destrutivamente 
    o seu estado para tapada e devolve a própria parcela.
    """
    p["estado"] = "tapada"
    return p

def esconde_mina(p):#modificador
    """
    parcela -> parcela
    Recebe uma parcela, modifica destrutivamente 
    a parcela escondendo uma mina na mesma
    e devolve a própria parcela.
    """
    p["mina"] = "sim"
    return p

def eh_parcela(arg):#reconhecedor
    """
    universal -> booleano
    Recebe qualquer argumento e devolve "True" caso esse 
    argumento seja uma TAD parcela e "False" caso contrário.
    """
    return type(arg) == dict and len(arg) == 2 and "estado" in arg and "mina" in arg

def eh_parcela_tapada(arg):#reconhecedor
    """
    parcela -> booleano
    Recebe uma parcela e devolve "True" caso essa 
    parcela se encontre "tapada" e "False" caso contrário.
    """
    return arg["estado"] == "tapada"

def eh_parcela_marcada(arg):#reconhecedor
    """
    parcela -> booleano
    Recebe uma parcela e devolve "True" caso essa 
    parcela se encontre "marcada" e "False" caso contrário.
    """
    return arg["estado"] == "marcada"

def eh_parcela_limpa(arg):#reconhecedor
    """
    parcela -> booleano
    Recebe uma parcela e devolve "True" caso essa 
    parcela se encontre "limpa" e "False" caso contrário.
    """
    return arg["estado"] == "limpa"

def eh_parcela_minada(arg):#reconhecedor
    """
    parcela -> booleano
    Recebe uma parcela e devolve "True" caso essa 
    parcela esconda uma mina e "False" caso contrário.
    """
    return arg["mina"] == "sim"

def parcelas_iguais(p1,p2):#teste
    """
    parcela x parcela -> booleano
    Recebe uma parcela(p1) e uma parcela(p2) e devolve
    "True" se ambas forem iguais.
    """
    return p1["estado"] == p2["estado"] and p1["mina"] == p2["mina"]

def parcela_para_str(p):#transformadores
    """
    parcela -> str
    Recebe uma parcela(p) e devolve a cadeia de 
    caracteres que a representa, dependendo do
    seu estado. 
    """
    if  eh_parcela_tapada(p):
        return "#"
    
    if eh_parcela_marcada(p):
        return "@"
    
    if eh_parcela_limpa(p) and eh_parcela_minada(p):
        return "X"
    
    return "?"

def alterna_bandeira(p):#alto nivel
    """
    parcela -> booleano
    Recebe uma parcela e modifica-a destrutivamente dependendo do seu estado.
    Desmarca se estiver marcada e marca se estiver tapada, devolvendo "True".
    Em qualquer outro caso, não modifica a parcela e devolve "False".
    """
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True

    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True   
    
    return False

#TAD campo
def cria_campo(c,l):#construtor
    """
    A representação interna que escolhi para o TAD campo foi o tipo "list".
    Cada elemento desta lista é um tuplo composto por uma coordenada e pela 
    sua respetiva parcela, por esta ordem, ou seja, um tuplo com 2 elementos. 
    Isto faz com que o número de elementos desta lista seja o número de 
    parcelas de um campo de minas.

    str x int -> campo
    Recebe uma string(c) e um inteiro(l), correspondentes à
    ultima coluna e à ultima linha de um campo, respetivamente.
    Devolve o campo do tamanho pretendido composto por parcelas
    tapadas sem minas.
    """

    if type(c) != str or len(c) != 1 or c < "A" or c > "Z" or \
        type(l) != int or l < 1 or l > 99:
        raise ValueError("cria_campo: argumentos invalidos")

    campo = []
    comprimento = (ord(c) - ord("A")) + 1
    
    for el in range(1, l + 1):
        for i in range(1, comprimento + 1):
            campo += ((cria_coordenada(chr(64 + i), el), cria_parcela()),)
            #campo em que cada elemento representa uma parcela e a
            #sua respetiva coordenada
    return campo

def cria_copia_campo(m):#construtor
    """
    campo -> campo
    Recebe um campo(m) e devolve uma nova cópia do campo
    """
    novo_c = []
    for el in range(len(m)):
        novo_c += ((m[el][0], cria_copia_parcela(m[el][1])),)

    return novo_c

def obtem_ultima_coluna(m):#seletor
    """
    campo -> str
    Recebe um campo(m) e devolve a string 
    correspondente à ultima coluna do campo.
    """
    return m[len(m) - 1][0][0]

def obtem_ultima_linha(m):#seletor
    """
    campo -> int
    Recebe um campo(m) e devolve o inteiro
    correspondente à ultima linha do campo.
    """
    return m[len(m) - 1][0][1]

def obtem_parcela(m,c):#seletor
    """
    campo x coordenada -> parcela
    Recebe um campo(m) e uma coordenada(c) e 
    devolve a parcela do campo m correspondente 
    a essa coordenada.
    """
    for el in range(len(m)):
        if obtem_coluna(m[el][0]) == obtem_coluna(c) and \
        obtem_linha(m[el][0]) == obtem_linha(c):
            return m[el][1]

def obtem_coordenadas(m,s):#seletor
    """
    campo x str -> tuplo
    Recebe um campo(m) e uma string(s) e retorna
    um tuplo formado pelas coordenadas das parcelas
    com o estado de "s".
    """
    tuplo_final = ()
    if s == "limpas":
        for parcela in range(len(m)):
            if eh_parcela_limpa(m[parcela][1]):
                tuplo_final += (m[parcela][0],)
    
    if s == "tapadas":
        for parcela in range(len(m)):
            if eh_parcela_tapada(m[parcela][1]):
                tuplo_final += (m[parcela][0],)
    
    if s == "marcadas":
        for parcela in range(len(m)):
            if eh_parcela_marcada(m[parcela][1]):
                tuplo_final += (m[parcela][0],)
    
    if s == "minadas":
        for parcela in range(len(m)):
            if eh_parcela_minada(m[parcela][1]):
                tuplo_final += (m[parcela][0],)
    
    return tuplo_final

def obtem_numero_minas_vizinhas(m,c):#seletor
    """
    campo x coordenada -> int
    Recebe um campo(m) e uma coordenada(c) e retorna
    o número de parcelas vizinhas da parcela na 
    coordenada c que escondem uma mina.
    """
    count = 0
    c_vizinhas = obtem_coordenadas_vizinhas(c)

    for cord in c_vizinhas:
        if eh_coordenada_do_campo(m,cord):   
            if eh_parcela_minada(obtem_parcela(m,cord)):
                count += 1

    return count

def eh_campo(arg):#reconhecedor
    """
    universal -> booleano
    Recebe qualquer argumento e devolve "True" caso esse 
    argumento seja uma TAD campo e "False" caso contrário.
    """

    if type(arg) != list or len(arg) == 0:
        return False
    
    for el in range(len(arg)):#verificar cada coordenada
        if not eh_coordenada(arg[el][0]):
           return False

    for el in range(len(arg)):#verificar cada parcela
        if not eh_parcela(arg[el][1]):
            return False

    return True

def eh_coordenada_do_campo(m,c):#reconhecedor
    """
    campo x coordenada -> booleano
    Recebe um campo(m) e uma coordenada(c) e devolve "True" 
    se "c" é uma coordenada válida dentro do campo "m".
    """
    for el in range(len(m)):
        if m[el][0] == c:
            return True
    return False

def campos_iguais(m1,m2):#teste
    """
    campo x campo -> booleano
    Recebe uma campo(m1) e uma campo(m2) e devolve
    "True" se ambos forem campos e forem iguais.
    """
    if not eh_campo(m1) or not eh_campo(m2):
        return False
    
    if len(m1) != len(m2):
        return False
    
    for el1 in range(len(m1)):
        if not parcelas_iguais(m1[el1][1], m2[el1][1]):
            return False
        if cria_coordenada(obtem_coluna(m1[el1][0]), obtem_linha(m1[el1][0])) != \
        cria_coordenada(obtem_coluna(m2[el1][0]), obtem_linha(m2[el1][0])) :
            return False
    return True

def campo_para_str(m):#transformador
    """
    campo -> str
    Recebe um campo(m) e devolve a cadeia de 
    caracteres que o representa, de acordo 
    com o exemplo. 
    """
    str_colunas = "" #string com a letra de cada coluna
    for parcela in range(len(m)):
        str_colunas += m[parcela][0][0]
        if m[parcela][0][0] == obtem_ultima_coluna(m):
            break
    
    lista_linhas = [] #lista com todas as coordenadas de uma coluna
    for parcela in range(1,len(m) + 1, len(str_colunas)):
        lista_linhas += (coordenada_para_str(m[parcela][0]),)
        if m[parcela][0][1] == obtem_ultima_linha(m):
            break
    
    for cord in range(len(lista_linhas)):#ficar apenas com o numero de cada linha numa lista
        lista_linhas[cord] =  lista_linhas[cord][1:]
    
    str_linhas_campo = ""#string com as parcelas todas do campo
    i = 0
    count = 1
    for el in range(len(lista_linhas)):
        str_linhas_campo += lista_linhas[el] + "|"#adicionar o número da linha + o carater "|"
        while i != (len(str_colunas) * count):#até à ultima parcela do campo
            if eh_parcela_limpa(m[i][1]) and not eh_parcela_minada(m[i][1]):
                if obtem_numero_minas_vizinhas(m, m[i][0]) == 0:     
                    str_linhas_campo+= " "
                else:#quando a parcela tem minas vizinhas adiciona-se o nº de minas vizinhas
                     str_linhas_campo+= str(obtem_numero_minas_vizinhas(m, m[i][0]))
            else:
                str_linhas_campo+= parcela_para_str(m[i][1])
            i+= 1#iterar pelas parcelas
        str_linhas_campo+= "|\n"#adicionar isto no final de cada linha do campo (igual ao exemplo)
        count+= 1#iterar pelas linhas do campo
    
    str_colunas_inicio = "   " + str_colunas #para estarem bem estruturadas as colunas no campo 
    
    return str_colunas_inicio + "\n" + "  +" + "-"*len(str_colunas) + "+\n" + str_linhas_campo + \
         "  +" + "-"*len(str_colunas) + "+"

def coloca_minas(m,c,g,n):#alto nível
    """
    campo x coordenada x gerador x int -> campo
    Recebe um campo(m) e um int(n) e modifica de forma destrutiva
    o campo escondendo "n" minas em parcelas do campo. As 
    coordenadas para as "n" minas são geradas com o gerador(g) sem
    coincidir com a coordenada "c" nem com vizinhas da mesma, nem com
    coordenadas geradas anteriormente. Devolve o campo modificado.
    
    """
    maior_cord_possivel = cria_coordenada(obtem_ultima_coluna(m),obtem_ultima_linha(m))
    
    lista_cord_geradas = []
    i = 0
    while i != n:
        random_cord = obtem_coordenada_aleatoria(maior_cord_possivel,g)
        if random_cord != c and random_cord not in obtem_coordenadas_vizinhas(c) and \
            random_cord not in lista_cord_geradas:#condições do enunciado
            esconde_mina(obtem_parcela(m,random_cord))
            lista_cord_geradas += (random_cord,)
            i += 1
    return m

def limpa_campo(m,c):#alto nível
    """
    campo x coordenada -> campo
    Recebe um campo(m) e uma coordenada(c) e modifica de forma destrutiva
    o campo limpando a parcela na coordenada "c". Se não houver nenhuma
    mina vizinha escondida são limpas iterativamente todas as parcelas 
    vizinhas tapadas. Se a parcela já se encontrar limpa, a operação
    não tem efeito. Retorna o campo modificado.
    """
    if eh_parcela_limpa(obtem_parcela(m,c)):
        return m
    if eh_parcela_minada(obtem_parcela(m,c)):
        limpa_parcela(obtem_parcela(m,c))
        return m
    
    limpa_parcela(obtem_parcela(m,c))
    
    y = () #tuplo com as coordenadas vizinhas de todas as coordenadas existentes
    x = (0,)#tuplo com as coordenadas vizinhas que faltam verificar
    i = c
    while len(x) != 0:
        x = x[1:] #retirar a coordenada experimentada
        if obtem_numero_minas_vizinhas(m,i) == 0:
            tuplo_cord_viz_campo = ()
            tuplo_cord_viz = obtem_coordenadas_vizinhas(i)
            for elemento in tuplo_cord_viz:
                if eh_coordenada_do_campo(m,elemento) and \
                    not eh_parcela_limpa(obtem_parcela(m,elemento)):
                #selecionar apenas as coordenadas não limpas/pertencentes ao campo
                    tuplo_cord_viz_campo += (elemento,)
            
            for cord in tuplo_cord_viz_campo:
                if eh_parcela_tapada(obtem_parcela(m,cord)):
                    limpa_parcela(obtem_parcela(m,cord))
                    if eh_parcela_minada(obtem_parcela(m,cord)):#se limpar parcela minada termina
                        return m
        
            for count in range(len(tuplo_cord_viz_campo)):
            #filtrar a variável "x" para esta não ter coordenadas repetidas ou já verificadas
                if tuplo_cord_viz_campo[count] not in x and tuplo_cord_viz_campo[count] != c and \
                    tuplo_cord_viz_campo[count] not in y:
                    x += (tuplo_cord_viz_campo[count],)
            
            y += tuplo_cord_viz_campo #variável que não é filtrada 
        if len(x) == 0:
            return m
        i = x[0] #mudar a coordenada a verificar
    return m

#Funções adicionais
def jogo_ganho(m):
    """
    campo -> booleano
    Recebe um campo(m) e devolve "True" se todas as parcelas
    sem minas se encontram limpas ou "False" caso contrário.
    """
    t_todas_coor = obtem_coordenadas(m,"marcadas") + obtem_coordenadas(m,"tapadas") + \
        obtem_coordenadas(m,"limpas")
    
    t_todas_coor_sem_mina = ()
    for el in t_todas_coor:
        if not eh_parcela_minada(obtem_parcela(m,el)):
            t_todas_coor_sem_mina += (el,)
    
    count = 0
    for coor in t_todas_coor_sem_mina:
        if eh_parcela_limpa(obtem_parcela(m,coor)):
            count += 1 #verificar se todas as parcelas
                       #sem mina estão limpas

    return count == len(t_todas_coor_sem_mina)

def turno_jogador(m):
    """
    campo -> booleano
    Recebe um campo de minas e dá ao jogador a possibilidade de escolher
    uma ação e uma coordenada. O jogador tem a opção de limpar ou marcar
    uma coordenada à sua escolha. De acordo com a escolha do utilizador a 
    função modifica de forma destrutiva o campo, returnando "False" caso
    uma parcela com mina seja limpa ou "True" caso contrário.
    """
    mensagem_inicial = input("Escolha uma ação, [L]impar ou [M]arcar:")

    while mensagem_inicial != "L" and mensagem_inicial != "M":
        mensagem_inicial = input("Escolha uma ação, [L]impar ou [M]arcar:")
        #repetir a mensagem até a jogada ser válida
    
    escolher_cord = input("Escolha uma coordenada:")
 
    while type(escolher_cord) != str or len(escolher_cord) != 3 or \
        escolher_cord[0] > chr(90) or escolher_cord[0] < chr(65) or \
        escolher_cord[1] > chr(57) or escolher_cord[1] < chr(48) or \
        escolher_cord[2] > chr(57) or escolher_cord[2] < chr(48) or \
        int(escolher_cord[1:]) < 1 or int(escolher_cord[1:]) > 99:
        escolher_cord = input("Escolha uma coordenada:")
        #repetir a mensagem até a jogada ser válida(ver se era uma coordenada válida)
    
    while not eh_coordenada_do_campo(m, str_para_coordenada(escolher_cord)):
        escolher_cord = input("Escolha uma coordenada:")
        #repetir a mensagem até a jogada ser válida(ver se pertencia ao campo escolhido)
    
    if mensagem_inicial == "L":
        limpa_campo(m, str_para_coordenada(escolher_cord))
        if eh_parcela_minada(obtem_parcela(m,str_para_coordenada(escolher_cord))):
            return False #se limpar parcela minada acaba
    
    else:
        alterna_bandeira(obtem_parcela(m,str_para_coordenada(escolher_cord)))
    
    return True

def minas(c,l,n,d,s):
    """
    str x int x int x int x int -> booleano
    Recebe uma cadeia de carateres(c) que corresponde à ultima coluna, um inteiro(l)
    que corresponde à ultima linha, um inteiro(n) que corresponde ao nº de parcelas
    com minas, um inteiro(d) que corresponde à dimensão do gerador e um inteiro(s)
    que corresponde à seed do gerador. Esta função retorna "True" se o jogador 
    conseguir ganhar o jogo ou "False" caso contrário. 
    """
    if type(c) != str or type(l) != int or type (n) != int or \
        type(d) != int or type(s)!= int:
        raise ValueError("minas: argumentos invalidos")
    if len(c) != 1 or c < chr(65) or c > chr(90) or \
        l < 1 or l > 99 or n < 2:
        raise ValueError("minas: argumentos invalidos")
    if d != 32 and d != 64 or s <= 0:
        raise ValueError("minas: argumentos invalidos")

    campo = cria_campo(c,l)

    if n > (l * (ord(c) - ord("A") + 1)):
        raise ValueError("minas: argumentos invalidos")

    gerador = cria_gerador(d,s)
    parcelas_com_bandeira = obtem_coordenadas(campo, "marcadas")
    print("   [Bandeiras " + str(len(parcelas_com_bandeira)) + "/" + str(n) + "]" )
    print(campo_para_str(campo))

    primeira_jogada = input("Escolha uma coordenada:")
    #caso especial para a primeira jogada

    while type(primeira_jogada) != str or len(primeira_jogada) != 3 or \
        primeira_jogada[0] > chr(90) or primeira_jogada[0] < chr(65) or \
        primeira_jogada[1] > chr(57) or primeira_jogada[1] < chr(48) or \
        primeira_jogada[2] > chr(57) or primeira_jogada[2] < chr(48) or \
        int(primeira_jogada[1:]) < 1 or int(primeira_jogada[1:]) > 99:
        primeira_jogada = input("Escolha uma coordenada:")
        #repetir a mensagem até a ação ser válida(ver se era uma coordenada válida)

    while not eh_coordenada_do_campo(campo, str_para_coordenada(primeira_jogada)):
        primeira_jogada = input("Escolha uma coordenada:")
        #repetir a mensagem até a ação ser válida(ver se pertencia ao campo escolhido)

    coloca_minas(campo,str_para_coordenada(primeira_jogada), gerador, n)
    limpa_campo(campo, str_para_coordenada(primeira_jogada))
    print("   [Bandeiras " + str(len(parcelas_com_bandeira)) + "/" + str(n) + "]" )
    #representação igual à do exemplo
    print(campo_para_str(campo))

    while not jogo_ganho(campo):
        if turno_jogador(campo):
            parcelas_com_bandeira = obtem_coordenadas(campo, "marcadas")
            print("   [Bandeiras " + str(len(parcelas_com_bandeira)) + "/" + str(n) + "]" )
            print(campo_para_str(campo))
        else:#jogo perdido
            parcelas_com_bandeira = obtem_coordenadas(campo, "marcadas")#alteração
            print("   [Bandeiras " + str(len(parcelas_com_bandeira)) + "/" + str(n) + "]" )
            print(campo_para_str(campo))
            print("BOOOOOOOM!!!")
            return False 
    
    print("VITORIA!!!")
    return True


