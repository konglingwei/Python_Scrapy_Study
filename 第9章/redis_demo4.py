#引入redis模块StrictRedis和ConnectionPool方法
from redis import StrictRedis,ConnectionPool
#连接redis数据库
pool = ConnectionPool(host='127.0.0.1', port=6379,db=0, password='')
key = StrictRedis(connection_pool=pool)
# 清空Redis
key.flushall()
# 在name对应的有序集合中添加元素
key.zadd('k1', '111', 1, '222', 2, '333', 3, '444', 4, '555', 5, '666', 6,'444',7)
# 获取name对应的有序集合元素的数量
print(key.zcard('k1'))
# 获取name对应的有序集合中分数 在 [min,max] 之间的个数
print(key.zcount('k1', 200, 400))
# 自增name对应的有序集合的 name 对应的分数
key.zincrby('k1', '111', amount=5)
# 值111被排序到最后;此处表示按元素的值升序排列
print(key.zrange('k1', 0, -1, desc=False, withscores=True))
# 获取某个值在 name对应的有序集合中的排行（从 0 开始）
print(key.zrank('k1', 2))
# 删除name对应的有序集合中值是values的成员
key.zrem('k1', '444')
#按元素的值降序排列
print(key.zrevrange('k1', 0, -1, withscores=True))
# 根据排行范围删除
key.zremrangebyrank('k1', 0, 1)
print(key.zrange('k1', 0, -1, desc=False, withscores=True))
# 根据分数范围删除
key.zremrangebyscore('k1', 300, 500)
print(key.zrange('k1', 0, -1, desc=False, withscores=True))
#获取name对应有序集合中 value 对应的分数
print(key.zscore('k1', 200))
