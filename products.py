#檢查檔案存在
import os
products = []
if os.path.isfile('products.csv'):
	print('找到檔案')

	#讀取檔案
	with open('products.csv', 'r') as f:
 		for line in f:
 			if '商品名稱,價格' in line:
 				continue
 			name, price = line.strip().split(',')
 			products.append([name, price])
	print(products)
else:
	print('找不到檔案...')

#輸入商品及價格
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])
#print(products)
for p in products:
	print('商品名稱:', p[0], ',價格:', p[1])

#寫入檔案
with open('products.csv', 'w') as f:
	f.write('商品名稱,價格'+'\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


