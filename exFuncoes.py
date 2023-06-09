# def mult(*args ):
# total = 1
#
# for num in args:
#
# total *= num
#
# return total
# numeros = 1, 2, 3, 4
# resultado = mult(*numeros)
# print(resultado)

def par_impar(num:int):
    return 'É par' if num%2==0 else 'É impar'

numero = 5
print(par_impar(numero))