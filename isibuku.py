import wx
import lihatbuku
import database

class databuku(lihatbuku.MyFrame1):
    def __init__(self,parent):
        wx.MessageBox('Data Buku pada Toko', 'Welcome', wx.OK | wx.ICON_INFORMATION)
        lihatbuku.MyFrame1.__init__(self, parent)
        self.database = database.Database()
        self.data()

    def data(self):
        column_names = self.database.get_tablecolumn(tableName="buku")
        datasets = self.database.set_query("SELECT * FROM buku").fetchall()
        print("data", datasets)

        self.gridbuku.DeleteRows(0, self.gridbuku.GetNumberRows())
        self.gridbuku.DeleteCols(0, self.gridbuku.GetNumberCols())

        self.gridbuku.AppendCols(len(column_names))
        self.gridbuku.AppendRows(len(datasets))

        # column label
        for index in range(len(column_names)):
            self.gridbuku.SetColLabelValue(index, column_names[index])
        # colum cell data
        for i in range(len(datasets)):
            for j in range(len(datasets[i])):
                field = "%s"%datasets[i][j]
                self.gridbuku.SetCellValue(i,j, field)

    
    def datagridOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        col = event.GetCol()

if __name__ == "__main__":
    app = wx.App()
    frame = databuku(parent=None)
    frame.Show()
    app.MainLoop()