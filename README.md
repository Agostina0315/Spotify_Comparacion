# Spotify_Comparacion
# Análisis Comparativo de Géneros Musicales: Metal, Clásico y Pop

Este proyecto está dedicado a comparar tres géneros musicales: **Metal**, **Clásico** y **Pop**.

La motivación principal fue analizar dos géneros que suelen ser menos populares en mi entorno (Metal y Clásico) frente a uno mucho más difundido en Argentina: el Pop. La idea era observar diferencias y similitudes en características musicales, subgéneros, y evolución a lo largo del tiempo.

## 🎧 Recolección de Datos

Para obtener los datos utilicé la **API de Spotify**. Esta API permite obtener información de hasta 50 artistas por solicitud, por lo que realicé múltiples extracciones aleatorias, evitando que el análisis se centre únicamente en los artistas más escuchados.

Dado que no todas las consultas devolvieron la misma cantidad de datos por género, la cantidad final de artistas varía:

- **Metal:** 413 artistas  
- **Clásico:** 769 artistas  
- **Pop:** 545 artistas

> ⚠️ Esto implica que la comparación no es perfectamente equilibrada en términos de volumen de datos por género, aunque sigue siendo válida para un análisis general.

## 🌍 Criterios de Selección

Uno de los filtros principales fue que los artistas fueran **escuchados en Argentina**, independientemente de su país de origen. Si bien la selección fue aleatoria, por cada artista obtuve:

- Sus canciones más populares
- Subgéneros asociados
- Álbumes publicados y sus años de lanzamiento

## ⚙️ Proceso de Trabajo

Durante la recolección de datos, me aseguré de que **no se repitieran artistas** dentro de un mismo género. Aunque algunos artistas aparecen asociados a múltiples subgéneros, utilicé la combinación de `offset` y `limit` para evitar que fueran extraídos nuevamente en futuras solicitudes a la API de Spotify.

### 🧩 ¿Cómo funciona `offset`?

- `limit` indica cuántos artistas se quieren traer en cada extracción (por ejemplo, 50).
- `offset` indica desde qué posición empezar a traer los resultados.

📌 Ejemplo:  
- En la primera extracción (`offset=0`), se obtienen los primeros 50 artistas.  
- En la segunda (`offset=50`), los siguientes 50.  
- Y así sucesivamente.

Esto permite **paginar los resultados** y obtener artistas distintos en cada batch, evitando repeticiones (salvo que Spotify modifique el orden de los resultados entre consultas).

Una vez finalizadas todas las extracciones, obtuve múltiples archivos `.csv`. Para continuar con el análisis, desarrollé un segundo script que se encargó de **unificar todos los archivos en un solo dataset consolidado**.

Cada archivo contiene las siguientes columnas:

- `nombre`: nombre del artista  
- `popularidad`: puntaje de popularidad del artista (según Spotify)  
- `genero`: subgénero asociado al artista  
- `cantidad de álbumes`: total de álbumes publicados por el artista  
- `mejor pista`: canción más popular del artista  
- `álbum de la mejor pista`: álbum en el que se encuentra esa canción  
- `año de la mejor pista`: año de lanzamiento del álbum correspondiente

Luego, cargué estos tres datasets en una base de datos de **SQL Server**, donde creé una base llamada `Spotify`. Esto me permitió **consultar los datos con mayor comodidad**, además de preparar los datos de forma más estructurada para **visualizarlos en Power BI**.

## 📊 Visualización en Power BI

Para el análisis visual trabajé con **Power BI**, donde diseñé distintos dashboards para explorar y comparar los datos recolectados.

- Comencé modelando la **hoja de Metal**, definiendo visualizaciones clave como distribución de popularidad, cantidad de álbumes por artista y evolución temporal.
- Una vez validado ese diseño, repliqué la lógica de visualización para los otros dos géneros: **Clásico** y **Pop**, manteniendo la coherencia visual y estructural entre las páginas.

Además, desarrollé una **hoja comparativa** donde analizo la **popularidad promedio y distribución** de artistas entre los tres géneros, teniendo en cuenta la diferencia en la cantidad de artistas disponibles por cada uno (Metal: 413, Clásico: 769, Pop: 545). Esto garantiza una comparación lo más justa y representativa posible.

Estas visualizaciones permiten identificar tendencias, diferencias y similitudes entre los géneros desde una perspectiva cuantitativa basada en datos reales extraídos de Spotify.

## 📷 Visualizaciones

### 🎸 Hoja de análisis: Metal
![Dashboard Metal](./Visualizaciones/Visualizacion_metal.png)

### 🎧 Análisis de artistas y subgéneros musicales en Argentina *(Dashboard Metal - Power BI)*

Esta visualización se centra en analizar la distribución y popularidad de artistas y subgéneros musicales dentro del género **Metal** en el contexto argentino, como parte de una comparación general con los géneros **Clásico** y **Pop**.

#### 🎯 Objetivo

Explorar el comportamiento de distintos subgéneros del metal en la escena local, evaluando tanto el volumen de lanzamientos como los niveles de popularidad. La muestra considera artistas seleccionados de manera aleatoria, por lo que los resultados no representan necesariamente a los exponentes más conocidos ni más difundidos del género.

#### 🧩 Datos clave

- **Total de artistas analizados:** 413  
- **Subgéneros más representados (por cantidad de álbumes):**  
  Argentine Rock, Christian Rock, Groove Metal, Thrash Metal, Hardcore Punk.

#### 🔍 Insights destacados

- **Dominancia del Argentine Rock y subgéneros extremos:**  
  El *Argentine Rock* lidera en cantidad de álbumes, seguido por géneros más pesados como *Thrash Metal*, *Groove Metal* y *Hardcore Punk*, reflejando una preferencia local por estilos intensos y con fuerte identidad regional.

- **Mayor volumen de álbumes por artista:**  
  2X y A.N.I.M.A.L. son los artistas que presentan mayor producción dentro de esta muestra aleatoria. Sin embargo, esto no implica necesariamente que tengan mayor trayectoria o reconocimiento que otros artistas del género, ya que la selección no se basó en criterios de popularidad histórica o difusión mediática.

- **Popularidad acumulada por artista:**  
  Transmetal, V8, A.N.I.M.A.L. y DGM se destacan en esta muestra por su nivel de popularidad acumulada. Es importante remarcar que, al tratarse de una selección aleatoria, estos valores no reflejan necesariamente a los artistas más difundidos o influyentes del metal a nivel internacional o nacional.

- **Pistas más populares en promedio:**  
  Canciones como Marmichula, Había Volar Volar y MAESTROS lideran el promedio de popularidad dentro de esta muestra. Nuevamente, estos resultados deben interpretarse con cautela, ya que no representan un ranking oficial de popularidad general del género.
  
- **Popularidad por subgénero:**  
 Aunque el Argentine Rock concentra la mayor producción, géneros como Anime Rap y Groove Metal muestran alta popularidad relativa, reflejando una escena diversa que cruza lo local con lo global.

#### 📌 Consideraciones metodológicas

- **Contexto local:**  
  El análisis se enfoca en artistas y géneros con impacto en la escena argentina, incluyendo tanto exponentes nacionales como internacionales con presencia relevante en el país.

- **Clasificación automatizada de géneros:**  
  Los géneros fueron extraídos de Spotify y asignados automáticamente. Esto puede generar inconsistencias, como la inclusión de géneros que no corresponden directamente al metal (*anime rap*, *boom bap*, etc.). Estas etiquetas fueron respetadas como parte del enfoque exploratorio de los datos disponibles.

### 🎻 Hoja de análisis: Clásico
![Dashboard Clásico](./Visualizaciones/Visualizacion_Clasico.png)

### 🎻 Análisis de artistas y subgéneros clásicos en Argentina *(Dashboard Clásico - Power BI)*

Este tablero analiza la música **clásica** en el contexto argentino, explorando los subgéneros predominantes, los artistas con mayor volumen de producción, y las piezas más populares entre los oyentes locales.

#### 🎯 Objetivo

Observar cómo se distribuyen los subgéneros de la música clásica, qué artistas aparecen con mayor frecuencia y qué niveles de popularidad se registran.
Los artistas fueron seleccionados de manera aleatoria, por lo que no se trata necesariamente de los compositores más importantes, ni de los intérpretes más conocidos en la historia de la música clásica.

#### 🧩 Datos clave

- **Total de artistas analizados:** 769  
- **Subgéneros más representados:**  
  Classical, Classical Piano, Opera, Orchestra, Neoclassical, Chamber Music, Requiem, Choral.

#### 🔍 Insights destacados

- **Dominancia del subgénero "Classical" como etiqueta general:**  
  La categoría *Classical* agrupa la mayor cantidad de álbumes. Esto refleja tanto la diversidad interna del género como la forma en que Spotify clasifica obras históricas bajo etiquetas amplias.

- **Alta concentración de álbumes en pocos artistas:**  
  Instituciones como *Academy of St. Martin in the Fields* o directores como *Alexander Gibson* se destacan por su enorme volumen de producción. Esta tendencia responde, en parte, a la reutilización de grabaciones históricas en múltiples lanzamientos.

- **Pistas más populares:**  
  Obras como *21 Hungarian Dances*, *Orchestral Suite No. 3*, *Requiem in D Minor* y *Piano Sonata No. 14 (Moonlight)* se encuentran entre las más escuchadas. Su popularidad puede explicarse por su presencia en playlists educativas, cinematográficas o de relajación.

- **Popularidad acumulada por género:**  
  Los subgéneros *Classical*, *Opera*, *Orchestra* y *Classical Piano* concentran la mayor parte de la popularidad, evidenciando una audiencia interesada tanto en obras sinfónicas como en piezas para instrumentos solistas.

#### 📌 Consideraciones metodológicas

- **Volumen de datos significativamente mayor:**  
  A diferencia del Pop o el Metal, el género Clásico aportó el mayor número de registros en la extracción, lo que impacta directamente en las métricas de popularidad. A mayor cantidad de artistas y álbumes, mayor volumen acumulado. Esta desproporción debe tenerse en cuenta al comparar con otros géneros.

- **Clasificación automática de subgéneros:**  
  Como en los demás dashboards, los géneros provienen de la API de Spotify y fueron asignados automáticamente. Esto puede generar etiquetas redundantes o poco precisas (*classical*, *neoclassical*, *minimalism*, etc.) que no siempre responden a una curaduría musicológica rigurosa.


### 🎤 Hoja de análisis: Pop
![Dashboard Pop](./Visualizaciones/Visualizacion_pop.png)

## 🎤 Análisis de artistas y subgéneros musicales en Argentina  
*(Dashboard Pop - Power BI)*

Este dashboard presenta una exploración de artistas vinculados al **Pop**, en el contexto argentino, como parte del análisis comparativo con los géneros **Clásico** y **Metal**.

### 🎯 Objetivo

Examinar las tendencias dentro del pop argentino, identificando los subgéneros más frecuentes y los artistas con mayor presencia en la muestra. Como en los otros géneros, los artistas fueron seleccionados de forma **aleatoria**, por lo tanto **no representan necesariamente a los más famosos, históricos o difundidos del género**.

### 🧩 Datos clave

- **Total de artistas analizados:** 545 
- **Subgéneros destacados (según cantidad de álbumes):**  
  Pop argentino, Electropop, Dance Pop, Indie Pop, Latin Pop. También aparecen géneros como Cumbia, RKT y Cuarteto.

### 🔍 Insights destacados

- **Presencia de géneros populares en la cultura local:**  
  Además de subgéneros típicamente vinculados al pop, como *Electropop* o *Latin Pop*, aparecen estilos como *Cumbia*, *RKT* y *Cuarteto*, muy difundidos en Argentina. Aunque no son estrictamente subgéneros del pop, fueron etiquetados como tal por Spotify, probablemente por su alto grado de masividad.

- **Artistas de alta popularidad en la escena nacional, pero muestra aleatoria:**  
  Algunos artistas incluidos presentan altos niveles de popularidad, pero esto se debe a la aleatoriedad de la muestra. No fue una selección curada por fama o éxito comercial.

- **Popularidad general más alta en promedio que metal y clásico:**  
  A pesar de no haber seleccionado los artistas más top intencionalmente, el género pop presenta valores de popularidad más elevados en promedio. Esto puede vincularse con el carácter masivo del género y con la familiaridad del público argentino con muchos de sus subgéneros.

### 📌 Consideraciones metodológicas

- **Selección aleatoria de artistas:**  
  Al igual que con los otros géneros, los artistas y subgéneros fueron tomados de manera aleatoria desde Spotify. Esto significa que la muestra incluye tanto artistas reconocidos como otros de menor difusión, sin priorización intencionada.

- **Clasificación automatizada de géneros:**  
  Spotify asigna etiquetas de género de forma automática. Esto puede haber generado la inclusión de géneros como *Cumbia* o *RKT* dentro del pop, reflejando una clasificación basada más en popularidad que en una estructura musical académica.



### ⚖️ Comparativa entre géneros
![Dashboard Comparativo](./Visualizaciones/Visualizacion_comparativa.png)

### 📌 Conclusión general del análisis

Este estudio exploró la popularidad relativa de tres géneros musicales —metal, clásico y pop— utilizando un conjunto de datos diseñado intencionalmente para evitar sesgos hacia artistas ampliamente reconocidos. En lugar de ello, se seleccionaron artistas de forma aleatoria, lo que permite observar patrones de consumo musical más amplios y menos condicionados por la lógica del mainstream.

#### 🔍 Principales hallazgos:

- **Metal** presenta una popularidad distribuida de forma pareja, con pocos picos, lo que sugiere que en este muestreo sus artistas tienen una presencia consistente pero limitada.

- **Clásico** reúne la mayor cantidad de artistas, pero también es el género con menor visibilidad general. Esto se debe en parte a la inclusión de numerosos artistas que no pertenecen estrictamente al ámbito clásico, convirtiéndolo en el género más "contaminado" del análisis.

- **Pop**, si bien no domina en términos absolutos, muestra una ligera ventaja en popularidad relativa. Varios artistas alcanzan los valores máximos dentro del conjunto, lo que indica que incluso en un muestreo aleatorio, el pop logra filtrar propuestas con mayor alcance comercial.

#### 🧠 Reflexión final:

En un contexto de muestreo sin sesgo hacia lo más escuchado, el **pop** mantiene cierta capacidad de inserción mediática, mientras que el **metal** y el **clásico** —especialmente este último por su alta heterogeneidad— sostienen un perfil más bajo y disperso. Esto refuerza la idea de que la popularidad no solo depende del género, sino también del grado de cohesión interna y su representación algorítmica en plataformas como Spotify.

---

### 📊 Comparación metodológica entre dashboards

| Criterio                          | Pop                              | Metal                            | Clásico                          |
|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Inclusión de otros géneros       | Sí, pero en menor medida         | Presente pero moderada           | Muy alta (más dispersión)        |
| Homogeneidad de artistas         | Media                            | Alta                             | Baja                             |
| Dominancia de subgéneros claros | Media (latin pop fuerte)         | Alta (subgéneros metal claros)   | Baja                             |
| Popularidad concentrada          | Baja                             | Media                            | Baja                             |



---

📇 **Autor:** [Agostina Marengo](https://www.linkedin.com/in/agostina-marengo/)

_Proyecto desarrollado en el marco de mi formación en visualización de datos y análisis exploratorio. Gracias por visitar mi portfolio._
