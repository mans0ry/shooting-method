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

def methodEuler( x0, y0, z0, h, n):
	'''
	Реализация метода Эйлера
	'''
	yn, zn = [], []
	for each in xrange( 1, n ):

		y1 = y0 + f1( x0, y0, z0 ) * h
		z1 = z0 + f2( x0, y0, z0 ) * h

		yn.append( round( y1, 2 ) )
		zn.append( round( z1, 2 ) )

		x0 = x0 + h
		y0 = y1
		z0 = z1
	print 'yn =', yn 
	print 'zn =', zn	
	return yn, zn		

xn = grid( 0, 1, 10 ) 
print '-' * 20, 'Exact number', '-' * 20
unnew, vnnew = setUnVn( xn )
print '-' * 20, 'Eulers method', '-' * 20
un, vn = methodEuler( 0, 0, 2, 0.1, 10 )
