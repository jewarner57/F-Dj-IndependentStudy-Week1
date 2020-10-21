## Questions
1. Why do I need an \_\_init\_\_.py in each blueprint folder?
2. Why can't I just have a route/ folder with a main.py and party.py? Why do I need seperate folders?
  * Is this just best practice?
3. What is the correct class configuration for my config file?
  * I just have the class with values being set inside of it. 
4. On a larger project is it bad to have a template folder in each blueprint folder?
5. Is it best practice to use a url prefix for all blueprints or can use one only when I think it's necessary?
6. Is it best practice to have the app start using \_\_init\_\_.py?
7. Is it possible to store @app.error_handler() routes inside their own blueprint?
  * I was having issues getting them to work outside of my main file and I couldn't find a solution.