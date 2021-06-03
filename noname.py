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
## Class frameLogin
###########################################################################

class frameLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.username = wx.StaticText( self, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )

		bSizer1.Add( self.username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_username, 0, wx.ALL|wx.EXPAND, 5 )

		self.password = wx.StaticText( self, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )

		bSizer1.Add( self.password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_password, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_Register = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Register, 0, wx.ALL, 5 )

		self.m_Login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Login, 0, wx.ALL, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_Register.Bind( wx.EVT_BUTTON, self.RegisterButton )
		self.m_Login.Bind( wx.EVT_BUTTON, self.LoginButton )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def RegisterButton( self, event ):
		event.Skip()

	def LoginButton( self, event ):
		event.Skip()
