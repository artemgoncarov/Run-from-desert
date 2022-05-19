import random
import time

rare = int(input("Сколько раундов играем?"))
rounds = 1
comp_score = 0 
you_score = 0

while True:
    if rounds <= rare:
        you = input('Выбирайте: камень / ножницы / бумага')
        if you == 'камень'or you == 'бумага' or you == 'ножницы':
            comp = random.randint(1,3)
            if comp == 1:
                comp = "камень"
            if comp == 2:
                comp = 'бумага'
            if comp == 3:
                comp = 'ножницы'
            print('камень, ножницы, бумага')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('3')
            if you == 'камень'and comp == 'камень':
                print(rounds, "раунд окончен! ","Ничья, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'бумага'and comp == 'бумага':
                print(rounds, "раунд окончен! ","Ничья, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'ножницы'and comp == "ножницы":
                print(rounds, "раунд окончен! ","Ничья, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'камень'and comp == 'ножницы':
                you_score +=1
                print(rounds, "раунд окончен! ","Вы победили, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'бумага' and comp == 'камень':
                you_score +=1
                print(rounds, "раунд окончен! ","Вы победили, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'ножницы' and comp == 'бумага':
                you_score +=1
                print(rounds, "раунд окончен! ","Вы победили, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'бумага' and comp == 'ножницы':
                comp_score += 1
                print(rounds, "раунд окончен! ","Вы проиграли, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'ножницы' and comp == 'камень':
                comp_score += 1
                print(rounds, "раунд окончен! ","Вы проиграли, счет" ,you_score ,":" ,comp_score)
                rounds +=1
            elif you == 'камень' and comp == 'бумага':
                comp_score += 1
                print(rounds, "раунд окончен! ","Вы проиграли, счет" ,you_score ,":" ,comp_score)
                rounds +=1
        else:
            print("Нет такого варианта")
    else:
        print("Игра окончена, счет", you_score ,":" ,comp_score)
        break