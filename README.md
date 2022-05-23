# Transformer Generator


# Contents
* [Introduction](#Introduction)
    * [Application](#Application)
* [Software Planning](#Software planning)
    * [Kanban Board](#Kanban-Board)
    * [Risk Assessment](#Risk-Assessment)
    * [Test plans](#Test-plans)
* [Continous Integration/Deployment pipelines](#Continous-Integration/Deployment-pipelines)
* [Architectures](#Architectures)
    * [Docker Compose](#Docker-Compose)
    * [Docker Swarm](#Docker-Swarm)
    * [Nginx](#Niginx)
* [Application Configuration](#Application-Configuration)
* [Front-End Design](#Front-End-Design)
* [Future Imporvements](#Future-Improvements)


## Introduction

The objective of this project was to produce an application that generates "objects" upon a set of predefined rules.

To be more specific the application should consist of four microservices: the first service should act as a from end service, two back-end services which generate objects and a thrid back-end servie which uses the objects to generate a response which is shown on service one.

The constraint of the project were the following:

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL

### Application

To meet the criteria stated above I chose to create a Transformer generator based on a colour and car brand. The application works as so:

* Service 1 is a front end web page that displays the results of the three back-end services.
* Service 2 produces a colour which is randomly chosen from a list of colours.
* Service 3 produces a car brand which is randomly chosen from a list of car brands.
* Service 4 takes the information from service 2 and 3 and uses this to decide what transformer will be displayed in service 1.


## Software Planning

### Kanban Board

My project tracking was done using Jira, I chose this because it is extremely popular in the industry. The full board can be found here: https://karljay98.atlassian.net/jira/software/projects/PPQ/boards/1.

Unfortunately, I was unable to implement nginx and Jenkins, I did write a Jenkins script which can be found in the Jenksfile branch. 


## Risk Assessment

### Initial risk assessment

![image](https://user-images.githubusercontent.com/71146682/169899580-42523e74-f9b0-41f1-9383-0f721f8e0e13.png)

### Developed risk assessment

![image](https://user-images.githubusercontent.com/71146682/169901670-b5eea29e-2282-4cc8-9b4a-7c0b793d6170.png)

### Full risk assessment

https://docs.google.com/spreadsheets/d/1nodtkZQhORem74N3cXGjemBx2pv_kwR9UhCzZeuHgZY/edit?usp=sharing

