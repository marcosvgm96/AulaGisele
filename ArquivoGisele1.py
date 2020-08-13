class Maiordeidade():
    def metodo1(self):
        print("iniciando")

    def testeidade(self, idade):
        if idade >= 18:
            print("Essa pessoa é maior de idade!")
        else:
            print("Essa pessoa é menor de idade!")
        return idade

pessoa = Maiordeidade()
pessoa.metodo1()
pessoa.testeidade(int(input("Sua idade: ")))