from restaurante import InterfaceUsuario

def main():
    app = InterfaceUsuario()

    app.gerenciador.adicionar_restaurante("Sashimi", "Comida Japonesa")
    app.gerenciador.adicionar_restaurante("Piazzetta", "Comida Italiana")
    app.gerenciador.adicionar_restaurante("Baeti", "Comida Mexicana")

    app.main()

if __name__ == '__main__':
    main()