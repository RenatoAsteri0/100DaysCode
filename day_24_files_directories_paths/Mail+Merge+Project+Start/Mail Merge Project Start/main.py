#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Pegar o esboço
with open('C:/Users/renat/OneDrive/Pessoal/Profissao/python/pythonprojects/day-24-files,directories,paths/'
          'Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r') as doc_original:
    conteudo_original = doc_original.read()

#Pegar os nomes das pessoas a serem inseridas do esboço
with open('C:/Users/renat/OneDrive/Pessoal/Profissao/python/pythonprojects/day-24-files,directories,paths/'
          'Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as arq_nomes:
    conteudo_nomes = arq_nomes.readlines()

#Apartir do esboço, criar novos arquivos com os nomes e enviar para a pasta ready to sent

#listar os nomes
for nome in conteudo_nomes:
    nome_limpo = nome.replace('\n', '')
    criar_arq = open(f'C:/Users/renat/OneDrive/Pessoal/Profissao/python/pythonprojects/day-24-files,directories,paths/'
        f'Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/{nome_limpo}.txt', 'x')
    criar_arq.close()
    conteudo_final = conteudo_original.replace(f'[name]', f'{nome_limpo}')
    final_arq = open(f'C:/Users/renat/OneDrive/Pessoal/Profissao/python/pythonprojects/day-24-files,directories,paths/'
        f'Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/{nome_limpo}.txt', 'w')
    final_arq.write(conteudo_final)
    final_arq.close()


