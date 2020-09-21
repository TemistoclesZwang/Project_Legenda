import re

teste = open('/home/temistocles/Documentos/IFPI/__Estudos/Project Legenda/matrix.srt', 'r', encoding="latin-1").readlines()
legenda_tratada = open('/home/temistocles/Documentos/IFPI/__Estudos/Project Legenda/legenda_tratada.txt','w') #tratada gera um arquivo de texto

lista = []

for linha in teste: 
   linha = linha.strip().upper()  # Utilizado para retirar a impressão do \ palavra 
   sub = re.sub(r'\d\d:\d\d:\d\d,\d\d\d|-->|<i>|</i>', '',linha)  # Substitui os caractéres por espaço 
   # para substituir: Palavra que vai ser substituída, palavra substituta, fonte do texto 
   #search = re.findall(r'(?<= )\w+',sub) #encontra as palavras após um espaço 
   search2 = re.findall(r'(?<! )\w+|\w+ | \w+',sub) #encontra as palavras antes de um espaço depois de um espaço e no começo dos paragrafos 
   
   for palavra in search2: 
      sub2 = re.sub(r' |\d','',palavra) #substitui todos os espaços e todos os números por nada
      print(sub2) 
      legenda_tratada.write(sub2+'\n') #\n coloca uma palavra em cada linha
legenda_tratada.close() #Se não der close não vai escrever tudo


legenda_tratada = open('/home/temistocles/Documentos/IFPI/__Estudos/Project Legenda/legenda_tratada.txt',
         'r', encoding="UTF-8").readlines()  # texto gera uvo de texto

lista = []
nova_lista = []

def contar_repetidas():
   for palavra in legenda_tratada:
      if palavra != '\n': #para não pegar espaços
         lista.append(palavra.rstrip('\n')) #remove os espaços no começo e fim da string



def remover_ocorrencias():
   for palavra in lista:
      contador = lista.count(palavra) #contar palavras repetidas
      for i in range(contador): 
         lista.remove(palavra)
      # Se o número x aparece 4 vezes apague as 4 vezes que ele aparece na lista deixando só 1
      
      if contador > 10 and len(palavra) > 5 and palavra not in nova_lista:
         unificar = contador, palavra
         nova_lista.append(unificar)



def organizar_e_mostrar():
   nova_lista.sort(reverse = True) # colocar a lista em ordem crescente
   for item in nova_lista:
      print(item)



contar_repetidas()
remover_ocorrencias()
organizar_e_mostrar()


