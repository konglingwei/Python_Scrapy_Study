#引入redis模块StrictRedis和ConnectionPool方法
from redis import StrictRedis,ConnectionPool
#连接redis数据库
pool = ConnectionPool(host='127.0.0.1', port=6379,db=0, password='')
key = StrictRedis(connection_pool=pool)
# 清空Redis
key.flushall()
# hset(name, key, value),name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
key.hset('m1', 'k1', 'v1')
print(key.hget('m1', 'k1'))
# hmset(name, mapping),在name对应的hash中批量设置键值对
key.hmset('m2', {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'})
print(key.hmget('m2', 'k2'))
# 获取name对应hash的所有键值
print(key.hgetall('m2'))
# 获取name对应的hash中键值对的个数
print(key.hlen('m2'))
# 获取name对应的hash中所有的key的值
print(key.hkeys('m2'))
# 获取name对应的hash中所有的value的值
print(key.hvals('m2'))
# 检查name对应的hash是否存在当前传入的key
print(key.hexists('m2', 'k4'))
# 将name对应的hash中指定key的键值对删除
key.hdel('m2', 'k3')
key.hset('m3', 'k1', 1)
# hincrby(name, key, amount=1),自增name对应的hash中的指定key的value的值，不存在则创建key=amount
key.hincrby('m3', 'k1', amount=1)
print(key.hgetall('m3'))
