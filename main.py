from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
try:
  french=pandas.read_csv("./data/words_to_learn.csv")
except:
  original_data = pandas.read_csv("./data/french_words.csv")
  to_learn=original_data.to_dict(orient="records")
else:  
  to_learn=french.to_dict(orient="records")




def change_cards():
  global current_card,flip_timer
  window.after_cancel(flip_timer)
  current_card=random.choice(to_learn)
  canvas.itemconfig(canvas_img,image=card_front)
  canvas.itemconfig(lang,text="French",fill="black")
  canvas.itemconfig(words,text=current_card['French'],fill="black")
  
  flip_timer=window.after(3000,func=flip_card)

def flip_card():
  canvas.itemconfig(canvas_img,image=card_back)
  canvas.itemconfig(lang,text="English",fill="white")
  canvas.itemconfig(words,text=current_card["English"],fill="white")

def known_words():
  to_learn.remove(current_card) 
  data = pandas.DataFrame(to_learn)
  data.to_csv("data/words_to_learn.csv",index=False)
  change_cards()
  print(f"words remaining:{len(to_learn)}")

  




window=Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)


canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file=".\images\card_front.png")
card_back=PhotoImage(file=".\images\card_back.png")
canvas_img=canvas.create_image(400,263,image=card_front)




lang=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
words=canvas.create_text(400,263,text="word",font=("Arial",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)



right_img_url=PhotoImage(file=".\images\\right.png")
right_btn=Button(image=right_img_url,highlightthickness=0,command=known_words)
right_btn.grid(row=1,column=0)

wrong_img_url=PhotoImage(file=".\images\wrong.png") 
wrong_btn=Button(image=wrong_img_url,highlightthickness=0,command=change_cards)
wrong_btn.grid(row=1,column=1)



change_cards()

window.mainloop()
