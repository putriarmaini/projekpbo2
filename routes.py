import trs2
import main
import buku

class Init:
    loginPanel = main
    buku = buku

    @staticmethod
    def base(parent):
        Init.loginPanel = LoginPanel.LoginPanel(parent)
        Init.dashboardPanel = DashboardPanel.DashboardPanel(parent)
        Init.initPanel()

    @staticmethod
    def initPanel():
        Init.loginPanel.Hide()
        Init.dashboardPanel.Hide()


