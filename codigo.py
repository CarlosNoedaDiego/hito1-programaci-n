
def codigo():
    # creamos una lista para registrar los datos del cliente
    datosCliente = []
    # creamos una lista con los paises a los que se importa los productos
    listaPaises = ['españa', 'portugal', 'italia', 'alemania', 'eeuu']

    # pedimos los datos al cliente y los guardamos en la lista

    #creamos un bucle while True para conseguir que los datos de el nombre no se puedan poner en blanco y guardar los datos en la lista datos cliente
    while True:
        nombre = input('nombre y apellidos ')
        if nombre == '':
            print('Ese nombre no es válido. Inserte un nombre válido.')
        else:
            datosCliente.append(nombre)
            break
    # creamos un bucle while True para conseguir que los datos de la documentacion sean si o si 9 cifras y guardar los datos en la lista datos cliente
    while True:
        documentacion = input('DNI/NIF: ')
        # Verificar si la entrada tiene exactamente 9 cifras
        if len(documentacion) == 9:
            datosCliente.append(documentacion)
            break
        else:
            print("Por favor, introduce un DNI/NIF válido con exactamente 9 cifras.")

    # hacemos un bucle while para ver que IVA se le van a aplicar en en las facturas
    while True:
        pais = input(f"¿en que país vives? Los paises a los que enviamos productos son: {listaPaises} ").lower()
        if pais in listaPaises:
            if pais == listaPaises[0]:
                IVA = 0.21
            if pais == listaPaises[1]:
                IVA = 0.15
            if pais == listaPaises[2]:
                IVA = 0.1
            if pais == listaPaises[3]:
                IVA = 0.07
            if pais == listaPaises[4]:
                IVA = 0.18
            break
        else:
            print(f'pais no valido, esta es la lista de paises: {listaPaises} ')

    print('ahora te vamos a mostrar los productos que tenemos en venta ')

    # creamos una diccionario con  todos los productos y los valores de cada uno
    # (si bien nosotros le damos los valores 1 a 1 esto se podra aceder a una base de datos para ver los valores de cada producto)

    productos = {
        'camisa': {'precio': 7, },
        'pantalon': {'precio': 10, },
        'cafe': {'precio': 2.5, },
        'pantalones vaqueros': {'precio': 17, },
        'teclado': {'precio': 50, },
        'ratón': {'precio': 60, },
    }

    # con este for in mostramos los productos, unidades y precio de cada producto que tenemos guardados en el diccionario
    for producto, info in productos.items():
        print(f"{producto}: precio {info['precio']}")
    #creamos un diccionario para poder guardar los productos y las unidaddes
    carrito = {}

    # hacemos un while para que seleccionemos un producto y se meta en el diccionario carrito,
    # y podamos resetear el diccionario y terminar en el caso de que queramos finalizar la compra
    while True:
        productoCo = input('Selecciona un producto: ')
        productosComprar = productoCo.lower()

        # salir del bucle
        if productosComprar == 'fin':
            break

        # resetear el diccionario
        if productosComprar == 'borrar':
            carrito = {}
            print("Carrito reiniciado.")
            continue

        # añadir productos al diccionario
        if productosComprar in productos:
            # Si el producto ya está en el carrito, incrementa la cantidad en 1
            if productosComprar in carrito:
                carrito[productosComprar]['cantidad'] += 1
            else:
                # Si es la primera vez que se añade el producto, inicializa la entrada en el diccionario
                carrito[productosComprar] = {'precio': productos[productosComprar]['precio'], 'cantidad': 1}

            print(f"Producto agregado al carrito: {carrito}")
            print(
                f"Esta es tu compra: {carrito}, si quieres dejar de comprar escribe fin o borrar para borrar la lista")
        else:
            print('Producto no encontrado en el catálogo.')
    #cambiamos el diccionario carrito a una lista
    listaCarrito = list(carrito.items())

    # Calcular el precio total sin IVA utilizando la lista
    precioTotal = sum(info['precio'] * info['cantidad'] for _, info in listaCarrito)

    # Calcular el precio total con IVA
    precioIVA = precioTotal * (1 + IVA)

    print(f"Esta es tu compra: {listaCarrito}")
    print(f"Precio total con IVA: {precioIVA}")

    #preguntamos al cliente si quiere que le mandemos un SMS com los datos de la factura
    respuesta = input('¿Quieres recibir un mensaje con los datos de la factura? si o no: ')
    if respuesta == 'si':
        numero = int(input('cual es tu numero de telefono'))
        print(f"SMS enviado al numero {numero}, nombre del cliente {datosCliente[0]} y DNI/NIF {datosCliente[2]} ")
    else:
        print('')
