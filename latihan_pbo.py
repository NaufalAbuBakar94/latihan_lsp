def garis():
    print ("=====================================")

print("======== HOTEL SMK JAKARTA PUSAT 1 ========")
print(" -- lama inap -- superior -- deluxe -- premuium --")
print(" -- 1/2hari -- 200.000/hari -- 150.000/hari -- 100.000/hari")

tipe_kamar = input("Masukkan tipe kamar : ")
lama_inap = int(input("Masukkan lama inap : "))

if tipe_kamar == "superior":
    if lama_inap <= 2 :
        total_harga = 200000*lama_inap
    elif lama_inap <= 4 :
        total_harga = 200000*lama_inap
    else:
        total_harga = 600000*lama_inap

elif tipe_kamar == "deluxe":
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
print("Kamar yang dipilih : ",(tipe_kamar))
print("Lama inap : ",(lama_inap))
print("Total Harga : ",(total_harga))
