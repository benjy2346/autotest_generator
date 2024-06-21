import sys  
from PyQt5.QtWidgets import QTextEdit, QCheckBox, QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout  
from PyQt5.QtCore import Qt  
from template_prompts import template_prompts
from request import connect2llm
import os

class TestCaseGenerator(QMainWindow):  
    def __init__(self):  
        super().__init__()  
  
        self.initUI()  
  
    def initUI(self):  
        self.setWindowTitle('雷达产品以太网配置测试用例生成器')  
  
        # 布局和控件  
        main_widget = QWidget(self)  
        self.setCentralWidget(main_widget)  
        layout = QVBoxLayout(main_widget)  
        
        self.llm_engine_label = QLabel('引擎',self)
        layout.addWidget(self.llm_engine_label)

        
        self.llm_engine = QComboBox(self)
        self.llm_engine.addItems(['百度/文心一言/ERNIE-Speed'])
        layout.addWidget(self.llm_engine)
        
        self.ai_identity_label = QLabel('ai身份设定',self)
        layout.addWidget(self.ai_identity_label)
        
        self.capacity = QLineEdit(self)
        self.capacity.setText('你是一个测试工程师')
        layout.addWidget(self.capacity)
  
        self.info_block_label = QLabel('包含信息：',self)
        layout.addWidget(self.info_block_label)
        
        self.info_blocks = QLabel('测试模块、测试标题、前置条件、测试步骤、预期结果、实际结果、测试方法',self)
        layout.addWidget(self.info_blocks)
  
        # 生成个数 
        
        self.min_data_count_label= QLabel('生成测试用例个数',self) 
        layout.addWidget(self.min_data_count_label) 
        
        self.min_data_count= QLineEdit(self)  
        self.min_data_count.setText('0')
 
        layout.addWidget(self.min_data_count) 
  
        # 测试方法
        
        self.testing_methods_label= QLabel('测试方法：',self) 
        layout.addWidget(self.testing_methods_label)
        check_box_group = QWidget(self)  
        check_box_layout = QGridLayout(check_box_group)  
        #   '等价类划分法、边界值方法、因果图法、判定表法、正交排列法、错误推算法、场景法等'
        self.check_box_1 = QCheckBox('等价类划分法', self)  
        self.check_box_2 = QCheckBox('边界值方法', self)  
        self.check_box_3 = QCheckBox('因果图法', self)  
        self.check_box_4 = QCheckBox('判定表法', self)  
        self.check_box_5 = QCheckBox('错误推算法', self) 
        self.check_box_6 = QCheckBox('场景法', self) 

        
        check_box_layout.addWidget(self.check_box_1, 0, 0)  
        check_box_layout.addWidget(self.check_box_2, 0, 1)  
        check_box_layout.addWidget(self.check_box_3, 1, 0, 1, 2)  # 跨列  
        check_box_layout.addWidget(self.check_box_4, 1, 1, 1, 1)  # 跨列  
        check_box_layout.addWidget(self.check_box_5, 2, 1, 1, 2)  # 跨列  
        check_box_layout.addWidget(self.check_box_6, 2, 2, 1, 3)  # 跨列         
        layout.addWidget(check_box_group)  

        
        # 信息板块
        # info_blocks = QWidget(self)  
        # info_blocks_layout = QGridLayout(info_blocks)  
        # #   '测试模块、测试标题、前置条件、测试步骤、预期结果、实际结果、测试方法等'
        # self.info_blocks_1 = QCheckBox('测试模块', self)  
        # self.info_blocks_2 = QCheckBox('测试标题', self)  
        # self.info_blocks_3 = QCheckBox('前置条件', self)  
        # self.info_blocks_4 = QCheckBox('测试步骤', self)  
        # self.info_blocks_5 = QCheckBox('预期结果', self) 
        # self.info_blocks_6 = QCheckBox('实际结果', self) 
        # self.info_blocks_7 = QCheckBox('测试方法', self) 
        
        # info_blocks_layout.addWidget(self.info_blocks_1, 0, 0)  
        # info_blocks_layout.addWidget(self.info_blocks_2, 0, 1)  
        # info_blocks_layout.addWidget(self.info_blocks_3, 1, 0, 1, 2)  # 跨列  
        # info_blocks_layout.addWidget(self.info_blocks_4, 1, 1, 1, 1)  # 跨列  
        # info_blocks_layout.addWidget(self.info_blocks_5, 2, 1, 1, 2)  # 跨列  
        # info_blocks_layout.addWidget(self.info_blocks_6, 2, 2, 1, 3)  # 跨列    
        # info_blocks_layout.addWidget(self.info_blocks_7, 2, 0, 1, 1)  # 跨列       
        # layout.addWidget(info_blocks)  
    
        # 测试模块包括 
        self.testing_module_included_label = QLabel('测试模块：',self)
        layout.addWidget(self.testing_module_included_label)
        
        self.testing_module_included = QLineEdit(self)
        layout.addWidget(self.testing_module_included)
        
        speed_info_label = QLabel('产品背景描述:', self)   
        layout.addWidget(speed_info_label)  

        self.textEdit = QTextEdit()  
        self.textEdit.setMinimumSize(400, 300)  
        layout.addWidget(self.textEdit)  
        
        
        # 生成按钮  
        generate_button = QPushButton('生成测试用例', self)  
        generate_button.clicked.connect(self.generate_testcase)  
        layout.addWidget(generate_button)  
        self.setGeometry(300, 300, 300, 200)  
        self.show()
                
    def generate_testcase(self):  
        
        
        testing_methods = '测试方法中必须包括：'
        for t in [self.check_box_1,
                  self.check_box_2,
                  self.check_box_3,
                  self.check_box_4,
                  self.check_box_5,
                  self.check_box_6]:
            if t.isChecked():
                testing_methods += t.text() + '、'
        testing_methods = testing_methods[:-2] + '。'
        
    
        capacity = self.capacity.text()
        insight = self.textEdit.toPlainText()
        testing_module_included = self.testing_module_included.text()
        if testing_module_included != '':
            testing_module_included = '测试模块必须包括：' +  testing_module_included 
        personality_requirements=''
        info_blocks = self.info_blocks.text()
        min_data_num = self.min_data_count.text()
        connect2llm(insight,info_blocks,personality_requirements,min_data_num,testing_module_included,testing_methods,capacity)


        
if __name__ == '__main__':  
    app = QApplication([])  
    widget = TestCaseGenerator()  
    widget.show()  
    app.exec_()