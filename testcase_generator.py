from qss import qss
from PyQt5.QtWidgets import QTextEdit, QCheckBox, QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout  
from template_prompts import template_prompts
from engine import connect2llm
from PyQt5.QtGui import QIcon 
class TestCaseGenerator(QMainWindow):  
    def __init__(self):  
        super().__init__()  

        self.initUI()  
        self.setStyleSheet(qss)  
            
            
    def initUI(self):  
        self.setWindowTitle('雷达产品以太网配置测试用例生成器')  
  
        # 布局和控件  
        main_widget = QWidget(self)  
        self.setCentralWidget(main_widget)  
        layout = QVBoxLayout(main_widget)  
        
        self.llm_engine_label = QLabel('引擎',self)
        layout.addWidget(self.llm_engine_label)

        
        self.llm_engine = QComboBox(self)
        self.llm_engine.addItems(['百度/文心一言/ERNIE-Speed',"Llama3_Instruct"])
        layout.addWidget(self.llm_engine)
        
        self.accumulate = QComboBox(self)
        self.accumulate.addItems(['累计',"非累计"])
        layout.addWidget(self.accumulate)
        
        self.ai_identity_label = QLabel('ai身份设定',self)
        layout.addWidget(self.ai_identity_label)
        
        self.capacity = QLineEdit(self)
        self.capacity.setText('你是一个测试工程师')
        layout.addWidget(self.capacity)
  
        # self.info_block_label = QLabel('包含信息：',self)
        # layout.addWidget(self.info_block_label)
        
        # self.info_blocks = QLabel('测试模块、测试标题、前置条件、测试步骤、预期结果、实际结果、测试方法',self)
        # layout.addWidget(self.info_blocks)

  
        # 测试方法
        
        # self.testing_methods_label= QLabel('测试方法：',self) 
        # layout.addWidget(self.testing_methods_label)
        # check_box_group = QWidget(self)  
        # check_box_layout = QGridLayout(check_box_group)  
        # #   '等价类划分法、边界值方法、因果图法、判定表法、正交排列法、错误推算法、场景法等'
        # self.check_box_1 = QCheckBox('等价类划分法', self)  
        # self.check_box_2 = QCheckBox('边界值方法', self)  
        # self.check_box_3 = QCheckBox('因果图法', self)  
        # self.check_box_4 = QCheckBox('判定表法', self)  
        # self.check_box_5 = QCheckBox('错误推算法', self) 
        # self.check_box_6 = QCheckBox('场景法', self) 

        
        # check_box_layout.addWidget(self.check_box_1, 0, 0)  
        # check_box_layout.addWidget(self.check_box_2, 0, 1)  
        # check_box_layout.addWidget(self.check_box_3, 1, 0, 1, 2)  # 跨列  
        # check_box_layout.addWidget(self.check_box_4, 1, 1, 1, 1)  # 跨列  
        # check_box_layout.addWidget(self.check_box_5, 2, 1, 1, 2)  # 跨列  
        # check_box_layout.addWidget(self.check_box_6, 2, 2, 1, 3)  # 跨列         
        # layout.addWidget(check_box_group)  
    
        runtime_envir_label = QLabel('运行环境', self)   
        layout.addWidget(runtime_envir_label)  

        self.runtime_envir = QTextEdit()  
        self.runtime_envir.setMinimumSize(100, 100)  
        self.runtime_envir.setText(
            '''我们的雷达产品以太网配置如下，
''')
        layout.addWidget(self.runtime_envir)  
        
        
        runtime_tools_label = QLabel('使用工具：', self)   
        layout.addWidget(runtime_tools_label)  

        self.runtime_tools = QTextEdit()  
        self.runtime_tools.setMinimumSize(200, 200)  
        self.runtime_tools.setText(
            '''
运行canoe工程文件，
运行capl脚本，
查看trace报文
''')
        layout.addWidget(self.runtime_tools)  
        
        parameter = QLabel('参数:(包含单位和取值范围)', self)   
        layout.addWidget(parameter)  

        
        self.textEdit = QTextEdit()  
        self.textEdit.setMinimumSize(100, 250)  
        self.textEdit.setText(
            '''协议版本: 2011 
domain number: 0 
BMCA设置: 关闭 
Announce Message: Disabled 
Signaling Message: Enabled by default 
asCapable: TRUE 
Clock type: Hardware Sync， interval: 125ms
Destination MAC Address: 01:80:C2:00:00:0E
Ethertype: 0x88F7 Two Step mode only 支持预定义Path Delay和Freq Ration 
角色：slave PDelay Interval: 1秒''')
        layout.addWidget(self.textEdit)  
        
        
        # 生成按钮  
        generate_button = QPushButton('生成测试用例', self)  
        generate_button.clicked.connect(self.generate_testcase)  
        layout.addWidget(generate_button)  
        self.setGeometry(300, 300, 300, 200)  
        self.show()
                
    def generate_testcase(self):  
        
        
        # testing_methods = '测试方法中必须包括：'
        # for t in [self.check_box_1,
        #           self.check_box_2,
        #           self.check_box_3,
        #           self.check_box_4,
        #           self.check_box_5,
        #           self.check_box_6]:
        #     if t.isChecked():
        #         testing_methods += t.text() + '、'
        # testing_methods = testing_methods[:-2] + '。'
        
    
        capacity = self.capacity.text()
        insight = self.textEdit.toPlainText()
       
        testing_methods = '等价类划分法、边界值方法、因果图法、判定表法、正交排列法、错误推算法、场景法等。'
        personality_requirements=''
        info_blocks = '测试模块、测试标题、前置条件、测试步骤、预期结果、实际结果、测试方法等。'
        engine = self.llm_engine.currentText()
        t = self.accumulate.currentText()
        if  t== "非累计":
            accumulate = False
        else:
            accumulate = True
        connect2llm(engine,accumulate, insight,info_blocks,personality_requirements,testing_methods,capacity)
        
        

        
if __name__ == '__main__':  
    import sys
    from PyQt5.QtCore import Qt
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    widget = TestCaseGenerator()  
    
    widget.setMinimumSize(1700,1300)
 
    widget.setWindowIcon(QIcon('ai.png'))
    widget.move(0,100)
    widget.show()  
    app.exec_()