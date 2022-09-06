canastaFamiliar = ['Lacteo', 'Carne', 'Huevo', 'Fruta', 'Cereal', 'Verdura']
aseo = ['Jabon', 'Desodorante', 'Shampoo', 'Detergente', 'Cepillo']
top = ['Panela', 'Licor', 'Embutido', 'Confiteria']

iva = {'canastaFamiliar': 3.0, 'aseo': 19.0, 'top': 10.5}

productos = [
    {'nombre': 'Leche Colanta',
        'categoria': canastaFamiliar[0], 'medida': 'litro', 'valorNeto': 3400},
    {'nombre': 'Lomo de res',
        'categoria': canastaFamiliar[1], 'medida': 'libra', 'valorNeto': 18000},
    {'nombre': 'Cubeta huevos',
        'categoria': canastaFamiliar[2], 'medida': 'uni', 'valorNeto': 17000},
    {'nombre': 'Manzana',
        'categoria': canastaFamiliar[3], 'medida': 'libra', 'valorNeto': 2000},
    {'nombre': 'Mango',
        'categoria': canastaFamiliar[3], 'medida': 'libra', 'valorNeto': 900},
    {'nombre': 'Zucaritas',
        'categoria': canastaFamiliar[4], 'medida': 'gramos', 'valorNeto': 7500},
    {'nombre': 'Desodorante Rexona',
        'categoria': aseo[1], 'medida': 'gramos', 'valorNeto': 15000},
    {'nombre': 'Jabón Dove',
        'categoria': aseo[0], 'medida': 'gramos', 'valorNeto': 3000},
    {'nombre': 'Shampoo Tio Nacho',
        'categoria': aseo[2], 'medida': 'ml', 'valorNeto': 23000},
    {'nombre': 'Detergente Ariel',
        'categoria': aseo[3], 'medida': 'kilo', 'valorNeto': 7500},
    {'nombre': 'Cepillo Colgate',
        'categoria': aseo[4], 'medida': 'uni', 'valorNeto': 7400},
    {'nombre': 'Panela Trebol',
        'categoria': top[0], 'medida': 'uni', 'valorNeto': 2350},
    {'nombre': 'Jack Daniel\'s',
        'categoria': top[1], 'medida': 'ml', 'valorNeto': 105000},
    {'nombre': 'Salchichas Rancheras',
        'categoria': top[2], 'medida': 'gramos', 'valorNeto': 6500},
    {'nombre': 'Galletas Sultana',
        'categoria': top[3], 'medida': 'gramos', 'valorNeto': 4700},
]


def realizarCompras(productos: list):
    productosComprados = []
    nProducto = []
    cont = 1
    ban = True
    msjProductos = 'Ingrese el producto que va a comprar:\n'
    for producto in productos:
        nProducto.append(producto['nombre'])
        msjProductos += str(cont) + '. ' + \
            producto['nombre'] + ' -> ' + str(producto['valorNeto']) + ' c/u\n'
        cont += 1
    while ban:
        pro = int(input(msjProductos))
        cant = int(input('Ingrese la cantidad a comprar: '))
        for aux in productos:
            if aux['nombre'] == nProducto[pro - 1]:
                productosComprados.append(
                    {'nombre': aux['nombre'], 'cantidad': cant, 'categoria': aux['categoria'],
                     'valorNeto': aux['valorNeto']})
        while True:
            res = input(
                "¿Desea comprar otro producto? ¿si/no?: ")
            if res.lower() == "no":
                ban = False
                break
            elif res.lower() == "si":
                break
            else:
                print("Solo puede ingresar \'si\' ó \'no\'")
                continue
    return productosComprados


def realizarFactura(lista: list):
    factura = []
    total = 0.0
    cont = 1
    for product in lista:
        precioFinal = 0.0
        _iva = 0.0
        if product['categoria'] in canastaFamiliar:
            _iva = iva['canastaFamiliar']
        elif product['categoria'] in aseo:
            _iva = iva['aseo']
        else:
            _iva = iva['top']
        precioFinal = (product['cantidad'] *
                       product['valorNeto']) * ((_iva/100)+1)
        factura.append({'numero': cont, 'nombre': product['nombre'], 'cantidad': product[
            'cantidad'], 'precioNeto': product['valorNeto'], 'iva': str(_iva) + '%', 'subtotal': precioFinal})
        total += precioFinal
        cont += 1
    factura.append({'total': total})
    return factura


lista = realizarCompras(productos)
print(lista)
factura = realizarFactura(lista)
print(factura)
