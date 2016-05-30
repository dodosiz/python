"""coupon_creator now includes punctuation letters in order to increase the number of combinations
the coupon_list takes a parameter for the number of digits each coupon has, I set it to 20"""

import string
import random

def coupon_creator(digit):	
	coupon = ''
	for word in range(digit):
		coupon += random.choice(string.punctuation + string.ascii_lowercase + string.digits)
	return coupon

def coupon_list(number_of_coupons, digit_for_each):
	data = ''
	for count in range(number_of_coupons):
		data += coupon_creator(digit_for_each)+'\n'
	
	return data

coupons = open('coupons.txt','w')
coupons.write(coupon_list(200,20))
coupons.close()
