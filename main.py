#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def u( x ):
	"""
	Функция, на которой проводится исследования
	"""
	return x ** 2

def v( x ):
	"""
	Первая производная функции
	"""
	du = derivative(u)
	return du(x)

def derivative( func ):
	"""
	Функция для вычисления производной
	"""
	def df( x, h = 0.1e-5 ):
		return ( func( x + h / 2 ) - func( x - h / 2) ) / h
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

def methodEuler( xn, a, b ):
	B = v ( b )
	
xn = grid( 0, 1, 10 ) 
methodEuler( xn, 0, 1 )