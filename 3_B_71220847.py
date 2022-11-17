print ("========== CATATAN BELANJA ==========")

print ("========== Daftar 1 ==========")
daftarBelanja1 = ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']
print ("Daftar Belanja 1: ", daftarBelanja1)
print ("")

print ("========== Daftar 2 ==========")
daftarBelanja2 = ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']
print ("Daftar Belanja 2: ", daftarBelanja2)
print ("")

print ("Jawab dengan angka [1/2]")
print ("1. Rubah Belanjaan")
print ("2. Keluar")

a = input("Masukan Pilihan ")
if a == 2:
    print
else:
    if a == 1:
        b = input("Masukan nama item ke daftar 1 : ")
        c = int(input("Masukan index yang di ingin di rubah : "))
        daftarBelanja1[c]=b
        d = input("Masukan nama item ke daftar 2 : ")
        e = int(input("Masukan index yang ingin dirubah : "))
        daftarBelanja2[e]=d
        print("")
        print("========== Daftar 1 ==========")
        print("Daftar Belanja 1: ", daftarBelanja1)
        print("")
        print("Daftar Belanja 2: ", daftarBelanja2)
    else:
        print("Wrong Input")
