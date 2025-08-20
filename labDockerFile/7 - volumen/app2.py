with open("/app/data/archivo.txt", "a") as f:
    f.write("Hola desde app2\n")
with open("/app/data/archivo.txt") as f:
    print("Contenido actual:")
    print(f.read())
