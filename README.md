# Correlacion-convolucion
# Introducción 
Este laboratorio se realizó con la intención de identificar como funciona una convolución, una correlación, una transformada de fourier, el cálculo de la densidad espectral y como estas se ven gráficamente, aplicando las funciones a una gráfica importada desde Physionet, el proceso para observar las gráficas se realiza desde un programa en python con el uso de funciones y librerías específicas que nos permitan el análisis de la gráfica importada y la diseñada.
# Proceso 
Para este laboratorio el proceso inicial fue el entendimiento de como funciona una convolución matemáticamente y gráficamente, la convolución es una operación que une dos funciones generando una nueva, se analizó inicialmente en papel para poder observar el comportamiento de la unión de las dos funciones presentadas mediante un análisis gráfico sencillo, luego iniciamos con el proceso de programación del código para el análisis de nuestra señal electromiográfica importada desde Physionet, esta señal se importa desde el 'Physionet bank atm' la cual es una página que contiene archivos y recursos de señales fisiológicas.

![image](https://github.com/user-attachments/assets/18347faf-dbcb-4372-a700-c83a6775da0b)

![image](https://github.com/user-attachments/assets/3ea8f575-210f-419e-9314-a3413159a899)

![image](https://github.com/user-attachments/assets/06ab62e3-70ed-44b8-a854-171c29a95268)

![image](https://github.com/user-attachments/assets/ccf82cb7-97d0-4dc9-a2f1-9badfa060fcb)

# Código   
Para este código nos apoyamos de las librerias: matplotlib.pyplot, numpy, scipy.io, scipy.signal. Estas librerías nos ayudan a realizar los cálculos mediante funciones, nos ayuda a graficar las funciones y señales y a cargar los archivos de Physionet, principalmente se hacen arreglos de las funciones que vamos a convolucionar y posteriormente se grafican cada función individual y su convolución 

![image](https://github.com/user-attachments/assets/1b0235b0-3ecf-4993-af2f-b1fa7cfb71cb)

# Función h[n]

![image](https://github.com/user-attachments/assets/a7730b92-afcf-461d-bb72-a804c07f6a07)

# Función x[n]

![image](https://github.com/user-attachments/assets/a503f9df-3209-492d-b8db-5c0114279aa0)

# Función convolucionada

![image](https://github.com/user-attachments/assets/d42061dd-07bc-409d-aa4b-6d0c607ab682)

# Importación y análisis de la señal de Physionet 
Usando la función de la libreria scipy importamos el archivo .mat que se obtuvo de Physionet, dando valores a la frecuencia y periodo de muestreo, con esto iniciamos calculando la media, la desviación estándar usando funciones y sin funciones.

![image](https://github.com/user-attachments/assets/8b688149-740f-4b95-ae68-dd64a34ddf5e)

![image](https://github.com/user-attachments/assets/a61e5e39-e528-4c0b-8038-c1f127f24b3a)

![image](https://github.com/user-attachments/assets/ac95e133-ec25-4c24-ac50-a19278a2a14a)

# Correlación de señales sinusoidales 
Para el análisis de la correlación usamos funciones seno y coseno, realizando la correlación mediante funciones de la libreria numpy y graficando ambas funciones de manera discontinua para poder observar de mejor manera cada una individualmente y la correlación entre estas.

![image](https://github.com/user-attachments/assets/3723b77f-1011-4cc4-8242-795f16b28a24)

![image](https://github.com/user-attachments/assets/58f46a29-2247-4f5e-8102-2974e9090b40)

Esta correlación nos permite observar la similitud  de estas señales según el desplazamiento que estas tienen.

# Grafica de la señal respecto al tiempo 
Esta gráfica se realiza para analizarla respecto al tiempo con un tiempo inicial de 0 y como valor máximo la desviación estandar.

![image](https://github.com/user-attachments/assets/9d77b527-7716-42c3-97b7-deca20ea6114)

![image](https://github.com/user-attachments/assets/c9e32fd8-68a5-43e5-a742-dd719b9b8618)

# Transformada de fourier y gráfica respecto a la EMG
Para este paso con el uso de funciones realizamos una transformada de fourier, esto para que se pueda analizar la señal descomponiendola en sus componentes de frecuencia y su intensidad, la transformada se realiza mediante una función de la librería numpy la cual realiza la transformada de fourier y calculando la magnitud y frecuencia de la señal a la que se le quiere aplicar, luego se grafica para que se pueda observar como actúan las intensidades de su frecuencia, luego se calculan su frecuencia media, frecuencia mediana y desviación a partir de funciones,tomando valores de magnitud y frecuencia. 

![image](https://github.com/user-attachments/assets/bda3a9f5-154c-4b0f-a85f-8ab1d5b464ed)

![image](https://github.com/user-attachments/assets/b402596f-f8d9-4408-84ae-d3f68c0fc1a6)

![image](https://github.com/user-attachments/assets/6a9e4f7b-b81b-4664-9d65-32250cf15adf)

![image](https://github.com/user-attachments/assets/6ac2e63e-097f-4c19-8122-2ab249bb254c)


# Densidad espectral
La densidad espectral se calcula para observar como la potencia de la señal se distribuye en función de la frecuencia, para calcular esto hacemos uso de la librería scipy que nos permite mediante una función, usando la frecuencia de muestreo y una función la cual divide los puntos en los que se mostrará antes de aplicar la transformada, para finalizar se grafica en una escala logaritmica que permite visualizar de mejor manera la gráfica.

![image](https://github.com/user-attachments/assets/d90be83e-ab42-4af2-8064-c203945affc2)

![image](https://github.com/user-attachments/assets/09c45fbe-c3e4-4c23-b563-d3496445ca0c)

# Histograma de la señal EMG
Se grafica la señal emg suavizada como un histograma para observar los valores de amplitud y frecuencia que tiene esta señal.

![image](https://github.com/user-attachments/assets/968292a6-d609-49d2-9066-3b0b399e3027)

# Fin
Con esto termina el código y proceso utilizado para analizar de manera parcial, la correlación, convolución, función en dominio de la frecuencia y densidad espectral. Todo esto a partir de el uso de herramientas de programación y fuentes de imágenes fisiológicas que nos permiten ver a detalle el comportamiento de las mismas, en este github se encontrará la señal electromiográfica usada para este laboratorio y el código en python con el que se analizaron las señales. 

