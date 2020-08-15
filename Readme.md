### Spam Detection using Machine Learning

Email spam, also called junk email, is unsolicited messages sent in bulk by email (spamming). The name comes from Spam luncheon meat by way of a Monty Python sketch in which Spam is ubiquitous, unavoidable, and repetitive.

This project aims at identifying potential spam messages(SMS) by looking at the message. This is achieved using Machine Learning in python.

The dataset for the project is from https://www.kaggle.com/uciml/sms-spam-collection-dataset#spam.csv which is also in /data directory.

The model building exercise is done using Jyputer Notebook  present in directory "/Model_Building/spam identification using ML.ipynb", This is reproducible code.

For quick view on what has been done you can look at notebook as pdf from "/Model_Building/spam identification using ML.pdf"

For model deployment I have created Docker Container.
A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

Docker related code is present at "/Docker Files/"

### Creating Docker Image from the Dockerfile

Please follow the steps for creating a custom container which can be used to server the model as an API.

1. Install Docker on the machine by following the instructions on Docker site.(https://docs.docker.com/engine/install/)
2. Once the docker is installed, login to dockerhub using registration.
3. Open command promt in machine and navigate to path where "/Docker Files" is located.
4. type the command `docker build -t spam_classifier_production .`
5. wait for completion, We have our docker image built.
6. type `docker images` and you must see the file with name "spam_classifier_production" to verify the image build is sucessful
7. for starting the container type `docker run -p 1722:80 spam_classifier_production`
Lets look at what the above command is : we are specifying docker to run the image with name "spam_classifier_production".
Our API from flask is on port number 80 of the container, however if we have to access it on machine, we have to map the port to a free port on our machine. "-p 1722:80" specifies this.
8. Once you see the server is up, to verify if the server is started correctly navigate to "http://localhost:1722/isAlive", you must see an message on screen which says "Yes!! server is running"
9. '/Docker Files/client_test.py' is an example of how to get predictions from the container that we just started.
