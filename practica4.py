MENU = ["buscar_pedido", "ver_menu"]  # lista de herramientas permitidas (el menú)

def herramienta_permitida(nombre, permitidas) -> bool:  # define la función; recibe un nombre y la lista de permitidas
    if nombre in permitidas:  # "in" pregunta: ¿este nombre está dentro de la lista?
        return True  # si está, devuelve True (permitido)
    return False  # si no está, devuelve False (rechazado)

print(herramienta_permitida("buscar_pedido", MENU))  # debería mostrar True
print(herramienta_permitida("borrar_todo", MENU))  # debería mostrar False

def herramienta_permitida(nombre, permitidas) -> bool:
    if nombre in permitidas:
        return True
    return False