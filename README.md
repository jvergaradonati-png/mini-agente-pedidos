\# Mini agente de pedidos (práctica en Python)



Proyecto de aprendizaje: construyo paso a paso las piezas de un agente de IA que usa herramientas, con una analogía de restaurante (cliente, mesero y cocina).



\## Qué contiene

\- `herramientas.py`: funciones para armar fichas de herramientas, armar pedidos y buscar el pedido en una respuesta.

\- `practica3.py`: `buscar\_pedido`, que encuentra el pedido de herramienta dentro de la respuesta de la IA.

\- `practica4.py`: `herramienta\_permitida`, que revisa si una herramienta está en el menú.

\- `practica5.py`: `revisar\_pedido`, el "mesero": rechaza lo que no está en el menú o no trae los datos obligatorios.



\## Cómo correrlo

Necesitas Python 3. En la terminal:



&#x20;   py practica5.py



\## Lo que aprendí

\- Diccionarios, listas, bucles `for`, `if` y `return`.

\- La forma de una respuesta de la API: `content` y `stop\_reason`.

\- Por qué un agente necesita un menú y revisión antes de ejecutar algo.



\## Próximos pasos

\- Hacer la primera llamada real a la API de Claude, con la clave guardada en `.env`.

\- Conectar las funciones en un bucle completo de agente.

