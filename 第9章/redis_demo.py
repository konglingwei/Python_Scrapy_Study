#引入redis模块StrictRedis和ConnectionPool方法
from redis import StrictRedis,ConnectionPool
#引入时间模块
import time
#连接redis数据库
pool = ConnectionPool(host='127.0.0.1', port=6379,db=0, password='klw120110119')
key = StrictRedis(connection_pool=pool)
#设置key名为name的值为Linda
key.set('name', 'Linda')
#打印key名为name的值
print(key.get('name'))
# 清空Redis
key.flushall()
print(key.get('name'))
# 设置key名为password的值为1111，过期时间为2s
key.setex('password', value='1111', time=2)
print(key.get('password'))
# 批量设置新值
# key.mset(A1 = 'v1', A2 = 'v2', A3 = 'v3')
# 批量获取新值
print(key.mget('A1', 'A2', 'A3', 'A4'))
# 设置新值并获取原来的值
print(key.getset('password', 'lindaying'))
# 获取子序列 0 <= x <= 1
print(key.getrange('password', 0, 4))
# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加），返回值的长度
key.setrange('password',0,'linda')
j=0
while j < 5:
    print(key.get('password'))
    time.sleep(1)
    j+=1
source = 'qing'
key.set('m1',source)
key.setbit('m1',7,1)
print(key.get('m1'))
# 获取n1对应的值的二进制表示中的某位的值 （0或1）
print(key.getbit('m1', 7))
key.set('m2','小百货')
# 返回对应的字节长度（一个汉字3个字节）
len = key.strlen('m2')
print(len)
key.set('num',1)
key.incr('num', amount=10)
key.decr('num',amount=1)
# 自增num对应的值，当name不存在时，则创建name＝amount，否则，则自增
print(key.get('num'))
# 在redis num对应的值后面追加内容
key.append('num',112)
print(key.get('num'))
