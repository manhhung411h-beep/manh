from nhap_lieu import nhap_so
from san_pham import tim_san_pham, cap_nhat_trang_thai


def nhap_kho(ds):
    print("\n========== NHAP KHO ==========")
    ma = input("Nhap ma san pham: ").strip()
    sp = tim_san_pham(ds, ma)

    if sp is None:
        print("Khong tim thay san pham!")
        return

    so_luong = nhap_so("So luong can nhap: ", False)
    sp["SoLuongTon"] = sp["SoLuongTon"] + so_luong

    cap_nhat_trang_thai(sp)
    print("Nhap kho thanh cong!")
    print("So luong ton moi:", sp["SoLuongTon"])


def xuat_kho(ds):
    print("\n========== XUAT KHO ==========")
    ma = input("Nhap ma san pham: ").strip()
    sp = tim_san_pham(ds, ma)

    if sp is None:
        print("Khong tim thay san pham!")
        return

    print("So luong ton hien tai:", sp["SoLuongTon"])
    so_luong = nhap_so("So luong can xuat: ", False)

    if so_luong > sp["SoLuongTon"]:
        print("So luong xuat vuot qua so luong ton!")
    else:
        sp["SoLuongTon"] = sp["SoLuongTon"] - so_luong
        cap_nhat_trang_thai(sp)
        print("Xuat kho thanh cong!")
        print("So luong ton con lai:", sp["SoLuongTon"])
        