products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])
print(products)
for p in products:
	print('商品名稱:', p[0], ',價格為:', p[1])


