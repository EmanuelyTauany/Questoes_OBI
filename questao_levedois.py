quant = int(input("Quantos chocolates você vai levar?"))

choc = []
grupos = []
tamanho_g = 3
soma_v = []
soma = []

for i in range(1,quant+1):
    x=int(input(f"Digite os preço do {i}º chocolate:"))
    
    choc.append(x)
    choc.sort(reverse=True)
    
for i in range (0, len(choc), tamanho_g):
        
    grupo = choc[i:i + tamanho_g]
    soma_v.append(sum(grupo[:2]))
    

pagar = sum(soma_v)
    
print(pagar)