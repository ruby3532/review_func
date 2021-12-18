# 介紹 function

def wash(dry):
	print('加水')
	print('旋轉')
	print('加洗衣精')
	if dry:
		print('烘衣')

wash(True)
wash(False)

def say_hi():
	print('hi')

say_hi()

def add(x, y):
	print(x + y)

add(5, 6)
add(123, 2323)

# 有預設值的情況下
def count(a=1, b=0):
	print(a + b)

count() # 即使不給參數仍可以執行功能，因為有預設值
count(5) # 參數會自動按照順序投
count(b=5) # 即使有預設參數，仍可以指定投的東西




