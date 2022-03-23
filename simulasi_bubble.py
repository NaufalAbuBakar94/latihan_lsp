def garis():
    print("===================================")

def ascending(mylist):
    mylist = sorted(mylist)
    return(mylist)

def descending(mylist):
    mylist = sorted(mylist, reverse = True)
    return(mylist)

print("Masukkan 3 buah Nilai ")

nilaiA = int(input("Masukkan nilai A : "))
nilaiB = int(input("Masukkan nilai B : "))
nilaiC = int(input("Masukkan nilai C : "))
angka = [nilaiA, nilaiB, nilaiC]
garis()

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka)/len(angka)

print("Masukkan Nilai ascending : ",(ascending(angka)))
print("Masukkan Nilai descending : ",(descending(angka)))
garis()
print("Nilai Terbesar : ",max(angka))
print("Nilai Terkecil : ",min(angka))
print("Rata - rata : ",rata_rata(angka))
