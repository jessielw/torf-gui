# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 1029)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth()
        )
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 465, 904))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutMain = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents
        )
        self.verticalLayoutMain.setContentsMargins(12, 12, 12, 12)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.inputGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.inputGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.inputGroupBox.setSizePolicy(sizePolicy)
        self.inputGroupBox.setObjectName("inputGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.inputGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.fileRadioButton = QtWidgets.QRadioButton(self.inputGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fileRadioButton.sizePolicy().hasHeightForWidth()
        )
        self.fileRadioButton.setSizePolicy(sizePolicy)
        self.fileRadioButton.setObjectName("fileRadioButton")
        self.gridLayout.addWidget(self.fileRadioButton, 0, 0, 1, 1)
        self.batchModeCheckBox = QtWidgets.QCheckBox(self.inputGroupBox)
        self.batchModeCheckBox.setObjectName("batchModeCheckBox")
        self.gridLayout.addWidget(self.batchModeCheckBox, 4, 0, 1, 1)
        self.excludeLabel = QtWidgets.QLabel(self.inputGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.excludeLabel.sizePolicy().hasHeightForWidth()
        )
        self.excludeLabel.setSizePolicy(sizePolicy)
        self.excludeLabel.setObjectName("excludeLabel")
        self.gridLayout.addWidget(self.excludeLabel, 5, 0, 1, 4)
        self.excludeEdit = QtWidgets.QPlainTextEdit(self.inputGroupBox)
        self.excludeEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.excludeEdit.sizePolicy().hasHeightForWidth()
        )
        self.excludeEdit.setSizePolicy(sizePolicy)
        self.excludeEdit.setMinimumSize(QtCore.QSize(0, 90))
        self.excludeEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.excludeEdit.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.excludeEdit.setObjectName("excludeEdit")
        self.gridLayout.addWidget(self.excludeEdit, 6, 0, 1, 4)
        self.inputEdit = QtWidgets.QLineEdit(self.inputGroupBox)
        self.inputEdit.setText("")
        self.inputEdit.setDragEnabled(True)
        self.inputEdit.setReadOnly(True)
        self.inputEdit.setObjectName("inputEdit")
        self.gridLayout.addWidget(self.inputEdit, 1, 0, 1, 4)
        self.horizontalLayout_inputButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_inputButtons.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint
        )
        self.horizontalLayout_inputButtons.setObjectName(
            "horizontalLayout_inputButtons"
        )
        self.browseButton = QtWidgets.QPushButton(self.inputGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.browseButton.sizePolicy().hasHeightForWidth()
        )
        self.browseButton.setSizePolicy(sizePolicy)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_inputButtons.addWidget(self.browseButton)
        self.pasteButton = QtWidgets.QPushButton(self.inputGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pasteButton.sizePolicy().hasHeightForWidth()
        )
        self.pasteButton.setSizePolicy(sizePolicy)
        self.pasteButton.setObjectName("pasteButton")
        self.horizontalLayout_inputButtons.addWidget(self.pasteButton)
        self.gridLayout.addLayout(
            self.horizontalLayout_inputButtons, 2, 0, 1, 4
        )
        self.directoryRadioButton = QtWidgets.QRadioButton(self.inputGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.directoryRadioButton.sizePolicy().hasHeightForWidth()
        )
        self.directoryRadioButton.setSizePolicy(sizePolicy)
        self.directoryRadioButton.setObjectName("directoryRadioButton")
        self.gridLayout.addWidget(self.directoryRadioButton, 0, 2, 1, 1)
        self.verticalLayoutMain.addWidget(self.inputGroupBox)
        self.seedingGroupBox = QtWidgets.QGroupBox(
            self.scrollAreaWidgetContents
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.seedingGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.seedingGroupBox.setSizePolicy(sizePolicy)
        self.seedingGroupBox.setObjectName("seedingGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.seedingGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.trackerLabel = QtWidgets.QLabel(self.seedingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.trackerLabel.sizePolicy().hasHeightForWidth()
        )
        self.trackerLabel.setSizePolicy(sizePolicy)
        self.trackerLabel.setObjectName("trackerLabel")
        self.verticalLayout_2.addWidget(self.trackerLabel)
        self.trackerEdit = QtWidgets.QPlainTextEdit(self.seedingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.trackerEdit.sizePolicy().hasHeightForWidth()
        )
        self.trackerEdit.setSizePolicy(sizePolicy)
        self.trackerEdit.setMinimumSize(QtCore.QSize(0, 90))
        self.trackerEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.trackerEdit.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.trackerEdit.setObjectName("trackerEdit")
        self.verticalLayout_2.addWidget(self.trackerEdit)
        self.webSeedLabel = QtWidgets.QLabel(self.seedingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.webSeedLabel.sizePolicy().hasHeightForWidth()
        )
        self.webSeedLabel.setSizePolicy(sizePolicy)
        self.webSeedLabel.setObjectName("webSeedLabel")
        self.verticalLayout_2.addWidget(self.webSeedLabel)
        self.webSeedEdit = QtWidgets.QPlainTextEdit(self.seedingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.webSeedEdit.sizePolicy().hasHeightForWidth()
        )
        self.webSeedEdit.setSizePolicy(sizePolicy)
        self.webSeedEdit.setMinimumSize(QtCore.QSize(0, 90))
        self.webSeedEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.webSeedEdit.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.webSeedEdit.setObjectName("webSeedEdit")
        self.verticalLayout_2.addWidget(self.webSeedEdit)
        self.verticalLayoutMain.addWidget(self.seedingGroupBox)
        self.optionGroupBox = QtWidgets.QGroupBox(
            self.scrollAreaWidgetContents
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.optionGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.optionGroupBox.setSizePolicy(sizePolicy)
        self.optionGroupBox.setObjectName("optionGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.optionGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pieceCountLabel = QtWidgets.QLabel(self.optionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pieceCountLabel.sizePolicy().hasHeightForWidth()
        )
        self.pieceCountLabel.setSizePolicy(sizePolicy)
        self.pieceCountLabel.setObjectName("pieceCountLabel")
        self.gridLayout_2.addWidget(self.pieceCountLabel, 3, 1, 1, 1)
        self.pieceSizeComboBox = QtWidgets.QComboBox(self.optionGroupBox)
        self.pieceSizeComboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pieceSizeComboBox.setObjectName("pieceSizeComboBox")
        self.gridLayout_2.addWidget(self.pieceSizeComboBox, 3, 0, 1, 1)
        self.md5CheckBox = QtWidgets.QCheckBox(self.optionGroupBox)
        self.md5CheckBox.setObjectName("md5CheckBox")
        self.gridLayout_2.addWidget(self.md5CheckBox, 10, 0, 1, 2)
        self.pieceSizeLabel = QtWidgets.QLabel(self.optionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pieceSizeLabel.sizePolicy().hasHeightForWidth()
        )
        self.pieceSizeLabel.setSizePolicy(sizePolicy)
        self.pieceSizeLabel.setObjectName("pieceSizeLabel")
        self.gridLayout_2.addWidget(self.pieceSizeLabel, 2, 0, 1, 1)
        self.privateTorrentCheckBox = QtWidgets.QCheckBox(self.optionGroupBox)
        self.privateTorrentCheckBox.setObjectName("privateTorrentCheckBox")
        self.gridLayout_2.addWidget(self.privateTorrentCheckBox, 8, 0, 1, 2)
        self.randomizeInfoHashCheckBox = QtWidgets.QCheckBox(
            self.optionGroupBox
        )
        self.randomizeInfoHashCheckBox.setObjectName(
            "randomizeInfoHashCheckBox"
        )
        self.gridLayout_2.addWidget(self.randomizeInfoHashCheckBox, 9, 0, 1, 2)
        self.commentLabel = QtWidgets.QLabel(self.optionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.commentLabel.sizePolicy().hasHeightForWidth()
        )
        self.commentLabel.setSizePolicy(sizePolicy)
        self.commentLabel.setObjectName("commentLabel")
        self.gridLayout_2.addWidget(self.commentLabel, 4, 0, 1, 1)
        self.commentEdit = QtWidgets.QLineEdit(self.optionGroupBox)
        self.commentEdit.setObjectName("commentEdit")
        self.gridLayout_2.addWidget(self.commentEdit, 5, 0, 1, 2)
        self.sourceLabel = QtWidgets.QLabel(self.optionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sourceLabel.sizePolicy().hasHeightForWidth()
        )
        self.sourceLabel.setSizePolicy(sizePolicy)
        self.sourceLabel.setObjectName("sourceLabel")
        self.gridLayout_2.addWidget(self.sourceLabel, 6, 0, 1, 1)
        self.sourceEdit = QtWidgets.QLineEdit(self.optionGroupBox)
        self.sourceEdit.setObjectName("sourceEdit")
        self.gridLayout_2.addWidget(self.sourceEdit, 7, 0, 1, 2)
        self.verticalLayoutMain.addWidget(self.optionGroupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout.addWidget(self.createButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImportProfile = QtWidgets.QAction(MainWindow)
        self.actionImportProfile.setObjectName("actionImportProfile")
        self.actionExportProfile = QtWidgets.QAction(MainWindow)
        self.actionExportProfile.setObjectName("actionExportProfile")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionImportProfile)
        self.menuFile.addAction(self.actionExportProfile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputGroupBox.setTitle(_translate("MainWindow", "Input path"))
        self.fileRadioButton.setText(_translate("MainWindow", "File"))
        self.batchModeCheckBox.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>If enabled, a torrent will be created for each directory and file one level below the input directory. The piece size for each torrent will be determined automatically.</p></body></html>",  # noqa: E501
            )
        )
        self.batchModeCheckBox.setText(_translate("MainWindow", "Batch mode"))
        self.excludeLabel.setText(
            _translate(
                "MainWindow",
                "Filename exclusion patterns (globs, one per line)",
            )
        )
        self.browseButton.setText(_translate("MainWindow", "Browse..."))
        self.pasteButton.setText(
            _translate("MainWindow", "Paste from clipboard")
        )
        self.directoryRadioButton.setText(
            _translate("MainWindow", "Directory")
        )
        self.seedingGroupBox.setTitle(_translate("MainWindow", "Seeding"))
        self.trackerLabel.setText(
            _translate("MainWindow", "Tracker URLs (one per line)")
        )
        self.webSeedLabel.setText(
            _translate("MainWindow", "HTTP/FTP seeds (one per line)")
        )
        self.optionGroupBox.setTitle(
            _translate("MainWindow", "Torrent options")
        )
        self.pieceCountLabel.setText(_translate("MainWindow", "# pieces"))
        self.randomizeInfoHashCheckBox.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>If enabled, this adds an entropy field to the info section of the metainfo and sets it to a random integer, to help with cross-seeding.</p></body></html>",  # noqa: E501
            )
        )
        self.randomizeInfoHashCheckBox.setText(
            _translate("MainWindow", "Randomize info hash")
        )
        self.md5CheckBox.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>This is not used by BitTorrent at all, but it is included by some programs for greater compatibility.</p></body></html>",  # noqa: E501
            )
        )
        self.md5CheckBox.setText(
            _translate("MainWindow", "Compute MD5 hashes")
        )
        self.pieceSizeLabel.setText(_translate("MainWindow", "Piece size"))
        self.privateTorrentCheckBox.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>If enabled, clients will not use DHT or Peer Exchange to discover peers or transfer data. Make sure to enable this option for private trackers.</p></body></html>",  # noqa: E501
            )
        )
        self.privateTorrentCheckBox.setText(
            _translate("MainWindow", "Private torrent")
        )
        self.commentLabel.setText(_translate("MainWindow", "Comment"))
        self.sourceLabel.setText(_translate("MainWindow", "Source"))
        self.sourceEdit.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>An optional source string that wil be added to the info dictionary. Useful for creating torrents with unique info hashes for private trackers.</p></body></html>",  # noqa: E501
            )
        )
        self.createButton.setText(_translate("MainWindow", "Create..."))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionImportProfile.setText(
            _translate("MainWindow", "Import profile...")
        )
        self.actionImportProfile.setShortcut(
            _translate("MainWindow", "Ctrl+O")
        )
        self.actionExportProfile.setText(
            _translate("MainWindow", "Export profile...")
        )
        self.actionExportProfile.setShortcut(
            _translate("MainWindow", "Ctrl+S")
        )
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "F1"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
