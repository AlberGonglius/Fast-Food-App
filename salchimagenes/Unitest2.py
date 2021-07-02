# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:21:12 2021

@author: Jader Peñaloza
"""

import unittest


precios= {"Hamburguesa Sencilla":3000,"Hamburguesa Especial":7000,"Papa Frita":3000,"Yuca Frita":3000,
                       "Queso":3000,"Salchipapa Sencilla":3000,"Salchipapa Especial":6000,"Salvajada":20000,"Perro Sencillo":3000,
                       "Perro Especial":6000,"Coca Cola":4000,"Pepsi":3000,"Aguila":4500}
        
productos={"Hamburguesa Sencilla":0,"Hamburguesa Especial":0,"Papa Frita":0,"Yuca Frita":0,
                       "Queso":0,"Salchipapa Sencilla":0,"Salchipapa Especial":0,"Salvajada":0,"Perro Sencillo":0,
                       "Perro Especial":0,"Coca Cola":0,"Pepsi":0,"Aguila":0}

def sumar_elemento(nombre_producto:str, productos:dict)->int:
    
    productos[nombre_producto]+=1
        
    return productos[nombre_producto]
    
def restar_elemento(nombre_producto:str, productos:dict)->int:
    
    if productos[nombre_producto] > 0:
        
        productos[nombre_producto]-=1

    return productos[nombre_producto]

def calcular_valor_total(precios:dict,productos:dict)->float:
    
    return sum([productos[producto]*precios[producto] 
                for producto in productos])


class Pruebas(unittest.TestCase):
    def test2(self):
        
        suma=sumar_elemento("Papa Frita",productos)
        
        self.assertEqual(suma, 1)
        
        resta=restar_elemento("Papa Frita",productos)
        
        self.assertEqual(resta, 0)
        
        total=calcular_valor_total(precios, productos)
        
        self.assertEqual(total,0)
        
        
        
if __name__=="__main__":
    unittest.main()