#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import numpy as np

a = 0.
b = 1.
n = 10

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

def grid( a, b, n ):
	"""
	Создание сетки xn, размерность = n 
	"""
	arrayOfX = []
	h = ( a + b ) / n
	print 'h =', h
	lv = b
	arrayOfX.append(b)

	for num in range( n, 0, -1 ):
		lv = lv - h
		arrayOfX.append( round( lv, 3) )

	print 'xn =', arrayOfX
	return arrayOfX, h	

def methodEuler( xlast, ylast, zlast, h, n ):
	'''
	Реализация метода Эйлера

	'''
	yn, zn = [], []
	yn.append( ylast )
	zn.append( zlast )
	for each in xrange( n - 1, 1, -1):

		ycurrent = ylast - v( xlast ) * h
		zcurrent = zlast - dv( xlast ) * h

		yn.append( round( ycurrent, 3 ) )
		zn.append( round( zcurrent, 3 ) )

		xlast = xlast - h
		ylast = ycurrent
		zlast = zcurrent

	print 'yn =', yn 
	print 'zn =', zn	
	return yn, zn			

xn, h = grid(a, b, n)
methodEuler(b, u(b), round(v(b), 3), h, n)	