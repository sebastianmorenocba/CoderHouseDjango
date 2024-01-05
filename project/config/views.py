from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola!")

def saludo2(request):
    nombre = input('Ingresa tu nombre')
    return HttpResponse(f'Hola {nombre} !')

def tirar_dados(request):
    import random
    numero = random.randint(1,6)
    if numero == 6:
        return HttpResponse(f'Felicitaciones obtuviste el numero {numero}')
    else: 
        return HttpResponse(f'Has tirado el numero {numero}, Vuelve a intentar')