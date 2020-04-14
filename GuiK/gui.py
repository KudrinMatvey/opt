import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction

from gui.mplwidget import MplWidget
from src.opt import opt


class params:
    a = None
    b = None
    c = None
    d = None
    r = None
    left_bound = None
    right_bound = None
    max_iter = None
    method = None

    def __init__(self, a=1, b=1, c=1, d=1, r=2, left_bound=0, right_bound=10, max_iter=100):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.r = r
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.max_iter = max_iter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setMaximumSize(QtCore.QSize(960, 300))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelFunc = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.labelFunc.setFont(font)
        self.labelFunc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelFunc.setObjectName("labelFunc")
        self.verticalLayout.addWidget(self.labelFunc)
        self.labelInterval_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.labelInterval_2.setFont(font)
        self.labelInterval_2.setObjectName("labelInterval_2")
        self.labelErr = QtWidgets.QLabel(self.groupBox)
        self.verticalLayout.addWidget(self.labelInterval_2)
        self.verticalLayout.addWidget(self.labelErr)
        self.labelErr.setObjectName("labelErr")
        self.labelIter = QtWidgets.QLabel(self.groupBox)
        self.labelIter.setMaximumSize(QtCore.QSize(1280, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelIter.setFont(font)
        self.labelIter.setObjectName("labelIter")
        self.verticalLayout.addWidget(self.labelIter)
        self.labelR = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelR.setFont(font)
        self.labelR.setObjectName("labelR")
        self.verticalLayout.addWidget(self.labelR)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setMaximumSize(QtCore.QSize(1920, 50))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.funcParamA = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamA.setObjectName("funcParamA")
        self.horizontalLayout_3.addWidget(self.funcParamA)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.funcParamB = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamB.setObjectName("funcParamB")
        self.horizontalLayout_3.addWidget(self.funcParamB)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.funcParamC = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamC.setObjectName("funcParamC")
        self.horizontalLayout_3.addWidget(self.funcParamC)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.funcParamD = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamD.setObjectName("funcParamD")
        self.horizontalLayout_3.addWidget(self.funcParamD)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setMaximumSize(QtCore.QSize(1920, 50))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.maxIterCount = QtWidgets.QLineEdit(self.groupBox_6)
        self.maxIterCount.setObjectName("maxIterCount")
        self.horizontalLayout_4.addWidget(self.maxIterCount)
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.r = QtWidgets.QLineEdit(self.groupBox_6)
        self.r.setObjectName("r")
        self.horizontalLayout_4.addWidget(self.r)
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.funcParamLeftB = QtWidgets.QLineEdit(self.groupBox_6)
        self.funcParamLeftB.setObjectName("funcParamLeftB")
        self.horizontalLayout_3.addWidget(self.funcParamLeftB)
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.funcParamRightB = QtWidgets.QLineEdit(self.groupBox_6)
        self.funcParamRightB.setObjectName("funcParamRightB")
        self.horizontalLayout_3.addWidget(self.funcParamRightB)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(1280, 50))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonCalculate = QtWidgets.QPushButton(self.groupBox_3)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonCalculate.setFont(font)
        self.pushButtonCalculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.horizontalLayout.addWidget(self.pushButtonCalculate)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setCentralWidget(self.centralwidget)
        menu = MainWindow.menuBar()
        method_menu = menu.addMenu("Метод")
        self.MethodP = QAction('Пиявского', checkable=True)
        self.MethodP.setChecked(True)
        self.MethodP.triggered.connect(self.setMethodP)
        method_menu.addAction(self.MethodP)
        self.MethodS = QAction('Стронгина', checkable=True)
        method_menu.addAction(self.MethodS)
        self.MethodS.triggered.connect(self.setMethodS)
        self.MethodB = QAction('Перебора', checkable=True)
        method_menu.addAction(self.MethodB)
        self.MethodB.triggered.connect(self.setMethodB)
        self.pushButtonCalculate.clicked.connect(self.DisplaySolution)
        self.initInputContainers()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа Кудрин 381606-1"))
        self.labelFunc.setText(_translate("MainWindow", "f(x) =  A * sin( B * x) + C  * cos( D * x)"))
        self.labelInterval_2.setText(_translate("MainWindow", "x ∈[ t  ; T  ]"))
        self.label.setText(_translate("MainWindow", "A = "))
        self.label_2.setText(_translate("MainWindow", "B = "))
        self.label_4.setText(_translate("MainWindow", "C = "))
        self.label_5.setText(_translate("MainWindow", "D = "))
        self.label_3.setText(_translate("MainWindow", "Ограничение итераций = "))
        self.label_8.setText(_translate("MainWindow", "Коэффициент надежности ="))
        self.label_6.setText(_translate("MainWindow", "t ="))
        self.label_7.setText(_translate("MainWindow", "T ="))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Запуск метода"))

    def initInputContainers(self):
        default_params = params()
        self.funcParamA.setText(str(default_params.a))
        self.funcParamB.setText(str(default_params.b))
        self.funcParamC.setText(str(default_params.c))
        self.funcParamD.setText(str(default_params.d))
        self.funcParamLeftB.setText(str(default_params.left_bound))
        self.funcParamRightB.setText(str(default_params.right_bound))
        self.r.setText(str(default_params.r))
        self.maxIterCount.setText(str(default_params.max_iter))

    def setMethodP(self):
        self.MethodP.setChecked(True)
        self.MethodS.setChecked(False)
        self.MethodB.setChecked(False)

    def setMethodS(self):
        self.MethodP.setChecked(False)
        self.MethodS.setChecked(True)
        self.MethodB.setChecked(False)

    def setMethodB(self):
        self.MethodP.setChecked(False)
        self.MethodS.setChecked(False)
        self.MethodB.setChecked(True)

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def ClearPlot(self):
        self.solutionX.setText("")
        self.solutionY.setText("")
        self.solutionIterCount.setText("")

    def DisplaySolution(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelErr.setText(_translate("MainWindow", ""))
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.SecondWindow = QtWidgets.QMainWindow()
        self.SecondWindow.setObjectName("SecondWindow")
        self.centralwidgetS = QtWidgets.QWidget(self.SecondWindow)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidgetS)
        self.groupBox_2.setMaximumSize(QtCore.QSize(1280, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.solutionX = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solutionX.setFont(font)
        self.solutionX.setObjectName("solutionX")
        self.verticalLayout_2.addWidget(self.solutionX)
        self.solutionY = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solutionY.setFont(font)
        self.solutionY.setObjectName("solutionY")
        self.solutionIterCount = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solutionIterCount.setFont(font)
        self.solutionIterCount.setObjectName("solutionIterCount")
        self.finalFuncLabel = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finalFuncLabel.setFont(font)
        self.finalFuncLabel.setObjectName("finalFuncLabel")
        self.verticalLayout_secondary = QtWidgets.QVBoxLayout(self.centralwidgetS)
        self.verticalLayout_secondary.setObjectName("verticalLayout_secondary")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setMinimumSize(QtCore.QSize(960, 300))
        self.MplWidget.setObjectName("MplWidget")
        self.groupBox_2.setTitle(_translate("SecondWindow", ""))
        self.solutionX.setText(_translate("SecondWindow", ""))
        self.solutionY.setText(_translate("SecondWindow", ""))
        self.solutionIterCount.setText(_translate("SecondWindow", ""))
        self.verticalLayout_secondary.addWidget(self.finalFuncLabel)
        self.verticalLayout_secondary.addWidget(self.MplWidget)
        self.verticalLayout_secondary.addWidget(self.solutionIterCount)
        self.verticalLayout_secondary.addWidget(self.solutionX)
        # self.verticalLayout_secondary.addWidget(self.solutionY)

        self.SecondWindow.setCentralWidget(self.centralwidgetS)
        optimizer = opt()
        opt_params = params()
        try:
            opt_params.a = float(self.funcParamA.text())
            opt_params.b = float(self.funcParamB.text())
            opt_params.c = float(self.funcParamC.text())
            opt_params.d = float(self.funcParamD.text())
            opt_params.left_bound = float(self.funcParamLeftB.text())
            opt_params.right_bound = float(self.funcParamRightB.text())
            opt_params.max_iter = int(self.maxIterCount.text())
            opt_params.r = float(self.r.text())

            if opt_params.left_bound >= opt_params.right_bound:
                raise ValueError()

            if self.MethodB.isChecked():
                opt_params.method = optimizer.methods.BruteForse
            elif self.MethodP.isChecked():
                opt_params.method = optimizer.methods.Piyavsky
            elif self.MethodS.isChecked():
                opt_params.method = optimizer.methods.Strongin

            for param in dir(opt_params):
                if "__" not in param:
                    print(param, "=", getattr(opt_params, param), type(getattr(opt_params, param)))

            optimizer.SetFunctionParameters(opt_params.a, opt_params.b, opt_params.c, opt_params.d)
            solution = optimizer.Minimize(opt_params.left_bound, opt_params.right_bound, opt_params.r,
                                          opt_params.method, max_iter=opt_params.max_iter)

            points_multiplier = 100
            num_points = int(abs(opt_params.right_bound - opt_params.left_bound) * points_multiplier)
            step = abs(opt_params.right_bound - opt_params.left_bound) / num_points

            x = []
            for i in range(num_points):
                x.append(i * step + opt_params.left_bound)

            y = [optimizer.Func(point) for point in x]

            self.MplWidget.canvas.axes.plot(x, y, color="black")

            for point in solution.points:
                self.MplWidget.canvas.axes.plot(point[0], solution.minimum[1] - 0.1, color="black", marker="*")

            self.MplWidget.canvas.axes.plot(solution.minimum[0], solution.minimum[1], color="red", marker="o")
            self.solutionX.setText(
                "(" + str(round(solution.minimum[0], 7)) + ", " + str(round(solution.minimum[1], 7)) + ")")
            self.solutionIterCount.setText("Пройдено " + str(solution.spent_iter) + " итераций")
            self.finalFuncLabel.setText("f(x) =  " + str(opt_params.a) +" * sin( " + str(opt_params.b) +" * x) + " + str(opt_params.c) +"  * cos( " + str(opt_params.d) +" * x)")
            self.SecondWindow.show()
            self.MplWidget.canvas.draw()
        except ValueError:
            self.labelErr.setText(_translate("MainWindow", "Неправильные параметры ввода"))
        except Exception:
            self.labelErr.setText(_translate("MainWindow", "Неожиданная ошибка ("))

