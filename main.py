#trabalho do horário das aulas

''' Alunos: 
José Alan De Aquino Santos
Nikeldon Carvalho da Silva
'''

#cronograma

#Variáveis
segunda = ("Segunda\n\n07:00 - 07:50 : SEM AULA\n07:50 - 08:40 : ESAR\n08:40 - 09:30 : ESAR\n09:50 - 10:40 : GEOG\n10:40 - 11:30 : GEOG\n11:30 - 12:20 : SEM AULA\n\n")

terça = ("Terça\n\n07:00 - 07:50 : SEM AULA\n07:50 - 08:40 : SEM AULA\n08:40 - 09:30 : INPG\n09:50 - 10:40 : LPOR\n10:40 - 11:30 : LPOR\n11:30 - 12:20 : SEM AULA\n\n")

quarta = ("Quarta\n\n07:00 - 07:50 : SEM AULA\n07:50 - 08:40 : SEM AULA\n08:40 - 09:30 : BIOL\n09:50 - 10:40 : BIOL\n10:40 - 11:30 : FILO\n11:30 - 12:20 : FILO\n\n")

quinta = ("Quinta\n\n07:00 - 07:50 : SEM AULA\n07:50 - 08:40 : SEM AULA\n08:40 - 09:30 : SEM AULA\n09:50 - 10:40 : INPG\n10:40 - 11:30 : FISC\n11:30 - 12:20 : FISC\n\n")

sexta = ("Sexta\n\n07:00 - 07:50 : SEM AULA\n07:50 - 08:40 : LING\n08:40 - 09:30 : LING\n09:50 - 10:40 : QUIM\n10:40 - 11:30 : QUiM\n11:30 - 12:20 : LPOR\n\n")


#estrutura de repetição
while True:
  dia = input("Qual dia você quer saber o horário? ")
  if dia == 'segunda':
    print(segunda)
    break
  elif dia == 'terça':
    print(terça)
    break
  elif dia == 'quarta':
    print(quarta)
    break
  elif dia == 'quinta':
    print(quinta)
    break
  elif dia == 'sexta':
    print(sexta)
    break
  elif dia == "sabado":
    print("final de semana")
    break
  elif dia == "domingo":
    print("final de semana")
    break
  elif dia == "todos":
    print("\n\n",segunda, "\n", terça,"\n", quarta, "\n", quinta,"\n", sexta,"\n\n")
  else:
    print("Dia inválido, tente novamente. \n")
    continue