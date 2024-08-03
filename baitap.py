n = int(input ("Nhap so tu nhien: "))
kq = True
if n <= 1:
    kq = False

for i in range(2, n//2+1):
    if n % i == 0:
        kq = False
    if kq == True:
        print("la so nguyen to")
    else:
        print("khong la so nguyen to")