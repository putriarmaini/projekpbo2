import wx
import noname

class subClass(noname.frameLogin):
    def __init__(self, parent):
        noname.frameLogin.__init__(self,parent)
        self.database = {"user":"admin"}

    def cek(self):
        self.username = self.m_username.GetValue()
        self.password = self.m_password.GetValue()

    def RegisterButton(self, event):
        self.cek()
        self.database[self.username] = self.password
        wx.MessageBox("Pendaftaran Berhasil")

    def LoginButton(self, event):
        self.cek()
        try:
            if self.database[self.username] == self.password:
                wx.MessageBox("Login Berhasil")
            else:
                wx.MessageBox("Login Gagal")

        except:
            wx.MessageBox("Login Gagal")

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()
        
