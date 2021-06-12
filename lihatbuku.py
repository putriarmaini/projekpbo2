# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Daftar Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.gridbuku = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridbuku.CreateGrid( 5, 4 )
		self.gridbuku.EnableEditing( True )
		self.gridbuku.EnableGridLines( True )
		self.gridbuku.EnableDragGridSize( False )
		self.gridbuku.SetMargins( 0, 0 )

		# Columns
		self.gridbuku.EnableDragColMove( False )
		self.gridbuku.EnableDragColSize( True )
		self.gridbuku.SetColLabelSize( 30 )
		self.gridbuku.SetColLabelValue( 0, u"id" )
		self.gridbuku.SetColLabelValue( 1, u"Nama Buku" )
		self.gridbuku.SetColLabelValue( 2, u"Jenis Buku" )
		self.gridbuku.SetColLabelValue( 3, u"Harga Buku" )
		self.gridbuku.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridbuku.EnableDragRowSize( True )
		self.gridbuku.SetRowLabelSize( 80 )
		self.gridbuku.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridbuku.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.gridbuku, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.inputbuku = wx.Button( self, wx.ID_ANY, u"kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.inputbuku, 0, wx.ALL, 5 )

		self.inputransaksi = wx.Button( self, wx.ID_ANY, u"Input Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.inputransaksi, 0, wx.ALL, 5 )

		self.daftartransaksi = wx.Button( self, wx.ID_ANY, u"Daftar Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.daftartransaksi, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.gridbuku.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.gridbukuOnGridSelectCell )
		self.inputbuku.Bind( wx.EVT_BUTTON, self.inputbukuOnButtonClick )
		self.inputransaksi.Bind( wx.EVT_BUTTON, self.inputransaksiOnButtonClick )
		self.daftartransaksi.Bind( wx.EVT_BUTTON, self.daftartransaksiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def gridbukuOnGridSelectCell( self, event ):
		event.Skip()

	def inputbukuOnButtonClick( self, event ):
		event.Skip()

	def inputransaksiOnButtonClick( self, event ):
		event.Skip()

	def daftartransaksiOnButtonClick( self, event ):
		event.Skip()


