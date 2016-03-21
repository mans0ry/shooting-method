#!/usr/bin/env python 
# -*- coding: utf-8 -*-

constn = 100
a, b = 0, 1
consth = round( a + b , 2) / constn

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

def derivative( functinon ):
	"""
	Функция для вычисления производной
	"""
	def df( x, h = 0.1e-5 ):
		return ( functinon( x + h / 2 ) - functinon( x - h / 2) ) / h
	return df

def grid( a, b, n ):
	"""
	Создание сетки xn, размерность = n 
	"""
	arrayOfX = []
	h = round( a + b , 1) / n
	lv = a

	for num in range( 1, n ):
		lv = lv + h
		arrayOfX.append( round( lv, 1) )

	return arrayOfX	

def setUnVn( xn ):
	'''
	Создание un, vn
	'''
	un, vn = [], []

	for it in xn:
		un.append( round( u( it ), 2 ) )
		vn.append( round( v( it ), 2 ) )
	un.reverse()
	vn.reverse()	
	print 'yn =', un
	print 'zn =', vn
	return un, vn

def f1( x, u, v ):
	'''
	du/dx = f1( x, u, v )
	'''
	return v 

def f2( x, u, vv ):
	'''
	dv/dx = f2( x, u, v )
	'''
	dv = derivative( v ) 
	return dv( x ) 

def methodEuler( xlast, ylast, zlast, h, n):
	'''
	Реализация метода Эйлера

	'''
	yn, zn = [], []
	for each in xrange( n, 1, -1):

		ycurrent = ylast - f1( xlast, ylast, zlast ) * h
		zcurrent = zlast - f2( xlast, ylast, zlast ) * h

		yn.append( round( ycurrent, 2 ) )
		zn.append( round( zcurrent, 2 ) )

		xlast = xlast - h
		ylast = ycurrent
		zlast = zcurrent

	print 'yn =', yn 
	print 'zn =', zn	
	return yn, zn		

xn = grid( 0, 1, constn ) 
print '-' * 20, 'Exact number', '-' * 20
unnew, vnnew = setUnVn( xn )
print '-' * 20, 'Eulers method', '-' * 20
un, vn = methodEuler( 1, 3, 5, consth, constn )