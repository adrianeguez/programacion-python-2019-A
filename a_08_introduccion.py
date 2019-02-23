#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:12:33 2019

@author: usrdel
"""

import numpy as np
import pandas as pd

## Series [1,2,3,4,5,6]

## DataFrames ['Nombre','Apellido']
##            ['Adrian','Eguez']
##            ['Vicente','Sarzosa']

serie_numeros = pd.Series([1,2,3,4])

serie_varios = pd.Series(
        [True,
         2.2,
         "Adrian",
         None])

print(serie_numeros[0])

serie_con_indices = pd.Series([
        "Adrian",
        "Vicente",
        "Wendy",
        "Carolina"
        ], index=["A","B","C","D"])

print(serie_con_indices["B"])

print(type(serie_con_indices))

valores_por_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }

serie_ciudades = pd.Series(
        valores_por_ciudad)

print(serie_ciudades["Ibarra"])
ciudades_menores = serie_ciudades < 10000
        
print(
      serie_ciudades[ciudades_menores])


print(serie_ciudades[serie_ciudades < 10000])

serie_ciudades["Loja"] = 3500

serie_ciudades[
        serie_ciudades<8000]=4000
        
# 1 in [1,2,3] True

print("Lima" in serie_ciudades)

serie_ciudades / 3

np.square(serie_ciudades)

ciudades_uno = pd.Series({
           "Quito":1500,
           "Loja":4000
        })

ciudades_dos = pd.Series({
           "Montana":300,
           "Guayaquil":10000,
           "Quito":1500
        })

 print(ciudades_uno+ ciudades_dos)


randomico = np.random.rand(3)

serie_rand_tres = pd.Series(randomico)

ciudades_uno.index

# DataFrames

randomico_2_3 = np.random.rand(3,2)

df = pd.DataFrame(randomico_2_3)

df.columns = ["Uno","Dos"]

df["Dos"][1]

df_ciudades = pd.DataFrame([
        ciudades_uno,
        ciudades_dos
        ])


































