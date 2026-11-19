from san_pham import hien_thi_mot_san_pham

tinh_nhanh_gia_tri_ton = lambda sp: sp["GiaNhap"] * sp["SoLuongTon"]


def thong_ke_kho(ds):
    print("\n========== THONG KE KHO ==========")

    if len(ds) == 0:
        print("Chua co du lieu de thong ke!")
        return

    tong_so_luong = 0
    tong_gia_tri = 0
    so_hang_sap_het = 0

    for sp in ds:
        tong_so_luong = tong_so_luong + sp["SoLuongTon"]
        tong_gia_tri = tong_gia_tri + tinh_nhanh_gia_tri_ton(sp)

        if sp["SoLuongTon"] < sp["MucTonToiThieu"]:
            so_hang_sap_het = so_hang_sap_het + 1

    print("Tong so mat hang:", len(ds))
    print("Tong so luong hang:", tong_so_luong)
    print("Tong gia tri ton kho:", tong_gia_tri, "VND")
    print("So san pham duoi muc ton toi thieu:", so_hang_sap_het)

    cac_nhom = set()

    for sp in ds:
        cac_nhom.add(sp["NhomSP"])

    print("\nTHONG KE THEO NHOM SAN PHAM")
    for nhom in cac_nhom:
        dem = 0
        for sp in ds:
            if sp["NhomSP"] == nhom:
                dem = dem + 1
        print(nhom, ":", dem, "san pham")

    print("\nSAN PHAM DUOI MUC TON TOI THIEU")
    co_san_pham = False

    for sp in ds:
        if sp["SoLuongTon"] < sp["MucTonToiThieu"]:
            hien_thi_mot_san_pham(sp)
            co_san_pham = True

    if co_san_pham == False:
        print("Khong co san pham nao!")