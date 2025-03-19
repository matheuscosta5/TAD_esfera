import math

class Esfera:
    def __init__(self, raio):
        #Inicializa a esfera com um raio específico
        self.raio = raio
    
    def get_raio(self):
        #Retorna o raio da esfera
        return self.raio
    
    def get_area(self):
        #Área da superfície da esfera: 4 * π * r^2
        return  4 * math.pi * (self.raio ** 2)
    
    def get_volume(self):
        #Volume da esfera: (4/3) * π * r^3
        return (4/3) * math.pi * (self.raio **3)
    
    def __str__(self):
        #Retorna os valores formatados da esfera
        return (f"Esfera de raio {self.raio:.2f}\n"
                f"Área da superfície: {self.get_area():.2f}\n"
                f"Volume: {self.get_volume():.2f}")

if __name__ == "__main__":
#Só roda se o script for executado diretamente

    while True:  
        try:
            entrada = input('Digite o raio ou "sair" para cancelar: ')  
            if entrada.lower() == "sair":
                print("Programa Encerrado.")
                exit()  # Encerra o programa
        
            raio = float(entrada)
            if raio <= 0:
                print("O raio deve ser um número positivo. Tente novamente.")
                continue  
            break  
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

esfera = Esfera(raio)
print(esfera)