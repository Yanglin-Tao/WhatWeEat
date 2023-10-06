# TurboGears2 Simple Tutorial
> Yanglin Tao 10/06/2023
## Installing TurboGears
Prerequisite: install Python and pip tools.
```
pip install TurboGears2
```

1. A very nice and easy to understand video tutorial: https://www.youtube.com/watch?v=2O-55SNeIDA
2. Tutorial Point: https://www.tutorialspoint.com/turbogears/index.htm
3. Official documentation:
https://turbogears.org/

## Hello World example
This example demos a single web page that displays a message. 
### a. helloworld.py
The class has a index method that returns a message. The @expose('helloworld.xhtml') renders content in helloworld.xhtml.
### b. helloworld.xhtml
The HTML file is a template that includes a placeholder for the message.
To start the demo:
 1. run 'python3 helloworld.py'
 2. go to http://localhost:8080/

 ## Calculator example
 This example demos a calculator with multiple web pages and multiple arithmic methods.
 ### calculator.py
 The class has three methods: a index method (default page), a addition method that takes two operands as arguments, and a multiplication method that also takes arguments.
To start the demo:
 1. run 'python3 multiple_pages.py'
 2. go to http://localhost:8080/
 3. enter http://localhost:8080/add?a=10&b=20
 4. enter http://localhost:8080/multiply?a=10&b=20

## Calculator Template Example
The similar calculator example with HTML template.
### calculator_template.py
The class has two methods: a index method and a calculator method that passes in two operands. 
### calculator_template.xhtml
The template renders the addition, subtraction, multiplication, and division results of the two operands.
To start the demo:
 1. run 'python3 calculator_template.py'
 2. go to http://localhost:8080
 3. enter http://localhost:8080/calculator

