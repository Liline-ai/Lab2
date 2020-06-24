from datetime import datetime
from collections import Counter

d = {'Иванов':[{'Услуга':'Окрашивание', 'Стоимость': 234, 'Дата': '23.04.1999'},
               {'Услуга':'Окрашивание', 'Стоимость': 235, 'Дата': '23.04.1999'}],
            
     'Петров':[{'Услуга':'Окрашивание', 'Стоимость': 2345, 'Дата': '23.04.1999'}],
     'Сидоров':[{'Услуга':'Окрашивание', 'Стоимость': 12355, 'Дата': '23.04.1999'}]
     }
def add_client():
#добавление клиента
    Name = input("Имя? ")
    Service = input("Услуга? ")
    Price = input("Стоимость? ")
    Date= input("Дата? ")
    d[Name] = {'Услуга':Service, 'Стоимость':Price, 'Дата':Date}
    print(d)

def del_client():
#удаление клиента
    Name = input("Имя? ")
    d.pop(Name)
    print(d)

def add_element():
#Добавление элемента
    Name = input("Имя? ")
    Service = input("Услуга? ")
    Price = input("Стоимость? ")
    Date= input("Дата? ")
    d[Name].append({'Услуга': Service, 'Стоимость': Price, 'Дата': Date})
    print(d)
    
def sum_price():
#найти Сумму потраченных денег
    Name = input("Имя? ")
    sum=0
    for i in range(len(d[Name])):
        sum=sum+d[Name][i]['Стоимость']
    print(sum)

def client_find():
#Найти самого частого клиента
    Name = ["Иванов", "Петров", "Сидоров"]
    number = 0
    for i in range(len(d)):
        if len(d[Name[i]]) > number:
            number = len(d[Name[i]])
            Name_Find = Name[i]
    print(Name_Find)

def client_rich():
#Найти самого богатого клиента
    Name = ["Иванов", "Петров", "Сидоров"]
    n=0
    sum=0
    for i in range(len(d)):
        for j in range(len(d[Name[i]])):
            sum=sum+d[Name[i]][j]['Стоимость']
        if sum>n:
            n=sum
            rich=Name[i]
    print(rich)
a=int(input())
#добавление клиента после нажатия цифры 1
if a==1:
    add_client()
#Удаление клиента после нажатия цифры 2
if a==2:
    del_client()
#Добавление элемента после нажатия цифры 3
if a==3:
    add_element()
#расчет протраченных денег после нажатия цифры 4
if a==4:
    sum_price()
#Расчет самого частого клиента после нажатия цифры 5
if a==5:
    client_find()
#Найти самого богатого клиента после нажатия цифры 6
if a==6:
    client_rich()
    
            
