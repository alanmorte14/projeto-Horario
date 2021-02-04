# trabalho do horário das aulas

# Alunos:
# José Alan De Aquino Santos
# Nikeldon Carvalho da Silva


# horas das aulas

h1 = "07:00 - 07:50 : "
h2 = "07:50 - 08:40 : "
h3 = "08:40 - 09:30 : "
h4 = "09:50 - 10:40 : "
h5 = "10:40 - 11:30 : "
h6 = "11:30 - 12:20 : "


# matérias

a0 = "Sem Aula"
a1 = "ESAR"
## a0 = "GEOG"
a3 = "INPG"
a4 = "LPOR"
a5 = "BIOL"
a6 = "FILO"
## a0 = "FISC"
a8 = "LING"
a9 = "QUIM"


# cronograma

segunda = f"\nSegunda:\n\n{h1}{a0}\n{h2}{a1}\n{h3}{a1}\n{h4}{a0}\n{h5}{a0}\n{h6}{a0}\n\n"
terça = f"\nTerça:\n\n{h1}{a0}\n{h2}{a0}\n{h3}{a3}\n{h4}{a4}\n{h5}{a4}\n{h6}{a0}\n\n"
quarta = f"\nQuarta:\n\n{h1}{a0}\n{h2}{a0}\n{h3}{a5}\n{h4}{a5}\n{h5}{a6}\n{h6}{a6}\n\n"
quinta = f"\nQuinta:\n\n{h1}{a0}\n{h2}{a0}\n{h3}{a0}\n{h4}{a3}\n{h5}{a0}\n{h6}{a0}\n\n"
sexta = f"\nSexta:\n\n{h1}{a0}\n{h2}{a8}\n{h3}{a8}\n{h4}{a9}\n{h5}{a9}\n{h6}{a4}\n\n"


# estrutura e execução

num = input("Comandos do programa:\n\"cronograma\"\tinterface do horário.\n\"notas\"\t\t\tinterface das notas.\n\"sair\"\t\t\tfechar programa.\n")

if num == "cronograma":
  while True:
    dia = input("Qual dia da semana você quer saber o horário?\n")
    if dia == "segunda":
      print(segunda)
    elif dia == "terça":
      print(terça)
    elif dia == "quarta":
      print(quarta)
    elif dia == "quinta":
      print(quinta)
    elif dia == "sexta":
      print(sexta)
    elif dia == "sabado":
      print("\nfinal de semana\n")
    elif dia == "domingo":
      print("\nfinal de semana\n")
    elif dia == "todos":
      print(segunda, terça, quarta, quinta, sexta)
      break
    elif dia == "sair":
      break
    else:
      print("\nDia inválido, tente novamente. \n")

elif num == "notas":
  while True:
    print("\nInforme as notas bimestrais:\n(nota de corte: 6.00)\n")
    b1 = float(input("Primeira nota: "))
    b2 = float(input("Segunda nota: "))
    b3 = float(input("Terceira nota: "))
    b4 = float(input("Quarta nota: "))
    total = (b1 + b2 + b3 + b4) / 4
    if total >= 6:
      print(f"\nO aluno foi APROVADO com média total de: {total:.2f} pontos.")
    else:
      print(f"\nO aluno foi REPROVADO com média de: {total:.2f} pontos.")
elif num == "sair":
  print("")
else:
  print("Digite um comando válido.")