Assumptions made:

1. I uploaded a large data set of cities to this project. The cities had countries associated 
   with them, but not cities. There are about 40,000 cities in the data set and there are many
   duplicate city names. In the instructions, it seemed to suggest the user would enter the city 
   and state and get weather directly after they click. Instead, to solve the duplicate problem,
   I added a second page where the user can select the specific city they desire from a list.

2. I added a recommended cities list that will dynamically update based on what the user is typing.
   I felt like this was a good compromise for the first issue.

3. I chose django for this project because I'm most familiar with this framework.

4. I added the .env file for ease of access. Normally I wouldn't upload it to GitHub. 

install instructions:

1. Install a virtual environment 
   
   a. To create the virutal environment, enter this line of text into the command line:
        
        windows:
        $ py -m venv weather_venv

        Unix/MacOS:
        $ python -m venv weather_venv 

   b. To activate the virtual environment, enter this line of text into the command line:
        
        windows:
        $ weather_venv\Scripts\activate.bat 

        Unix/MacOS:
        $ source weather_venv/bin/activate 

   c. To install all of the requirements, enter this line of text into the command line:
        
        $ pip install -r requirements.txt

2. Running the server and accessing the website:
   
   a. To run the server, enter this line of text into the command line:
      
        $ python manage.py runserver
   
   b. the output should look like this: 
      
      System check identified no issues (0 silenced).
      March 06, 2023 - 23:46:15
      Django version 4.1.7, using settings 'weather_project.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CONTROL-C.
    
   c. click on the underlined URL and it should take you to the website. 
 