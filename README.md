# turvey

Turvey is a Terminal User Interface with which you can create and take part
in surveys that are stored in the Cloud. The Interface is written in Python,
the server in Node.js and as a database I'm using MongoDB.
A survey can contain multiple questions and the questions in surveys can
be one of these different types:
- Right or Wrong
- Multiple Choice
- A number (there can be a minimum and maximum)

## Installation

1. Make sure you have installed Python 3 on your computer
2. Clone this Repository and cd into it
3. Execute the setup shell script for your os
4. Add ~/bin to your $PATH variable
5. Now you should be good to go if no errors have occured running the setup script

## Usage

- Creating a new survey: ```turvey create {surveyName}```
- Create a diagram visualizing the results: ```turvey visualize {surveyId}``` (the diagram will be saved as a png file)
- Take part in a survey: ```turvey do {surveyId}```
