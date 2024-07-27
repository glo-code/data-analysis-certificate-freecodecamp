import numpy as np


def calculate(list):
   array=np.array(list)
   array_corretto=np.resize(array,(3,3))
   array_appiattito=array_corretto.flatten()
   lista_nomi=['mean','variance','standard deviation','max','min','sum']
   lista_funzioni=[np.mean,np.var,np.std]
   #lista_dizionari=[]

   #for nomi,function in zip(lista_nomi,lista_funzioni):
   calculations={lista_nomi[0]:         
                 [lista_funzioni[0](array_corretto,axis=0,dtype=np.float64).tolist(),
                 lista_funzioni[0](array_corretto,axis=1,dtype=np.float64).tolist(),
                 lista_funzioni[0](array_appiattito,dtype=np.float64).tolist()],
lista_nomi[1]:         
 [lista_funzioni[1](array_corretto,axis=0,dtype=np.float64).tolist(),
 lista_funzioni[1](array_corretto,axis=1,dtype=np.float64).tolist(),
 lista_funzioni[1](array_appiattito,dtype=np.float64).tolist()],
lista_nomi[2]:         
 [lista_funzioni[2](array_corretto,axis=0,dtype=np.float64).tolist(),
 lista_funzioni[2](array_corretto,axis=1,dtype=np.float64).tolist(),
 lista_funzioni[2](array_appiattito,dtype=np.float64).tolist()],
lista_nomi[3]:[np.max(array_corretto,axis=0).tolist(),np.max(array_corretto,axis=1).tolist(),np.max(array_appiattito).tolist()],
lista_nomi[4]:[np.min(array_corretto,axis=0).tolist(),np.min(array_corretto,axis=1).tolist(),np.min(array_appiattito).tolist()],
lista_nomi[5]:[np.sum(array_corretto,axis=0).tolist(),
                          np.sum(array_corretto,axis=1).tolist(),
                          np.sum(array_appiattito).tolist()]
            }

   if len(list)!=9:
      raise ValueError ('List must contain nine numbers.')


   return calculations

#calculate([2,6,2,8,4,0,1,5,7])
