import wx
import trs1
import database
import routes

class transaksi(trs1.MyFrame1):
    def __init__(self,parent):
        wx.MessageBox('Selamat Datang Di Kasir Toko Buku', 'Welcome', wx.OK | wx.ICON_INFORMATION)
        trs1.MyFrame1.__init__(self, parent)
        self.database = database.Database()
    
    def jumlah(self, event):
        namabuku = self.InpuNama.GetValue()
        jumlahbuku = self.InputJumlah.GetValue()
        hargabuku = self.InputHarga.GetValue()
        jual = (namabuku, jumlahbuku, hargabuku)
        if (self.database.set_query("INSERT INTO penjualan (namabuku, jumlahbuku, hargabuku) VALUES (%s, %s, %s)", jual)\
                .execute()\
                .get_rowcount() > 0):
            wx.MessageBox("Data Penjualan berhasil Ditambah", "Berhasil")
        else:
            wx.MessageBox("Data Penjualan gagal Ditambah", "Gagal")

        a = int(self.InputJumlah.GetValue())
        b = int(self.InputHarga.GetValue())
        c = a * b
        self.Hasil.SetValue(str(c))

if __name__ == "__main__":
    app = wx.App(False)
    frame = transaksi(None)
    frame.Show(True)
    app.MainLoop()