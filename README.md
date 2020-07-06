# Project Title
Image Scraper using Python Flask

## Introduction
This is one of my Python projects from [Machine Learning and Deep Learning with Deployment](https://academy.ineuron.ai/machine-learning-masters.php) course, from [iNeuron.ai](https://academy.ineuron.ai/index.php). In this course, code was written to scrap or collect the required images from any website based on the keyword given by the user. The code needs to generate the web URL based on the given keyword, send a request to web URL to get raw HTML data, parse the obtained data(HTML) to get the source of the image, download the image to system, and display the result to the user.

**Image scraping** is the process or act of scraping a website for its image content. It's web scraping for image content only. You can scrape images data from websites with a webs scraping tool. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database, for later retrieval or analysis.

## Install
This project requires Python3. Also, some of the python libraries like Flask, bs4, request, pillow, and urllib.request.
All the libraries can be installed using the following commands...
```
pip install flask
pip install bs4
pip install requests
pip install urllib
pip install pillow
```
The project also requires **Cloud Foundry CLI** for **Pivotal Web Services** for deploying the app on the cloud which can be installed from [here](https://github.com/cloudfoundry/cli). The download can be confirmed by running the following command in terminal/ cmd<br>
```
cf
``` 
Also, the project requires some HTML  knowledge to build the web pages for taking Keyword form the user and displaying the result to the user.

## Application Architecture
![Blank Diagram](https://user-images.githubusercontent.com/50728879/86622696-f6f2b400-bfdd-11ea-84ca-e8bbb08ab72a.png)
## Code
* `Step-1` Start the flask app which will run the **"main.html"** on the cloud and get the search string given by the user.
* `Step-2` Search the internet for the desired images.
* `Step-3` Download the obtained images from Step-2
* `Step-4` Show the obtained images to the user through **"Show.html"**

## Deployment

To deploy the app on the cloud, the following steps are followed-
* `Step-1` Create an account on Pivotal Web Services, which can be done from [here](https://run.pivotal.io/)
* `Step-2` open the **terminal(Linux/ Mac)** or **Cmd(Windows)** and navigate to the folder that contaions all the file.
* `Step-3` Run ```cf login -a https://api.run.pivotal.io``` command. On execution, it will ask for Email Id and Password for Pivotal Web Services
* `Step-4` After, logging in run ```cf push``` command and wait for some time. On successful execution, it will provide the URL for the app.

The link for runnig app is - https://image-scrapper-persistent-quoll-ur.cfapps.io/

| ![image scraper](https://user-images.githubusercontent.com/50728879/86624231-96b14180-bfe0-11ea-87b1-45ef62f58de1.gif) |
|:--:|
|***App Preview***|
