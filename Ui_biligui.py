# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\WYC20\Documents\tools\bilidown\GUI\biligui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 449)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setGeometry(QtCore.QRect(10, 0, 124, 38))
        self.TitleLabel.setObjectName("TitleLabel")
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setGeometry(QtCore.QRect(10, 40, 461, 251))
        self.CardWidget.setObjectName("CardWidget")
        self.title = SubtitleLabel(self.CardWidget)
        self.title.setGeometry(QtCore.QRect(20, 10, 271, 51))
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.author = StrongBodyLabel(self.CardWidget)
        self.author.setGeometry(QtCore.QRect(20, 80, 131, 19))
        self.author.setObjectName("author")
        self.CaptionLabel = CaptionLabel(self.CardWidget)
        self.CaptionLabel.setGeometry(QtCore.QRect(20, 110, 31, 16))
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.cover = QtWidgets.QLabel(self.CardWidget)
        self.cover.setGeometry(QtCore.QRect(300, 10, 151, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cover.sizePolicy().hasHeightForWidth())
        self.cover.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cover.setFont(font)
        self.cover.setText("")
        self.cover.setPixmap(QtGui.QPixmap(":/cover/book-cover-no.svg"))
        self.cover.setScaledContents(True)
        self.cover.setObjectName("cover")
        self.ScrollArea_2 = ScrollArea(self.CardWidget)
        self.ScrollArea_2.setGeometry(QtCore.QRect(60, 110, 231, 121))
        self.ScrollArea_2.setWidgetResizable(True)
        self.ScrollArea_2.setObjectName("ScrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 229, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.description = BodyLabel(self.scrollAreaWidgetContents)
        self.description.setGeometry(QtCore.QRect(0, 0, 220, 1000))
        self.description.setMinimumSize(QtCore.QSize(220, 1000))
        self.description.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.ScrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 300, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(True)
        font.setWeight(75)
        self.StrongBodyLabel_2.setFont(font)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.horizontalLayout.addWidget(self.StrongBodyLabel_2)
        self.seriesnum = LineEdit(self.horizontalLayoutWidget)
        self.seriesnum.setObjectName("seriesnum")
        self.horizontalLayout.addWidget(self.seriesnum)
        self.get = PushButton(self.horizontalLayoutWidget)
        self.get.setObjectName("get")
        self.horizontalLayout.addWidget(self.get)
        self.ScrollArea = ScrollArea(Form)
        self.ScrollArea.setGeometry(QtCore.QRect(480, 10, 341, 381))
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setObjectName("ScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 339, 379))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.ListWidget = ListWidget(self.scrollAreaWidgetContents_2)
        self.ListWidget.setGeometry(QtCore.QRect(0, 0, 340, 380))
        self.ListWidget.setMinimumSize(QtCore.QSize(340, 380))
        self.ListWidget.setObjectName("ListWidget")
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 400, 801, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Start = PushButton(self.horizontalLayoutWidget_2)
        self.Start.setObjectName("Start")
        self.horizontalLayout_2.addWidget(self.Start)
        self.ProgressBar = ProgressBar(self.horizontalLayoutWidget_2)
        self.ProgressBar.setObjectName("ProgressBar")
        self.horizontalLayout_2.addWidget(self.ProgressBar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TitleLabel.setText(_translate("Form", "Bilidown"))
        self.title.setText(_translate("Form", "标题"))
        self.author.setText(_translate("Form", "作者："))
        self.CaptionLabel.setText(_translate("Form", "简介："))
        self.description.setText(_translate("Form", "简介"))
        self.StrongBodyLabel_2.setText(_translate("Form", "书籍序号："))
        self.seriesnum.setPlaceholderText(_translate("Form", "2600"))
        self.get.setText(_translate("Form", "获取"))
        self.Start.setText(_translate("Form", "开始下载"))
from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, LineEdit, ListWidget, ProgressBar, PushButton, ScrollArea, StrongBodyLabel, SubtitleLabel, TitleLabel
import resources_rc