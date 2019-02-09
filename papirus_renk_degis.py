#!/usr/bin/python3
import os


def klasor_ara(url,degisecekRenk,yeniRenk):
	liste = ["actions","devices","panel","places"]
	dosyaninici = os.listdir(url)
	dosyaninici.sort()
	for i in dosyaninici:
		print(i)
		try:

			if os.path.isdir(url+"/"+i):
				if i not in liste:
					pass
				klasor_ara(url+"/"+i,degisecekRenk,yeniRenk)
				print(url+"/"+i)
			else:
				dosya = open(url+"/"+i,"r")
				okunan = dosya.read()
				fonkk = degistirKoordinat(okunan,degisecekRenk)
				okunan_1 = degistir(okunan,yeniRenk,fonkk)
				dosya.close()
				dosya = open(url+"/"+i,"w")
				dosya.write(okunan_1)
				dosya.close()
		except:
			pass

def degistirKoordinat(metin,renk):
	liste = []
	for i in range(len(metin)):
		if metin[i:i+len(renk)]==renk:
			liste.append(i)
	return liste

def degistir(metin,yrenk,listeKoordinat):
	yeniMetin = ""
	koordinat = 0
	if len(listeKoordinat) != 0:
		for x in listeKoordinat:
			yeniMetin += metin[koordinat:x]
			yeniMetin += yrenk
			koordinat = x + len(yrenk)
		yeniMetin += metin[koordinat:len(metin)]
		return yeniMetin
	else:
		return metin

for i in [("/Papirus-Dark","dfdfdf","cfd0c2"),("/Papirus-Light","444444","272822"),("/Papirus","dfdfdf","cfd0c2"),("/Papirus","444444","272822")]:
	klasor_ara(os.getcwd()+i[0],i[1],i[2])