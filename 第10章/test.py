# a = open('num.txt')
# lines = a.readlines()
# lists = []#直接用一个数组存起来就好了
# for line in lines:
#         lists.append(int(line.replace('\n','')))
#
# lists.sort()
#
# result = []
# for num in lists:
#     if num not in result:
#         result.append(num)
# print(result)
# print(len(result))
# for i in range(1,161):
#     if i not in result:
#         print(i)


# print("______________________________________________________________________________")
# #引入redis模块StrictRedis和ConnectionPool方法
# from redis import StrictRedis,ConnectionPool
# #连接redis数据库
# pool = ConnectionPool(host='127.0.0.1', port=6379,db=0, password='')
# key = StrictRedis(connection_pool=pool)
#
# # for i in range(1,200):
# #     key.lpush('questionspider:start_urls', i)
#
#
# def list_iter(name):
#     list_count = key.llen(name)
#     for index in range(list_count):
#         yield key.lindex(name, index)
# #
#
# print(key.llen('questionspider:start_urls'))
#
# filename = 'start_urls.txt'
# with open(filename, 'a',encoding='utf-8') as file_object:
#     for item2 in list_iter('questionspider:start_urls'):
#         print(item2)
#         item2 = item2.decode('utf-8')
#         file_object.write(item2+'\n')
