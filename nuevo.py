nuevo = {
    'a': 100,   # Cambiado
    'li': 200,  # Cambiado
    'c': 300,   # Cambiado
    'd': 400,   # Cambiado
    'ño': 500,  # Cambiado
    'f': 600,   # Cambiado
}

"I love dogs!"  # Mensaje diferente

def nuevo1(nuevo):
    for data1 in nuevo:
        print(f"Key -> {data1}: {nuevo[data1]}")  # Print modificado

nuevo1(nuevo)