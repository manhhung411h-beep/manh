from cau_hinh import TEN_FILE

from san_pham import (
    them_san_pham,
    hien_thi_danh_sach,
    cap_nhat_san_pham,
    xoa_san_pham
)

from tim_kiem import tim_kiem_san_pham, sap_xep_san_pham
from thong_ke import thong_ke_kho
from kho import nhap_kho, xuat_kho
from xu_ly_file import luu_du_lieu, doc_du_lieu, khoi_tao_du_lieu


def hien_thi_menu():
    print("\n========== QUAN LY NHAP XUAT KHO ==========")
    print("1. Them san pham")
    print("2. Hien thi danh sach san pham")
    print("3. Cap nhat san pham")
    print("4. Xoa san pham")
    print("5. Tim kiem san pham")
    print("6. Sap xep san pham")
    print("7. Tinh toan va thong ke")
    print("8. Nhap kho")
    print("9. Xuat kho")
    print("10. Luu du lieu")
    print("11. Doc du lieu")
    print("0. Thoat")
    print("===========================================")


def main():
    ds = khoi_tao_du_lieu()

    while True:
        hien_thi_menu()
        chon = input("Lua chon cua ban: ").strip()

        if chon == "1":
            them_san_pham(ds)

        elif chon == "2":
            hien_thi_danh_sach(ds)

        elif chon == "3":
            cap_nhat_san_pham(ds)

        elif chon == "4":
            xoa_san_pham(ds)

        elif chon == "5":
            tim_kiem_san_pham(ds)

        elif chon == "6":
            sap_xep_san_pham(ds)

        elif chon == "7":
            thong_ke_kho(ds)

        elif chon == "8":
            nhap_kho(ds)

        elif chon == "9":
            xuat_kho(ds)

        elif chon == "10":
            luu_du_lieu(ds)

        elif chon == "11":
            ds_moi = doc_du_lieu(TEN_FILE)

            if ds_moi is not None:
                ds = ds_moi

        elif chon == "0":
            xac_nhan = input(
                "Ban co muon luu du lieu truoc khi thoat? (y/n): "
            )

            if xac_nhan.lower() == "y":
                luu_du_lieu(ds)

            print("Cam on ban da su dung chuong trinh!")
            break

        else:
            print("Lua chon khong hop le. Vui long chon lai!")


if __name__ == "__main__":
    main()