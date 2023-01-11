import requests
from tkinter import *
from PIL import Image, ImageTk

message = "Trykk på Donald for et Trump gullkorn..."

screen = Tk()
screen.title("Donald Says...")
screen.config(padx=50, pady=50)

def get_quote():
  global message
  try:
    response = requests.get(url="https://api.whatdoestrumpthink.com/api/v1/quotes/random/")
    response.raise_for_status()

    data = response.json()
  except:
    print("error")
  else:
    message = data['message']
    canvas.itemconfig(quote_text, text=message)

canvas = Canvas(width=300, height=414)
trump_image = Image.open('donald.png')
trump_image = trump_image.resize((200,200))
donald_image = ImageTk.PhotoImage(trump_image)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(150, 207, text=message, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# donald_img = PhotoImage(file=trump_image)
donald_button = Button(image=donald_image, highlightthickness=0, command=get_quote)
donald_button.grid(row=1, column=0)





screen.mainloop()