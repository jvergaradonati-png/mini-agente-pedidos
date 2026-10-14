def describir_herramienta(nombre, descripcion, propiedades, requeridos) -> dict:  # arma la ficha de una herramienta
    ficha = {  # abro la caja grande, se llama ficha
        "name": nombre,  # nombre de la herramienta
        "description": descripcion,  # para qué sirve
        "input_schema": {  # caja pequeña que describe la entrada
            "type": "object",  # la entrada es un diccionario
            "properties": propiedades,  # campos permitidos
            "required": requeridos,  # campos obligatorios
        },  # cierro la caja pequeña
    }  # cierro la caja grande
    return ficha  # devuelvo ficha, el mismo nombre con el que abrí la caja


def armar_pedido(id_pedido, nombre, entrada) -> dict:  # arma el pedido que haría el modelo
    bloque = {  # abro la caja, se llama bloque
        "type": "tool_use",  # etiqueta fija: pide usar una herramienta
        "id": id_pedido,  # número del pedido
        "name": nombre,  # herramienta que quiere usar
        "input": entrada,  # datos con los que quiere usarla
    }  # cierro la caja
    return bloque  # devuelvo bloque, el mismo nombre con el que abrí la caja


def buscar_pedido(respuesta) -> dict:  # busca el pedido dentro de la respuesta del modelo
    if respuesta["stop_reason"] != "tool_use":  # si el modelo no terminó pidiendo una herramienta
        return {}  # no hay pedido: devuelvo un diccionario vacío
    for bloque in respuesta["content"]:  # recorro cada bloque de la respuesta
        if bloque["type"] == "tool_use":  # si este bloque es un pedido de herramienta
            return bloque  # lo devuelvo y la función termina aquí
    return {}  # si no encontré ninguno, devuelvo vacío


ficha = describir_herramienta(  # llamo a la función 1 con datos de prueba
    "buscar_pedido",  # nombre de la herramienta
    "Busca un pedido por su número",  # descripción
    {"numero": {"type": "string"}},  # campo numero, de tipo texto
    ["numero"],  # numero es obligatorio
)  # cierro la llamada
print(ficha)  # muestro la ficha

pedido = armar_pedido("t1", "buscar_pedido", {"numero": "A-102"})  # llamo a la función 2
print(pedido)  # muestro el pedido

respuesta_con_pedido = {  # respuesta falsa de un modelo que sí pide una herramienta
    "content": [  # lista de bloques de la respuesta
        {"type": "text", "text": "Voy a buscar tu pedido."},  # un bloque de texto normal
        pedido,  # el bloque de pedido que armé arriba
    ],  # cierro la lista de bloques
    "stop_reason": "tool_use",  # el modelo se detuvo porque quiere usar una herramienta
}  # cierro la respuesta
respuesta_sin_pedido = {  # respuesta falsa de un modelo que solo responde texto
    "content": [{"type": "text", "text": "Hola, ¿en qué te ayudo?"}],  # solo un bloque de texto
    "stop_reason": "end_turn",  # el modelo terminó de hablar, sin pedir herramienta
}  # cierro la respuesta

print(buscar_pedido(respuesta_con_pedido))  # debería mostrar el pedido
print(buscar_pedido(respuesta_sin_pedido))  # debería mostrar un diccionario vacío