1) git clone https://github.com/ghelie123/TP2_QA.git

2) mvn clean package jetty:run

3) cd jguwekarest

4) docker pull mongo; docker run --name mongodb -d mongo

5) docker run -p 8080:8080 -p 8849:8849 --link mongodb:mongodb dockerhubuser/jguweka:OAS3
 