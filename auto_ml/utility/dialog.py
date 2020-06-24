# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import config
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def __init__(self):   
        super(Ui_Dialog, self).__init__()
        self.setupUi()

    
    def setupUi(self):
        cfg = config.load_config()       
        
        self.setObjectName("Dialog")
        self.resize(438, 310)
        self.comboBox_saved_count = QtWidgets.QComboBox(self)
        self.comboBox_saved_count.setGeometry(QtCore.QRect(359, 225, 71, 21))
        self.comboBox_saved_count.setObjectName("comboBox_saved_count")
        self.comboBox_saved_count.addItem("")
        self.comboBox_saved_count.addItem("")
        self.comboBox_saved_count.addItem("")
        self.comboBox_saved_count.addItem("")
        self.comboBox_saved_count.addItem("")
        self.comboBox_saved_count.addItem("")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(273, 210, 81, 51))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 4, 141, 30))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(10, 30, 241, 271))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_BernoulliNB = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_BernoulliNB.setEnabled(True)
        self.checkBox_BernoulliNB.setCheckable(True)
        self.checkBox_BernoulliNB.setChecked(cfg['search_space']['BernoulliNB'])
        self.checkBox_BernoulliNB.setObjectName("checkBox_BernoulliNB")
        self.gridLayout.addWidget(self.checkBox_BernoulliNB, 11, 1, 1, 1)
        self.checkBox_LogisticRegression = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_LogisticRegression.setEnabled(True)
        self.checkBox_LogisticRegression.setCheckable(True)
        self.checkBox_LogisticRegression.setChecked(cfg['search_space']['LogisticRegression'])
        self.checkBox_LogisticRegression.setObjectName("checkBox_LogisticRegression")
        self.gridLayout.addWidget(self.checkBox_LogisticRegression, 9, 0, 1, 1)
        self.checkBox_XGBoost = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_XGBoost.setChecked(cfg['search_space']['XGBoost'])
        self.checkBox_XGBoost.setObjectName("checkBox_XGBoost")
        self.gridLayout.addWidget(self.checkBox_XGBoost, 1, 0, 1, 1)
        self.checkBox_AdaBoost = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_AdaBoost.setChecked(cfg['search_space']['AdaBoost'])
        self.checkBox_AdaBoost.setObjectName("checkBox_AdaBoost")
        self.gridLayout.addWidget(self.checkBox_AdaBoost, 0, 0, 1, 1)
        self.checkBox_GaussianProcess = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_GaussianProcess.setEnabled(True)
        self.checkBox_GaussianProcess.setCheckable(True)
        self.checkBox_GaussianProcess.setChecked(cfg['search_space']['GaussianProcess'])
        self.checkBox_GaussianProcess.setObjectName("checkBox_GaussianProcess")
        self.gridLayout.addWidget(self.checkBox_GaussianProcess, 9, 1, 1, 1)
        self.checkBox_NearestCentroid = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_NearestCentroid.setEnabled(True)
        self.checkBox_NearestCentroid.setCheckable(True)
        self.checkBox_NearestCentroid.setChecked(cfg['search_space']['NearestCentroid'])
        self.checkBox_NearestCentroid.setObjectName("checkBox_NearestCentroid")
        self.gridLayout.addWidget(self.checkBox_NearestCentroid, 8, 1, 1, 1)
        self.checkBox_LinearSVC = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_LinearSVC.setEnabled(True)
        self.checkBox_LinearSVC.setCheckable(True)
        self.checkBox_LinearSVC.setChecked(cfg['search_space']['LinearSVC'])
        self.checkBox_LinearSVC.setObjectName("checkBox_LinearSVC")
        self.gridLayout.addWidget(self.checkBox_LinearSVC, 7, 0, 1, 1)
        self.checkBox_DecisionTree = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_DecisionTree.setEnabled(True)
        self.checkBox_DecisionTree.setCheckable(True)
        self.checkBox_DecisionTree.setChecked(cfg['search_space']['DecisionTree'])
        self.checkBox_DecisionTree.setObjectName("checkBox_DecisionTree")
        self.gridLayout.addWidget(self.checkBox_DecisionTree, 5, 1, 1, 1)
        self.checkBox_GaussianNB = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_GaussianNB.setEnabled(True)
        self.checkBox_GaussianNB.setCheckable(True)
        self.checkBox_GaussianNB.setChecked(cfg['search_space']['GaussianNB'])
        self.checkBox_GaussianNB.setObjectName("checkBox_GaussianNB")
        self.gridLayout.addWidget(self.checkBox_GaussianNB, 12, 1, 1, 1)
        self.checkBox_ELM = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_ELM.setEnabled(True)
        self.checkBox_ELM.setCheckable(True)
        self.checkBox_ELM.setChecked(cfg['search_space']['ELM'])
        self.checkBox_ELM.setObjectName("checkBox_ELM")
        self.gridLayout.addWidget(self.checkBox_ELM, 3, 1, 1, 1)
        self.checkBox_SVM = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_SVM.setEnabled(True)
        self.checkBox_SVM.setCheckable(True)
        self.checkBox_SVM.setChecked(cfg['search_space']['SVM'])
        self.checkBox_SVM.setObjectName("checkBox_SVM")
        self.gridLayout.addWidget(self.checkBox_SVM, 0, 1, 1, 1)
        self.checkBox_Ridge = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_Ridge.setEnabled(True)
        self.checkBox_Ridge.setCheckable(True)
        self.checkBox_Ridge.setChecked(cfg['search_space']['Ridge'])
        self.checkBox_Ridge.setObjectName("checkBox_Ridge")
        self.gridLayout.addWidget(self.checkBox_Ridge, 6, 0, 1, 1)
        self.checkBox_RandomForest = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_RandomForest.setEnabled(True)
        self.checkBox_RandomForest.setCheckable(True)
        self.checkBox_RandomForest.setChecked(cfg['search_space']['RandomForest'])
        self.checkBox_RandomForest.setObjectName("checkBox_RandomForest")
        self.gridLayout.addWidget(self.checkBox_RandomForest, 1, 1, 1, 1)
        self.checkBox_HistGB = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_HistGB.setEnabled(True)
        self.checkBox_HistGB.setCheckable(True)
        self.checkBox_HistGB.setChecked(cfg['search_space']['HistGB'])
        self.checkBox_HistGB.setObjectName("checkBox_HistGB")
        self.gridLayout.addWidget(self.checkBox_HistGB, 5, 0, 1, 1)
        self.checkBox_SGD = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_SGD.setEnabled(True)
        self.checkBox_SGD.setCheckable(True)
        self.checkBox_SGD.setChecked(cfg['search_space']['SGD'])
        self.checkBox_SGD.setObjectName("checkBox_SGD")
        self.gridLayout.addWidget(self.checkBox_SGD, 6, 1, 1, 1)
        self.checkBox_PassiveAggressive = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_PassiveAggressive.setEnabled(True)
        self.checkBox_PassiveAggressive.setCheckable(True)
        self.checkBox_PassiveAggressive.setChecked(cfg['search_space']['PassiveAggressive'])
        self.checkBox_PassiveAggressive.setObjectName("checkBox_PassiveAggressive")
        self.gridLayout.addWidget(self.checkBox_PassiveAggressive, 8, 0, 1, 1)
        self.checkBox_MLP = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_MLP.setChecked(cfg['search_space']['MLP'])
        self.checkBox_MLP.setObjectName("checkBox_MLP")
        self.gridLayout.addWidget(self.checkBox_MLP, 3, 0, 1, 1)
        self.checkBox_KNeighbors = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_KNeighbors.setEnabled(True)
        self.checkBox_KNeighbors.setCheckable(True)
        self.checkBox_KNeighbors.setChecked(cfg['search_space']['KNeighbors'])
        self.checkBox_KNeighbors.setObjectName("checkBox_KNeighbors")
        self.gridLayout.addWidget(self.checkBox_KNeighbors, 7, 1, 1, 1)
        self.checkBox_xRandTrees = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_xRandTrees.setEnabled(True)
        self.checkBox_xRandTrees.setCheckable(True)
        self.checkBox_xRandTrees.setChecked(cfg['search_space']['xRandTrees'])
        self.checkBox_xRandTrees.setObjectName("checkBox_xRandTrees")
        self.gridLayout.addWidget(self.checkBox_xRandTrees, 2, 1, 1, 1)
        self.checkBox_BaggingSVC = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_BaggingSVC.setEnabled(True)
        self.checkBox_BaggingSVC.setCheckable(True)
        self.checkBox_BaggingSVC.setChecked(cfg['search_space']['Bagging(SVC)'])
        self.checkBox_BaggingSVC.setObjectName("checkBox_BaggingSVC")
        self.gridLayout.addWidget(self.checkBox_BaggingSVC, 2, 0, 1, 1)
        self.checkBox_LabelSpreading = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_LabelSpreading.setEnabled(True)
        self.checkBox_LabelSpreading.setCheckable(True)
        self.checkBox_LabelSpreading.setChecked(cfg['search_space']['LabelSpreading'])
        self.checkBox_LabelSpreading.setObjectName("checkBox_LabelSpreading")
        self.gridLayout.addWidget(self.checkBox_LabelSpreading, 10, 1, 1, 1)
        self.checkBox_LDA = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_LDA.setEnabled(True)
        self.checkBox_LDA.setCheckable(True)
        self.checkBox_LDA.setChecked(cfg['search_space']['LDA'])
        self.checkBox_LDA.setObjectName("checkBox_LDA")
        self.gridLayout.addWidget(self.checkBox_LDA, 10, 0, 1, 1)
        self.checkBox_QDA = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_QDA.setEnabled(True)
        self.checkBox_QDA.setCheckable(True)
        self.checkBox_QDA.setChecked(cfg['search_space']['QDA'])
        self.checkBox_QDA.setObjectName("checkBox_QDA")
        self.gridLayout.addWidget(self.checkBox_QDA, 11, 0, 1, 1)
        self.checkBox_Perceptron = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_Perceptron.setEnabled(True)
        self.checkBox_Perceptron.setCheckable(True)
        self.checkBox_Perceptron.setChecked(cfg['search_space']['Perceptron'])
        self.checkBox_Perceptron.setObjectName("checkBox_Perceptron")
        self.gridLayout.addWidget(self.checkBox_Perceptron, 12, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setGeometry(QtCore.QRect(270, 30, 161, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_PolynomialNetwork = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_PolynomialNetwork.setEnabled(True)
        self.checkBox_PolynomialNetwork.setCheckable(True)
        self.checkBox_PolynomialNetwork.setChecked(cfg['search_space']['PolynomialNetwork'])
        self.checkBox_PolynomialNetwork.setObjectName("checkBox_PolynomialNetwork")
        self.gridLayout_2.addWidget(self.checkBox_PolynomialNetwork, 2, 0, 1, 1)
        self.checkBox_FactorizationMachine = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_FactorizationMachine.setChecked(cfg['search_space']['FactorizationMachine'])
        self.checkBox_FactorizationMachine.setObjectName("checkBox_FactorizationMachine")
        self.gridLayout_2.addWidget(self.checkBox_FactorizationMachine, 1, 0, 1, 1)
        self.checkBox_DBN = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_DBN.setEnabled(True)
        self.checkBox_DBN.setCheckable(True)
        self.checkBox_DBN.setChecked(cfg['search_space']['DBN'])
        self.checkBox_DBN.setObjectName("checkBox_DBN")
        self.gridLayout_2.addWidget(self.checkBox_DBN, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(273, 106, 81, 51))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.comboBox_metric = QtWidgets.QComboBox(self)
        self.comboBox_metric.setGeometry(QtCore.QRect(361, 120, 69, 22))
        self.comboBox_metric.setObjectName("comboBox_metric")
        self.comboBox_metric.addItem("")
        self.comboBox_metric.addItem("")
        self.comboBox_metric.addItem("")
        self.comboBox_metric.addItem("")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(273, 156, 81, 51))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.comboBox_validation = QtWidgets.QComboBox(self)
        self.comboBox_validation.setGeometry(QtCore.QRect(361, 170, 69, 22))
        self.comboBox_validation.setObjectName("comboBox_validation")
        self.comboBox_validation.addItem("")
        self.comboBox_validation.addItem("")
        self.comboBox_validation.addItem("")
        self.comboBox_validation.addItem("")
        
        
        
        self.btn_ok = QtWidgets.QPushButton(self)
        self.btn_ok.setGeometry(QtCore.QRect(350, 270, 81, 31))
        self.btn_ok.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_ok.setAcceptDrops(False)
        self.btn_ok.setCheckable(False)
        self.btn_ok.setAutoRepeat(False)
        self.btn_ok.setAutoExclusive(False)
        self.btn_ok.setAutoDefault(True)
        self.btn_ok.setDefault(True)
        self.btn_ok.setFlat(False)
        self.btn_ok.setObjectName("btn_ok")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(270, 4, 141, 30))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.frame_2.raise_()
        self.comboBox_saved_count.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.frame_3.raise_()
        self.label_3.raise_()
        self.comboBox_metric.raise_()
        self.label_5.raise_()
        self.comboBox_validation.raise_()
        self.btn_ok.raise_()
        self.label_4.raise_()

        self.retranslateUi(self)
        self.btn_ok.clicked.connect(self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.btn_ok, self.comboBox_saved_count)
        
        self.setModal(True) # !!!
        
        
        saved_count_index = self.getIndexComboBox(cfg['search_options']['saved_top_models_amount'],'saved_count')
        metric_index = self.getIndexComboBox(cfg['search_options']['metric'],'metric')
        validation_index = self.getIndexComboBox(cfg['search_options']['validation'],'validation')
        
        self.comboBox_saved_count.setCurrentIndex(saved_count_index)
        self.comboBox_metric.setCurrentIndex(metric_index)
        self.comboBox_validation.setCurrentIndex(validation_index)

        
        
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Дополнительные настройки"))
        self.comboBox_saved_count.setItemText(0, _translate("Dialog", "Все"))
        self.comboBox_saved_count.setItemText(1, _translate("Dialog", "Лучшая"))
        self.comboBox_saved_count.setItemText(2, _translate("Dialog", "Топ 5"))
        self.comboBox_saved_count.setItemText(3, _translate("Dialog", "Топ 10"))
        self.comboBox_saved_count.setItemText(4, _translate("Dialog", "Топ 25"))
        self.comboBox_saved_count.setItemText(5, _translate("Dialog", "Топ 50"))
        
        self.label.setText(_translate("Dialog", "Количество сохраняемых моделей"))
        self.label_2.setText(_translate("Dialog", "Пространство поиска"))
        self.checkBox_BernoulliNB.setText(_translate("Dialog", "BernoulliNB"))
        self.checkBox_LogisticRegression.setText(_translate("Dialog", "LogisticRegression"))
        self.checkBox_XGBoost.setText(_translate("Dialog", "XGBoost"))
        self.checkBox_AdaBoost.setText(_translate("Dialog", "AdaBoost"))
        self.checkBox_GaussianProcess.setText(_translate("Dialog", "GaussianProcess"))
        self.checkBox_NearestCentroid.setText(_translate("Dialog", "NearestCentroid"))
        self.checkBox_LinearSVC.setText(_translate("Dialog", "SVM(linear)"))
        self.checkBox_DecisionTree.setText(_translate("Dialog", "DecisionTree"))
        self.checkBox_GaussianNB.setText(_translate("Dialog", "GaussianNB"))
        self.checkBox_ELM.setText(_translate("Dialog", "ELM"))
        self.checkBox_SVM.setText(_translate("Dialog", "SVM"))
        self.checkBox_Ridge.setText(_translate("Dialog", "Ridge"))
        self.checkBox_RandomForest.setText(_translate("Dialog", "RandomForest"))
        self.checkBox_HistGB.setText(_translate("Dialog", "HistGB"))
        self.checkBox_SGD.setText(_translate("Dialog", "SGD"))
        self.checkBox_PassiveAggressive.setText(_translate("Dialog", "PassiveAggressive"))
        self.checkBox_MLP.setText(_translate("Dialog", "MLP"))
        self.checkBox_KNeighbors.setText(_translate("Dialog", "KNeighbors"))
        self.checkBox_xRandTrees.setText(_translate("Dialog", "xRandTrees"))
        self.checkBox_BaggingSVC.setText(_translate("Dialog", "BaggingSVС"))
        self.checkBox_LabelSpreading.setText(_translate("Dialog", "LabelSpreading"))
        self.checkBox_LDA.setText(_translate("Dialog", "LDA"))
        self.checkBox_QDA.setText(_translate("Dialog", "QDA"))
        self.checkBox_Perceptron.setText(_translate("Dialog", "Perceptron"))
        self.checkBox_PolynomialNetwork.setText(_translate("Dialog", "PolynomialNetwork"))
        self.checkBox_FactorizationMachine.setText(_translate("Dialog", "FactorizationMachine"))
        self.checkBox_DBN.setText(_translate("Dialog", "DBN"))
        self.label_3.setText(_translate("Dialog", "Метрика"))
        self.comboBox_metric.setItemText(0, _translate("Dialog", "accuracy"))
        self.comboBox_metric.setItemText(1, _translate("Dialog", "f1"))
        self.comboBox_metric.setItemText(2, _translate("Dialog", "f1_micro"))
        self.comboBox_metric.setItemText(3, _translate("Dialog", "f1_macro"))
        self.label_5.setText(_translate("Dialog", "Валидация"))
        self.comboBox_validation.setItemText(0, _translate("Dialog", "10 fold CV"))
        self.comboBox_validation.setItemText(1, _translate("Dialog", "5 fold CV"))
        self.comboBox_validation.setItemText(2, _translate("Dialog", "3 fold CV"))
        self.comboBox_validation.setItemText(3, _translate("Dialog", "holdout"))
        self.btn_ok.setText(_translate("Dialog", "Применить"))
        self.label_4.setText(_translate("Dialog", "Экспериментальные"))
        
        
        
    def getIndexComboBox(self, str_val, CB_type):
        items=[]
        
        if(CB_type == 'saved_count'):
            items.append("Все")
            items.append("Лучшая")
            items.append("Топ 5")
            items.append("Топ 10")
            items.append("Топ 25")
            items.append("Топ 50")
            for i in range(0, len(items)):
                if(items[i]==str_val):
                    return i
              
        elif(CB_type == 'metric'):
            items.append("accuracy")
            items.append("f1")
            items.append("f1_micro")
            items.append("f1_macro")
            for i in range(0, len(items)):
                if(items[i]==str_val):
                    return i
            
        elif(CB_type == 'validation'):
            items.append("10 fold CV")
            items.append("5 fold CV")
            items.append("3 fold CV")
            items.append("holdout")
            for i in range(0, len(items)):
                if(items[i]==str_val):
                    return i  
        return -1 # error
            
                 







class Ui_WarningPaths(QDialog):
    def __init__(self):   
        super(Ui_WarningPaths, self).__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("WarningPaths")
        self.resize(234, 106)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(140, 70, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.setModal(True)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.setModal(True)

    def retranslateUi(self, WarningPaths):
        _translate = QtCore.QCoreApplication.translate
        WarningPaths.setWindowTitle(_translate("WarningPaths", "Предупреждение"))
        self.label.setText(_translate("WarningPaths", "Файл с набором данных и файл с описанием его столбцов должны быть загружены"))




class Ui_WarningName(QDialog):
    def __init__(self):   
        super(Ui_WarningName, self).__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("WarningName")
        self.resize(234, 106)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(140, 70, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.setModal(True)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.setModal(True)

    def retranslateUi(self, WarningPaths):
        _translate = QtCore.QCoreApplication.translate
        WarningPaths.setWindowTitle(_translate("WarningPaths", "Предупреждение"))
        self.label.setText(_translate("WarningPaths", "Название эксперимента не должно быть пустым"))




class Ui_WarningModels(QDialog):
    def __init__(self):   
        super(Ui_WarningModels, self).__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("WarningName")
        self.resize(234, 106)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(140, 70, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.setModal(True)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.setModal(True)

    def retranslateUi(self, WarningPaths):
        _translate = QtCore.QCoreApplication.translate
        WarningPaths.setWindowTitle(_translate("Ui_WarningModels", "Предупреждение"))
        self.label.setText(_translate("WarningPaths", "Выберите хотя бы один алгоритм классификации"))




