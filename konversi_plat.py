kode=["AB","AA","A","AD"]
kota_plat=["Jogja","Magelang","Banten","Bandung"]
def hasil():
  print("kode plat : AB,AA,A,AD")
  kd_plat=(input("masukkan kode PLAT yang akan di konversi :"))
  for i in range(0,len(kode)) :
      if kd_plat==kode[i]:
          print("plat",kode[i],"adalah :","kota",kota_plat[i])
  ask=(input("mau isi lagi ?[y/t] :"))
  if ask=="y" or ask=="Y":
      hasil()
  else :
      exit()
hasil()
