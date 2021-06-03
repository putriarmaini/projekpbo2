import wx
import trs1

class transaksi(trs1.MyFrame1):
    def __init__(self,parent):
        wx.MessageBox('Selamat Datang Di Kasir Toko Buku', 'Welcome', wx.OK | wx.ICON_INFORMATION)
        trs1.MyFrame1.__init__(self, parent)
    
    def jumlah(self, event):
        a = int(self.InputJumlah.GetValue())
        b = int(self.InputHarga.GetValue())
        c = a * b
        self.Hasil.SetValue(str(c))

if __name__ == "__main__":
    app = wx.App(False)
    frame = transaksi(None)
    frame.Show(True)
    app.MainLoop()