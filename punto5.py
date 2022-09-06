canastaFamiliar = ['Lacteo', 'Carne', 'Huevo', 'Fruta', 'Cereal', 'Verdura']
aseo = ['Jabon', 'Desodorante', 'Shampoo', 'Detergente', 'Cepillo']
top = ['Panela', 'Licor', 'Embutido', 'Confiteria']

iva = {'canastaFamiliar': 5.0, 'aseo': 19.0, 'top': 10.5}

productos = [
    {'nombre': 'Leche Colanta',
        'categoria': canastaFamiliar[0], 'medida': 'litro', 'valorBase': 3400},
    {'nombre': 'Lomo de res',
        'categoria': canastaFamiliar[1], 'medida': 'libra', 'valorBase': 18000},
    {'nombre': 'Cubeta huevos',
        'categoria': canastaFamiliar[2], 'medida': 'uni', 'valorBase': 17000},
    {'nombre': 'Manzana',
        'categoria': canastaFamiliar[3], 'medida': 'libra', 'valorBase': 2000},
    {'nombre': 'Mango',
        'categoria': canastaFamiliar[3], 'medida': 'libra', 'valorBase': 900},
    {'nombre': 'Zucaritas',
        'categoria': canastaFamiliar[4], 'medida': 'gramos', 'valorBase': 7500},
    {'nombre': 'Desodorante Rexona',
        'categoria': aseo[1], 'medida': 'gramos', 'valorBase': 15000},
    {'nombre': 'Jabón Dove',
        'categoria': aseo[0], 'medida': 'gramos', 'valorBase': 3000},
    {'nombre': 'Shampoo Tio Nacho',
        'categoria': aseo[2], 'medida': 'ml', 'valorBase': 23000},
    {'nombre': 'Detergente Ariel',
        'categoria': aseo[3], 'medida': 'kilo', 'valorBase': 7500},
    {'nombre': 'Cepillo Colgate',
        'categoria': aseo[4], 'medida': 'uni', 'valorBase': 7400},
    {'nombre': 'Panela Trebol',
        'categoria': top[0], 'medida': 'uni', 'valorBase': 2350},
    {'nombre': 'Jack Daniel\'s',
        'categoria': top[1], 'medida': 'ml', 'valorBase': 105000},
    {'nombre': 'Salchichas Rancheras',
        'categoria': top[2], 'medida': 'gramos', 'valorBase': 6500},
    {'nombre': 'Galletas Sultana',
        'categoria': top[3], 'medida': 'gramos', 'valorBase': 4700},
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
            producto['nombre'] + ' -> ' + str(producto['valorBase']) + ' c/u\n'
        cont += 1
    while ban:
        while True:
            try:
                pro = int(input(msjProductos))
                assert pro > 0
                assert pro <= len(productos)
                break
            except ValueError:
                print("Solo puede ingresar valores númericos")
                continue
            except AssertionError:
                print("Debe ingresar un número entre 0 y", len(productos), "\n")
                continue
        while True:
            try:
                cant = int(input('Ingrese la cantidad a comprar: '))
                assert cant > 0
                for aux in productos:
                    if aux['nombre'] == nProducto[pro - 1]:
                        productosComprados.append(
                            {'nombre': aux['nombre'], 'cantidad': cant, 'categoria': aux['categoria'],
                            'valorBase': aux['valorBase']})
                break
            except ValueError:
                print("Solo puede ingresar valores númericos")
                continue
            except AssertionError:
                print("Debe ingresar un número mayor a 0")
                continue
        while True:
            res = input(
                "¿Desea comprar otro producto? ¿S/N?: ")
            if res.lower() == "n":
                ban = False
                break
            elif res.lower() == "s":
                print('')
                break
            else:
                print("Solo puede ingresar \'S\' ó \'N\'")
                continue
    return productosComprados


def realizarFactura(lista: list):
    factura = []
    comprasIva = {5: 0.0, 19: 0.0, 10.5: 0.0}
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
                       product['valorBase']) * ((_iva/100)+1)
        factura.append({'numero': cont, 'nombre': product['nombre'], 'cantidad': product[
            'cantidad'], 'precioBase': product['valorBase'], 'iva': str(_iva) + '%', 'subtotal': precioFinal})
        comprasIva[_iva] += precioFinal
        total += precioFinal
        cont += 1
    factura.append({'total': total})
    return factura, comprasIva


lista = realizarCompras(productos)
factura, cIvas = realizarFactura(lista)
print('\n----------------------- PRODUCTOS COMPRADOS -----------------------\n')
print(f'{"N°":3}{"PRODUCTO":25}{"CANTIDAD":10}{"PRECIO":10}{"IVA":10}{"SUBTOTAL":1}')
for aux in factura:
    llaves = list(aux.keys())
    if llaves[0] != 'total':
        print(f'{str(aux[llaves[0]]):3}{aux[llaves[1]]:25}{str(aux[llaves[2]]):10}{str(aux[llaves[3]]):10}{str(aux[llaves[4]]):10}{str(aux[llaves[5]]):1}')
    else:
        print('--------------------------- DETALLE IVA ---------------------------')
        print(f'{"TIPO":19}{"COMPRA":19}{"BASE":19}{"IVA":1}')
        totalC = 0.0
        totalB = 0.0
        totalI = 0.0
        for llaves2 in list(cIvas.keys()):
            vBase = cIvas[llaves2]/((llaves2/100)+1)
            vIva = cIvas[llaves2] - vBase
            totalC += cIvas[llaves2]
            totalB += vBase
            totalI += vIva
            print(
                f'{str(llaves2)+"%":19}{str(cIvas[llaves2]):19}{str(vBase):19}{str(vIva):1}')
        print(f'{"Total:":19}{str(totalC):19}{str(totalB):19}{str(totalI):1}')
        print('-------------------------------------------------------------------')
        print(f'{"":3}{"TOTAL NETO:":55}{str(aux[llaves[0]]):1}')
        print('-------------------- GRACIAS POR SU COMPRA-------------------------')
print('')
