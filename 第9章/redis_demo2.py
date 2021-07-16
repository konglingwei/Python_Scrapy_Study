#引入redis模块StrictRedis和ConnectionPool方法
from redis import StrictRedis,ConnectionPool
#连接redis数据库
pool = ConnectionPool(host='127.0.0.1', port=6379,db=0, password='')
key = StrictRedis(connection_pool=pool)
# 清空Redis
key.flushall()
# 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
key.lpush('oo', 111)
key.lpushx('oo', 000)
# name对应的list元素的个数
print(key.llen('oo'))
# 在111之前插入值999
key.linsert('oo', 'before', 111, 999)
# 对name对应的list中的某一个索引位置重新赋值
key.lset('oo', 1, 888)
# 打印在name对应的列表分片获取的数据
print(key.lrange('oo', 0, -1))
# 打印在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
print(key.lpop('oo'))
# 打印在name对应的列表中根据索引获取列表元素
print(key.lindex('oo', 0))
# index为0
key.lpush('list', 111)
key.rpush('list', 222)
key.rpush('list', 333)
key.rpush('list', 444)
# index为4
key.rpush('list', 555)
# 在name对应的列表中移除没有在[start-end]索引之间的值
key.ltrim('list', 1, 3)
print(key.lrange('list', 0, -1))
# 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边;src要取数据的列表的name, dst要添加数据的列表的name
key.rpoplpush('list', 'list')
print(key.lrange('list', 0, -1))
# timeout，当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞
key.brpoplpush('list', 'list', timeout=3)
print(key.lrange('list', 0, -1))
# 从列表头部取出第一个元素，返回该元素值并从列表删除（l代表left，左边）
print(key.blpop('list', 3))
print(key.lrange('list', 0, -1))
print('自定义增量：')
key.flushall()
# index为0
key.lpush('list', 111)
key.rpush('list', 222)
key.rpush('list', 333)
key.rpush('list', 444)
# index为4
key.rpush('list', 555)
def list_iter(name):
    list_count = key.llen(name)
    for index in range(list_count):
        yield key.lindex(name, index)
# for item in list_iter('list'):
#     print(item)

print("______________________________________________________________________________")
#
print(key.llen('slave:items'))
for item2 in list_iter('slave:items'):
    print(item2)