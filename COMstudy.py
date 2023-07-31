#encoding=utf-8
#-------------------------------数据库编程-------------------------------------------------------------------------------------------
#SQL语句编写
# 查询记录：select 字段列表 from 表名 [where 条件]
# 查询表中的全部字段：*
# 插入记录：insert into 表名(列1,列2,...) values(值1,值2,...)
#     '当向表中所有字段添加记录时，可以省略表名后面（）里的内容
#     '表名和values有三个一致：数量一致、顺序一致、类型一致
# 删除记录：delete from 表名 [where 条件]，如果忽略条件，那么删除所有记录
# 更新记录：update 表名 set 字段=值 [where 条件]，如果忽略条件，那么更新所有记录
# 数据定义功能:
#        创建表：create table ...
#        删除表：drop table 表名
#        修改表：alter table 表名
'''
CREATE TABLE ＜表名＞ （＜列名＞＜数据类型＞ ［列级完整性约束条件］
[，＜列名＞＜数据类型＞ ［列级完整性约束条什］］   [，＜表级完整性约束条件＞］）
数据类型
CHAR(n), CHARACTER(n)                   长度为n的定长字符串
VARCHAR(n), CHARACTERVARYING1n          最大长度为n的变长字符串
CLOB                                    字符串大对象
BLOB                                    二进制大对象
INT, INTEGER                            长整数 (4字节）
SMALLINT                                短整数 (2字节）
BIGINT                                  大整数 (8字节）
NUMERIC(p,d)                            定点数，由p位数字（不包括符号、小数点）组成，小数点后面有d 位数字
FLOAT(n)                                可选精度的浮点数，精度至少为n位数字
BOOLEAN                                 逻辑布尔量
DATE                                    包含年、月、日，格式为YYYY-MM-DD
TIME                                    时、分、秒，格式为HH:MM:SS
TIMESTAMP                               时间戳类型
INTERVAL                                时间间隔类型
REAL                                    取决于机器精度的单精度浮点数
sql = "create table 期末成绩(学号 text(10) not null,""姓名 text(8) not null,性别 text(1) not null,"
"班级 text(10) not null,语文 single not null,""数学 single not null,英语 single not null,"
"物理 single not null,化学 single not null,""生物 single not null,总分 single not null)"
'''
# 增加字段：alter table 表名 add 字段名 类型(大小)
# sql = "alter table " & myTable & " add 备注 text(50)"
# 删除字段：alter table 表名 drop 字段名
# sql = "alter table 成绩 drop 备注"
# 修改字段类型和大小：alter table 表名 alter 字段名 类型(大小)
# sql = "alter table 成绩 alter 课程代码 text(20)"

#字段查询
#     sql = "select * from 院系"                  '3-1：查询全部字段（*）
#     sql = "select 姓名,性别,职称 from 导师"     '3-2：指定部分字段
#     sql = "select distinct 研究方向 from 学生"  '3-3：提取不重复记录
#     sql = "select 课程代码,成绩 from 成绩 order by 成绩 asc"   '3-4：排序 desc降序
#     sql = "select *,2006 from 学生"             '3-5：生成新的字段
#     sql = "select 学号,姓名,性别,year(入学日期) as 年份 from 学生" '3-6  计算现有字段
#     sql = "select 姓名,性别,'学生' as 身份 from 学生 union all select 姓名,性别,'老师' as 身份 from 导师"  增加新字段
# union:去除重复，并按照第一个字段升序排序
# union all：全部复制，重复的也不管，不排序
# 3、条件查询（where 条件）
# 3-1：等于或不等于查询
# sql = "select * from 学生 where 性别<>'男'"  '!=
# sql = "select * from 成绩 where 成绩 >80 order by 成绩 desc"
# 3-2：列表查询（In或Not In）
# sql = "select * from 学生 where 研究方向 in('风险投资','项目投资')"
# sql = "select * from 学生 where 研究方向 not in('风险投资','项目投资')"
#
# 3-3：介于查询（Between）
# sql = "select * from 成绩 where 成绩 between 70 and 80"
# 3-4：空值查询（Null）
# sql = "select * from 成绩 where 成绩 is not null"
# 3-5：字符连接（&）  shift+7
# sql = "select 学号&姓名 as 学号姓名,性别,班级 from 学生"
# sql = "select * from 学生 where 性别='女' and 班级='1班'"
# sql = "select * from 学生 where 性别&班级='女1班'"

# 3、模糊查询（where 字段 Like 统配表达式）
#   %   任意字符
#   _   单个字符
#   []  字符集
# sql = "select * from 员工 where 姓名 like '李%'"
# sql = "select * from 员工 where 姓名 like '%丽'"
# sql = "select * from 员工 where 简历 not like '%摄影%'"
# sql = "select * from 员工 where 姓名 like '张_'"
# sql = "select * from 员工 where 姓名 like '__'"
# sql = "select * from 员工 where 电子邮件 like '[!h-m]%'"
# sql = "select * from 员工 where 身份证号 like '______199[0-9]%'"
# sql = "select * from 员工 where 户籍&工作地 like '%北京%'"
# sql = "select * from 员工 where 姓名 like '[张王李刘]%'"
# 3 分组计算查询
# 3-1：聚合函数（sum、avg、max、min、count）
# 普通字段不能与聚合函数同时放到一起，因为它们得到的记录条数不对应
# 普通字段如果与聚合函数同时出现在select后面，那么普通字段要么聚合、要么分组。
# sql = "select count(部门) as 总人数,avg(年龄) as 平均年龄 from 员工"
# 3-2：分组统计（gourp by）
# sql = "select 部门,avg(年龄) as 平均年龄 from 员工 group by 部门"
# 3-3：小组筛选（having）
# sql = "select 部门,avg(年龄) as 平均年龄 from 员工 group by 部门 having avg(年龄)<=35"
# 3 ?生成表查询
# 3-1：将查询结果生成一个新表
# sql = "select * into 优秀 from 成绩 where 成绩>=90"
# 3-2：将查询结果追加到已有的表
# sql = "insert into 优秀 select * from 成绩 where 成绩 between 85 and 89"

#多表查询
#1 等值查询（Where连接）    sql = "select * from tablename1,tablename2,tablename3 " & "where 学生.学号=成绩.学号 and 课程.课程代码=成绩.课程代码"
#eg  sql = "select * from 学生,课程,成绩 " & "where 学生.学号=成绩.学号 and 课程.课程代码=成绩.课程代码"
#2 内连接      from 课程 inner join 成绩 on 课程.课程代码=成绩.课程代码 "
# 例：查询所有课程的平均成绩，结果包含课程名称、平均成绩2个字段
# sql = "select 课程名称 as 课程,avg(成绩) as 平均成绩 " _
#     & "from 课程 inner join 成绩 on 课程.课程代码=成绩.课程代码 " _
#     & "group by 课程名称 having avg(成绩)>=85"
#3 （外连接）基本格式:from 左表 连接类型(left、right、full） 右表 on 连接条件
# 左连接：左表连接字段有的，而右表没有的，左表全部显示，右表留空
# 右连接：右表连接字段有的，而左表没有的，右表全部显示，左表留空
#全连接：Excel不支持全连接，其他标准数据库支持全连接，并集查询
#4 自连接
# Select语句的执行顺序：from-->where-->group-->having-->select
# sql = "select 课程名称 as 课程,avg(成绩) as 平均成绩 " _
#     & "from 课程 inner join 成绩 on 课程.课程代码=成绩.课程代码 " _
#     & "where 课程<>'投资学' group by 课程名称 "
#4 子查询（也叫嵌套查询）
# 1 子查询必须用小括号括起来
# 2、在一个select语句中，子查询必定会首先执行
# 用法1：将子查询做数据源
# sql = "select 部门,count(*) as 人数 from (select * from 员工 where 年龄>=30) group by 部门"
# sql = "select * from (select 部门,count(*) as 人数 from 员工 group by 部门) order by 人数"
# 用法2：将子查询做条件
# 1、当子查询的结果只有1个值的时候，where条件后面可以使用=  <  >  <>
# 2、当子查询的结果有多个值的时候，where条件必须用in   not in
# 3 、子查询只能有1个字段
# 例2：查询年龄高于平均年龄的员工信息，包含姓名、身份证号、部门、年龄、职务
# sql = "select 姓名,性别,部门,年龄,职务 from 员工 where 年龄>(select avg(年龄) from 员工)"
# sql = "select 部门,avg(年龄) from 员工 group by 部门"
# 例3：查询年龄排在第5-10名的员工信息，包含姓名、身份证号、部门、年龄、职务
# sql = "select top 6 姓名,性别,部门,年龄,职务 from 员工 where 年龄 not in(select top 4 年龄 from 员工 order by 年龄 desc)"
#------------------------------------ODBC方式-------------------------------------------------------------------
# import odbc
# '''
# #连接出错时，卸载office,重新安装
# odbc数据库编程，定义数据源，配置32或64位odbc,SysWOW64\odbcad32.exe或C:\Windows\System32\odbcad32.exe
# '''
# db=odbc.odbc('db')      #管理工具数据源定义名称
# # help(db)
# cursor=db.cursor()
# cursor.execute("select * from 学生")
# # help(cursor)
# print(cursor.description)
# result=cursor.fetchall()
# for col in cursor.description:
#     print(col)
# for row in result:
#     print(row)
#     print(row[0])
# sql="update 学生 set 姓名='黄小丽',性别='女' where 学号='A01200601'"
# result1=cursor.execute(sql)     #无返回值
# ---------------------------------pypyodbc-------python database api2.0标准----------------------------------------------------
# import pypyodbc
# con=pypyodbc.connect("DSN=db")          #通过数据源DSN连接
# con=pypyodbc.connect("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\study.accdb")      #不需要配置数据源，路径与数据库不能有汉字
# cursor=con.cursor()
# for table in cursor.tables(tableType='table') :      #获取所有表
#     print(table)
# sql='select name from MSysObjects WHERE Type=1 and Flags=0'
# for table in cursor.execute(sql):
#     print(table)
# for table in cursor.columns(table='员工'):
    # print(table)
# rs=cursor.execute("select * from 学生")
# cursor.fetchall()
# print(result[0])
# print(b)      #修改数据时影响的行数
# print(cursor.description)
# print(cursor.statement)
#----------------------------------adodbapi--------------------------------------------------------
# import adodbapi
# conn=adodbapi.connect("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=学生管理.accdb" )
# for tbname in conn.get_table_names():
#     print(tbname)
# cursor=conn.cursor()
# cursor.execute('select * from 学生')
# print(cursor.columnNames)
# for row in cursor.fetchall():
#     print(row[0],row['姓名'])
#----------------------------------sqlite3--------------------------------------------------------
# import sqlite3
# db=sqlite3.connect('test.db')
# cursor=db.cursor()
# -----------------------------------ADO方式----------------------------------------------------
# 从CLSID生成COM对象     pywin32         无法加载工程需要的包时可能是创建文件路径被删除
# from win32com.client import Dispatch
# from adodbapi.ado_consts import *
# import adodbapi       #见\Python38\Lib\site-packages\adodbapi\examples例子获取所有表名
# conn=Dispatch('ADODB.Connection')              #实例化ADO连接对象
# source="Provider=Microsoft.ACE.OLEDB.12.0;Data Source=学生管理.accdb"       #12.0版本对应access2010驱动,不需要设置数据源
# source=r"Provider=Microsoft.ACE.OLEDB.12.0;User ID=Admin;Data Source=F:\个人学习\2021年度改进\读书计划文件\Ofice 高级应用\excel\VBA Access\学生管理.accdb;Mode=Share Deny None;Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";"
# conn.Open(source)       #连接出错时，卸载office,重新安装
# co=conn.Version
# rs=Dispatch('ADODB.Recordset')      #实例化记录集对象
# rs=conn.OpenSchema(adSchemaTables)
#
# print(rs)

# sql="select * from 学生"
# rs.Open(sql,conn)
# rs.Open(sql,conn,CursorType=3,LockType=4)   #静态游标与只读同时用才有效
# rs.Open(sql,conn,CursorType=1)   #静态游标与只读同时用才有效
# print(rs.CursorType)
# print(rs.LockType)
# print(rs.RecordCount)       #只有键值游标或静态游标时才返回实际行数
# array = rs.GetRows(-1)
# print(array)
# rs.AddNew(('学号','导师编号'),('A04200604',19))
# rs.Update()
# rs.UpdateBatch()
# rs.MoveFirst()
# while not rs.EOF:
#     for x in range(rs.Fields.count):
#         print(rs.Fields.Item(x).Name,end='  ')
#         print(rs.Fields.Item(x),end='  ')
#         print(rs.Fields('学号'))
#         print()
#     rs.MoveNext()
# rs.Close()
# conn.Close()



# -------------------------使用COM组件----------------------------------------------------------
# import win32com.client as win32
# import pythoncom
# a=Dispatch('{00024500-0000-0000-C000-000000000046}')   or a=Dispatch('Excel.Application')     #动态引用
# a=Dispatch('{00024500-0000-0000-C000-000000000046}')
# a=win32.Dispatch('Excel.Application')           #创建win32实例对象
# 从CLSID找到ProgID名称，有缓存时可能出错
# from pythoncom import ProgIDFromCLSID
# a=ProgIDFromCLSID('{00024500-0000-0000-C000-000000000046}')
# print(a)
# ----------------------------------------------------------------------------
# 调用对象属性、方法
# activeworkbook=a.WorkBooks.Open(r"C:\Users\Administrator\Desktop\学习模块.xlsx")
# workbook=a.ActiveWorkbook
# print(activeworkbook.ActiveSheet.Name)
# a.Visible = 1
# a.workbooks.Add()
# class worksheet:
    # def OnSheetActivate(self,name):
    # def OnSheetSelectionChange(self,sh,Target):     #对应程序级别事件名称
    #     print(sh.Name,Target.Address)
    # def OnSelectionChange(self,target):             #对应工作表级别事件名称
    #     print(target.Address)
    #     print('this worksheetevents')
# ac=win32.GetActiveObject('Excel.Application')
# events=win32.WithEvents(ac,worksheet)           #ac是程序级别事件
# activesheet=ac.ActiveSheet
# import numpy as np
# activesheet.Range("a1:d1").Value=np.array([1,6,8,3])
# activesheet.Range("a1:d2").Value=[[10,6,8,3],[3,9,0,7]]
# events=win32.WithEvents(activesheet,worksheet)      ##对应工作表级别事件
# while True:
#     pythoncom.PumpWaitingMessages()
# a.Cells(1,1)=98
# a.quit()
# -----------------------------------------------------------------------------------
# import pythoncom
# print(pythoncom.CreateGuid())   #用python控制台运行不会出错
#------------------------------------------------------------------------------------
#COM组件开发,本质上是调用此文件
# import pythoncom
# class COMstudy:
#     _reg_clsctx_=pythoncom.CLSCTX_LOCAL_SERVER
# #可不用，改python版本
#     _public_methods_=['SplitString']
#     _reg_progid_ = "COMstudy"
#     _reg_clsid_ = "{81C7B82E-1F6D-4DAC-98D9-4FB4F4A64E4A}"
#     def SplitString(self, val, item=None):
#         import string
#         if item!=None:
#             item=str(item)
#         return str(val).split(item)
#         # return string.split(str(val),item)
# if __name__=='__main__':          #运行此操作并不会实际注册
#     print("Registering COM server...")
#     import win32com.server.register
#     win32com.server.register.UseCommandLine(COMstudy)
#必须在当前文件目录下CMD 控制台注册此文件才能在其它地方用，已注册成功到注册表.按住shift不放，点右键，进入CMD
#目录CMD下 python COMstudy.py  注册。#excel创建对象，Set a = CreateObject("COM_excel")
#测试可用
# a=Dispatch('COMstudy')
# print(a.SplitString("Hello from me"))
#=========================================================================================
# 生成虚拟数据    faker   模块
# from faker import Faker
# import pandas as pd
# faker=Faker(['zh_CN'])
# # Faker.seed(0)
# lis_key=["姓名","身份证","出生年月","手机号码","邮箱","工作","公司","公司地址","邮区编号"]
# df=pd.DataFrame(columns=lis_key)
# def get_data():
#     name=faker.name()
#     ssn=faker.ssn()
#     birthday=faker.date(pattern="%Y-%m-%d", end_datetime=None)
#     company=faker.company()
#     phone_number=faker.phone_number()
#     address=faker.address()
#     email=faker.email()
#     job=faker.job()
#     postcode=faker.postcode()       #邮政编码；邮区号
#     port_number=faker.port_number() #端口号；通道数
#     street_address=faker.street_address()
#     lis_value=[name,ssn,birthday,phone_number,email,job,company,address,postcode]
#     person_info=dict(zip(lis_key,lis_value))
#     return person_info
# for i in range(1000):
#     person_info=[get_data()]
#     df1=pd.DataFrame(person_info)
#     df=pd.concat([df,df1])
# df.reset_index(drop=True,inplace=True)
# df.index=df.index+1
# df.to_excel(r"C:\Users\Administrator\Desktop\faker_data.xlsx",index=False)
# print(faker.simple_profile(sex=None))
# print(faker.profile(fields=None, sex=None))         #详细个人信息
# print(faker.date(pattern="%Y-%m-%d", end_datetime=None))
# df1=pd.Series(data=person_info)
# help(Faker(['zh_CN']).name())
# info=Factory.create()
# print(info.__dict__)
# print(faker.providers)
#=========================================================================================
# import numpy as np
# a=np.arange(9)
# a=np.arange(9).reshape(3,3)
# a=np.array([[1,2,3],[4,5,6]])
# a=np.zeros(9)
# a=np.ones(9)
# b=np.ones_like(a)
# b=np.eye(3)
# b=np.empty(8)
# a=np.random.randn(8)        #符合正态分布
# print(a)
# b=np.arange(8)
# print(a.clip(3, 6))
# print(b.compress(b>3))  # compress方法返回一个根据给定条件筛选后的数组。
# print(np.diff(a))
# print(np.ravel(a))
# print(np.ravel(a))
# a.flatten()     #flatten 这个函数恰如其名，flatten就是展平的意思，与ravel函数的功能相同。不过，flatten函数会请求分配内存来保存结果，而ravel函数只是返回数组的一个视图（view）
# b=np.where(a > 4)       #。where函数可以根据指定的条件返回所有满足条件的数组元素的索引值。
# print(np.take(a,b))
# print(np.argmin(a))
# print(np.maximum(a))
# print(np.where(a > 4)[1])
# print(a[np.where(a > 4)])
# print(np.full((3, 3), 8))
# print(np.full_like(a, 8))
# print(np.linspace(1,8,5))
# print(np.logspace(2, 20, 10))

# print(a.tolist())
# print(a.T)
# print(a[1,1])       #第2个元素，第2列
# print(a[:,1])       #行列选择元素，列表式
# print(a.ndim,a.shape,sep='\t-----')
# a=np.mat([[2,3],[1,2]])
# b=np.mat([[3,-2],[-2,1]])
# print(np.dot(a,b))
#=========================================================================================
#matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# line=plt.plot([1,4,6,9,16,6,3],ls='--')
# t=np.arange(0.,5.,0.2)
# lines=plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')         #绘制多条线,返回Line2D对象列表
# print(type(lines[1]))
# plt.setp(lines[2],color='y', linewidth=5.0)     #Line2D对象属性
# plt.setp(line)      #获取可设置的线条属性的列表

# plt.grid(visible=True)
# plt.show()
# plt.close()     #

#=========================================================================================
#pandas
# import pandas as pd
# path=r"C:\Users\Administrator\Desktop\pandas_test.xlsx"
# df=pd.Series(lis1,index=['a','b','c','d','e'])
# df1=pd.DataFrame(lis2,lis3)
# df=pd.DataFrame()   #创建空数据框
# df=pd.DataFrame(columns=['序号','生产单位','数量','单价'])   #创建列名称的空数据框

#外面是列表
# lis=[['序号','生产单位','数量','单价']]   #创建一行数据框
# lis=[['序号','生产单位','数量','单价'],['001','深圳上药','23','500.00'],['002','广东股份','58','80.00']]   #创建多行数据框
# lis=[{'序号':'001','生产单位':'深圳上药','数量':'23','单价':'500.00'}]   #创建指定列名的一行数据框
# lis=[{'序号':'001','生产单位':'深圳上药','数量':'23','单价':'500.00'},{'序号':'002','生产单位':'Americ','数量':'89','单价':'90.00'}]   #创建指定列名的多行数据框

#外面是字典
# lis={'序号':['001','深圳上药','23','500.00']}  #创建一列的数据框
# lis={'序号':['001','深圳上药','23','500.00'],'名称':['阿西洛韦','深圳上药','78','40.00']}  #创建多列的数据框
# lis={'序号':{'001':'阿莫西林','数量':'23','单价':'500.00'},'名称':{'001':'阿西洛韦','数量':'78','单价':'40.00'}}  #创建多列指定索引的数据框
# df=pd.DataFrame(lis)

# df1=pd.read_excel(path,usecols=['序号','生产单位','数量','单价'],index_col=0)
# df2=pd.read_excel(path,sheet_name="sheet2",usecols=['序号','生产单位','单价','数量'],index_col=0)
# df2=pd.read_excel(path,sheet_name="sheet2",index_col=0).head(10)
# pd.set_option('display.max_columns',100)
# pd.set_option('display.unicode.east_asian_width',True)
# print(df)
# print(df2)
# df1=pd.read_excel(path)['单价']
# df2=df1.info()
# df1=df1.iloc[:,1]
# df1=df1.iloc[0:2,1]             #不含标题，从1开始
# print(df1.at[2,'数量'])        #获取单个值
# print(df1.flags)
# print(df1.index)
# print(list(df1.columns))
# print(df1.ndim)
# print(df1.shape)
# print(df1.head(3))
# help(df1.to_excel)
# help(pd.read_excel)
# help(df1.query)
# print(df1[df1["单价"].between(218,240)],end="----------------------------")
# print(df1[df1["单价"].between(218,240,"right")])
# print(df1[df1["单价"].between(218,240).apply(lambda x:not x)])

# print(df1[df1["单价"]>250])
# print(df1.query("单价>250 & 单价<270"))
# help(df1.iterrows)
# for index,row in df1.iterrows():
#     print(index,row["单价"],sep="-------------")
#     if index == 5686:
#         break
# print(df1.append(df2))
# print(pd.concat([df1,df2],axis=0))
# help(pd.concat)
#数据库交互
# import sqlite3
# con=sqlite3.connect(r"test.db")
# df=pd.read_sql("select * from user",con=con)
# print(df)
# cur=con.cursor()
# rs=cur.execute("select * from sqlite_master").fetchall()    #获取数据库所有表
# new_df=df.head(2)
# new_df.to_sql("user",con,if_exists='append',index=False)        #提交数据到新表(表不存在则创建）
# con.commit()
# con.close()
# print(rs)

#mysql
# https://dev.mysql.com/downloads/windows/installer/      #安装mysql软件,仅安装服务器
# cmd 下输入启动命令，net start mysql版本，成功后，输入帐户密码，mysql -u root -p
# from sqlalchemy import create_engine
import pymysql
# db=pymysql.connect(user='root',password='123456',database='mr')
# cur=db.cursor()
# engine=create_engine('mysql+pymysql://root:root@localhost:3306/mysqltest?charset=utf8')
# df_write=pd.DataFrame({'ID':[1,2],'name':['ming','lili']})
# df_write.to_sql('sql',engine,if_exists='append',index=False)


#======================================================================================================================
# from sklearn.preprocessing import Binarizer,label_binarize
# x=[[1,4,2,0],[0.8,7,1,6]]
# x=[3,6,4,3,5,5,8,5,4,5,3,5]
# lable=label_binarize(x,classes=[3,4,5,6,8])     #标签独热编码并匹配结果
# print(lable)

# tr=Binarizer(threshold=4).fit(x)        #Binarize data (set feature values to 0 or 1) according to a threshold.
# print(tr.transform(x))
#======================================================================================================================
# import tensorflow as tf
# tf.estimator
# help(tf.python.)
#======================================================================================================================
# import pyautogui,pyperclip
# import re,win32gui
# im=pyautogui.screenshot("test.png",(50,50,200,300))  #PS吸管工具下，标尺可测距离，L表示两点间距离，H表示高度，W表示宽。按住shift以45度移动
# help(pyautogui.screenshot)
# ms=pyautogui.position()
# window=pyautogui.getActiveWindow()
# window=pyautogui.getAllTitles()
# window.minimize()
# a=pyautogui.getWindowsWithTitle('false data.xlsx - Excel')
# print(a)
# b=win32gui.GetWindowText(1902392)
# b=win32gui.GetClassName(1902392)
# print(b)
#
# print(a)
# print(window)
# pyautogui.sleep(5)
# pyautogui.click("window.PNG")        #window自带sniping tool工具可抓png图片，用于识别。此句识别窗口图片位置并单击。
# pyautogui.click("newford.PNG")
# i=pyautogui.getActiveWindow()
# print(pyautogui.getActiveWindowTitle())
# pyautogui.mouseInfo()
# location=pyautogui.locateOnScreen("window.PNG")     #定位匹配图片屏幕位置
# pyautogui.click(pyautogui.center(location))         #定位图像中心
# pyautogui.write("my first autogui\n",interval=0.3)      #控制键盘发送文字
# pyautogui.press(['m','y','g','u','i'],interval=0.3)      #模拟人按键盘操作
# pyautogui.keyDown('shift','ctrl')       #不能达到预期效果
#=========================
#可以达到预期效果
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('shift')
# pyautogui.press('right')
# pyautogui.keyUp('shift')
# pyautogui.keyUp('ctrl')     #应单独释放，否则可能释放不成功

# pyautogui.hold('ctrl','shift',"right")        #进入上下按键文管理器
# pyautogui.keyUp("right","shift","ctrl")
# pyperclip.copy("我是中国人")     #发送文字到剪切板，用于中文输入
# pyautogui.sleep(1)
# pyautogui.hotkey('ctrl','v')    #调用热键
#================================= pywinauto============================================================================
# from pywinauto.application import Application
# Application(backend="uia").start("notepad.exe")
# Application().start(r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
#=======================================================================================================================
# import win32api
# a=win32api.GetComputerName()
# a=win32api.InitiateSystemShutdown(win32api.GetComputerName())
# print(a)
# win32api.AbortSystemShutdown(a)

#=======================================================================================================================
# import pyautogui
# import subprocess,shlex             #shlex用于打开文件时分隔参数，否则出错
# app=subprocess.Popen(r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
# app=subprocess.Popen([r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE",r"F:\个人学习\2022年度改进\读书计划文件\pythonProject\false data.xlsx"])
# app=subprocess.Popen([r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE","false data.xlsx"])
# print(app.__doc__)
# pyautogui.PAUSE=20
# window=pyautogui.getActiveWindow()
# window.maximize()
# if not app.wait():        #等待进程操作完后，进程关闭或结束才进入下行代码
#     app.kill()
# else:
#     app.wait()


#=======================================================================================================================
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# im=Image.open(r"E:\PS自处理图片\_DSC5199.jpg")
# print(im.size)
# im=im.resize(size=(600,400))
# # im.resize(size=(300,200))     #无效
# new=Image.new(mode='RGB',size=(300,500),color="white")  #创建空白画板
# txt_im=ImageDraw.Draw(im)         #创建画笔对象，才能在其上绘图，文字
# txt_im=ImageDraw.Draw(new)
# logo=Image.open(r"E:\PS自处理图片\_DSC5199.jpg")
# box=(1000,700,5000,3000)        #,原点（0，0），座标必须正确，左、上、右、下，否则出错
# logo_file=logo.crop(box)
# font=ImageFont.truetype("STXINGKA.TTF",20)
# txt_im.text((20,50),text="我爱你，一生一世",fill=(0,255,255),font=font)
# logo_file.save("OK.jpg")
# im.paste(new,(0,0))
# im.paste(logo_file,(0,0))
# im.save(r"E:\PS自处理图片\_DSC5199-------ok.jpg")      #重命名不影响原图保存
# logo.close()
# im.close()
# im.show()
#=======================================================================================================================
# import schedule,time
# def time_task(gg):
#     print("my fixed time task",gg)
# schedule.every(2).seconds.do(time_task,"first")
# schedule.every().days.at("11:00").do(time_task,44)
# schedule.every().sunday.at("11:00").do(time_task,44)
# while True:
#     schedule.run_pending()
#     time.sleep(5)
# import time
# st=time.strftime("%Y-%m-%d  %H:%M:%S")
# print(st)
#=======================================================================================================================
#日志
# import logging
'''
Logger对象一般不会直接实例化得到，而是通过模块级别的函数logging.getLogger(name)得到。
以相同的名称多次调用getLogger()将永远返回相同Logger对象的引用。
name可以是一个以句号分隔的层次结构的值，比如foo.bar.baz（它也可以只是普通的foo）。层次列表下游的loggers是上游loggers的子孙。
例如，对于给定的一个logger对象 foo，其它logger对象foo.bar, foo.bar.baz, foo.bam，它们都是foo的子辈。
logger对象名字的层级和python包的层级是相似的,并且如果你使用推荐的结构logging.getLogger(__name__)来管理你的loggers对象的话，
那就与python包的层级结构是一模一样的。因为在一个模块中__name__是一个在python包中名字空间的模块的名称。

Logger.debug(msg, *args, **kwargs)
在logger上记录一条级别为DEBUG的消息。msg为消息格式字符串，args为通过字符串格式操作符合并到msg的参数。
（注意这意味着可以在格式字符串中使用关键字和一个字典参数。）
在kwargs中有三个关键字参数，它们被检查：exc_info，stack_info和extra。
如果exc_info不计算为假，则会导致将异常信息添加到日志记录消息中。如果提供了异常元组（以sys.exc_info()返回的格式）或异常实例，
则使用它；否则，调用sys.exc_info()以获取异常信息。
第二个可选的关键字参数是stack_info，默认为False。如果为true，则将堆栈信息添加到日志记录消息中，包括实际的日志调用。
注意，这不是通过指定exc_info显示的堆栈信息：前者是从堆栈底部到当前线程中的日志调用的堆栈帧，而后者是有关堆栈帧，它们在寻找异常处理程序时例外之后被解开。
您可以独立于exc_info指定stack_info，例如只是展示你如何到达代码中的某一点，即使没有引发异常。堆栈帧打印在标题行后面
第三个关键字参数是extra，可用于传递一个字典，用于填充为具有用户定义属性的日志记录事件创建的LogRecord的__dict__。你可以随意使用这些自定义属性。例如，它们可以合并到日志消息中。示例：
'''
# FORMAT = '%(asctime)-15s %(client_ipid)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'client_ipid': '192.168.0.1', 'user': 'fbloggs'}
# logger = logging.getLogger('tcpserver')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)
'''如果决定要在日志消息中使用这些属性，使用时要小心。拿上面的例子，Formatter的格式字符串期待LogRecord的属性字典中有'client_ipid'和'user'。
如果缺失的话，该消息就不会被记录，因为会发生字符串格式异常。在这种情况下，你总是要传递带这些键的extra字典。主要在一些特定的环境下使用。
如有一个多线程服务器，相同的代码会在许多上下文执行，而感兴趣的条件在上下文才会出现（如上例中的远端客户端IP地址和已认证用户名）。
在这种环境下，很可能对特殊的Handler使用特定的Formatter。
'''
'''
Logger.exception(msg, *args, **kwargs)
在该logger上以ERROR级别记录一条信息。其参数的解释与debug()相同。异常信息将添加到日志信息中。该方法应该只在异常处理器调用。
Logger.addFilter(filt)  添加指定的filter filt 到该logger。
Logger.removeFilter(filt)   删除该logger中的filter filt。
Logger.addHandler(hdlr) 将指定的handlerhdlr添加到logger中.Logger.removeHandler(hdlr)
Logger.handle(record)   处理一个record，将它传给该logger及其祖先的所有的handler（直到propagate为假为止）。
该方法用于从套接字接收到的反序列化的record，以及那些本地创建的。使用filter()日志级别过滤会应用。
Logger.makeRecord(name, lvl, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None)
这是一个工厂方法，可以在子类中覆盖它来创建特定的LogRecord实例。
Logger.hasHandlers()    检查此记录器是否已配置任何处理程序。这是通过在记录器层次结构中查找此记录器及其父节点中的处理程序来完成的。
如果找到处理程序，则返回True，否则False。当找到具有“propagate”属性设置为False的记录器时，该方法停止搜索层次结构 - 这将是检查处理程序是否存在的最后一个记录器。

Handler Objects
Handler不应该直接被实例化，此类应该作为基类来子类化出一些有用的类。然而，__init__()方法在子类中需要被Handler.__init__()来调用。
Handler.flush() 确保所有的日志输出被刷新。基类版本不做任何事情，留给子类来实现。
Handler.handleError(record) 此方法应该在调用emit()时遇到异常后从handlers被调用。如果模块级属性raiseExceptions为False，异常会被静默忽略掉。
日志系统常见的行为——大多数用户并不关心日志系统中的错误，他们只关心应用的错误。当然如果你愿意，你可以用自定义的处理器来替换它。
record参数是异常发生时正在处理的record。（raiseExceptions的默认值为True，这在开发中很有用）。
Handler.format(record)  格式化record，如果有formatter，使用formatter。否则使用模块默认的formatter。
Handler.emit(record)    做记录日志record真正需要的动作。基类版本抛出NotImplementedError，留给子类来实现。

Formatter Objects
负责将LogRecord转换（通常）成人类和其它系统可以理解的字符串。基类Formatter允许指定某个格式的字符串。
如果提供None，那么'%(message)s'将会作为默认值，它仅仅包括日志调用中的信息。
Formatter对象可以用一个使LogRecord的属性的反应信息有用的字符串来进行实例化。例如上面提到的用来使用户信息和参数预格式化进LogRecord对象的 message属性有效的默认值。
logging.Formatter(fmt=None, datefmt=None, style='%')
返回一个Formatter类的新实例。实例以整个消息的格式化字符串以及消息中日期／时间部分的格式化字符串来初始化。如果fmt不被指定, '%(message)s'将会被使用。
如果不指明datefmt，将使用ISO8601日期格式。style可以是 ‘%’, ‘{‘ or ‘$’中的任何一个，并且它决定格式化字符串将会怎样与它的数据融合.
format(record)  记录的属性字典被用作字符格式化操作的参数。返回结果字符串。在格式化字典之前将会执行一些准备性的动作。
记录的message属性用msg % args来计算。如果格式化字符串包含'(asctime)'，formatTime()将会被调用用以格式化事件的时间。
如果有异常信息，使用formatException()来格式化它，并将结果附加到消息。注意格式化过的异常信息缓存于exc_text属性。
这是有用的，因为异常信息可以被序列化并在网络上传递；但是如果你有多个Formatter子类，每个子类都定制了异常信息的格式化方式，这种情况下就得注意。
在这种情况下，在一个formatter完成了格式化操作之后需要清掉缓存的值，这样下一个formatter才会重新计算而不是使用缓存值。
如果堆栈信息可用，它将附加在异常信息之后，使用formatStack()在必要时对其进行转换。
formatException(exc_info)   将指明的异常信息（如sys.exc_info()返回的标准异常元组）格式化成字符串。默认实现使用traceback.print_exception()。返回结果字符串。
formatStack(stack_info) 格式化指定的堆栈信息（由traceback.print_stack()返回的字符串，但删除了最后一个换行符）作为字符串。这个默认实现只返回输入值。

Filter Objects
Filters和Handlers可以使用Loggers来完成比级别更复杂的过滤。filter基类只允许特定logger层次以下的事件。例如，用“A.B”初始化的过滤器将允许由记录器“A.B”，“A.B.C”，“A.B.C.D”，“A.B.D”等记录的事件。
但是,不接受“A.BB”，“B.A.B”等的格式。如果用空字符串来初始化，所有的事件都接受。
class logging.Filter(name='')
返回Filter类的实例。如果指明了name，它是一个logger的名字，该logger及其子logger的事件运行通过该过滤器。如果name是空字符串，所有的事件都允许。
filter(record)  特定的记录是否要记下来？0为否，非0为是。如果认为合适，该方法可以修改记录
注意，在处理程序发出事件之前，请参考处理程序附带的过滤器，而记录事件时会查询附加到日志记录器的过滤器（使用debug()，info 等。），然后将事件发送给处理程序。
这意味着子logger产生的事件是不会被logger的filter设定所过滤掉的，除非filter也适用于子logger。
您不需要创建专门的Filter类，或使用其他类与filter方法：函数（或其他可调用）作为过滤器。过滤逻辑将检查过滤器对象是否具有filter属性：如果是，则假设它是Filter及其filter()否则，假定它是一个可调用的，并以该记录作为单个参数进行调用。返回的值应符合filter()返回的值。
尽管filter主要用比级别更复杂的标准来过滤记录，但它能看到它所附于的handler或者logger所处理的所有记录：这可以做许多有用的事情，比如对特定的logger或者handler所处理的记录的计数；或者对正在处理的LogRecord，添加、修改或者移除属性。修改LogRecord需要小心，但是它可以在日志中注入上下文信息

LogRecord Objects








'''
# logging.basicConfig(filename='example.log',level=logging.DEBUG)         #默认等级是WARNING,debug是最低的内置安全等级
# logging.basicConfig(filename='example.log',format='%(levelname)s:%(message)s', level=logging.DEBUG)     #del root
# logging.basicConfig(filename='example.log',format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S',filemode='w', level=logging.DEBUG)     #datefmt参数的格式与time.strftime()是相同的
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.critical("very critical error")
# logging.warning('%s before you %s', 'Look', 'leap!')        #格式化输入
# logging.warning('what {} want to do'.format('you'))        #格式化输入

#配置了一个非常简单的记录器，一个控制台处理器和一个简单的格式化器：
# create logger
# logger = logging.getLogger('my_simple_example')
# logger.setLevel(logging.DEBUG)
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # add formatter to ch
# ch.setFormatter(formatter)
# # add ch to logger
# logger.addHandler(ch)
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

# import logging.config
# logging.config.fileConfig('logging.conf')       #必须要配置此logging.conf文件
# # create logger
# logger = logging.getLogger('simpleExample')
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
'''配置日志的时候也要考虑一些情况。如果使用的应用程序不使用日志，但是库的代码又调用了日志功能, （正如前面部分描述）
WARNING安全事件和更高级的事件将会被打印到sys.stderr。
什么都不做的handler对象存在logging包中：NullHandler (since Python 3.1).如果你想防止在没有配置日志时将信息输出到 sys.stderr ，
你可以把NullHandler的实例加入到最高等级的logging名字空间的logger。
import logging
logging.getLogger('foo').addHandler(logging.NullHandler())
将会起作用。如果一个组织产生许多库，那么特定的记录器的名字可以是“orgname.foo”，而不是只是"foo"。
强烈建议给你的库的记录器NullHandler,如果你暗自添加了处理器，你也许会影响开发者做单元测试
只有在你需要定义自己的级别，且自定义级别相对于预定义值的时候才有用。如果定义具有相同数值的级别，它将覆盖预定义值；预定义的名称将丢失。
级别 数字值 
CRITICAL 50 
ERROR 40 
WARNING 30 
INFO 20 
DEBUG 10 
NOTSET 0 
级别能关联到记录器，由开发者设置或通过载入一个日志配置。当调用一个记录器的日志方法时，记录器比较它的级别和方法所关联的级别。
如果记录器的级别高于方法的级别，那么没有日志消息产生。这是控制日志输出详细程度的基本机制
记录器祖先的处理器也被用来分发消息（除非记录器的propagate标志位设为假，这时就不会将日志传递给记录器祖先的处理器）
如果一个handler决定分发一个事件，emit()方法就会被用来发送信息到它的目的地。多数用户定义的Handler需要重写emit()方法。

Useful Handlers
除了基类Handler，有许多有用的子类：
StreamHandler   实例将消息发送至流（类文件对象）。
FileHandler 实例将消息发送至磁盘文件。
BaseRotatingHandler 是在特定点循环使用日志文件的处理器的基类。它不应该被直接实例化。而应使用RotatingFileHandler或TimedRotatingFileHandler。
RotatingFileHandler 实例将消息发送至磁盘文集，支持最大日志文件限制和循环使用日志文件。
TimedRotatingFileHandler    实例将消息发送至磁盘文件，以特定时间间隔循环使用日志文件。
SocketHandler   实例向TCP / IP套接字发送消息。自3.4以来，还支持Unix域套接字。
DatagramHandler 实例向UDP套接字发送消息。自3.4以来，还支持Unix域套接字。
SMTPHandler 实例将消息发送至指定的邮箱地址。
SysLogHandler   实例将消息发送至Unix syslog服务进程，它可能在远端机器上。
NTEventLogHandler   实例将消息发送至Windows NT/2000/XP事件日志（服务）。
MemoryHandler   实例将消息发送至内存缓冲，在特定条件满足时会被清掉。
HTTPHandler 实例使用GET或POST语义向HTTP服务器发送消息。
WatchedFileHandler  实例观察用以记录日志的文件。如果文件改变，它将关闭然后重新打开文件名。此处理程序仅在类Unix系统上有用； Windows不支持所使用的底层机制。
QueueHandler    实例向队列发送消息，例如在queue或multiprocessing模块中实现的队列。
NullHandler 实例对错误消息什么都不做。库的开发者会使用该处理器，他们希望使用日志，同时也希望在库的使用者没有配置日志的时候避免出现‘No handlers could be found for logger XXX’消息。参见Configuring Logging for a Library。


'''
#-------------------------------------------------------------------------------------------
import heapq
# lis=[5,-2,3,8,7,1,4]
# a=heapq.nlargest(2,lis)
# b=heapq.nsmallest(2,lis)
# print(a)
# print(b)
# from collections import *
# q=deque(maxlen=3)
# q.append(2)
# q.append(6)
# q.append(8)
# print(q)
# q.append(9)
# q.appendleft(9)
# print(q)
# d=defaultdict(list)
# for i in range(1,10,2):
#     d[i-1]=i
# print(d)
# print(d[2])
# from collections import Counter
# lis=[5,-2,3,3,5,3,7]
# print(Counter(lis))         #找出序列元素出现最多的次数,底层是字典
# print(Counter(lis).most_common(2))

#sys module
# from PyQt5.QtWidgets import QWidget
# from PyQt5.QtWidgets import QTabWidget
# import sys
# out=sys.stdout
# sys.stdout=open(r"D:\python\PYQT\test.txt","w")
# help(QTabWidget)
# print("i love you")
# print(QTabWidget)
# sys.stdout.close()
# sys.stdout=out
#-------------------------------------------------------------------------------------------
# tesseract OCR
# from PIL import Image
# import pytesseract
# from paddleocr import PaddleOCR
# # import paddleocr
# # path="C:/Users/Administrator/Desktop/123.PNG"
# path=r"C:/Users/Administrator/Desktop/shengfeng.jpg"
# ocr=PaddleOCR(use_angle_cls=True,lang="ch")
# result=ocr.ocr(path,cls=True)
# # # text=pytesseract.image_to_string(Image.open(path),lang='chi_sim+eng')
# # # text=pytesseract.image_to_string(Image.open(path))
# for line in result[0]:
#     print(line[-1][0])
#-------------------------------------------------------------------------------------------
# PDF文件处理
import fitz

path=r"D:\python\data analysize\sklearn_0.21.3中文手册.pdf"
doc=fitz.open(path)
# print(doc.metadata)
# print(doc.get_toc())        #获取目录内容
page=doc.load_page(26)
print(page.get_text("text"))        #只能提取文字型的PDF文件
# print(page.get_text("words"))        #只能提取文字型的PDF文件
# print(page.get_words())
# print(doc[37].get_text())
# for page in doc.pages(37,40,1):
#     # print(page.get_links())
#     # print(page.get_text("text"))
#     print(page.getTextWords())

import pdfplumber
# pdf=pdfplumber.open(path)
# page=pdf.pages[26]
# text=page.extract_text()
# # text=page.extract_words()
# print(text)








