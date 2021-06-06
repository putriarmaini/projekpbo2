# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class framedaftarbuku
###########################################################################

class framedaftarbuku ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Tambahkan Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.namabuku = wx.StaticText( self, wx.ID_ANY, u"Nama Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namabuku.Wrap( -1 )

		fgSizer1.Add( self.namabuku, 0, wx.ALL, 5 )

		self.inputnamabuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.inputnamabuku, 0, wx.ALL, 5 )

		self.jenisbuku = wx.StaticText( self, wx.ID_ANY, u"Jenis Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenisbuku.Wrap( -1 )

		fgSizer1.Add( self.jenisbuku, 0, wx.ALL, 5 )

		self.inputjenisbuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.inputjenisbuku, 0, wx.ALL, 5 )

		self.hargabuku = wx.StaticText( self, wx.ID_ANY, u"Harga Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hargabuku.Wrap( -1 )

		fgSizer1.Add( self.hargabuku, 0, wx.ALL, 5 )

		self.inputhargabuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.inputhargabuku, 0, wx.ALL, 5 )

		self.stokbuku = wx.StaticText( self, wx.ID_ANY, u"Stok Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stokbuku.Wrap( -1 )

		fgSizer1.Add( self.stokbuku, 0, wx.ALL, 5 )

		self.inputstokbuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.inputstokbuku, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.btnsimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnsimpan, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Lihat Daftar Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnsimpan.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.btnlihatbuku )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button2OnButtonClick( self, event ):
		event.Skip()

	def btnlihatbuku( self, event ):
		event.Skip()


