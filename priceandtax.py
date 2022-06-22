print("""Harga :
1. Kaset = 103.450
2. Basara = 250.250
3. Downhill = 267.520
4. SmackD = 654.200
5. GTA = 317.530 """)

price = None
item = None
harga =[]
barang = []
temp = 0

while True:
    buy = input("Pilih barang yang ingin anda beli : ")

    if buy == '1':
        price = 103450
        item = "Kaset"
        print(f"Anda membeli {item} seharga {price}")
    elif buy == '2':
        item = "Basara"
        price = 250250
        print(f"anda membeli {item} seharga {price} ")    
    elif buy == '3':
        item = "Downhill"
        price = 267520
        print(f"anda membeli {item} seharga {price} ")    
    elif buy == '4':
        item = "SmackD"
        price = 654200
        print(f"anda membeli {item} seharga {price} ")    
    elif buy == '5':
        item = "GTA"
        price = 317530
        print(f"anda membeli {item} seharga {price} ")

    opt = input("apakah anda ingin beli lagi ?")
    harga.append(price)
    barang.append(item)
    if opt == 'n':
        break

for x in harga:
    x = int(x)

    temp += x


print(harga)
tax = (10/100) * temp

total = tax + temp

print(f"Anda membeli {barang} dengan harga Rp{total:,.0f}".format(total).replace(',','.'))
