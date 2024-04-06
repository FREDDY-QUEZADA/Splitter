from flask import Flask, request, jsonify

app = Flask(__name__)

def process_electronics(producto):
    # Procesa productos electrónicos, como verificar la garantía.
    return f"Verificando garantía para {producto['nombre']}..."

def process_clothing(producto):
    # Procesa artículos de ropa, realizando tareas como control de calidad.
    return f"Realizando control de calidad para {producto['nombre']}..."

def process_food(producto):
    # Procesa productos alimenticios, comprobando aspectos como la fecha de caducidad.
    return f"Comprobando fecha de caducidad para {producto['nombre']}..."

def process_product(producto):# ESTA PARTE DE CODIGO ACTUA COMO SPLITTER  
    # Verifica la categoría del producto y lo dirige al proceso correspondiente
    if producto['categoria'] == "Electrónica":
        return process_electronics(producto)
    elif producto['categoria'] == "Ropa":
        return process_clothing(producto)
    elif producto['categoria'] == "Alimentos":
        return process_food(producto)
    else:
        return f"No hay proceso definido para la categoría {producto['categoria']}"

@app.route('/procesar-pedido', methods=['POST'])  
def procesar_pedido():
    pedido = request.json
    resultados = [process_product(producto) for producto in pedido['productos']]
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)