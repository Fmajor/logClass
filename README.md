logClass
========

to log function calls
examples:
# test data list
largeList=[1,2,3,4,3,22,2,3,4,6,54,5,6,43,3,432,56,34,3,45,43,534,6,43,5432,5,324,23,5,435,43,5,32,4532,4,23,432,4,2]

# first, we should have a logClass instance
logit = logClass()
# log file we want to use
logFile='test.log'

# we want to log the function test1, so add a decorator
@logit.logit(logFile)
def test1(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=[1,2,'123',[3,2,1],{1:1}],inDict2={1:[1,2,3,[2,3]]}):
	test2(2222,u'测试2',['test1',1],{'test1':['test1']},inList2=[1,2,'123',[3,2,1],{1:1}])

# we also want to log the function test2
@logit.logit(logFile)
	def test2(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=[1,2,'123',[3,2,1],{1:1}],inDict2={1:[1,2,3,[2,3]]}):

# we also want to log the function test3
@logit.logit(logFile)
def test3(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=largeList ,inDict2={1:[1,2,3,[2,3]]}):
	test1(1111,'test1',largeList,{'test1':['test1']},inDict2={1:[1,2,3,[2,3]]})
		
# we do not want to log the funciton test4
def test4(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=[1,2,'123',[3,2,1],{1:1}],inDict2={1:[1,2,3,[2,3]]}):
	test1(1111,'test1',['test1',1],{'test1':['test1']},inDict2={1:[1,2,3,[2,3]]},inList2=largeList)

# function calls
test1(1111,'test1',['test1',1],{'test1':['test1']},inDict2={1:[1,2,3,[2,3]]})
test3(3333,u'测试3',[u'测试3',1],{'test1':['test1']},inStr2=u"呵呵")
test4(3333,u'测试3',[u'测试3',1],{'test1':['test1']},inStr2=u"呵呵")

==========================================================================================

the functions are called in turn of

test1           #logit
     test2      #logit
test3           #logit
     test1      #logit
	      test2 #logit
test4           #nolog
     test1      #logit
	      test2 #logit

the indent stand for the call relations

log file is like
=============================2014-06-20 13:15:10====================================
    13:15:10  test2(2222, "测试2", ['test1', 1], {'test1': ['test1']},  inList2 = [1, 2, '123', [3, 2, 1], {1: 1}])
13:15:10  test1(1111, "test1", ['test1', 1], {'test1': ['test1']},  inDict2 = {1: [1, 2, 3, [2, 3]]})
        13:15:11  test2(2222, "测试2", ['test1', 1], {'test1': ['test1']},  inList2 = [1, 2, '123', [3, 2, 1], {1: 1}])
    13:15:11  test1(1111, "test1", [1, 2, 3, 4, 3, 22, 2, 3, 4, 6, 54, 5, 6, 43......, {'test1': ['test1']},  inDict2 = {1: [1, 2, 3, [2, 3]]})
13:15:10  test3(3333, "测试3", [u'测试3', 1], {'test1': ['test1']},  inStr2 = "呵呵")
      13:15:11  test2(2222, "测试2", ['test1', 1], {'test1': ['test1']},  inList2 = [1, 2, '123', [3, 2, 1], {1: 1}])
  13:15:11  test1(1111, "test1", ['test1', 1], {'test1': ['test1']},  inDict2 = {1: [1, 2, 3, [2, 3]]}, inList2 = [1, 2, 3, 4, 3, 22, 2, 3, 4, 6, 54, 5, 6, 43......)

the indent stand for the depth of the run stack
logs are in the reverse turn of the run stack
test4 is missing because we do log it
but the run stack indent is still there

