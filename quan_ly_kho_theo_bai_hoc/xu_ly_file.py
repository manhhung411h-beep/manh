import os

from cau_hinh import TEN_FILE, TEN_FILE_MAU
from san_pham import tao_san_pham, tim_san_pham


def luu_du_lieu(ds):
    try:
        print("\nDang luu du lieu...")
        print("Duong dan file:", TEN_FILE)
        print("So san pham:", len(ds))

        with open(TEN_FILE, "w", encoding="utf-8") as tep:
            for sp in ds:
                dong = (
                    sp["MaSP"] + "|" +
                    sp["TenSP"] + "|" +
                    sp["NhomSP"] + "|" +
                    sp["DonViTinh"] + "|" +
                    sp["NhaCungCap"] + "|" +
                    str(sp["GiaNhap"]) + "|" +
                    str(sp["GiaBan"]) + "|" +
                    str(sp["SoLuongTon"]) + "|" +
                    str(sp["MucTonToiThieu"]) + "|" +
                    sp["TrangThai"] + "\n"
                )
                tep.write(dong)

        print("Luu du lieu thanh cong!")

    except OSError as loi:
        print("Loi khi ghi file:", loi)


def doc_du_lieu(ten_file):
    ds_moi = []

    try:
        if os.path.exists(ten_file) == False:
            print("File khong ton tai:", ten_file)
            return None

        with open(ten_file, "r", encoding="utf-8") as tep:
            for dong in tep:
                dong = dong.strip()

                if dong == "":
                    continue

                thong_tin = dong.split("|")

                if len(thong_tin) != 10:
                    print("Mot dong trong file khong dung cau truc!")
                    return None

                ma = thong_tin[0]
                ten = thong_tin[1]
                nhom = thong_tin[2]
                don_vi = thong_tin[3]
                nha_cung_cap = thong_tin[4]

                try:
                    gia_nhap = int(thong_tin[5])
                    gia_ban = int(thong_tin[6])
                    so_luong = int(thong_tin[7])
                    muc_ton = int(thong_tin[8])
                except ValueError:
                    print("Du lieu so trong file khong hop le!")
                    return None

                if (ma == "" or ten == "" or nhom == ""
                        or don_vi == "" or nha_cung_cap == ""):
                    print("File co thong tin bat buoc bi trong!")
                    return None

                if gia_nhap < 0 or gia_ban < 0 or so_luong < 0 or muc_ton < 0:
                    print("File co gia tri am!")
                    return None

                if tim_san_pham(ds_moi, ma) is not None:
                    print("File co ma san pham bi trung:", ma)
                    return None

                sp = tao_san_pham(
                    ma, ten, nhom, don_vi, nha_cung_cap,
                    gia_nhap, gia_ban, so_luong, muc_ton
                )
                ds_moi.append(sp)

        print("Doc file thanh cong. So san pham:", len(ds_moi))
        return ds_moi

    except OSError:
        print("Khong the doc file!")
        return None


def khoi_tao_du_lieu():
    ds = doc_du_lieu(TEN_FILE)

    if ds is not None:
        return ds

    ds = doc_du_lieu(TEN_FILE_MAU)

    if ds is not None:
        print("Chuong trinh dang su dung du lieu mau.")
        return ds

    print("Danh sach san pham hien dang rong.")
    return []