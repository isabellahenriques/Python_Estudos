# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input("Digite uma distância em metros: "))
km = medida / 1000
hm = medida /100
dam = medida /10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000

#print("A medida de {}m corresponte a {}cm e {}mm". format(medida, cm, mm))
print("A medida de{}m corresponte a\n {} km\n {} hm\n {} dam\n {} m\n {} dm\n {} cm\n {} mm".format(m, km, hm, dam, m, dm, cm, mm))
