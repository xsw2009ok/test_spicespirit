# -*- coding:utf-8 -*-

import sys,unittest,os,HTMLTestRunner,time

reload(sys)
sys.setdefaultencoding('utf-8')


''' 找出TestCase目录下所有的*Test.py文件'''
def suite():
    dir_case = unittest.defaultTestLoader.discover(
        os.getcwd()+'\\TestCase',
        pattern='*Test.py',
        top_level_dir=None,
    )
    return dir_case

'''获取当前时间'''
def getNowTime():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

'''生成报告'''
def runTestCase():
    htmlpath = os.getcwd() + '\\TestReport\\TestReport_' +getNowTime()+'.html'
    fp = open(htmlpath,'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description=u'自动化测试结果详情'
    )
    runner.run(suite())
    #unittest.TextTestRunner(verbosity=2).run(suite())

if __name__=='__main__':
    runTestCase()
