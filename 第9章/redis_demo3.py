#引入redis模块StrictRedis和ConnectionPool方法
from redis import StrictRedis,ConnectionPool
#连接redis数据库
pool = ConnectionPool(host='127.0.0.1', port=6379,db=0, password='')
key = StrictRedis(connection_pool=pool)
# 清空Redis
key.flushall()
# name对应的集合k1中添加元素
key.sadd('k1', 'v1', 'v2', 'v2', 'v3')
# name对应的集合中k2添加元素
key.sadd('k2', 'v2', 'v4')
# 打印获取name对应的集合中元素个数
print(key.scard('k1'))
#打印在第一个name对应的集合中且不在其他name对应的集合的元素集合
print(key.sdiff('k1', 'k2'))
# 获取第一个name对应的集合中且不在其他name对应的集合，再将其新加入到dest对应的集合中
key.sdiffstore('k3', 'k1', 'k2')
# 打印获取k3对应的集合的所有成员
print(key.smembers('k3'))
# 打印获取k1, k2对应集合的交集
print(key.sinter('k1', 'k2'))
key.sinterstore('k4', 'k1', 'k2')
# 获取k1, k2对应集合的交集，并将其存放到集合是k4中
print(key.smembers('k4'))
# 打印获取k1, k2对应集合的并集
print(key.sunion('k1', 'k2'))
# 获取k1, k2对应集合的交集，并将其存放到集合是k5中
key.sunionstore('k5', 'k1', 'k2')
print(key.smembers('k5'))
# 打印检查value是否是name对应的集合的成员
print(key.sismember('k4', 'v4'))
# 将集合k2中成员v4移至集合k1中
key.smove('k2', 'k1', 'v4')
print(key.smembers('k1'))
# 在name对应的集合中删除某些值
key.srem('k1', 'v1')
# 打印从集合的右侧（尾部）移除一个成员，并将其返回 注意：由于集合是无序的，所以结果是随机的。
print(key.spop('k1'))
# 从name对应的集合中随机获取 numbers 个元素
print(key.srandmember('k1'))
