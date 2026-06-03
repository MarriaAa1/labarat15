from tkinter import *
import requests

root = Tk()

def get_places():
    city = cityField.get()
    url = f"https://ru.wikipedia.org/w/api.php?action=opensearch&search=достопримечательности {city}&limit=3&format=json"
    result = requests.get(url)
    data = result.json()

    places = data.get('results', [])
    if len(places) >= 2:
        place1 = places[0]
        place2 = places[1]
        text = f"{place1['title']}\n{place1['description']}\n\n {place2['title']}\n{place2['description']}"
    else:
        text = "Не найдено. Введите: msk, spb, kzn, nsk"

    fact_label['text'] = text

    
root = Tk()
root['bg'] = '#fafafa'
root.title('Достопримечательности')
root.geometry('400x300')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.45, relwidth=0.7, relheight=0.3)

cityField = Entry(frame_top, bg='white', font=20)
cityField.pack()

btn = Button(frame_top,
             text='Найти',
             command=get_places)
btn.pack()

info = Label(frame_bottom,
             text='Введите город',
             bg='#ffb700')
info.pack()

root.mainloop()