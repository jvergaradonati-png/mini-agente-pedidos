MENU = {"buscar_pedido": ["numero"], "ver_menu": []}

def revisar_pedido(pedido, menu) -> str:
    nombre = pedido["name"]
    if nombre not in menu:
        return "RECHAZADO: no esta en el menu"
    for campo in menu[nombre]:
        if campo not in pedido["input"]:
            return "RECHAZADO: falta " + campo
    return "APROBADO"
pedido1 = {"name": "buscar_pedido", "input": {"numero": "A-102"}}  # pedido correcto
pedido2 = {"name": "borrar_todo", "input": {}}  # herramienta que no está en el menú
pedido3 = {"name": "buscar_pedido", "input": {}}  # herramienta válida pero sin el dato "numero"

print(revisar_pedido(pedido1, MENU))  # debería mostrar APROBADO
print(revisar_pedido(pedido2, MENU))  # debería mostrar RECHAZADO: no esta en el menu
print(revisar_pedido(pedido3, MENU))  # debería mostrar RECHAZADO: falta numero
