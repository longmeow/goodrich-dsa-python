from bai1_1 import *


studentInfo = {
    "20200365": {
        'maSV': 20200365,
        'hoTen': 'Nguyen Hoang Long',
        'nickname': 'longmeow',
        'gioiTinh': 'Male',
        'ngaySinh': '26-4',
        'diaChi': 'Tuyen Quang',
        'lop': 'ETTN-K65',
        'khoa': 'ET'
    },
    "20200654": {
        'maSV': 20200654,
        'hoTen': 'Nguyen Van Truong',
        'nickname': 'mua1tang1',
        'gioiTinh': 'Male',
        'ngaySinh': '26-12',
        'diaChi': 'Hai Duong',
        'lop': 'ETTN-K65',
        'khoa': 'ET'
    },
    "20206203": {
        'maSV': 20206203,
        'hoTen': 'Nguyen Phuong Linh',
        'nickname': 'Idss',
        'gioiTinh': 'Female',
        'ngaySinh': '16-12',
        'diaChi': 'Ha Noi',
        'lop': 'ETTN-K65',
        'khoa': 'ET'
    },
    "20200646": {
        'maSV': 20200646,
        'hoTen': 'Nguyen Quoc Trung',
        'nickname': 'conReTuyenQuang',
        'gioiTinh': 'Male',
        'ngaySinh': '21-1',
        'diaChi': 'Thuong Hai',
        'lop': 'ETTN-K65',
        'khoa': 'ET'
    },
}


# Tạo ra Obj SinhVien dựa trên StudentID từ database, có thể có nhiều database khác nhau
def createSV(studentID: int, database: dict) -> SinhVien:
    for key, value in database.items():
        if (int(key) == studentID):
            sinhVien = SinhVien(value['maSV'], value['hoTen'], value['gioiTinh'],
                                value['ngaySinh'], value['diaChi'], value['lop'], value['khoa'])
    
    return sinhVien


# Khởi tạo một ListSV từ các Obj sinhVien được tạo ra từ database
def construct(data: list[SinhVien]) -> List:
    first = None
    # Duyệt ngược lại từ cuối danh sách sinh viên
    for i in reversed(range(len(data))):
        first = Node(data[i], first)
 
    return List(first, Node(data[-1]))


# Hàm thêm một sinh viên mới vào danh sách ListSV đã sắp xếp
def sortedInsert(first, newNode):
 
    dummy = Node(None, None)
    current = dummy
    dummy.link = first
 
    while current.link and current.link.data < newNode.data:
        current = current.link
 
    newNode.link = current.link
    current.link = newNode
    return dummy.link


# Sắp xếp danh sách
def insertSort(first):
    sortedListSV = None       
    current = first      
 
    while current:
        link = current.link
        sortedListSV = sortedInsert(sortedListSV, current)
        current = link
 
    return sortedListSV
 
 
def main():
        
    longMeow = createSV(20200365, studentInfo)
    vanTruong = createSV(20200654, studentInfo)
    phuongLinh = createSV(20206203, studentInfo)
    quocTrung = createSV(20200646, studentInfo)
    studentList = [longMeow, vanTruong, phuongLinh, quocTrung]
    
    # In ra tên các sinh viên đã được khởi tạo
    #[print(studentName) for studentName in [longMeow, vanTruong, phuongLinh, quocTrung]]

    # Khởi tạo các Node một cách ngẫu nhiên (chưa sắp xếp thứ tự theo MSSV)
    ListSV = construct(studentList)
    
    # Sắp xếp sv theo mssv tăng dần và in ra blabla
    sortedStudentList = sorted(studentList, key=lambda sinhvien: sinhvien.maSV)
    for i in sortedStudentList:
        print(i.maSV)
    
    
if __name__ == "__main__":
    main()
    


