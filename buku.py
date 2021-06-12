import wx
import daftarbuku
import database
import routes

class tambahbuku(daftarbuku.framedaftarbuku):
    def __init__(self,parent):
        wx.MessageBox('Selamat datang di Gudang Toko Buku', 'Welcome', wx.OK | wx.ICON_INFORMATION)
        daftarbuku.framedaftarbuku.__init__(self, parent)
        self.database = database.Database()

    def m_button2OnButtonClick(self, event):
        nama_buku = self.inputnamabuku.GetValue()
        jenis_buku = self.inputjenisbuku.GetValue()
        harga_buku = self.inputhargabuku.GetValue()
        stok_buku = self.inputstokbuku.GetValue()
        hasilbuku = (nama_buku, jenis_buku, harga_buku, stok_buku)
        if (self.database.set_query("INSERT INTO buku (nama_buku, jenis_buku, harga_buku, stok_buku) VALUES (%s, %s, %s, %s)", hasilbuku)\
                .execute()\
                .get_rowcount() > 0):
            wx.MessageBox("Data Buku berhasil Ditambah", "Berhasil")
        else:
            wx.MessageBox("Data Buku gagal Ditambah", "Gagal")
    
    def btnlihatbuku(self, event):
        routes.Init.bagiantambah.Hide()
        routes.Init.bagianbuku.Show()


if __name__ == "__main__":
    app = wx.App()
    frame = tambahbuku(parent=None)
    frame.Show()
    app.MainLoop()

