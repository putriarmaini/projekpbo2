import wx
import noname
# import routes
import database

class subClass(noname.frameLogin):
    def __init__(self, parent):
        noname.frameLogin.__init__(self,parent)
        self.database = database.Database()
        

    def RegisterButton(self, event):
        username = self.m_username.GetValue()
        password = self.m_password.GetValue()
        hasil = (username, password)
        if (self.database.set_query("INSERT INTO admin (username, password) VALUES (%s, %s)", hasil)\
                .execute()\
                .get_rowcount() > 0):
            wx.MessageBox("Data Admin berhasil Ditambah", "Berhasil")
        else:
            wx.MessageBox("Data Admin gagal Ditambah", "Gagal")

    def LoginButton(self, event):
        username = self.m_username.GetValue()
        password = self.m_password.GetValue()
        queryResult = self.database.set_query("SELECT * FROM `admin` WHERE `username` = '%s'"%(username))\
                                   .fetch()
        if (queryResult is not None):
            if (password == queryResult[2]):
                self.m_password.SetValue("")
                wx.MessageBox("Anda Berhasil Masuk")
                # routes.Init.subClass.Hide()
                # routes.Init.buku.Show()
            else:
                wx.MessageBox("Username atau Password tidak sesuai", "Login Gagal")
                self.m_password.SetValue("")
        else:
            wx.MessageBox("User dengan username tersebut tidak ditemukan", "Login Gagal")
            self.m_password.SetValue("")

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()
        
