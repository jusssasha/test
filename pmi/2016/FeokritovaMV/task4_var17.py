#Задача 4. Вариант 17.
#Напишите программу, которая выводит имя, под которым скрывается Грета Густафон. 
#Дополнительно необходимо вывести область интересов указанной личности, 
#место рождения, годы рождения и смерти (если человек умер), вычислить возраст 
#на данный момент (или момент смерти). Для хранения всех необходимых данных требуется 
#использовать переменные. После вывода информации программа должна дожидаться 
#пока пользователь нажмет Enter для выхода.

#Feokritova M.V..
#14.03.2017

Name='Грета Густафон'
NikName='Грета Гарбо'
PlaseOfBirth='Стокгольм'
YearOfBirth=1905
YearOfDeath=1990
Age=84
AreaOfInterest='актриса'
print(Name,'более известна, как ', NikName)
print('Место рождения: ', PlaseOfBirth)
print('Год рождения: ', YearOfBirth)
print('Год смерти: ', YearOfDeath)
print('Возраст: ', Age)
print('Область интересов: ', AreaOfInterest)
input('\n\nPress Enter')
