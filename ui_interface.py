# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 820)
        MainWindow.setStyleSheet(" *{\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    background: transparent;\n"
"    padding:0;\n"
"    margin:0;\n"
"    color: #fff;\n"
"}\n"
"#centralwidget{\n"
"    background-color:#1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"  background-color:#16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"  text-align: left;\n"
"  padding:5px 10px; \n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"\n"
"}\n"
"\n"
"#centerMenuSubContainer,#rightMenuSubContainer{\n"
"    background-color:#2c313c;\n"
"}\n"
"\n"
"#frame_4,#frame_8,#popupNotificationSubContainer{\n"
"    background-color:#16191d;\n"
"    border-radius:10px;\n"
"\n"
"}\n"
"\n"
"#headerContiner{\n"
"    background-color:#2c313c;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leftMenuContainer.setStyleSheet("")
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(self.frame)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons_2/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(70, 70))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.homeBtn = QtWidgets.QPushButton(self.frame_2)
        self.homeBtn.setStyleSheet("background-color: #1f232a")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons_2/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(70, 70))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_3.addWidget(self.homeBtn)
        self.dataBtn = QtWidgets.QPushButton(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons_2/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QtCore.QSize(70, 70))
        self.dataBtn.setObjectName("dataBtn")
        self.verticalLayout_3.addWidget(self.dataBtn)
        self.reportBtn = QtWidgets.QPushButton(self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons_2/printer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QtCore.QSize(70, 70))
        self.reportBtn.setObjectName("reportBtn")
        self.verticalLayout_3.addWidget(self.reportBtn)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsBtn = QtWidgets.QPushButton(self.frame_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons_2/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QtCore.QSize(70, 70))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_4.addWidget(self.settingsBtn)
        self.infoBtn = QtWidgets.QPushButton(self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons_2/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QtCore.QSize(70, 70))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_4.addWidget(self.infoBtn)
        self.helpBtn = QtWidgets.QPushButton(self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icons_2/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QtCore.QSize(70, 70))
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_4.addWidget(self.helpBtn)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.leftMenuSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.leftMenuContainer)
        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuContainer.setObjectName("centerMenuContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.centerMenuSubContainer = QtWidgets.QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuSubContainer.setObjectName("centerMenuSubContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.centerMenuSubContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.closeCenterMenuBtn = QtWidgets.QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icons_2/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon7)
        self.closeCenterMenuBtn.setIconSize(QtCore.QSize(40, 40))
        self.closeCenterMenuBtn.setObjectName("closeCenterMenuBtn")
        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setStyleSheet("")
        self.centerMenuPages.setObjectName("centerMenuPages")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.centerMenuPages.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.centerMenuPages.addWidget(self.page_3)
        self.verticalLayout_6.addWidget(self.centerMenuPages)
        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.centerMenuContainer)
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.headerContiner = QtWidgets.QWidget(self.mainBodyContainer)
        self.headerContiner.setObjectName("headerContiner")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.headerContiner)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.headerContiner)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setMaximumSize(QtCore.QSize(80, 40))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Fotos/images/Assa_Abloy_logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft)
        self.frame_6 = QtWidgets.QFrame(self.headerContiner)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.moreMenuBtn = QtWidgets.QPushButton(self.frame_6)
        self.moreMenuBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/icons_2/move.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreMenuBtn.setIcon(icon8)
        self.moreMenuBtn.setIconSize(QtCore.QSize(40, 40))
        self.moreMenuBtn.setObjectName("moreMenuBtn")
        self.horizontalLayout_6.addWidget(self.moreMenuBtn)
        self.profieMenuBtn = QtWidgets.QPushButton(self.frame_6)
        self.profieMenuBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/icons_2/map-pin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profieMenuBtn.setIcon(icon9)
        self.profieMenuBtn.setIconSize(QtCore.QSize(40, 40))
        self.profieMenuBtn.setObjectName("profieMenuBtn")
        self.horizontalLayout_6.addWidget(self.profieMenuBtn)
        self.horizontalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.headerContiner)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minimizeBtn = QtWidgets.QPushButton(self.frame_7)
        self.minimizeBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/icons_2/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon10)
        self.minimizeBtn.setIconSize(QtCore.QSize(30, 30))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_5.addWidget(self.minimizeBtn)
        self.restoreBtn = QtWidgets.QPushButton(self.frame_7)
        self.restoreBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/icons_2/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreBtn.setIcon(icon11)
        self.restoreBtn.setIconSize(QtCore.QSize(30, 30))
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout_5.addWidget(self.restoreBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame_7)
        self.closeBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/icons_2/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon12)
        self.closeBtn.setIconSize(QtCore.QSize(30, 30))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_5.addWidget(self.closeBtn)
        self.horizontalLayout_4.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_10.addWidget(self.headerContiner, 0, QtCore.Qt.AlignTop)
        self.mainbodyContent = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainbodyContent.sizePolicy().hasHeightForWidth())
        self.mainbodyContent.setSizePolicy(sizePolicy)
        self.mainbodyContent.setMinimumSize(QtCore.QSize(688, 198))
        self.mainbodyContent.setObjectName("mainbodyContent")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainbodyContent)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mainContentsContainer = QtWidgets.QWidget(self.mainbodyContent)
        self.mainContentsContainer.setObjectName("mainContentsContainer")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName("mainPages")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_12 = QtWidgets.QLabel(self.page_8)
        self.label_12.setGeometry(QtCore.QRect(9, 9, 731, 678))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/Fotos/images/marco.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.rect_label = QtWidgets.QLabel(self.page_8)
        self.rect_label.setGeometry(QtCore.QRect(90, 390, 100, 50))
        self.rect_label.setMaximumSize(QtCore.QSize(100, 50))
        self.rect_label.setStyleSheet("\n"
"background-image: url(:/Fotos/images/sensores.png);")
        self.rect_label.setText("")
        self.rect_label.setPixmap(QtGui.QPixmap(":/Fotos/images/sensores.png"))
        self.rect_label.setScaledContents(True)
        self.rect_label.setObjectName("rect_label")
        self.mainPages.addWidget(self.page_8)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.page_7)
        self.label_11.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_17.addWidget(self.label_11)
        self.mainPages.addWidget(self.page_7)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_14 = QtWidgets.QLabel(self.page_9)
        self.label_14.setMinimumSize(QtCore.QSize(200, 0))
        self.label_14.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_18.addWidget(self.label_14)
        self.mainPages.addWidget(self.page_9)
        self.verticalLayout_15.addWidget(self.mainPages)
        self.horizontalLayout_8.addWidget(self.mainContentsContainer)
        self.rightMenuContainer = QCustomSlideMenu(self.mainbodyContent)
        self.rightMenuContainer.setMinimumSize(QtCore.QSize(200, 400))
        self.rightMenuContainer.setMaximumSize(QtCore.QSize(232, 176))
        self.rightMenuContainer.setObjectName("rightMenuContainer")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.rightMenuSubContainer = QtWidgets.QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setMinimumSize(QtCore.QSize(200, 200))
        self.rightMenuSubContainer.setObjectName("rightMenuSubContainer")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_8 = QtWidgets.QFrame(self.rightMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.closeRightMenuBtn = QtWidgets.QPushButton(self.frame_8)
        self.closeRightMenuBtn.setText("")
        self.closeRightMenuBtn.setIcon(icon7)
        self.closeRightMenuBtn.setIconSize(QtCore.QSize(40, 40))
        self.closeRightMenuBtn.setObjectName("closeRightMenuBtn")
        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_12.addWidget(self.frame_8)
        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName("rightMenuPages")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.page_5)
        self.label_10.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_14.addWidget(self.label_10)
        self.frame_9 = QtWidgets.QFrame(self.page_5)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_13 = QtWidgets.QLabel(self.frame_10)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_20.addWidget(self.label_13)
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_20.addWidget(self.label_9)
        self.horizontalLayout_10.addWidget(self.frame_10)
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_17 = QtWidgets.QLabel(self.frame_12)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_22.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.frame_12)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_22.addWidget(self.label_16)
        self.horizontalLayout_10.addWidget(self.frame_12)
        self.verticalLayout_14.addWidget(self.frame_9, 0, QtCore.Qt.AlignHCenter)
        self.rightMenuPages.addWidget(self.page_5)
        self.verticalLayout_12.addWidget(self.rightMenuPages, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)
        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_10.addWidget(self.mainbodyContent)
        self.footeContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.footeContainer.setObjectName("footeContainer")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.footeContainer)
        self.horizontalLayout_11.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_11 = QtWidgets.QFrame(self.footeContainer)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_15 = QtWidgets.QLabel(self.frame_11)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_21.addWidget(self.label_15)
        self.horizontalLayout_11.addWidget(self.frame_11)
        self.sizeGrip = QtWidgets.QFrame(self.footeContainer)
        self.sizeGrip.setMinimumSize(QtCore.QSize(30, 30))
        self.sizeGrip.setMaximumSize(QtCore.QSize(40, 40))
        self.sizeGrip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizeGrip.setObjectName("sizeGrip")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11.addWidget(self.sizeGrip)
        self.verticalLayout_10.addWidget(self.footeContainer)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Position ( X, Y )"))
        self.dataBtn.setToolTip(_translate("MainWindow", "Data Analysis"))
        self.dataBtn.setText(_translate("MainWindow", "Data Analysis"))
        self.reportBtn.setToolTip(_translate("MainWindow", "Reports"))
        self.reportBtn.setText(_translate("MainWindow", "Reports"))
        self.settingsBtn.setToolTip(_translate("MainWindow", "Go to settings"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.infoBtn.setToolTip(_translate("MainWindow", "Information about the app"))
        self.infoBtn.setText(_translate("MainWindow", "Information"))
        self.helpBtn.setToolTip(_translate("MainWindow", "Get more help"))
        self.helpBtn.setText(_translate("MainWindow", "Help"))
        self.label.setText(_translate("MainWindow", "More Menu"))
        self.closeCenterMenuBtn.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label_2.setText(_translate("MainWindow", "Settings"))
        self.label_3.setText(_translate("MainWindow", "Information"))
        self.label_5.setText(_translate("MainWindow", "Help"))
        self.label_6.setText(_translate("MainWindow", "  Flow experiment"))
        self.moreMenuBtn.setToolTip(_translate("MainWindow", "More"))
        self.profieMenuBtn.setToolTip(_translate("MainWindow", "Profile"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "Minimize Window "))
        self.restoreBtn.setToolTip(_translate("MainWindow", "Restore Window"))
        self.closeBtn.setToolTip(_translate("MainWindow", "Close Window"))
        self.label_11.setText(_translate("MainWindow", "Data Analysis"))
        self.label_14.setText(_translate("MainWindow", "Reports"))
        self.label_7.setText(_translate("MainWindow", "Right Menu"))
        self.closeRightMenuBtn.setToolTip(_translate("MainWindow", "Close Menu"))
        self.label_8.setText(_translate("MainWindow", "Profile"))
        self.label_10.setText(_translate("MainWindow", "Position ( X, Y )"))
        self.label_13.setText(_translate("MainWindow", "( X ) AXIS"))
        self.label_9.setText(_translate("MainWindow", "( Y ) AXIS"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "Copyright Mequonic"))
from Custom_Widgets.Widgets import QCustomSlideMenu, QCustomStackedWidget
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
