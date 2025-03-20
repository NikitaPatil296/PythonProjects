##The application has the following features:

1. Fetch weather by city: Users can input a city name to get weather updates.
2. Fetch weather for current location: The application uses IP geolocation to determine the user's current   city and fetch weather updates for that city.
3. Professional layout using HTML and CSS: A modern web interface with Bootstrap for responsiveness and aesthetics.


##WeatherApp
├── app.py                # Your main Flask application
├── static/               # Your static files (CSS, JS, images)
├── templates/            # Your HTML templates
├── requirements.txt      # Optional - list of dependencies
└── WeatherApp.spec       # PyInstaller spec file (if exists)

1. Install PyInstaller
First, you need to install PyInstaller in your environment. 
This tool will help you bundle the application into a single executable.
Run the following command to install it:

>pip install pyinstaller


2. Use PyInstaller to Create the Executable

>pyinstaller --onefile --add-data "templates;templates" WeatherApp.py


##Explanation:
--onefile: Packages everything into a single .exe file.
--add-data "templates;templates": Includes the templates folder in the executable.
--add-data "static;static": Includes the static folder if you have any static assets like CSS or JavaScript files.
--WeatherApp.py: The entry script for your Flask app.


3. Locate the Executable
After running the command, PyInstaller will generate the executable in the dist folder inside your project directory. 

dist/
    app.exe