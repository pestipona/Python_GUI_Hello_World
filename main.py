# import widgets from quizero library
from guizero import App, Text

# create a container widget
app = App(title="Hello World")

# add a text widget
message = Text(app, text="Welcome to the app")

# display the gui app
app.display()