
print ("Horas", "Minutos","Segundos")

#separador#
print("Horas", "Minutos", "Segundos", sep="/") 

#end (impede a quebra linhas)#
print("Horas", "Minutos", "Segundos" , end="-->")
print ("Quebra de linhas") 


#tipos de dados e função type#
float, int , str , bool 

print(type(10)) #int#
print(type("10")) #string#
print(type(True)) #numeros booleanos#
print(type(34j))  #numeros complexos#
print(type(7.0)) #float#

#python não define variavel #

#variaveis(declaração e inicialização)#

x = 10
y = 20
print (x+y)

#entrada de dados#

nome =input("Insira o seu nome ")
num1 = int(input("Insira um numero inteiro")) #sempre retornará uma string# #precisa converter a string em outra variavel#

print(type(nome))
print(type(num1))

#operadores aritméticos#
print (5+5)
print(5-5)
print(5*5)
print(5/5) #sempre retorna um valor float com uma casa decimal#
print(14//5) #divisão que sempre retornará um número inteiro#
print (10%4)
print(pow(5,2))
print (5**2)


#operador de atribuição#
a = 1
b = 5
c = 9
d = 7
e = 2

a+=5  # a = a +5
b-=6 # b = b- 6
c*=2 # c = c*2
d/=7 # d = d/7
e%=2 # e = e%2

#operadores de comparação#

print(7=="7")#verificação de tipos#
#false#
print(7==8) #verifica se os dois valores são iguais#
#false#
print(7!=8) #verifica se os dois valores são diferentes#
#true#
print(7>8)
print(7<8)
print(7>=8)


#operadores lógicos#
x = 5
numero = x > 1 and  x ==5 #verifica de x >1 e x =5 e caso as duas condições sejam verdadeira, retorna TRUE#

numero = x >1 or x ==5 #verifica  se uma das condições é verdadeira , caso uma seja , retorna TRUE#

numero = not(x >1 or x ==5) # pega a condição verdadeira e inverte ela #


#concatenção (somente string , n pode int e float)(junção de duas strings) , conversão de tipos e formatação#

primeiro_nome= "Alexandre "
sobrenome= "Laureano"
idade = 20
altura = 1.78

print("Ola o meu nome é : " + primeiro_nome + sobrenome )#Concatenação de strings

print("Ola o meu nome é : " + primeiro_nome + sobrenome , "a minha idade é ", idade)#concatenação de strings e numeros

print("Ola o meu nome é : " + primeiro_nome + sobrenome , "a minha idade é ", str(idade))#concatenação de string e numeros com conversão

print("Ola o meu nome é : " + primeiro_nome + sobrenome , "a minha idade é " + str(idade))
#concatenação de string e numeros com conversão