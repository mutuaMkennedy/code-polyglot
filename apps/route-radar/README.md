# RouteRadar

<p align="start">
  <img alt="Python v3.12" src="https://img.shields.io/badge/python-v3.12-blue?logo=python&color=blue">
  <img alt="Django v5.0" src="https://img.shields.io/badge/django-v5.0-green?logo=django&color=%230C4B33" />
  <img alt="React v18.2" src="https://img.shields.io/badge/react-v18.2-blue?logo=react&color=blue" />
  <img alt="Docker v25.0.4" src="https://img.shields.io/badge/docker-v25.0.4-blue?logo=docker&color=blue" />
</p>

Welcome to RouteRadar, your go-to app for finding and filtering bus stations in your area using Mapbox integration!

## Introduction

RouteRadar is a web application designed to help users easily locate and filter bus stations based on their preferences and location. With RouteRadar, you can explore nearby bus stations, filter them by various criteria, and plan your transit routes with ease.

## Features

- Map Integration: Utilizes Mapbox to provide an interactive map interface for users to visualize bus stations and their surroundings.
- Location-based Search: Allows users to search for bus stations in their current location or any specified area.
- Filtering Options: Provides filtering options to narrow down search results based on criteria such as bus routes, accessibility features, amenities, etc.
- Detailed Information: Displays detailed information about each bus station, including routes served, schedules, amenities, and more.
- User-Friendly Interface: Offers an intuitive and easy-to-use interface for seamless navigation and exploration.

## Getting Started

To get started with RouteRadar, follow these steps:

Clone the Repository: Clone this repository to your local machine.

Using SSH

```
git clone git@github.com:mutuaMkennedy/cleartask.git
```

or  
Using HTTPS

```
git clone https://github.com/mutuaMkennedy/cleartask.git
```

Install docker and docker compose if you haven't done so. Installation instructions can be found [here](https://docs.docker.com/engine/install/)

Then navigate to the base directory of the project and create .env file based on the env.sample file provided on the project directory,  
then run the following command

```
docker compose -f docker-compose-dev.yml up --build
```

If you are want to build images from the production docker compose file, make sure you setup your ssl certificates to avoid errors.  
Or, just use the none SSL enabled nginx conf file by doing the following.

Open

```
docker-compose-prod.yml
```

find the Nginx block and change  
`- ./services/nginx/production:/etc/nginx/conf.d ` to `- ./services/nginx/development:/etc/nginx/conf.d `

then run this command

```
docker compose -f docker-compose-prod.yml up --build
```

**DOCKER IMAGES ARE ALSO AVAILABLE**

Don't have time to setup things? Pull the production ready docker images instead.  
Run the following commands

```
docker compose -f docker-compose-prod.yml pull
```

then run the project with

```
docker compose -f docker-compose-prod.yml up
```

## Contributing

Contributions to RouteRadar are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## Author

Mutua Kennedy | [Visit my website](https://kennedymutua.crunchgarage.com/)
