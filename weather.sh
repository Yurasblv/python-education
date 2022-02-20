#!/bin/bash

echo $( curl 'https://api.openweathermap.org/data/2.5/weather?lat=50&lon=36.25&appid=f5ba5b5bf8a56570b2104405f9a910f8') >> ${HOME}/weather.json

