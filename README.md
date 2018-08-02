# WhoIsLeavingEarth.com
A live website which shows upcoming rocket launches as well as information about the Astronauts who are currently in space. 


* The infromation for the upcoming missions to space was scpraped and parsed from [Space Flight Now](https://spaceflightnow.com/launch-schedule/).

* The API used to get the Names and Craft of the Astronauts currently in space can be found here: 

  > http://api.open-notify.org/astros.json

  > GitHub source code: https://github.com/open-notify

* The API to get the background information and photo of the Astronauts is the REST API from Wikimedia. It can be found at:
    
  > https://www.mediawiki.org/wiki/REST_API

## Technologies Used

* **Flask** - Web framework
* **Beautiful Soup** - Python package to parse html
* **Bootstrap** - Front end framework 

The app is being hosted at:
  > www.pythonanywhere.com 
