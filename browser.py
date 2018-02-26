from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("曲师教务系统")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version alpha bete1"))
        layout.addWidget(QLabel("Copyright 2018 段瀛轩 Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://202.194.188.21"))

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("工具栏")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon(os.path.join('images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)
        
        person_menu = self.menuBar().addMenu("&个人管理")
        
        userInfo = QAction(QIcon(os.path.join('images', 'question.png')), "个人信息", self)
        userInfo.setStatusTip("显示个人信息")  # Hungry!
        userInfo.triggered.connect(self.userInfo_action)
        person_menu.addAction(userInfo)
        
        xjInfoAction = QAction(QIcon(os.path.join('images', 'question.png')), "学籍信息", self)
        xjInfoAction.setStatusTip("显示学籍信息")  # Hungry!
        xjInfoAction.triggered.connect(self.xjInfoAction_action)
        person_menu.addAction(xjInfoAction)
        
        ydxx = QAction(QIcon(os.path.join('images', 'question.png')), "学籍信息", self)
        ydxx.setStatusTip("显示学籍异动信息")  # Hungry!
        ydxx.triggered.connect(self.ydxx_action)
        person_menu.addAction(ydxx)
        
        jcxx = QAction(QIcon(os.path.join('images', 'question.png')), "奖惩信息", self)
        jcxx.setStatusTip("显示奖惩信息")  # Hungry!
        jcxx.triggered.connect(self.jcxx_action)
        person_menu.addAction(jcxx)
        
        xsFabgsqAction = QAction(QIcon(os.path.join('images', 'question.png')), "辅修方案注册", self)
        xsFabgsqAction.setStatusTip("显注册辅修方案")  # Hungry!
        xsFabgsqAction.triggered.connect(self.xsFabgsqAction_action)
        person_menu.addAction(xsFabgsqAction)
        
        xjydcxAction = QAction(QIcon(os.path.join('images', 'question.png')), "学籍异动申请", self)
        xjydcxAction.setStatusTip("学籍异动申请")  # Hungry!
        xjydcxAction.triggered.connect(self.xjydcxAction_action)
        person_menu.addAction(xjydcxAction)
        
        xtcxAction = QAction(QIcon(os.path.join('images', 'question.png')), "网上选题", self)
        xtcxAction.setStatusTip("查询网上选题")  # Hungry!
        xtcxAction.triggered.connect(self.xtcxAction_action)
        person_menu.addAction(xtcxAction)
        
        lwtjAction = QAction(QIcon(os.path.join('images', 'question.png')), "论文提交", self)
        lwtjAction.setStatusTip("论文提交")  # Hungry!
        lwtjAction.triggered.connect(self.lwtjAction_action)
        person_menu.addAction(lwtjAction)
        
        queryAction = QAction(QIcon(os.path.join('images', 'question.png')), "毕业设计程序查询", self)
        queryAction.setStatusTip("毕业设计成绩查询")  # Hungry!
        queryAction.triggered.connect(self.queryAction_action)
        person_menu.addAction(queryAction)
        
        lwyxsjAction = QAction(QIcon(os.path.join('images', 'question.png')), "优秀毕业设计名单查询", self)
        lwyxsjAction.setStatusTip("优秀毕业设计名单查询")  # Hungry!
        lwyxsjAction.triggered.connect(self.lwyxsjAction_action)
        person_menu.addAction(lwyxsjAction)

        xk_menu = self.menuBar().addMenu("&选课管理")

        wsxk = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "网上选课", self)
        wsxk.setStatusTip("网上选课")
        wsxk.triggered.connect(self.wsxk_action)
        xk_menu.addAction(wsxk)
        
        xkjg = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "选课结果", self)
        xkjg.setStatusTip("选课结果")
        xkjg.triggered.connect(self.xkjg_action)
        xk_menu.addAction(xkjg)
        
        tk = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "退课", self)
        tk.setStatusTip("退课")
        tk.triggered.connect(self.tk_action)
        xk_menu.addAction(tk)
        
        wxxkjg = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "无效选课结果", self)
        wxxkjg.setStatusTip("无效选课结果")
        wxxkjg.triggered.connect(self.wxxkjg_action)
        xk_menu.addAction(wxxkjg)
        
        bxqkb = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "本学期课表", self)
        bxqkb.setStatusTip("本学期课表")
        bxqkb.triggered.connect(self.bxqkb_action)
        xk_menu.addAction(bxqkb)
        
        lnkb = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "历年课表", self)
        lnkb.setStatusTip("历年课表")
        lnkb.triggered.connect(self.lnkb_action)
        xk_menu.addAction(lnkb)
        
        sykxk = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "实验课选课", self)
        sykxk.setStatusTip("实验课选课")
        sykxk.triggered.connect(self.sykxk_action)
        xk_menu.addAction(sykxk)
        
        bxqzhkb = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "本学期综合表", self)
        bxqzhkb.setStatusTip("本学期综合表")
        bxqzhkb.triggered.connect(self.bxqzhkb_action)
        xk_menu.addAction(bxqzhkb)
        
        syxkWcgAll = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "未选中、已删除课程", self)
        syxkWcgAll.setStatusTip("未选中、已删除课程")
        syxkWcgAll.triggered.connect(self.syxkWcgAll_action)
        xk_menu.addAction(syxkWcgAll)

        ks_menu = self.menuBar().addMenu("&考务管理")
        
        ksApCxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "考试安排", self)
        ksApCxAction.setStatusTip("查询考试安排情况")
        ksApCxAction.triggered.connect(self.ksApCxAction_action)
        ks_menu.addAction(ksApCxAction)
        
        kwBmAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "考试报名", self)
        kwBmAction.setStatusTip("报名参加考试")
        kwBmAction.triggered.connect(self.kwBmAction_action)
        ks_menu.addAction(kwBmAction)
        
        cjSearchAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "考试成绩", self)
        cjSearchAction.setStatusTip("查询考试成绩")
        cjSearchAction.triggered.connect(self.cjSearchAction_action)
        ks_menu.addAction(cjSearchAction)
        
        jx_menu = self.menuBar().addMenu("&教学资源")
        
        jskbcxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "教室课表", self)
        jskbcxAction.setStatusTip("查询教室课表")
        jskbcxAction.triggered.connect(self.jskbcxAction_action)
        jx_menu.addAction(jskbcxAction)
        
        lskbcxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "教师课表", self)
        lskbcxAction.setStatusTip("查询教师课表")
        lskbcxAction.triggered.connect(self.lskbcxAction_action)
        jx_menu.addAction(lskbcxAction)
        
        bjkbcxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "班级课表", self)
        bjkbcxAction.setStatusTip("查询班级课表")
        bjkbcxAction.triggered.connect(self.bjkbcxAction_action)
        jx_menu.addAction(bjkbcxAction)
        
        kckbcxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "课程课表", self)
        kckbcxAction.setStatusTip("查询课程课表")
        kckbcxAction.triggered.connect(self.kckbcxAction_action)
        jx_menu.addAction(kckbcxAction)
        
        xszxcxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "自习教室", self)
        xszxcxAction.setStatusTip("查询无课教室")
        xszxcxAction.triggered.connect(self.xszxcxAction_action)
        jx_menu.addAction(xszxcxAction)
        
        jxlCxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "教室使用情况查询", self)
        jxlCxAction.setStatusTip("教室使用情况查询")
        jxlCxAction.triggered.connect(self.jxlCxAction_action)
        jx_menu.addAction(jxlCxAction)
        
        zh_menu = self.menuBar().addMenu("&综合查询")
        
        gradeLnAllAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "全部及格成绩", self)
        gradeLnAllAction.setStatusTip("查询全部及格成绩")
        gradeLnAllAction.triggered.connect(self.gradeLnAllAction_action)
        zh_menu.addAction(gradeLnAllAction)
        
        kcsxcj = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "课程属性成绩", self)
        kcsxcj.setStatusTip("查询课程属性成绩")
        kcsxcj.triggered.connect(self.kcsxcj_action)
        zh_menu.addAction(kcsxcj)
        
        fa = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "方案成绩", self)
        fa.setStatusTip("查询方案成绩")
        fa.triggered.connect(self.fa_action)
        zh_menu.addAction(fa)
        
        bjg = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "不及格成绩", self)
        bjg.setStatusTip("查询不及格成绩")
        bjg.triggered.connect(self.bjg_action)
        zh_menu.addAction(bjg)
        
        bxqcjcxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "本学期成绩", self)
        bxqcjcxAction.setStatusTip("查询本学期成绩")
        bxqcjcxAction.triggered.connect(self.bxqcjcxAction_action)
        zh_menu.addAction(bxqcjcxAction)
        
        fawc = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "方案完成情况", self)
        fawc.setStatusTip("查询方案完成情况")
        fawc.triggered.connect(self.fawc_action)
        zh_menu.addAction(fawc)
        
        zdxjxjh = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "指导性教学完成情况", self)
        zdxjxjh.setStatusTip("查询指导性教学完成情况")
        zdxjxjh.triggered.connect(self.zdxjxjh_action)
        zh_menu.addAction(zdxjxjh)
        
        courseSearchAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "本学期课程安排", self)
        courseSearchAction.setStatusTip("查询本学期课程安排")
        courseSearchAction.triggered.connect(self.courseSearchAction_action)
        zh_menu.addAction(courseSearchAction)
        
        kclbAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "课程基本信息", self)
        kclbAction.setStatusTip("查询课程基本信息")
        kclbAction.triggered.connect(self.courseSearchAction_action)
        zh_menu.addAction(kclbAction)
        
        pg_menu = self.menuBar().addMenu("&教学评估")
        
        ckgg = QAction(QIcon(os.path.join('images', 'question.png')), "评估公告", self)
        ckgg.setStatusTip("查询评估公告")
        ckgg.triggered.connect(self.ckgg_action)
        pg_menu.addAction(ckgg)
        
        jxpgXsAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "教学评估", self)
        jxpgXsAction.setStatusTip("进行教学评估")
        jxpgXsAction.triggered.connect(self.jxpgXsAction_action)
        pg_menu.addAction(jxpgXsAction)
        
        byspgXsAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "毕业生评估", self)
        byspgXsAction.setStatusTip("查看毕业生评估")
        byspgXsAction.triggered.connect(self.byspgXsAction_action)
        pg_menu.addAction(byspgXsAction)
        
        jcsfjzhsc_menu = self.menuBar().addMenu("&教材收费及综合审查")
        
        jcglAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "教材查询", self)
        jcglAction.setStatusTip("教材查询")
        jcglAction.triggered.connect(self.jcglAction_action)
        jcsfjzhsc_menu.addAction(jcglAction)
        
        jcxxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "教材选定查询", self)
        jcxxAction.setStatusTip("教材选定查询")
        jcxxAction.triggered.connect(self.jcxxAction_action)
        jcsfjzhsc_menu.addAction(jcxxAction)
        
        jclqcx = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "教材领取查询", self)
        jclqcx.setStatusTip("教材领取查询")
        jclqcx.triggered.connect(self.jclqcx_action)
        jcsfjzhsc_menu.addAction(jclqcx)
        
        sfCxAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "收费标准查询", self)
        sfCxAction.setStatusTip("收费标准查询")
        sfCxAction.triggered.connect(self.sfCxAction_action)
        jcsfjzhsc_menu.addAction(sfCxAction)
        
        scTxQueryAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "审查体系", self)
        scTxQueryAction.setStatusTip("审查体系查询")
        scTxQueryAction.triggered.connect(self.scTxQueryAction_action)
        jcsfjzhsc_menu.addAction(scTxQueryAction)
        
        scJlQueryAction = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "审查结论", self)
        scJlQueryAction.setStatusTip("审查结论查询")
        scJlQueryAction.triggered.connect(self.scJlQueryAction_action)
        jcsfjzhsc_menu.addAction(scJlQueryAction)
        
        xk_menu = self.menuBar().addMenu("&更多")

        about_action = QAction(QIcon(os.path.join('images', 'question.png')), "关于", self)
        about_action.setStatusTip("查看更多信息")  # Hungry!
        about_action.triggered.connect(self.about)
        xk_menu.addAction(about_action)
        
        self.show()

        self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - 曲阜师范大学教务系统" % title)

    def userInfo_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/userInfo.jsp"))
    
    def xjInfoAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xjInfoAction.do?oper=xjxx"))

    def ydxx_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xjInfoAction.do?oper=ydxx"))    

    def jcxx_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xjInfoAction.do?oper=jcxx"))        
        
    def xsFabgsqAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xsFabgsqAction.do?oper=faxdsq1"))       
    
    def xjydcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xjydcxAction.do"))          

    def xtcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xtcxAction.do"))        

    def lwtjAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/lwtjAction.do?type=showXtjg"))  

    def queryAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/queryAction.do"))   

    def lwyxsjAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/lwyxsjAction.do"))  
    
    def wsxk_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xkAction.do"))  
        
    def xkjg_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xkAction.do?actionType=6"))
        
    def tk_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xkAction.do?actionType=7"))

    def wxxkjg_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xkAction.do?actionType=16"))    

    def bxqkb_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xkAction.do?actionType=6")) 

    def lnkb_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/lnkbcxAction.do"))          

    def sykxk_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/syglSyxkAction.do?ejkch=&oper=goTosykcList"))   

    def bxqzhkb_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/syglSyxkAction.do?&oper=xsxkKcbAll"))       

    def syxkWcgAll_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/syglSyxkAction.do?oper=syxkWcgAll"))       

    def ksApCxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/ksApCxAction.do?oper=getKsapXx"))       

    def kwBmAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/kwBmAction.do?oper=getKsList"))       

    def cjSearchAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.19/cjSearchAction.do?oper=getKscjList"))       
    
    def jskbcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/jskbcxAction.do?oper=jskb_lb"))         
 
    def lskbcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/lskbcxAction.do?oper=lskb_lb"))     
        
    def bjkbcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/bjkbcxAction.do?oper=bjkb_lb"))     

    def kckbcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/kckbcxAction.do?oper=kckb_lb"))     

    def xszxcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/xszxcxAction.do?oper=xszxcx_lb")) 

    def jxlCxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/jxlCxAction.do?oper=ori"))      
    
    def gradeLnAllAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/gradeLnAllAction.do?type=ln&oper=qb")) 
        
    def kcsxcj_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/gradeLnAllAction.do?type=ln&oper=sx")) 

    def fa_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/gradeLnAllAction.do?type=ln&oper=fa")) 

    def bjg_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/gradeLnAllAction.do?type=ln&oper=bjg")) 

    def bxqcjcxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/bxqcjcxAction.do")) 

    def fawc_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/gradeLnAllAction.do?type=ln&oper=lnfaqk&flag=zx")) 

    def zdxjxjh_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/gradeLnAllAction.do?type=ln&oper=lnjhqk")) 

    def courseSearchAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/courseSearchAction.do?temp=1")) 

    def courseSearchAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/kclbAction.do")) 
   
    def ckgg_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/ckgg.jsp?type=-1")) 
 
    def jxpgXsAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/jxpgXsAction.do?oper=listWj")) 
 
    def byspgXsAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/byspgXsAction.do?oper=listWj")) 
 
    def jcglAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/jcglAction.do?actionType=1&oper=xs")) 

    def jcxxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/jcxxAction.do?actionType=3&oper=xs")) 

    def jclqcx_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/jcxxAction.do?actionType=4&oper=xs"))   

    def sfCxAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/sfCxAction.do?oper=current"))   

    def scTxQueryAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/scTxQueryAction.do?oper=CurrentScTxQuery"))     

    def scJlQueryAction_action(self):
        self.browser.setUrl(QUrl("http://202.194.188.21/scJlQueryAction.do?oper=CurrentScJlQuery"))     
        
    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://202.194.188.21"))

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_urlbar(self, q):

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-ssl.png')))

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("曲阜师范大学教务系统")
app.setOrganizationName("段瀛轩")
app.setOrganizationDomain("ddcome.com")


'''
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.browser.setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.browser.page().mainFrame().toHtml()
            with open(filename, 'w') as f:
                f.write(html)

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()
'''
window = MainWindow()

app.exec_()
