#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def u( x ):
	"""
	Функция, на которой проводится исследования
	"""
	return x ** 3 + 2 * x

def v( x ):
	"""
	Первая производная функции
	"""
	du = derivative( u )
	return du( x )

def dv( x ):
	dv = derivative(v)
	return dv(x)

def derivative( functinon ):
	"""
	Функция для вычисления производной
	"""
	def df( x, h = 0.1e-3 ):
		return ( functinon( x + h / 2 ) - functinon( x - h / 2) ) / h
	return df	

def grid( a, b, n, h ):
	"""
	Создание сетки xn, размерность = n 
	"""
	arrayOfX = []
	lv = b
	arrayOfX.append(b)

	for num in range( n, 0, -1 ):
		lv = lv - h
		arrayOfX.append( round( lv, 3) )

	print 'xn =', arrayOfX
	print '-' * 40
	return arrayOfX	

def methodEuler( xlast, ylast, zlast, h, n ):
	'''
	Реализация метода Эйлера

	'''
	yn, zn = [], []
	yn.append( ylast )
	zn.append( zlast )
	for each in xrange( n, 0, -1):

		ycurrent = ylast - zlast * h
		zcurrent = zlast - dv( xlast ) * h

		yn.append( round( ycurrent, 3 ) )
		zn.append( round( zcurrent, 3 ) )

		xlast = xlast - h
		ylast = ycurrent
		zlast = zcurrent

	print 'yn =', yn 
	print 'zn =', zn

	return yn, zn	

def readValues(name):
	dic = []
	
	file = open(name, 'r')
	for line in file.readlines():
		dic.append(line.split(' '))	

	a, b = float(dic[0][0]), float(dic[0][1]) 
	A, B = float(dic[2][0]), float(dic[2][1])
	alpha0, alpha1 = float(dic[3][0]), float(dic[3][1])
	eps = float(dic[4][0])
	
	n = int(dic[1][0])
	h = ( b + a ) / n

	return A, B, a, b, alpha0, alpha1, n, h, eps

def Fi(alp):
	u, z = methodEuler(b, alp, B, h, n)
	# print u[0]
	return u[n] - A

def main():
	global A, B, a, b, n, h, alpha0, alpha1
	A, B, a, b, alpha0, alpha1, n, h, EPS = readValues('input.txt')
	xn = grid(a, b, n, h)
	
	Fi0 = Fi( alpha0 )
	Fi1 = Fi( alpha1 )
	k = 0

	if abs( Fi0 ) > EPS:
	 	if  abs( Fi1 ) > EPS:
	 		while Fi0 * Fi1 < 0 and k < 1000:
 				if alpha0 >= alpha1:
					print 'Error get alpha'
					break
 				k += 1
 				alpha2 = (alpha0 + alpha1)/2.
	 			Fi2 = Fi(alpha2)
	 			if abs(Fi2) > EPS:
	 				if Fi0 * Fi2 < 0:
	 					alpha1 = alpha2 
	 					Fi1 = Fi(alpha2)
	 				else:
	 					alpha0 = alpha2 
	 					Fi0 = Fi(alpha2)	
	 			else:
	 				return Fi2	
	 	else:
	 		return Fi1	
	else:
		return Fi0

	
main()