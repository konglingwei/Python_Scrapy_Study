import csv

#找出一个csv文件中 重复的数据行
with open("questions.csv","r",encoding='utf-8') as csvfile:#打开csv文件
   rd = csv.reader(csvfile) #读取csv文件数据
   l = [] #定义一个空列表接收csv数据
   s = [] #再定义一个空列表，接收重复的数据
   for i in rd: #遍历csv文件数据添加到l列表里
      l.append(i)
   for i in range(0,len(l)):#遍历l列表下标
      if l[i] in l[i + 1:]:#通过下标判断，当前的元素是否有重复
         s.append(i)#如果有重复的元素就添加到s列表里
   print('总共{0}条数据，重复的数据有\n{1}'.format(len(l),s))