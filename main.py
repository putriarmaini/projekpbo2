import wx
import daftarbuku

class buku(daftarbuku.framedaftarbuku):
    def __init__(self,parent):
        wx.MessageBox('Selamat datang di Gudang Toko Buku', 'Welcome', wx.OK | wx.ICON_INFORMATION)
        daftarbuku.framedaftarbuku.__init__(self, parent)
    
    def __init__(self, parent):
        daftarbuku.framedaftarbuku.__init__(self,parent)
        self.database = {"tokobuku":"buku"}
    
    def cek(self):
        self.namabuku = self.inputnamabuku.GetValue()
        self.jenisbuku = self.inputjenisbuku.GetValue()
        self.hargabuku = self.inputhargabuku.GetValue()
        self.stokbuku = self.inputstokbuku.GetValue()

    def m_button2OnButtonClick(self, event):
        self.cek()
        self.database[self.namabuku] = self.jenisbuku
        wx.MessageBox("Data Buku Berhasil di Tambahkan")

if __name__ == "__main__":
    app = wx.App()
    frame = buku(parent=None)
    frame.Show()
    app.MainLoop()