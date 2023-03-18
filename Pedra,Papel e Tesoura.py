import rand

user_points = 0
computer_points = 0

option = ["r","p","t",]

while True:
    user_choice = input("Escolha R(Pedra)/P(Papel)/T(Tesoura) ou Q para sair.").lower()
   
    if user_choice == "q":
        break
    if user_choice not in option:
      continue


computer_choices = random.randint(0,2)
     # 0 = r(pedra)/ 1 = p(Papel)/ 2 = t(Tesoura)
computer_options = option[computer_choices]
print("O computador escolheu"+ computer_options)

if user_choice == computer_choices:
    print("Empate!")

elif user_choice == 'r' and computer_options == 't':
    print("Você ganhou!")
    user_points = user_points + 1

elif user_choice == 'p' and computer_options == 'r':
    print("Você ganhou!")
    user_points = user_points + 1

elif user_choice == 't' and computer_options == 'p':
    print("Você ganhou!")
    user_points = user_points + 1
else:
    print("Você perdeu!")
    computer_points = computer_points + 1

print("Sua pontuação:" + str(user_points))
print("Pontuação do Computador:" + computer_points)

if computer_points > user_points:
    print("Derrota!!!")

elif computer_points == user_points:
    print("Empate!")
else:
    print("Vitória!!!")
    
print("Fim de Jogo!")
        


    




