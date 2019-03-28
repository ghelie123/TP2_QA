# Prerequis

Vous aurez besoin d'avoir installé java, git, docker, docker.io, python3, mongodb et maven avant de pouvoir setup ce projet  
utilisez :  ```apt install <any>``` pour installer ce qui est requis. 

# Setup Q3 et Q4

1) $ `git clone https://github.com/ghelie123/TP2_QA.git`

2) $ `cd jguwekarest`

3) $ `mvn clean package jetty:run`

4) $ `docker pull mongo; docker run --name mongodb -d mongo`

5) $ `docker build -t dockerhubuser/jguweka:OAS3 .`

6) $ `docker run -p 8080:8080 -p 8849:8849 --link mongodb:mongodb dockerhubuser/jguweka:OAS3`
 
N.B: If docker container already running: docker start mongodb

7) Démarrer Jprofiler

8) Appuyer sur session -> Quick Attach  
   Choisir le bouton radio "On another computer"  
   Choisir "Direct network connection" to `localhost` Profiling port : `8849`  
   Appuyer sur Open puis Sampling(Recommanded) -> Ok  

9) Démarer JMeter  
   - File -> New  
   - TestPlan -> Add -> Thread users -> Thread Group  
   - Thread Group -> Add -> Sampler -> HTTPRequests  
   - Thread Group -> Add Listener -> View Results Tree/Graph Results/View Results in a table  
   - HttpRequest :   
      - Server Name or IP : Localhost:8080,  
      - Method : GET,   
      - Path : /algorythm  

   - Répéter pour le scénario 2 avec   
     - Method : POST ,  
     - Path : /algorythm/NaiveBayes  
     - FileUpload : trouver le fichier dans le projet git /Scénarios/weather.arff  
    
   - Répéter scenario 1 pour le scénario 3 avec   
     - Propriété du Thread Group :   
       - Number of threads : 100  
       - Loop : 10  
     - Method : GET ,  
     - Path : /algorythm  
    
    - Répéter scenario 2 pour le scénario 4 avec   
      - Propriété du Thread Group :   
         - Number of threads : 100  
         - Loop : 10  
    - Method : POST ,  
    - Path : /algorythm/NaiveBayes  
    - FileUpload : trouver le fichier dans le projet git /Scénarios/weather.arff  

    *Make sure Scenrios.py codes target localhost:80 for these questions*  

# Setup Q5

1) Stoppez et discarter les containeurs docker  : mongo et jguweka:OSA3 ajouté précédement

2) Retourner à la racine du répertoire Git

3) $ `sudo apt install docker-compose`

4) $ `docker stats`

5) $ `docker-compose up -d`

6) To scale up, use :  
   $ `docker-compose up -d --scale jguweka=4 --force-recreate`
   
7) To scale down, use :  
   $ `docker-compose up -d --scale jguweka=1 --force-recreate`

    *Make sure Scenrios.py codes target localhost:80 for these questions*  
    
# Utiliser les Scénarios

1) Naviguez au répertoire TP2_QA/Scenarios

2) $ `python3 scenarios.py`

*Les scénarios sont numérottés de 1 à 4 et sont de plus en plus exigent pour les services déployés. Assurez vous d'avoir les bons ports dans le code scénarios.py lors de l'éxécution pour les 2 setups présentés 8080 pour les Q3 et Q4 et 80 pour les Q5 et Q6*

