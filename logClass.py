# -*- coding: utf-8 -*-
import time
import re
import pdb
import inspect

class logClass():
	def __init__(self):
		self.n=1;	
		self.initDepth = len(inspect.stack())

	def logit(self,path):
		if self.n==1:
			f = open(path,'a')
			f.write('============================='+time.strftime('%Y-%m-%d %H:%M:%S')+'====================================\n')
			f.close()
			self.n=0

		def maxLength(inStr,maxLength=50):
			N = len(inStr)
			if N>maxLength:
				return inStr[:maxLength-6] + '......'
			else:
				return inStr

		def toPrint(u):
			us = re.findall(r'\\\w(\w{4})',unicode(u))
			uus = [unichr(int('0x'+each,16)) for each in us] 
			uuus = u 
			for i in uus:
				uuus = re.sub(r'\\(\w{5})',i,uuus,count=1)
			return uuus

		def _logit(func):
			def __logit(*args, **kwargs):
				depth = len(inspect.stack())-self.initDepth
				p0 = time.strftime('%H:%M:%S')
				p1 = func.func_name
				p2 = '('
				for i in args:
					if type(i)==str:
						p2 = p2 + '"' + maxLength(i.decode('utf8')) + '"' + ', '
					elif type(i)==unicode:
						p2 = p2 + '"' + maxLength(i) + '"' + ', '
					else:
						p2 = p2 + maxLength(unicode(i)) + ', '
				try:
					p2 = re.findall(r'<.*>,(.*)',p2)[0]
					p2 = '('+p2
				except:
					pass
				p3 = ' '
				for i in kwargs:
					if type(kwargs[i])==str:
						p3 = p3 + i + ' = ' + '"' + maxLength(kwargs[i].decode('utf8')) + '"' + ', '
					elif type(kwargs[i])==unicode:
						p3 = p3 + i + ' = ' + '"' + maxLength(kwargs[i]) + '"' + ', '
					else:
						p3 = p3 + i + ' = ' + maxLength(unicode(kwargs[i])) + ', '

				pn = depth * "  " + p0 + '  ' + p1 + p2 + p3[0:-2] + ')\n' 
				pn = toPrint(pn)
				ret = func(*args, **kwargs)
				#print pn
				f = open(path,'a')
				f.write(pn.encode('utf8'))
				f.close()
				return ret 
			return __logit
		return _logit


if __name__=='mian':
	largeList=[1,2,3,4,3,22,2,3,4,6,54,5,6,43,3,432,56,34,3,45,43,534,6,43,5432,5,324,23,5,435,43,5,32,4532,4,23,432,4,2]

	logit = logClass()
	logFile='test.log'
	@logit.logit(logFile)
	def test1(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=[1,2,'123',[3,2,1],{1:1}],inDict2={1:[1,2,3,[2,3]]}):
		test2(2222,u'测试2',['test1',1],{'test1':['test1']},inList2=[1,2,'123',[3,2,1],{1:1}])

	@logit.logit(logFile)
	def test2(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=[1,2,'123',[3,2,1],{1:1}],inDict2={1:[1,2,3,[2,3]]}):
		pass

	@logit.logit(logFile)
	def test3(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=largeList ,inDict2={1:[1,2,3,[2,3]]}):
		test1(1111,'test1',largeList,{'test1':['test1']},inDict2={1:[1,2,3,[2,3]]})

	def test4(inNum,inStr,inList,inDict,inNum2=1,inStr2="123",inList2=[1,2,'123',[3,2,1],{1:1}],inDict2={1:[1,2,3,[2,3]]}):
		test1(1111,'test1',['test1',1],{'test1':['test1']},inDict2={1:[1,2,3,[2,3]]},inList2=largeList)

	test1(1111,'test1',['test1',1],{'test1':['test1']},inDict2={1:[1,2,3,[2,3]]})
	test3(3333,u'测试3',[u'测试3',1],{'test1':['test1']},inStr2=u"呵呵")
	test4(3333,u'测试3',[u'测试3',1],{'test1':['test1']},inStr2=u"呵呵")

