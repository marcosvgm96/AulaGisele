def main():
    valorproduto = float(input("Digite o valor do produto: "))
    valorpago = float(input("Digite o valor pago: "))
    if valorpago < valorproduto:
        print("Pague direito")
    else:
        print("compra concluida!!!")
    return print("O troco é de: R$", valorpago - valorproduto)


main()