from san_pham import hien_thi_mot_san_pham, hien_thi_danh_sach


def tim_kiem_san_pham(ds):
    print("\n========== TIM KIEM SAN PHAM ==========")
    print("1. Tim theo ma san pham")
    print("2. Tim theo ten san pham")
    print("3. Tim theo nhom san pham")

    chon = input("Lua chon: ").strip()

    if chon not in ("1", "2", "3"):
        print("Lua chon khong hop le!")
        return

    tu_khoa = input("Nhap tu khoa: ").strip().lower()
    tim_thay = False

    for sp in ds:
        if chon == "1":
            if sp["MaSP"].lower() == tu_khoa:
                hien_thi_mot_san_pham(sp)
                tim_thay = True
        elif chon == "2":
            if tu_khoa in sp["TenSP"].lower():
                hien_thi_mot_san_pham(sp)
                tim_thay = True
        elif chon == "3":
            if tu_khoa in sp["NhomSP"].lower():
                hien_thi_mot_san_pham(sp)
                tim_thay = True

    if tim_thay == False:
        print("Khong tim thay san pham phu hop!")


def sap_xep_san_pham(ds):
    print("\n========== SAP XEP SAN PHAM ==========")
    print("1. Sap xep theo ten")
    print("2. Sap xep theo so luong ton")
    chon = input("Lua chon: ").strip()

    print("1. Tang dan")
    print("2. Giam dan")
    chieu = input("Lua chon thu tu: ").strip()

    if chon not in ("1", "2") or chieu not in ("1", "2"):
        print("Lua chon khong hop le!")
        return

    n = len(ds)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if chon == "1":
                gia_tri_1 = ds[j]["TenSP"].lower()
                gia_tri_2 = ds[j + 1]["TenSP"].lower()
            else:
                gia_tri_1 = ds[j]["SoLuongTon"]
                gia_tri_2 = ds[j + 1]["SoLuongTon"]

            if chieu == "1" and gia_tri_1 > gia_tri_2:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]
            elif chieu == "2" and gia_tri_1 < gia_tri_2:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]

    print("Sap xep thanh cong!")
    hien_thi_danh_sach(ds)