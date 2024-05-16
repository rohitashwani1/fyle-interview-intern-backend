# To run the code

* Open terminal in this folder
* Then create docker image by run the following command: **docker build -t demo-app .**
* Then run container from this image by run this command: **docker run -dp 127.0.0.1:7755:7755 demo-app**

* Now the app is running on 127.0.0.1:7755
* To Know the Container-ID, run the command:**docker ps**
* To check test open a terminal and enter command: **docker exec -it <CONTAINER-ID> bash**
* Now run the command: **pytest --cov**