per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} #Дано: словарь
money = int(input("Введите сумму вклада: ")) #Вводим сумму которую хотим положить на счет

deposit = list(per_cent.values()) #создаем словарь с процентами вклада
deposit = [round(i/100*money) for i in deposit] #считаем прибыль для каждого банка

print (deposit) #выводим прибыль для каждого банка

print ("Максимальная сумма, которую вы можете заработать:", max(deposit)) #выводим максимальную прибыль
