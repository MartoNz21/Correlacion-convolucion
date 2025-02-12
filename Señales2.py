# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:52:55 2025

@author: marti
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from scipy.signal import welch

h = np.array([5,6,0,0,7,6,7]) #Señal de entrada [Código de estudiante]
x = np.array([1,0,2,3,1,6,2,7,6,2]) #Señal de salida [C.C]


y = np.convolve(h, x) #Se calcula la convolución.


#Índices de señales.

nh = np.arange(len(h))
nx = np.arange(len(x))
ny = np.arange(len(y))

plt.figure(figsize=(10, 4),facecolor='Beige')

plt.plot(nh, h, color='Red')
plt.title('Señal h[n] ',color='Black')
plt.xlabel('n' , color='Black')
plt.ylabel('Amplitud', color='Black')
plt.grid ()
plt.show() 

plt.figure(figsize=(10, 4),facecolor='Beige')

plt.plot(nx, x, color='Red')
plt.title('Señal x[n] ',color='Black')
plt.xlabel('n',color='Black')
plt.ylabel('Amplitud',color='Black')
plt.grid ()
plt.show()  

plt.figure(figsize=(10, 4),facecolor='Beige')

plt.plot(ny, y, color='Red')
plt.title('Señal y[n]=h[n] * x[n]',color='Black')
plt.xlabel('n',color='Black')
plt.ylabel('Amplitud',color='Black')
plt.grid ()
plt.show()


 #Cargamos los datos de phyisionet al código.
x=loadmat('emg_myopathym.mat')

emg =(x['val']-0)/10000
emg =np.transpose(emg)
emg = emg.squeeze()
fs =4000
tm =1/fs


print("Estadísticos descriptivos:")
      

# Calcular la media aritmética manualmente
n = emg.size

if n > 1:
    suma = 0.0
    for x in emg:
        suma += x
    media = suma / n

# Calcular la desviación estándar manualmente
    suma1 = 0.0
    for x in emg:
        suma1 += (x - media) ** 2
    desvi = (suma1 / (n - 1)) ** 0.5  
else:
    media = float('error al calcular')
    desvi = float('error al calcular')

# Estadísticos calculados por medio de funciones
mediac = np.mean(emg)
desviacionc = np.std(emg, ddof=1) 

## coeficiente de variación calculado

coefi= desvi/media 

## coeficiente de variación con los valores de las funciones

coefi1= desviacionc/mediac

print(f"\nMedia calculada: {media}\n")
print(f"Desviación estándar calculada: {desvi}\n")
print(f"Coeficiente de variación calculado: {coefi}\n")
print(f"Media por funciones: {mediac}\n")
print(f"Desviación estándar por funciones: {desviacionc}\n")
print(f"Coeficiente de variación con valores de las funciones: {coefi1}\n")
#Correlacion señales sinusoidales

def signal_correlation():
    n = np.arange(0, 9)
    Ts = 1.25e-3
    freq = 100
    O = 2 * np.pi * freq * Ts
    
    x1 = np.cos(O * n)
    x2 = np.sin(O * n)
    
    correlation = np.correlate(x1, x2, mode='full')
    lags = np.arange(-len(x1) + 1, len(x1))
    
    # Plot signals
    plt.figure(figsize=(12, 5))
    plt.subplot(2, 1, 1)
    plt.stem(n, x1, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.stem(n, x2, linefmt='g-', markerfmt='go', basefmt='r-')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.title('Señales x1[n] y x2[n]')
    plt.legend(['x1[n]', 'x2[n]'])
    plt.grid()
    
    # Plot correlation
    plt.subplot(2, 1, 2)
    plt.stem(lags, correlation, linefmt='m-', markerfmt='mo', basefmt='r-')
    plt.xlabel('Retardo m')
    plt.ylabel('Correlación')
    plt.title('Correlación cruzada entre x1[n] y x2[n]')
    plt.grid()
    
    plt.tight_layout()
    plt.show()

signal_correlation()


#Graficamos la señal con respecto al tiempo:
tiempo=np.linspace(0,desviacionc,len(emg))
plt.figure(figsize=(10,4),facecolor='Beige')
plt.plot(tiempo, emg, label="Señal en el tiempo",color='Red')
plt.xlabel("Tiempo (s)", color='Black')
plt.ylabel("Amplitud" , color='Black')
plt.title("Señal en el Dominio del Tiempo", color='Black')
plt.legend()
plt.grid()
plt.show()

#Se crea la transformada de Fourier
N = len(emg)
frecuencias = np.fft.fftfreq(N, tm)
magnitudf = np.abs(np.fft.fft(emg))

#Se grafica la transformada de Fourier con respecto a la señal EMG
plt.figure(figsize=(10, 4),facecolor='Beige')
plt.plot(frecuencias, magnitudf, label="Magnitud de la Transformada de fourier",color='Red')
plt.xlabel("Frecuencia [Hz]", color='Black')
plt.ylabel("Magnitud" , color='Black')
plt.title("Transformada de Fourier de la Señal", color='Black')
plt.grid()
plt.legend()
plt.show()

#Calculos transformada
valpos=frecuencias>=0
frecuencias=frecuencias[valpos]
magnitudf=magnitudf[valpos]

frecmedia=np.sum(frecuencias*magnitudf)/np.sum(magnitudf)
frecmediana=frecuencias[np.searchsorted(np.cumsum(magnitudf), np.sum(magnitudf)/2)]
desviacionf=np.sqrt(np.sum(magnitudf* (frecuencias-frecmedia)**2)/np.sum(magnitudf))

print(f"\nFrecuencia media {frecmedia}\n")
print(f"Frecuencia mediana {frecmediana}\n")
print(f"Desviación(Fourier){desviacionf}\n")
#Se calcula la densidad espectral de potencia [PSD]
frecuen_psd, psd= welch(emg, fs, nperseg=(4000))
plt.figure(figsize=(10, 4),facecolor='Beige')
plt.semilogy(frecuen_psd, psd,label="Densidad Espectral",color='Red' )
plt.xlabel("Frecuencia [Hz]", color='Black')
plt.ylabel("Densidad de potencia" , color='Black')
plt.title("Densidad Espectral de la señal", color='Black')
plt.legend()
plt.show()

# Histograma
plt.figure(figsize=(10, 4),facecolor='Beige')
plt.hist(emg.flatten(),bins=50,color='Red',alpha=0.7 )
plt.xlabel("Amplitud", color='Black')
plt.ylabel("Frecuencia" , color='Black')
plt.title("Histograma de frecuencias", color='Black')
plt.grid()
plt.show()