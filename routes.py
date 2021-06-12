import trs2
import main
import buku
import isibuku
import isitransaksi

class Init:
    bagianlogin = main.subClass
    bagiantambah = buku.tambahbuku
    bagianbuku = isibuku.databuku
    bagiantransaksi = trs2.transaksi
    bagianpenjualan = isitransaksi.databuku

    @staticmethod
    def base(parent):
        Init.bagianlogin = main.subClass(parent)
        Init.bagiantambah = buku.tambahbuku(parent)
        Init.bagianbuku = isibuku.databuku(parent)
        Init.bagiantransaksi = trs2.transaksi(parent)
        Init.bagianpenjualan = isitransaksi.databuku(parent)
        Init.initPanel()

    @staticmethod
    def initPanel():
        Init.bagianlogin.Hide()
        Init.bagiantambah.Hide()
        Init.bagianbuku.Hide()
        Init.bagiantransaksi.Hide()
        Init.bagianpenjualan.Hide()

