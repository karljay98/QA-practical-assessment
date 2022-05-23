# Transformer Generator


# Contents
* [Introduction](#Introduction)
    * [Application](#Application)
* [Software Planning](#Software Planning)
    * [Kanban Board](#Kanban-Board)
    * [Risk Assessment](#Risk-Assessment)
    * [Test plans](#Test-plans)
* [Continous Integration/Deployment pipelines](#Continous-Integration/Deployment-pipelines)
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


## Test plans

Testing for this project is crucial as it allows the developers to identify if the app works and where potential errors could occur or currently are.

Service 1 results:

![image](https://user-images.githubusercontent.com/71146682/169902518-ec5ce0bd-8e96-40b4-8c30-8c929bbd18ea.png)

Service 2 results:

![image](https://user-images.githubusercontent.com/71146682/169902634-81db92ba-087c-44b6-b85d-deb5e2390378.png)


Service 3 results:

![image](https://user-images.githubusercontent.com/71146682/169902725-a55e2c3d-9284-45d9-93cf-45cf2a0c5a11.png)


Service 4 results:

![image](https://user-images.githubusercontent.com/71146682/169902783-7a02d845-7c3e-4ad1-b5b1-b4b9c2ba3555.png)

Although, the test coverage is not 100%, the lowest coverage score was 89% which is still very good.


## Continous Integration/Deployment pipelines

![image](https://user-images.githubusercontent.com/71146682/169903994-e66c9ca5-9efb-4705-997e-e047ddeea5be.png)


The Diagram above highlights the whole process of building the CI/CD pipeline which starts at development. At this stage a project tracking system is used (Trello or Jira), programming done using visual studio code which pushes the code to a version control system Github. To build the server Jenkins automates the testing and collection of code from github, this then uses docker-compose to push this to ansible. As the servicer is live ansible deploys the application using docker-swarm.

## Front-End Design 

The front end design is very simple ans shows the colour, car brand ans transformer generated.
![image](https://user-images.githubusercontent.com/71146682/169911940-6d845d3b-4247-4903-a054-47a8db6f1cbc.png)

## Future Improvements

The future improvements which need to be made inclue:

* Use of Jenkins
* Use of Nginx
* Explore the use of a SQL server to hold information.
* Have a more enticing front page as the current one is very basic, maybe include bootstrap templating.

## Video Presentation

https://drive.google.com/file/d/1O3xRXVbLIB3h7IC-ypBEGFpue_pKtuF-/view?usp=sharing










