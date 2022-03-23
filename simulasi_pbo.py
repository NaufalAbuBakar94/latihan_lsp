def garis():
    print("=====================================")

print("=========== HOTEL JEPE ONNE ==============")
print(" -- inap -- superior -- duluxe -- premium --")
print(" -- 1/2hari -- 200.000 -- 150.000 -- 100.000")

tipe_kamar = input("Masukkan tipe kamar : ")
lama_inap = int(input("Masukkan lama inap : "))

if tipe_kamar == "superior":
    if lama_inap <= 2 :
        total_harga = 200000*lama_inap
    elif lama_inap <= 4 :
        total_harga = 200000*lama_inap
    else:
        total_harga = 200000*lama_inap

elif tipe_kamar == "duluxe":
    if lama_inap <= 2 :
        total_harga = 150000*lama_inap
    elif lama_inap <= 4 :
        total_harga = 150000*lama_inap
    else:
        total_harga = 150000*lama_inap

elif tipe_kamar == "premium":
    if lama_inap <= 2 :
        total_harga = 100000*lama_inap
    elif lama_inap <= 4 :
        total_harga = 100000*lama_inap
    else:
        total_harga = 100000*lama_inap

garis()
print("Masukkan tipe kamar : ",(tipe_kamar))
print("Lama Inap : ",(lama_inap))
print("Total Harga : ",(total_harga))
