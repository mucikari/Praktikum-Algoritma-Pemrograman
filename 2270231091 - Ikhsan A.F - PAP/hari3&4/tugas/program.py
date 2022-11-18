import datetime

tanggal= datetime.datetime.now()
data_product = {
    1:" Cylinder Wheel",
    2:" Long Tie Rod  ",
    3:" Oil           ",
    4:" Filter Oil    ",
    5:" Break Pad     ",
    6:" Bosch Arm     ",
    7:" Ball Joint    ",
    8:" Gress         ",
    9:" Busi          ",
    10:"Lamp          "
}

data_price = {
    1: 250000,
    2: 350000,
    3: 300000,
    4: 300000,
    5: 250000,
    6: 150000,
    7: 150000,
    8: 80000, 
    9: 30000,
    10: 10000
}

dict_trx = {}

daftar_pembayaran ={
    1:" bank   ",
    2:" cash   ",
    3:" kasbon "
}


print("=========================================")
print("============= List Product ==============")
print("=============    ISANTUY   ==============")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|No     |Name                  |Price   |")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in data_product:
    print("",i,"    ",data_product[i],"\tRp",data_price[i])
    print("=========================================")
pilih_no = int(input("Pilih No  : "))
pilih_jumlah=int(input("Jumlah yang diinginkan: "))
if pilih_no in data_product:
    pilih_beli = input("Wanna Buy? (Y/N):")
    print(20*"=")
    if pilih_beli == "y" or pilih_beli == "Y":
        nama_penerima            = input ("Name      : ")
        addres_penerima          = input ("Addres    : ")
        telephone_penerima       = input ("Telephone : ")
        kurir_pengirim           = input ("Kurir     : ")
        dict_trx = {
            "nama penerima ": nama_penerima,
            "addres penereima ": addres_penerima,
            "telephone penerima ": telephone_penerima,
            "kurir pengirim ": kurir_pengirim,
            "product ": data_product,
            "harga": data_price,
        }
    else:
        pass

    jumlah= data_price[pilih_no]*pilih_jumlah
    
    if len (dict_trx)>0:
        print("=================== Metode Pembayaran ===============")
    for i in daftar_pembayaran:
            print("id :", i,"\t pembayaran : ", daftar_pembayaran[i])
            print("---------------------------------------------")
    pilih_pembayaran = int (input("pilih pembayaran: ",))
    if pilih_pembayaran in daftar_pembayaran:
             print("================= Nota =================")
             print("Tanggal        : ", tanggal)
             print("nama penerima  : ",dict_trx["nama penerima "])
             print("alamat penerima: ",dict_trx["addres penereima "])
             print("telephone      : ",dict_trx["telephone penerima "])
             print("pengiriman     : ",dict_trx["kurir pengirim "])
             print("product        : ",data_product[pilih_no])
             print("harga          : Rp.",data_price[pilih_no])
             print("pesan          : ",pilih_jumlah,"pcs")
             print("Total          : Rp.",jumlah)
             print("pembayaran     : ",daftar_pembayaran[pilih_pembayaran])
             
    else:
         print("id metode pembayaran tidak tersedia")
else:
     print("product id tersedia")