#Autor Temistocles Zwang
#Não esqueça de modificar o diretório de acordo com seu uso
import re
import os


def main(nome_do_arquivo):
   diretorio = os.getcwd()
   verificar = os.path.exists(nome_do_arquivo)

   if verificar == False:
      print(f'\nDiretório que você está no momento: {diretorio}')
      print(f'Arquivo que será utilizado ({nome_do_arquivo}): {verificar} \n')
      
      print('Verifique os erros mais comuns:\n (1) Verifique se o arquivo está de fato no diretório\n (2) Verifique se você está no diretório correto\n (3) Verifique então se o nome do arquivo está escrito da forma correta\n (4) Utilize o caminho completo dos diretórios até chegar no arquivo\n (5) ou adcione o "python.terminal.executeInFileDir": true, no settings.json do VSCode')
   else:
      tratar_legenda()
      contar_repetidas()
      remover_ocorrencias()


def tratar_legenda():
   arquivo_legenda = open('/home/temistocles/Documentos/IFPI/__Estudos/Project Legenda/Project/lovecraft.srt', 'r', encoding="latin-1").readlines()
   legenda_tratada = open('/home/temistocles/Documentos/IFPI/__Estudos/Project Legenda/Project/legenda_tratada.txt','w') 

   for linha in arquivo_legenda:
      linha = linha.strip().upper() 
      linha = re.sub(r'\.|^\-|\!|\,|\?|\:|\"', '',linha) #expressão regular ou REGEX
      if '-->' in linha:
         pass
      elif linha.isdigit() == True:
         pass
      else:
         #print(linha)
         #caso queira ver o processo
         for palavra in linha.split():
            legenda_tratada.write(palavra+'\n')
   legenda_tratada.close()


def contar_repetidas():
   legenda_tratada = open('/home/temistocles/Documentos/IFPI/__Estudos/Project Legenda/Project/legenda_tratada.txt','r', encoding="UTF-8").readlines()
   palavras_sem_espaco_no_comeco_e_fim = []
   for palavra in legenda_tratada:
      palavras_sem_espaco_no_comeco_e_fim.append(palavra.rstrip('\n'))

   return palavras_sem_espaco_no_comeco_e_fim


def remover_ocorrencias():
   palavras_sem_espaco_no_comeco_e_fim = contar_repetidas()
   filtrar_ocorrencias_e_tamanho_palavra = {}
   for palavra in palavras_sem_espaco_no_comeco_e_fim:
      palavras_repetidas = palavras_sem_espaco_no_comeco_e_fim.count(palavra) 

      if palavras_repetidas > 10 and len(palavra) > 5 and palavra not in filtrar_ocorrencias_e_tamanho_palavra:
         filtrar_ocorrencias_e_tamanho_palavra[palavra] = palavras_repetidas
   
   for item in sorted(filtrar_ocorrencias_e_tamanho_palavra, key = filtrar_ocorrencias_e_tamanho_palavra.get, reverse = True):
      print (filtrar_ocorrencias_e_tamanho_palavra[item], item)


main('lovecraft.srt')