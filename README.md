# OracleTimingBackup
Python练手程序。

Python实现， Oracle定时备份，使用命令行方式调用，定时备份指定oracle。

调用命令：
python oracletimingbackup.py -d #Z:\bak\# -t #time# -s #OracleSid# -u #username# -p #password# 
帮助命令：
--help

-d 表示备份目录文件夹(必须存在),默认D盘根目录;  
-t 表示备份循环时间（单位分钟），默认60;  
-s 表示数据库实例名;  
-u 表示数据库用户名;  
-p 表示数据库密码;  
