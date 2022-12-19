class Ngay:
    def __init__(self, ngay: int, thang: int, nam: int):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
        

class SinhVien:
    def __init__(self, maSV: str, hoTen: str, gioiTinh: int, ngaySinh: Ngay, diaChi: str, lop: str, khoa: str):
        self.maSV = maSV
        self.hoTen = hoTen
        self.gioiTinh = gioiTinh
        self.ngaySinh = ngaySinh
        self.diaChi = diaChi
        self.lop = lop
        self.khoa = khoa
        
    def __str__(self) -> str:
        return self.hoTen


class Node:
    def __init__(self, data: SinhVien, link=None):
        self.data = data
        self.link = link
    
    def __str__(self) -> str:
        return self.data.maSV
        
        

class List:
    def __init__(self, first: Node, last:Node):
        self.first = first
        self.last = last
