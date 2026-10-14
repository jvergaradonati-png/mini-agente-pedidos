respuesta_con_pedido = {"content": [{"type": "text", "text": "Voy a buscar."}, {"type": "tool_use", "id": "t1", "name": "buscar_pedido", "input": {"numero": "A-102"}}], "stop_reason": "tool_use"}  # respuesta falsa que sí trae un pedido
respuesta_sin_pedido = {"content": [{"type": "text", "text": "Hola"}], "stop_reason": "end_turn"}  # respuesta falsa que solo trae texto

def buscar_pedido(respuesta) -> dict:
    if respuesta["stop_reason"] != "tool_use":
        return {}
    for bloque in respuesta["content"]:
        if bloque["type"] == "tool_use":
            return bloque
    return {}

print(buscar_pedido(respuesta_con_pedido))
print(buscar_pedido(respuesta_sin_pedido))