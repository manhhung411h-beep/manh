from nhap_lieu import nhap_chuoi, nhap_so


def tao_san_pham(ma, ten, nhom, don_vi, nha_cung_cap,
                 gia_nhap, gia_ban, so_luong, muc_ton):
    san_pham = {
        "MaSP": ma,
        "TenSP": ten,
        "NhomSP": nhom,
        "DonViTinh": don_vi,
        "NhaCungCap": nha_cung_cap,
        "GiaNhap": gia_nhap,
        "GiaBan": gia_ban,
        "SoLuongTon": so_luong,
        "MucTonToiThieu": muc_ton,
        "TrangThai": ""
    }

    cap_nhat_trang_thai(san_pham)
    return san_pham


def cap_nhat_trang_thai(sp):
    if sp["SoLuongTon"] == 0:
        sp["TrangThai"] = "Het hang"
    elif sp["SoLuongTon"] < sp["MucTonToiThieu"]:
        sp["TrangThai"] = "Sap het hang"
    else:
        sp["TrangThai"] = "Con hang"


def tim_san_pham(ds, ma):
    for sp in ds:
        if sp["MaSP"].lower() == ma.lower():
            return sp

    return None


def them_san_pham(ds):
    print("\n========== THEM SAN PHAM ==========")

    while True:
        ma = nhap_chuoi("Ma san pham: ").upper()

        if tim_san_pham(ds, ma) is not None:
            print("Ma san pham da ton tai!")
        else:
            break

    ten = nhap_chuoi("Ten san pham: ")
    nhom = nhap_chuoi("Nhom san pham: ")
    don_vi = nhap_chuoi("Don vi tinh: ")
    nha_cung_cap = nhap_chuoi("Nha cung cap: ")
    gia_nhap = nhap_so("Gia nhap: ")
    gia_ban = nhap_so("Gia ban: ")
    so_luong = nhap_so("So luong ton: ")
    muc_ton = nhap_so("Muc ton toi thieu: ")

    sp = tao_san_pham(
        ma, ten, nhom, don_vi, nha_cung_cap,
        gia_nhap, gia_ban, so_luong, muc_ton
    )

    ds.append(sp)
    print("Them san pham thanh cong!")


def tinh_gia_tri_ton(sp):
    return sp["GiaNhap"] * sp["SoLuongTon"]


def hien_thi_mot_san_pham(sp):
    print("-" * 55)
    print("Ma san pham       :", sp["MaSP"])
    print("Ten san pham      :", sp["TenSP"])
    print("Nhom san pham     :", sp["NhomSP"])
    print("Don vi tinh       :", sp["DonViTinh"])
    print("Nha cung cap      :", sp["NhaCungCap"])
    print("Gia nhap          :", sp["GiaNhap"])
    print("Gia ban           :", sp["GiaBan"])
    print("So luong ton      :", sp["SoLuongTon"])
    print("Muc ton toi thieu :", sp["MucTonToiThieu"])
    print("Trang thai        :", sp["TrangThai"])
    print("Gia tri ton kho   :", tinh_gia_tri_ton(sp))


def hien_thi_danh_sach(ds):
    print("\n================ DANH SACH SAN PHAM ================")

    if len(ds) == 0:
        print("Danh sach san pham dang rong!")
        return

    tieu_de = ("MaSP", "TenSP", "NhomSP", "GiaNhap", "GiaBan", "Ton", "TrangThai")

    print("{:<9} {:<23} {:<17} {:>10} {:>10} {:>7} {:<14}".format(
        tieu_de[0], tieu_de[1], tieu_de[2], tieu_de[3],
        tieu_de[4], tieu_de[5], tieu_de[6]
    ))
    print("-" * 100)

    for sp in ds:
        print("{:<9} {:<23} {:<17} {:>10} {:>10} {:>7} {:<14}".format(
            sp["MaSP"],
            sp["TenSP"][:23],
            sp["NhomSP"][:17],
            sp["GiaNhap"],
            sp["GiaBan"],
            sp["SoLuongTon"],
            sp["TrangThai"]
        ))

    print("-" * 100)
    print("Tong so san pham:", len(ds))


def cap_nhat_san_pham(ds):
    print("\n========== CAP NHAT SAN PHAM ==========")
    ma = input("Nhap ma san pham can cap nhat: ").strip()
    sp = tim_san_pham(ds, ma)

    if sp is None:
        print("Khong tim thay san pham!")
        return

    hien_thi_mot_san_pham(sp)
    print("Nhan Enter neu muon giu lai thong tin cu.")

    ten = input("Ten san pham moi: ").strip()
    nhom = input("Nhom san pham moi: ").strip()
    don_vi = input("Don vi tinh moi: ").strip()
    nha_cung_cap = input("Nha cung cap moi: ").strip()

    if ten != "":
        sp["TenSP"] = ten
    if nhom != "":
        sp["NhomSP"] = nhom
    if don_vi != "":
        sp["DonViTinh"] = don_vi
    if nha_cung_cap != "":
        sp["NhaCungCap"] = nha_cung_cap

    print("Nhap gia tri moi. Nhap -1 neu muon giu gia tri cu.")

    while True:
        try:
            gia_nhap = int(input("Gia nhap moi: "))
            if gia_nhap == -1:
                break
            elif gia_nhap < 0:
                print("Gia nhap khong duoc am!")
            else:
                sp["GiaNhap"] = gia_nhap
                break
        except ValueError:
            print("Vui long nhap so nguyen!")

    while True:
        try:
            gia_ban = int(input("Gia ban moi: "))
            if gia_ban == -1:
                break
            elif gia_ban < 0:
                print("Gia ban khong duoc am!")
            else:
                sp["GiaBan"] = gia_ban
                break
        except ValueError:
            print("Vui long nhap so nguyen!")

    while True:
        try:
            so_luong = int(input("So luong ton moi: "))
            if so_luong == -1:
                break
            elif so_luong < 0:
                print("So luong khong duoc am!")
            else:
                sp["SoLuongTon"] = so_luong
                break
        except ValueError:
            print("Vui long nhap so nguyen!")

    while True:
        try:
            muc_ton = int(input("Muc ton toi thieu moi: "))
            if muc_ton == -1:
                break
            elif muc_ton < 0:
                print("Muc ton khong duoc am!")
            else:
                sp["MucTonToiThieu"] = muc_ton
                break
        except ValueError:
            print("Vui long nhap so nguyen!")

    cap_nhat_trang_thai(sp)
    print("Cap nhat san pham thanh cong!")


def xoa_san_pham(ds):
    print("\n========== XOA SAN PHAM ==========")
    ma = input("Nhap ma san pham can xoa: ").strip()
    sp = tim_san_pham(ds, ma)

    if sp is None:
        print("Khong tim thay san pham!")
        return

    hien_thi_mot_san_pham(sp)
    xac_nhan = input("Ban co chac chan muon xoa? (y/n): ").lower()

    if xac_nhan == "y":
        ds.remove(sp)
        print("Da xoa san pham!")
    else:
        print("Da huy thao tac xoa.")