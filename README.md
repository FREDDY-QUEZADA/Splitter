
#### EJECUTA TODO DES UN ENTORNO VITUAL
python -m venv venv
.\venv\Scripts\activate  --Windows 
source venv/bin/activate -- Linux/Mac.



# Proyecto de API de Supermercado en Línea
# API de Procesamiento de Pedidos

Este proyecto implementa una API en Flask que procesa pedidos de un supermercado en línea. Utiliza el patrón Splitter para descomponer un pedido en productos individuales y procesarlos según su categoría.

## Características

- Procesamiento de pedidos en tiempo real.
- Uso del patrón Splitter para descomponer los pedidos en productos individuales.
- Procesamiento diferenciado basado en la categoría del producto (Electrónica, Ropa, Alimentos).
- API REST que permite la integración con otras plataformas o servicios.

## Tecnologías Utilizadas

- Python
- Flask

## Requisitos

Para ejecutar este proyecto necesitas tener Python y Flask instalados en tu sistema. Las dependencias exactas se pueden encontrar en el archivo `requirements.txt`.

## Configuración y Ejecución

1. Clona este repositorio o descarga el código fuente.
2. Instala las dependencias necesarias usando el comando `pip install -r requirements.txt` en tu entorno de Python.
3. Ejecuta el servidor usando `python app.py` desde la línea de comandos.
4. La API estará accesible en `http://127.0.0.1:5000/procesar-pedido` para recibir peticiones POST con los datos de los pedidos.

## Uso de la API

Envía una solicitud POST a `http://127.0.0.1:5000/procesar-pedido` con un cuerpo JSON que represente un pedido. La API procesará cada producto en el pedido y devolverá los resultados del procesamiento.

### Ejemplo de Cuerpo de Solicitud

```json
{
    "id": "12345",
    "productos": [
        {"id": "a1", "nombre": "Laptop", "categoria": "Electrónica", "cantidad": 1},
        {"id": "b2", "nombre": "Camiseta", "categoria": "Ropa", "cantidad": 2},
        {"id": "c3", "nombre": "Manzanas", "categoria": "Alimentos", "cantidad": 3}
    ]
}