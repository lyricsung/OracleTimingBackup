import os
import sys
import getopt
import time

#备份目录
dir="d:"
#备份循环时间 如60 表示60分钟备份
timer="60"
#数据库实例名
oracle_ssid="orcl"
#数据库用户名
oracle_user="system"
#数据库密码
oracle_pwd="wsyj9003"

exp_node1 = "\n成功备份文件到目录...."

exp_node2 = "备份失败"



#获取命令参数 -d f:\test2\ -t 10 -s orcl -u nguser -p 9003
def getArgv(argv):
    try:
        options, args = getopt.getopt(argv, "hd:t:s:u:p:", ["help"])
    except getopt.GetoptError:
        sys.exit()
    if len(options)==1 and options[0][0]=="--help":
        print("-d 表示备份目录文件夹(必须存在),默认D盘根目录;")
        print("-t 表示备份循环时间（单位分钟），默认60;")
        print("-s 表示数据库实例名;")
        print("-u 表示数据库用户名;")
        print("-p 表示数据库密码;")
        return False

    for option, value in options:
        if option=="-d":
            global  dir
            dir = value
            print("目录: {0}".format(value))
        if option=="-t":
            global timer
            timer = value
            print("时间: {0}".format(value))
        if option=="-s":
            global  oracle_ssid
            oracle_ssid = value
            print("数据库名: {0}".format(value))
        if option=="-u":
            global  oracle_user
            oracle_user = value
            print("数据库用户: {0}".format(value))
        if option=="-p":
            global  oracle_pwd
            oracle_pwd = value
            print("数据库密码: {0}".format(value))
    return True
#检查路径
def check_path(str):
    ''''' 检查源文件和备份路径 '''
    if not os.path.exists(str):
        print("文件夹 {0} 不存在".format(str))
        return False
    return True

#获取日期
def getdate(): # 获取n天前的日期
    ctime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    return ctime

def oracle_exp():
    if oracle_user in ("system","sys"):
        exp_command = "exp %s/%s@%s file=%s%s_%s-%s-%s_%s%s%s.dmp full=y log=%s%s_%s-%s-%s_%s%s%s.log" % (
        oracle_user, oracle_pwd, oracle_ssid, dir, oracle_ssid, time.strftime('%Y'), time.strftime('%m'),
        time.strftime('%d'), time.strftime('%H'), time.strftime('%M'), time.strftime('%S'), dir, oracle_ssid,
        time.strftime('%Y'), time.strftime('%m'), time.strftime('%d'), time.strftime('%H'), time.strftime('%M'),
        time.strftime('%S'))
    else:
        exp_command = "exp %s/%s@%s file=%s%s_%s-%s-%s_%s%s%s.dmp log=%s%s_%s-%s-%s_%s%s%s.log" % (
        oracle_user, oracle_pwd, oracle_ssid, dir, oracle_ssid, time.strftime('%Y'), time.strftime('%m'),
        time.strftime('%d'), time.strftime('%H'), time.strftime('%M'), time.strftime('%S'), dir, oracle_ssid,
        time.strftime('%Y'), time.strftime('%m'), time.strftime('%d'), time.strftime('%H'), time.strftime('%M'),
        time.strftime('%S'))
    #exp_command = "exp %s/%s@%s file=%s%s_%s-%s-%s_%s%s%s.dmp full=y log=%s%s_%s-%s-%s_%s%s%s.log"  % (oracle_user,oracle_pwd,oracle_ssid,dir,oracle_ssid,time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),time.strftime('%H'),time.strftime('%M'),time.strftime('%S'),dir,oracle_ssid,time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),time.strftime('%H'),time.strftime('%M'),time.strftime('%S'))
    exp_note = "数据库开始执行备份语句...."
    print(exp_note)
    print(exp_command)
    if os.system(exp_command) == 0:
        print(exp_node1)
    else:
        print(exp_node2)


if __name__=='__main__':
    #获取命令参数
    if(getArgv(sys.argv[1:])):
        # 检查目录
        check_path(dir)
        curTime = getdate()
        # print(curTime)
        # 开始备份数据库
        while True:
            oracle_exp()
            time.sleep(int(timer)*60)
