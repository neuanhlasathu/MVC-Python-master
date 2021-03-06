import sinhvien_db

class SinhvienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng sinhvien
    def show_all_sinhvien(self):
        items = self.model.get_all_sinhvien()
        self.view.display_all_sinhvien(items)

    #Phương thức insert
    def them_sinhvien(self, hoten):
        resultIDstudent = self.model.them_sinhvien(hoten)
        self.view.ket_qua_insert(resultIDstudent)
    #Phương thức update
    def update_sinhvien(self, hoten, idstudent):
        self.model.update_sinhvien(hoten, idstudent)
        self.view.ket_qua_update()

    #Phương thức delete
    def delete_sinhvien(self, idstudent):
        self.model.delete_sinhvien(idstudent)
        self.view.ket_qua_delete()