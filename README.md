![logotipo](static/media/diabetes.jpg)
# **SIRCODI:** :drop_of_blood: :argentina:
 ## *Sistema de Registro y Control para Personas con Diabetes.* 
 
 Este es un Proyecto del tipo Web-App o API Realizado para el Curso de "Programador Python".
 
 
# **Tipo y Número de Proyecto:** 

 **2do Proyecto de la Carrera.**
 
 **Lenguaje Backend Utilizado:** *Python*
 
 **Curso:** *Programador Python* 
 
 **Carrera:** *Desarrollador Python*
 
 **Institución:** *Inove Coding School*
 
 
 # **Librería y Módulos Utilizados:**
 - **Flask** ---> microframework
 
 - **sqlite3** ---> DB - Data Base
 
 - **matplotlib**
 
 - **seaborn**
 
 - **numpy**
 
 - **traceback**
 
 - **io**
 
 - **logging**
 
 - **os**
 
 - **datetime**
 
 - **configparser**
 
 
 # Pre-requisitos 📋
Para poder ejecutar esta aplicación, será necesario tener instalada la versión 3.6 de Python o superior. También es necesario incluir varios módulos.
Recomendamos antes de descargar el repositorio, realizar los siguientes pasos:

```
pip3 install pip -U --upgrade
pip3 install numpy
pip3  install matplotlib
pip3 install -U seaborn
pip3 install -U Flask
```
 
 # Instalación y pruebas 🔧⚙️
Descargue el repositorio en su pc y abra el proyecto en su editor de código, luego ejecute el archivo ```app.py```. La aplicación crea un servidor local en la dirección http://127.0.0.1:5000/ en donde tendremos alojado el frontend de nuestra aplicación. Las direcciones para acceder a las páginas de la aplicación son:

- http://127.0.0.1:5000/          # Página principal que lo guiará para el uso de la WebApp.
- http://127.0.0.1:5000/formulario # Página en donde podremos ingresar los datos para ser enviados y luego cargados en la DB.
- http://127.0.0.1:5000/niveles/tabla   # Página que muestra todos los registros realizados en formato tabla HTML.
- http://127.0.0.1:5000/niveles/api   # Página que muestra el dataset en formato JSON de los registros realizados --> Útil para Desarrolladores
- http://127.0.0.1:5000/comparativa   # Página que muestra los gráficos de comparaciones de la cantidad de personas según grupo etario y sexo biológico.
- http://127.0.0.1:5000/info   # Página que muestra información y descripción del funcionamiento de la página.
 
 
# **Contacto**
 - ***Autor:*** Torres Molina, Emmanuel Oscar.
 
 - ***email:*** emmaotm@gmail.com
 
 - ***Repositorios*** ==> [Click](https://github.com/eotorresmolina?tab=repositories)


# **Descripción:**
#### *El Programa en cuestión permite el Registro de personas que han sido contagiadas de Covid-19. Dicho Registro consta de ciertos datos que se le irá pidiendo al usuario ingresar para completar el formulario del respectivo contagiado. Además de esto, permite ver Toda la Información Disponible de todos los casos como por ejemplo cantidad de promedio de contagios, muertes. Provincia y/o meses con más y menos contagios, etc. Por último el programa permite generar un informe con todo el análisis realizado de los casos positivos.*
#### *Cabe Aclarar que este Programa utiliza sus funciones basándose en datos de la República Argentina.*
 
 
# **Modos de Uso del Programa:**
 #### *A Continuación se Detalla Brevemente de Como Usar el Programa:*
 #### *El Programa al Iniciarse desplaya un Menú Principal con 3 opciones disponibles:*
 #### 1. Loguearse
 #### 2. Ingresar Como Invitado
 #### 3. Salir del Programa
 #### *Al Elegir la opción 1 el usuario deberá loguearse ingresando un nombre_de_usuario y una contraseña. Las mismas son: "user1234" "jilguero124". Tiene como Máximo 3 intentos para Ingresar Correctamente los datos de logueo. Una vez logueado podrá: 1-Cargar los datos de la persona contagiada, los cuales, serán almacenados en un       archivo con formato .csv ==> "registro_covid19.csv". 2-Ver todas las personas que fueron registradas hasta el momento.*
 #### *Al Elegir la Opción 2 el usuario que ahora tiene permisos de invitado veerá en pantalla un menú con la información disponible para consultar. Dentro de este menú  también exite una opción que permite ver y generar un Informe con Todo el Análisis Realizado en base a los registros de los casos. El nombre del informe que se           genera y/o actualiza es: "informe_covid19.txt".*


# **Módulo y/o Archivos para que el Programa Funcione Correctamente:**
 #### *Se debe Bajar los siguientes módulos:*
 1. app.py (Programa Principal)
 2. diabetes.py (Módulo/Librería que Contiene varias funciones utilizadas)
 3. analitycs.py (Módulo/Librería que Contiene varias funciones utilizadas)
 4. registro_covid19.py (Archivo .csv que Contiene todos los Registros de las Personas Contagiadas)


# **Versión y Última Actualización:**
 #### **Versión:** 1.1
 #### **Última Actualización:** 15-09-2020


# **Consulta y/o Problemas:**
 #### *Ante Cualquier mal funcionamiento del Programa y/o consultas acerca del uso del mismo pueden mandarme un mensaje al mail que más arriba se detalla.*
 #### *Muchas Gracias por haber llegado hasta acá.*
 #### *Emmanuel.*
