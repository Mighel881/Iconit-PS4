import time, json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import Iconit as main
from PIL import Image
import os
import Update


class Ui_ChangeIconWindow(object):
    def setupUi(
        self,
        ChangeIconWindow,
        IP,
        Port,
        Games,
        uFont,
        uIPath,
        uDPath,
        userHB,
        exGames,
        w,
        h,
        sysGames,
        modeSelected,
    ):
        self.ChangeIconWindow = ChangeIconWindow
        self.ver = Update.get_update_version()
        self.screenWidth = w
        self.screenHeight = h

        # Settings
        self.userFont = uFont
        self.userIPath = uIPath
        self.userDPath = uDPath
        self.userHB = userHB

        self.exGames = exGames
        self.sysGames = sysGames

        self.sysIconsAlgo = False
        if len(self.sysGames) > 0:
            self.sysIconsAlgo = True

        self.IP = IP
        self.Port = Port
        self.temp_path = main.temp_path
        self.img_dir = main.img_dir
        self.setting_path = main.setting_path
        self.modeSelected = modeSelected
        self.Games = Games
        temp = self.temp_path + "MegaSRX\\metadata\\" + self.modeSelected + "\\"
        self.CUSA_img = ""
        for i in temp:
            if i == "\\":
                self.CUSA_img += "/"
            else:
                self.CUSA_img += i
        # Get all icon names from local path sorted by value(gametitle)
        dirs = os.listdir(temp)
        self.imgs = []
        for i in self.Games.keys():
            self.imgs.append(i)

        # for img in dirs:
        #     if "png" in img:
        #         self.imgs.append(img)
        self.changeIconPath = ""
        self.changeBgPath = ""
        self.img_limit = len(self.imgs)
        self.img_counter = 0
        self.logging = (
            '<p align="center" style=" margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;">*Connected to PS4: '
            + self.IP
            + "*</span></p>\n"
        )

        # v4.72
        if len(self.sysGames) == 0:
            ReadJson = open("Data\prxUserMeta\MegaSRX\metadata\game\info.json")
            self.gameInfo = json.load(ReadJson)

        # v4.05
        self.prefloc = self.setting_path + "\\Data\\Pref\\"

        # v4.61
        self.bgImageChanged = False

        ChangeIconWindow.setObjectName("ChangeIconWindow")
        ChangeIconWindow.resize(1080, 720)
        ChangeIconWindow.setWindowIcon(
            QtGui.QIcon(self.prefloc + "ic1.@OfficialAhmed0")
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChangeIconWindow.sizePolicy().hasHeightForWidth())
        ChangeIconWindow.setSizePolicy(sizePolicy)
        ChangeIconWindow.setMinimumSize(QtCore.QSize(1300, 720))

        # Change bg accroding to user Resolution
        if self.screenWidth <= 1366:
            self.background = "SDbg.@OfficialAhmed0"
        elif self.screenWidth <= 1920:
            self.background = "HDbg.@OfficialAhmed0"
        elif self.screenWidth <= 2048:
            self.background = "2kbg.@OfficialAhmed0"
        else:
            self.background = "4kbg.@OfficialAhmed0"
        ChangeIconWindow.setStyleSheet(
            "background-image: url("
            + self.convert2Url(self.prefloc + self.background)
            + ");"
        )

        self.formLayout = QtWidgets.QFormLayout(ChangeIconWindow)
        self.formLayout.setObjectName("formLayout")
        self.TopLayout = QtWidgets.QFormLayout()
        self.TopLayout.setContentsMargins(20, 20, 20, -1)
        self.TopLayout.setObjectName("TopLayout")
        self.Title_label = QtWidgets.QLabel(ChangeIconWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_label.sizePolicy().hasHeightForWidth())
        self.Title_label.setSizePolicy(sizePolicy)
        self.Title_label.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setFamily(self.userFont)
        font.setWeight(75)
        self.Title_label.setFont(font)
        self.Title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")
        self.TopLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Title_label)
        self.homebrewLabel = QtWidgets.QLabel(ChangeIconWindow)
        self.homebrewLabel.setEnabled(False)

        sizePolicy.setHeightForWidth(
            self.homebrewLabel.sizePolicy().hasHeightForWidth()
        )
        self.homebrewLabel.setSizePolicy(sizePolicy)
        self.homebrewLabel.setMinimumSize(QtCore.QSize(200, 0))
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.homebrewLabel.setFont(font)
        self.homebrewLabel.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.homebrewLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.homebrewLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.homebrewLabel.setObjectName("homebrewLabel")
        self.TopLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.homebrewLabel)
        self.whiteBg = QtWidgets.QFrame(ChangeIconWindow)
        self.whiteBg.setMinimumSize(QtCore.QSize(4000, 1))
        self.whiteBg.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.prefloc + "White.@OfficialAhmed0")
            + ");"
        )
        self.whiteBg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.whiteBg.setLineWidth(1)
        self.whiteBg.setFrameShape(QtWidgets.QFrame.HLine)
        self.whiteBg.setObjectName("whiteBg")
        self.TopLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.whiteBg)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.TopLayout)
        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.LeftLayout.setContentsMargins(20, 30, -1, 10)
        self.LeftLayout.setSpacing(5)
        self.LeftLayout.setObjectName("LeftLayout")
        self.Icon = QtWidgets.QGraphicsView(ChangeIconWindow)

        sizePolicy.setHeightForWidth(self.Icon.sizePolicy().hasHeightForWidth())
        self.Icon.setSizePolicy(sizePolicy)
        self.Icon.setMinimumSize(QtCore.QSize(340, 370))
        self.Icon.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.prefloc + "White.@OfficialAhmed0")
            + ");"
        )
        self.Icon.setObjectName("Icon")
        self.LeftLayout.addWidget(self.Icon)
        self.Change_DownloadBtnLayout = QtWidgets.QFormLayout()
        self.Change_DownloadBtnLayout.setContentsMargins(-1, -1, -1, 0)
        self.Change_DownloadBtnLayout.setVerticalSpacing(3)
        self.Change_DownloadBtnLayout.setObjectName("Change_DownloadBtnLayout")
        self.ChangeIcon_btn = QtWidgets.QPushButton(ChangeIconWindow)

        sizePolicy.setHeightForWidth(
            self.ChangeIcon_btn.sizePolicy().hasHeightForWidth()
        )
        self.ChangeIcon_btn.setSizePolicy(sizePolicy)
        self.ChangeIcon_btn.setMinimumSize(QtCore.QSize(170, 35))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ChangeIcon_btn.setFont(font)
        self.ChangeIcon_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangeIcon_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.ChangeIcon_btn.setObjectName("ChangeIcon_btn")
        self.Change_DownloadBtnLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.ChangeIcon_btn
        )
        self.DownloadIcon_btn = QtWidgets.QPushButton(ChangeIconWindow)

        sizePolicy.setHeightForWidth(
            self.DownloadIcon_btn.sizePolicy().hasHeightForWidth()
        )
        self.DownloadIcon_btn.setSizePolicy(sizePolicy)
        self.DownloadIcon_btn.setMinimumSize(QtCore.QSize(0, 35))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.DownloadIcon_btn.setFont(font)
        self.DownloadIcon_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DownloadIcon_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.DownloadIcon_btn.setObjectName("DownloadIcon_btn")
        self.Change_DownloadBtnLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.DownloadIcon_btn
        )
        self.Prev_btn = QtWidgets.QToolButton(ChangeIconWindow)

        sizePolicy.setHeightForWidth(self.Prev_btn.sizePolicy().hasHeightForWidth())
        self.Prev_btn.setSizePolicy(sizePolicy)
        self.Prev_btn.setMinimumSize(QtCore.QSize(170, 30))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Prev_btn.setFont(font)
        self.Prev_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Prev_btn.setAutoFillBackground(False)
        self.Prev_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Prev_btn.setArrowType(QtCore.Qt.LeftArrow)
        self.Prev_btn.setObjectName("Prev_btn")
        self.Change_DownloadBtnLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.Prev_btn
        )
        self.Next_btn = QtWidgets.QToolButton(ChangeIconWindow)

        sizePolicy.setHeightForWidth(self.Next_btn.sizePolicy().hasHeightForWidth())
        self.Next_btn.setSizePolicy(sizePolicy)
        self.Next_btn.setMinimumSize(QtCore.QSize(0, 25))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Next_btn.setFont(font)
        self.Next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Next_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Next_btn.setArrowType(QtCore.Qt.RightArrow)
        self.Next_btn.setObjectName("Next_btn")

        self.Change_DownloadBtnLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.Next_btn
        )
        self.LeftLayout.addLayout(self.Change_DownloadBtnLayout)
        self.Submit_btn = QtWidgets.QPushButton(ChangeIconWindow)

        sizePolicy.setHeightForWidth(self.Submit_btn.sizePolicy().hasHeightForWidth())
        self.Submit_btn.setSizePolicy(sizePolicy)
        self.Submit_btn.setMinimumSize(QtCore.QSize(0, 50))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Submit_btn.setFont(font)
        self.Submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Submit_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Submit_btn.setObjectName("Submit_btn")
        self.LeftLayout.addWidget(self.Submit_btn)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.LeftLayout)
        self.RightLayout = QtWidgets.QFormLayout()
        self.RightLayout.setContentsMargins(-1, 60, 20, -1)
        self.RightLayout.setObjectName("RightLayout")
        self.GameTitle = QtWidgets.QLabel(ChangeIconWindow)
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.GameTitle.setFont(font)
        self.GameTitle.setMinimumHeight(45)
        self.GameTitle.setStyleSheet("color:rgb(255,255,255);")
        self.GameTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.GameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.GameTitle.setObjectName("GameTitle")
        self.RightLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.GameTitle
        )
        self.GameID_label = QtWidgets.QLabel(ChangeIconWindow)
        self.GameID_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(15)
        self.GameID_label.setFont(font)
        self.GameID_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.GameID_label.setFrameShape(QtWidgets.QFrame.Box)
        self.GameID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.GameID_label.setObjectName("GameID_label")
        self.RightLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.GameID_label
        )
        self.GameID = QtWidgets.QLabel(ChangeIconWindow)
        font.setPointSize(16)
        self.GameID.setFont(font)
        self.GameID.setStyleSheet("color:rgb(255, 255, 255);")
        self.GameID.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.GameID.setObjectName("GameID")
        self.RightLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.GameID)
        self.line = QtWidgets.QFrame(ChangeIconWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(50, 0))
        self.line.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.prefloc + "White.@OfficialAhmed0")
            + ");"
        )
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.RightLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.Ex_In_label = QtWidgets.QLabel(ChangeIconWindow)

        sizePolicy.setHeightForWidth(self.Ex_In_label.sizePolicy().hasHeightForWidth())
        self.Ex_In_label.setSizePolicy(sizePolicy)
        self.Ex_In_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Ex_In_label.setFont(font)
        self.Ex_In_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.Ex_In_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Ex_In_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Ex_In_label.setObjectName("Ex_In_label")
        self.RightLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Ex_In_label)
        self.Ex_In = QtWidgets.QLabel(ChangeIconWindow)
        font.setPointSize(16)
        self.Ex_In.setFont(font)
        self.Ex_In.setStyleSheet("color:rgb(255, 255, 255);")
        self.Ex_In.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.Ex_In.setObjectName("Ex_In")
        self.RightLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Ex_In)
        self.line_3 = QtWidgets.QFrame(ChangeIconWindow)
        self.line_3.setMinimumSize(QtCore.QSize(30, 3))
        self.line_3.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.prefloc + "White.@OfficialAhmed0")
            + ");"
        )
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.RightLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.TotalGames_label = QtWidgets.QLabel(ChangeIconWindow)
        self.TotalGames_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(15)
        self.TotalGames_label.setFont(font)
        self.TotalGames_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.TotalGames_label.setFrameShape(QtWidgets.QFrame.Box)
        self.TotalGames_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalGames_label.setObjectName("TotalGames_label")
        self.RightLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.TotalGames_label
        )
        self.TotalGames = QtWidgets.QLabel(ChangeIconWindow)
        font.setPointSize(16)
        self.TotalGames.setFont(font)
        self.TotalGames.setStyleSheet("color:rgb(255, 255, 255);")
        self.TotalGames.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.TotalGames.setObjectName("TotalGames")
        self.RightLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.TotalGames)
        self.line_4 = QtWidgets.QFrame(ChangeIconWindow)
        self.line_4.setMinimumSize(QtCore.QSize(100, 3))
        self.line_4.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.prefloc + "White.@OfficialAhmed0")
            + ");"
        )
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.RightLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.IconSize_label = QtWidgets.QLabel(ChangeIconWindow)
        self.IconSize_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(13)
        self.IconSize_label.setFont(font)
        self.IconSize_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.IconSize_label.setFrameShape(QtWidgets.QFrame.Box)
        self.IconSize_label.setAlignment(QtCore.Qt.AlignCenter)
        self.IconSize_label.setObjectName("IconSize_label")
        self.RightLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.IconSize_label
        )
        self.IconSize = QtWidgets.QLabel(ChangeIconWindow)
        font.setPointSize(16)
        self.IconSize.setFont(font)
        self.IconSize.setStyleSheet("color:rgb(255, 255, 255);")
        self.IconSize.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.IconSize.setObjectName("IconSize")
        self.RightLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.IconSize)
        self.line_5 = QtWidgets.QFrame(ChangeIconWindow)
        self.line_5.setMinimumSize(QtCore.QSize(100, 3))
        self.line_5.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.prefloc + "White.@OfficialAhmed0")
            + ");"
        )
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.RightLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_5)

        self.Select_btn = QtWidgets.QPushButton(ChangeIconWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Select_btn.sizePolicy().hasHeightForWidth())

        self.Select_btn.setSizePolicy(sizePolicy)
        self.Select_btn.setMinimumSize(QtCore.QSize(190, 0))
        font.setPointSize(20)
        self.Select_btn.setFont(font)
        self.Select_btn.setStyleSheet("color:rgb(255, 255, 255);")
        self.Select_btn.setObjectName("Select_btn")
        self.Select_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.RightLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Select_btn)
        self.GameTitles = QtWidgets.QComboBox(ChangeIconWindow)

        sizePolicy.setHeightForWidth(self.GameTitles.sizePolicy().hasHeightForWidth())
        self.GameTitles.setSizePolicy(sizePolicy)
        self.GameTitles.setMinimumSize(QtCore.QSize(0, 30))
        font.setPointSize(15)
        self.GameTitles.setFont(font)
        self.GameTitles.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GameTitles.setDuplicatesEnabled(True)
        self.GameTitles.setStyleSheet("color: rgb(0, 0, 0);")
        self.GameTitles.setObjectName("GameTitles")
        font.setPointSize(12)
        self.RightLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.GameTitles)

        font.setPointSize(15)
        self.bg_change_browse_btnLayout = QtWidgets.QFormLayout()
        self.bg_change_browse_btnLayout.setContentsMargins(200, 0, 200, -1)
        self.bg_change_browse_btnLayout.setObjectName("bg_change_browse_btnLayout")
        self.bg_change_browse_btn = QtWidgets.QPushButton(ChangeIconWindow)
        self.bg_change_browse_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.bg_change_browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bg_change_browse_btn.setStyleSheet("color:rgb(255, 255, 255);")
        self.bg_change_browse_btn.setObjectName("bg_change_browse_btn")
        self.bg_change_browse_btnLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.bg_change_browse_btn
        )
        self.RightLayout.setLayout(
            12, QtWidgets.QFormLayout.FieldRole, self.bg_change_browse_btnLayout
        )
        self.bg_change_browse_btn.setFont(font)

        font.setPointSize(12)
        self.Logs = QtWidgets.QTextEdit(ChangeIconWindow)
        self.Logs.setReadOnly(True)
        self.Logs.setObjectName("Logs")
        self.RightLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.Logs)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.RightLayout)
        self.BottomLayout = QtWidgets.QVBoxLayout()
        self.BottomLayout.setContentsMargins(20, 10, 20, 0)
        self.BottomLayout.setObjectName("BottomLayout")
        self.line_6 = QtWidgets.QFrame(ChangeIconWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setMinimumSize(QtCore.QSize(4000, 0))
        self.line_6.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.prefloc + "White.@OfficialAhmed0")
            + ");"
        )
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.BottomLayout.addWidget(self.line_6)
        self.CreditsLayout = QtWidgets.QVBoxLayout()
        self.CreditsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.CreditsLayout.setContentsMargins(500, 0, 0, -1)
        self.CreditsLayout.setSpacing(5)
        self.CreditsLayout.setObjectName("CreditsLayout")
        self.Title_label_2 = QtWidgets.QLabel(ChangeIconWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Title_label_2.sizePolicy().hasHeightForWidth()
        )
        self.Title_label_2.setSizePolicy(sizePolicy)
        self.Title_label_2.setMinimumSize(QtCore.QSize(10, 0))
        self.Title_label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Title_label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Title_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Title_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Title_label_2.setLineWidth(1)
        self.Title_label_2.setOpenExternalLinks(True)
        self.Title_label_2.setObjectName("Title_label_2")
        self.CreditsLayout.addWidget(self.Title_label_2)
        self.SupportMe = QtWidgets.QLabel(ChangeIconWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SupportMe.sizePolicy().hasHeightForWidth())
        self.SupportMe.setSizePolicy(sizePolicy)
        self.SupportMe.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SupportMe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SupportMe.setFrameShape(QtWidgets.QFrame.Box)
        self.SupportMe.setOpenExternalLinks(True)
        self.SupportMe.setObjectName("SupportMe")
        self.CreditsLayout.addWidget(self.SupportMe)
        self.BottomLayout.addLayout(self.CreditsLayout)
        self.formLayout.setLayout(
            3, QtWidgets.QFormLayout.SpanningRole, self.BottomLayout
        )

        # v4.01
        self.Icon.setStyleSheet(
            "border-image: url(" + self.CUSA_img + self.imgs[0] + ");"
        )
        self.Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Icon.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Icon.setLineWidth(2)
        self.Icon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Icon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # buttons back-end
        self.ChangeIcon_btn.clicked.connect(self.BrowseIcon)
        self.DownloadIcon_btn.clicked.connect(self.DownloadIcon)
        self.Next_btn.clicked.connect(self.Next)
        self.Prev_btn.clicked.connect(self.Prev)
        self.Submit_btn.clicked.connect(self.Resize_Upload)
        self.Select_btn.clicked.connect(self.Select)
        self.bg_change_browse_btn.clicked.connect(self.BrowseBg)

        # add items the number of games that are found without renaming them
        for _ in range(len(self.Games)):
            self.GameTitles.addItem("select")

        self.retranslateUi(ChangeIconWindow)
        self.GameTitles.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ChangeIconWindow)

    def retranslateUi(self, ChangeIconWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangeIconWindow.setWindowTitle(
            _translate(
                "ChangeIconWindow",
                "Iconit v"
                + str(self.ver)
                + " ("
                + str(Update.get_update_release_date())
                + ")",
            )
        )
        self.Title_label.setText(_translate("ChangeIconWindow", "Change Game Icon"))
        self.ChangeIcon_btn.setText(_translate("ChangeIconWindow", "Change Icon..."))
        self.DownloadIcon_btn.setText(
            _translate("ChangeIconWindow", "Download Icon...")
        )
        self.Prev_btn.setText(_translate("ChangeIconWindow", "Previous"))
        self.Next_btn.setText(_translate("ChangeIconWindow", "Next"))
        self.Submit_btn.setText(_translate("ChangeIconWindow", "Resize && Upload"))
        self.GameTitle.setText(_translate("ChangeIconWindow", "Game Title Here"))
        self.GameID_label.setText(_translate("ChangeIconWindow", "Game ID:"))
        self.GameID.setText(_translate("ChangeIconWindow", "TextLabel"))
        self.Ex_In_label.setText(_translate("ChangeIconWindow", "External / Internal"))
        self.Ex_In.setText(_translate("ChangeIconWindow", "TextLabel"))
        self.TotalGames_label.setText(_translate("ChangeIconWindow", "Total Games"))
        self.TotalGames.setText(_translate("ChangeIconWindow", "TextLabel"))
        self.IconSize_label.setText(
            _translate("ChangeIconWindow", "Min. Icon Size(512x512)")
        )
        self.IconSize.setText(
            _translate("ChangeIconWindow", "Current Icon size(512x512)")
        )
        self.Select_btn.setText(_translate("ChangeIconWindow", "Select"))
        self.bg_change_browse_btn.setText(
            _translate("ChangeIconWindow", "Change Game Pic...")
        )
        self.Logs.setHtml(
            _translate(
                "ChangeIconWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;">*Connected to PS4: '
                + self.IP
                + "*</span></p>\n"
                '<p align="center" style="-qt-paragraph-type:empty; margin: 0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;"><br /></p>\n',
            )
        )
        self.Title_label_2.setText(
            _translate(
                "ChangeIconWindow",
                '<html><head/><body><p align="center"><a href="https://twitter.com/OfficialAhmed0"><span style="font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#90f542; vertical-align:super;">Created By @OfficialAhmed0</span></a></p></body></html>',
            )
        )
        self.SupportMe.setText(
            _translate(
                "ChangeIconWindow",
                '<html><head/><body><p align="center"><a href="https://www.paypal.com/paypalme/Officialahmed0"><span style="font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#90f542; vertical-align:super;">Support me (PayPal)</span></a></p></body></html>',
            )
        )

        self.Next_btn.setText(_translate("ChangeIconWindow", "Browse Icon ..."))
        self.Prev_btn.setText(_translate("ChangeIconWindow", "Browse Icon ..."))
        self.GameTitle.setText(
            _translate("ChangeIconWindow", self.Games[self.imgs[self.img_counter]])
        )
        self.GameID.setText(_translate("ChangeIconWindow", self.imgs[self.img_counter]))
        self.TotalGames.setText(
            _translate(
                "ChangeIconWindow",
                str(self.img_counter + 1) + "/" + str(len(self.Games)),
            )
        )

        # Keyboard recognition v4.07
        self.Next_btn.setShortcut("Right")
        self.Prev_btn.setShortcut("Left")
        self.Select_btn.setShortcut("return")

        for i in range(len(self.Games)):
            self.GameTitles.setItemText(
                i,
                _translate(
                    "ChangeIconWindow",
                    " " * 8 + str(i + 1) + ": " + self.Games[self.imgs[i]],
                ),
            )
        if len(self.sysGames) > 1:
            self.homebrewLabel.setText(
                _translate("ChangeIconWindow", "System icon: Yes")
            )
            self.bg_change_browse_btn.hide()

        elif self.userHB == "True":
            if "CUSA" in self.imgs[self.img_counter]:
                self.homebrewLabel.setText(
                    _translate("ChangeIconWindow", "Homebrew icon: No")
                )
            else:
                self.homebrewLabel.setText(
                    _translate("ChangeIconWindow", "Homebrew icon: Yes")
                )
        else:
            self.homebrewLabel.setText(
                _translate("ChangeIconWindow", "Homebrew icon: Turned off")
            )
        if self.Games[self.imgs[self.img_counter]] in self.exGames:
            self.Ex_In.setText(_translate("ChangeIconWindow", "External"))
        else:
            self.Ex_In.setText(_translate("ChangeIconWindow", "Internal"))

        # Tool tips update v4.61
        self.TTTSS = "<p style='color:Black'>"  # TTTSS = ToolTipTagStyleStart
        self.TTTSE = "</p>"  # TTTSE = ToolTipTagStyleEnd

        self.Next_btn.setToolTip(self.TTTSS + "Next Icon" + self.TTTSE)
        self.Prev_btn.setToolTip(self.TTTSS + "Previous Icon" + self.TTTSE)
        self.ChangeIcon_btn.setToolTip(
            self.TTTSS + "Pick an Icon for the game" + self.TTTSE
        )
        self.DownloadIcon_btn.setToolTip(
            self.TTTSS + "Grab the Icon from PS4 to your Computer" + self.TTTSE
        )
        self.Submit_btn.setToolTip(
            self.TTTSS
            + "Upload the Icon and Pic after you change at least one of them"
            + self.TTTSE
        )
        self.Select_btn.setToolTip(
            self.TTTSS
            + "Click this to select the game from the games list"
            + self.TTTSE
        )
        self.Ex_In.setToolTip(
            self.TTTSS
            + "This is the location where the game is located on your PS4"
            + self.TTTSE
        )
        self.bg_change_browse_btn.setToolTip(
            self.TTTSS + "Pick a background to launch when the game starts" + self.TTTSE
        )
        self.GameTitle.setToolTip(
            self.TTTSS
            + "Some game titles are unknown because they're not legit (homebrews/PS2 converted games etc.)"
            + self.TTTSE
        )
        self.homebrewLabel.setToolTip(
            self.TTTSS
            + "Turned on = Homebrew will be visible and can be changed (turn it on/off from the settings)"
            + self.TTTSE
        )

    def convert2Url(self, path):
        result = ""
        for i in path:
            if i == "\\":
                result += "/"
            else:
                result += i
        return result

    def UpdateLogs(self):
        self.Logs.setHtml(
            '<p align="center" style=" margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;">'
            + self.logging
            + "</span></p>\n"
        )
        self.Logs.moveCursor(QtGui.QTextCursor.End)

    def UpdateInfo(self, CustomImgSelected=False):
        self.Submit_btn.setDisabled(True)
        current_img_path = self.CUSA_img + self.imgs[self.img_counter]
        if len(self.sysGames) == 0:
            GameTitle = self.gameInfo[self.imgs[self.img_counter]]
        else:
            GameTitle = self.Games[self.imgs[self.img_counter]]
        self.Icon.setStyleSheet("border-image: url(" + current_img_path + ");")

        self.GameTitle.setText(GameTitle)
        self.GameID.setText(self.imgs[self.img_counter])

        # If Custom image selected by choosing image manually
        if CustomImgSelected:
            self.TotalGames.setText(
                str(self.GameTitles.currentIndex() + 1) + "/" + str(len(self.Games))
            )
        else:
            self.TotalGames.setText(
                str(self.img_counter + 1) + "/" + str(len(self.Games))
            )

        # Check homebrew/Sys icon label
        if len(self.sysGames) > 1:
            self.homebrewLabel.setText("System icon: Yes")

        elif self.userHB == "True":
            if "CUSA" in self.imgs[self.img_counter]:
                self.homebrewLabel.setText("Homebrew icon: No")
            else:
                self.homebrewLabel.setText("Homebrew icon: Yes")

        # Change External or Internal
        if self.imgs[self.img_counter] in self.exGames:
            self.Ex_In.setText("External")
        else:
            self.Ex_In.setText("Internal")

    def ChangeIconSizeLabel(self, color="white", bg_image="", size="(512, 512)"):
        self.IconSize.setText("Current Icon size" + size + "")
        if bg_image != "":
            self.IconSize.setStyleSheet(
                "background-image: url(" + bg_image + "); color:" + color
            )
        else:
            self.IconSize.setStyleSheet("color:" + color)

    def backgroundImage2Original(self):
        self.bgImageChanged = False  # Reset bg image
        self.ChangeIconSizeLabel()
        self.BackgroundChange()
        self.ChangeIconWindow.setStyleSheet(
            "background-image: url("
            + self.convert2Url(self.prefloc + self.background)
            + ");"
        )

    def BackgroundChange(self):
        label_bg = (
            self.Ex_In_label,
            self.Title_label,
            self.Title_label_2,
            self.GameID_label,
            self.homebrewLabel,
            self.IconSize_label,
            self.TotalGames_label,
            self.TotalGames_label,
            self.Title_label,
            self.GameTitles,
            self.GameTitle,
            self.GameID,
            self.TotalGames,
            self.ChangeIcon_btn,
            self.Next_btn,
            self.Prev_btn,
            self.Select_btn,
            self.Submit_btn,
            self.DownloadIcon_btn,
            self.bg_change_browse_btn,
            self.Logs,
            self.Ex_In,
            self.IconSize,
            self.SupportMe,
        )

        # if bg image changed change labels bg to black
        if self.bgImageChanged:
            style = (
                "background-image: url("
                + self.convert2Url(self.prefloc + "Black.@OfficialAhmed0")
                + "); color:white"
            )
        else:
            style = "color:white"

        for bg in label_bg:
            bg.setStyleSheet(style)

    def BrowseBg(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.userIPath)

        img, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose a picture to open when game launches",
            "",
            "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg)",
            options=options,
        )

        if img:
            bg = Image.open(img)
            size = bg.size

            StyleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px"><span style="font-size:10pt; color:#e83c3c">[Error] : '
            StyleTagEnd = "</span></p></body></html>"

            if size[0] >= 1920 and size[0] <= 2048:
                if size[1] >= 1080 and size[1] <= 2048:
                    self.Submit_btn.setDisabled(False)
                    self.changeBgPath = img
                    self.ChangeIconWindow.setStyleSheet(
                        "background-image: url(" + img + ");"
                    )
                    self.bgImageChanged = True
                    self.BackgroundChange()
                else:
                    self.logging += (
                        StyleTagStart
                        + "Image height is too small or too large atleast (1920x1080) atmost (2048x2048)"
                        + StyleTagEnd
                    )
                    self.UpdateLogs()
            else:
                self.logging += (
                    StyleTagStart
                    + "Image width is too small or too large atleast (1920x1080) atmost (2048x2048)"
                    + StyleTagEnd
                )
                self.UpdateLogs()

    def Next(self):
        self.backgroundImage2Original()
        if self.img_counter < self.img_limit - 1:
            self.img_counter += 1
            if self.img_counter < self.img_limit and self.img_counter >= 0:
                self.UpdateInfo()

    def Prev(self):
        self.backgroundImage2Original()
        if self.img_counter > 0 and self.img_counter <= self.img_limit:
            self.img_counter -= 1
            self.UpdateInfo()

    def Select(self):
        self.backgroundImage2Original()
        self.img_counter = self.GameTitles.currentIndex()
        self.UpdateInfo(CustomImgSelected=True)

    def CheckImg(self, path):
        icon = Image.open(path)
        size = icon.size
        logStyleStart = "<p align='center' style='margin:0px; -qt-block-indent:0; text-indent:0px'><span style='font-size:10pt; color:#ffaa00'>[Warning] : "
        logStyleEnd = "</span></p></body></html>"

        # check if bg image changed then change label of current size image accordingly
        if size[0] == 512 and size[1] == 512:
            if self.bgImageChanged == True:
                self.ChangeIconSizeLabel(
                    "#0aff14;", self.prefloc + "Black.@OfficialAhmed0", str(icon.size)
                )
            else:
                self.ChangeIconSizeLabel("#0aff14;", size=str(icon.size))

        elif (
            (size[0] > 512 and size[1] > 512)
            or (size[0] == 512 and size[1] > 512)
            or (size[0] > 512 and size[1] == 512)
        ):
            if self.bgImageChanged == True:
                self.ChangeIconSizeLabel(
                    "#fa9600;", self.prefloc + "Black.@OfficialAhmed0", str(icon.size)
                )
            else:
                self.ChangeIconSizeLabel("#fa9600;", size=str(icon.size))

            self.logging += (
                logStyleStart + "Image will be resized (Too large)" + logStyleEnd
            )
            self.UpdateLogs()
        else:
            if self.bgImageChanged == True:
                self.ChangeIconSizeLabel(
                    "#fa0a14;", self.prefloc + "Black.@OfficialAhmed0", str(icon.size)
                )
            else:
                self.ChangeIconSizeLabel("#fa0a14;", size=str(icon.size))

            self.Submit_btn.setDisabled(True)
            self.logging += (
                logStyleStart
                + "Image cannot be used nor resized (Too Small)"
                + logStyleEnd
            )
            self.UpdateLogs()

    def BrowseIcon(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.userIPath)

        img, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose the icon to upload",
            "",
            "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg);; icon(*.ico)",
            options=options,
        )
        if img:
            self.Submit_btn.setDisabled(False)
            self.Icon.setStyleSheet("border-image: url(" + img + ");")
            self.CheckImg(img)
            self.changeIconPath = img

    def DownloadIcon(self):
        import Message

        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        self.ui.setupUi(
            self.window,
            "This feature is no longer available & will be removed next update as icons now auto backup before changing it.",
        )
        self.window.show()

    def Resize_Upload(self):
        import Confirm

        if self.bgImageChanged == False:
            self.changeBgPath = ""

        self.Submit_btn.setEnabled(False)
        Current_CUSA = self.imgs[self.img_counter]
        self.windo = QtWidgets.QWidget()
        self.ui = Confirm.Ui_ConfirmWindow()
        self.ui.setupUi(
            self.windo,
            self.changeIconPath,
            self.IP,
            self.Port,
            Current_CUSA,
            "Iconit",
            self.exGames,
            None,
            self.changeBgPath,
            self.modeSelected,
            self.sysIconsAlgo,
        )
        self.windo.show()

        styleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style="font-size:10pt; '
        styleTagEnd = "</span></p>\n"
        self.logging += (
            styleTagStart
            + 'color:#55ff00;">[Success] : Auto Backup '
            + Current_CUSA
            + " success. Next time you change this icon, Iconit will overwrite it"
            + styleTagEnd
        )

        styleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style="font-size:10pt; '
        styleTagEnd = "</span></p>\n"
        self.logging += (
            styleTagStart
            + 'color:#ffaa00">[Attention]: '
            + Current_CUSA
            + " might take sometime to change in both PS4 and Iconit, but everything went good you dont have to reupload"
            + styleTagEnd
        )

        self.UpdateLogs()


if __name__ == "__main__":
    import sys, os
    from func import playSound as play

    play(f"{os.getcwd()}/Data/Pref/bgm/home.@OfficialAhmed0")

    app = QtWidgets.QApplication(sys.argv)
    ChangeIconWindow = QtWidgets.QWidget()
    ui = Ui_ChangeIconWindow()
    ui.setupUi(ChangeIconWindow)
    ChangeIconWindow.show()
    sys.exit(app.exec_())
