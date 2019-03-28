# Prerequisite

You should have java, git, docker, docker.io, python3, mongodb and maven installed before trying to set up this project
use :  ```apt install <any>``` to install any of these you don't have installed yet. 

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

    *Make sure Scenrios codes target localhost:8080 for these questions*  

# Setup Q5

1) Stop and discard docker containers : mongo and jguweka:OSA3 previously added

2) Return to project root folder

3) $ `docker stats`

4) $ `docker-compose up -d`

    *Make sure Scenrios codes target localhost:8080 for these questions*  
