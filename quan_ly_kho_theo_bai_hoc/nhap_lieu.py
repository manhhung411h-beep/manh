def nhap_chuoi(thong_bao):
    while True:
        gia_tri = input(thong_bao).strip()

        if gia_tri == "":
            print("Thong tin khong duoc de trong!")
        elif "|" in gia_tri:
            print("Khong duoc nhap ky tu |")
        else:
            return gia_tri


def nhap_so(thong_bao, cho_phep_so_0=True):
    while True:
        try:
            gia_tri = int(input(thong_bao))

            if gia_tri < 0:
                print("Gia tri khong duoc am!")
            elif gia_tri == 0 and cho_phep_so_0 == False:
                print("Gia tri phai lon hon 0!")
            else:
                return gia_tri

        except ValueError:
            print("Vui long nhap so nguyen hop le!")