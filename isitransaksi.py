import wx
import lihattransaksi
import database

class databuku(lihattransaksi.MyFrame1):
    def __init__(self,parent):
        wx.MessageBox('Data Transaksi Toko Buku', 'Welcome', wx.OK | wx.ICON_INFORMATION)
        lihattransaksi.MyFrame1.__init__(self, parent)
        self.database = database.Database()
        self.data()

    def data(self):
        column_names = self.database.get_tablecolumn(tableName="penjualan")
        datasets = self.database.set_query("SELECT * FROM penjualan").fetchall()
        print("data", datasets)

        self.m_grid1.DeleteRows(0, self.m_grid1.GetNumberRows())
        self.m_grid1.DeleteCols(0, self.m_grid1.GetNumberCols())

        self.m_grid1.AppendCols(len(column_names))
        self.m_grid1.AppendRows(len(datasets))

        # column label
        for index in range(len(column_names)):
            self.m_grid1.SetColLabelValue(index, column_names[index])
        # colum cell data
        for i in range(len(datasets)):
            for j in range(len(datasets[i])):
                field = "%s"%datasets[i][j]
                self.m_grid1.SetCellValue(i,j, field)

    
    def m_button7OnButtonClick( self, event ):
        row = event.GetRow()
        col = event.GetCol()

if __name__ == "__main__":
    app = wx.App()
    frame = databuku(parent=None)
    frame.Show()
    app.MainLoop()