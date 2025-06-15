# imports
import sys
import os
import kmeans.py

# chamada do data-set
def ObtemDataset(name):
    print("Dataset importado com sucesso.")

# divisao treinamento X teste
def DivisaoTreinamentoTeste(DataSet):
    DsTreinamento = DataSet.sort() #corte de 80% para treinamento
    DsTeste = DataSet - DsTreinamento # 20% para teste
    
    return DsTreinamento, DsTeste

#  

# 

# Função Principal
def main(NomeDataset, K, MaxInteracao):
    #chama  a funcao do data-set
    ds = ObtemDataset(NomeDataset)

# Inicio do Programa:
if __name__ == "__main__":
    main()
