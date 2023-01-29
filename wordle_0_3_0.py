from tkinter import *
import json
import requests
import sys
import time

print("Loading Word List...")

try:
    response_API = requests.get("https://random-word-api.herokuapp.com/word?number=3")

    data = response_API.text

    data2 = list(data.split('"'))

    x = 0
    while True:
        if(data2[x] == '[') or (data2[x] == ',') or (data2[x] == ']'):
           data2.remove(data2[x])
        else:
            x += 1
except IndexError:
    print("Loading...SUCCESS!")
except Exception as e:
    print()
    print(f"LOADING ENCOUNTERED A FATAL ERROR: {e}")
    time.sleep(0.75)
    print()
    print()
    sys.exit("Please check your internet connection and try again. Thank you!")

numCorrect = 0
checkNumber = 0
points = 0
xx = 0

def checkWord():
    global numCorrect
    global data2
    global checkNumber
    global points
    global xx

    wordCheck = len(list(data2[0]))
    Word = wordEntry.get()

    splitWord = len(list(Word))

    print(data2[0])#REMOVE THIS BEFORE PUSH!!!!
    print(Word)

    if(points == 3):
        if(xx == 0):
            try:
                none_hints_entry.place_forget()
                x = 0
                
                response_API = requests.get(url="https://dictionaryapi.com/api/v3/references/collegiate/json/" + data2[0] + "?key=0893830c-c59b-4236-822a-d7b8af9696a6")
                
                def_data = response_API.json()

                shortDef = list(def_data[0]['shortdef'])
            except Exception:
                shortDefLabel = Entry(
                    ws,
                    bg='#0f4b6e',
                    fg='white',
                    font=('Arial',14),
                    justify='center',
                    width=40
                    )
                shortDefLabel.pack()
                shortDefLabel.insert(0,f'Unusual word, no definition available! (-8 guesses)')
                xx = 1
                points -= 8

            try:
                while True:
                    if(shortDef[x] == '[') or (shortDef[x] == ']'):
                       shortDef.remove(shortDef[x])
                    else:
                        x += 1
            except IndexError:
                shortDefLabel = Entry(
                    ws,
                    bg='#0f4b6e',
                    fg='white',
                    font=('Arial',14),
                    justify='center',
                    width=40
                    )
                shortDefLabel.pack()
                shortDefLabel.insert(0,f'Definition: {shortDef}')
                        
            ##<><><><><>##

        
    if(numCorrect == 0):
        if(checkNumber == 0) and (data2[0] != Word):
            if(splitWord > wordCheck):
                disp_tf.insert(0,f'{Word}: TOO MANY LETTERS!                                              ')
                points += 1
            elif(splitWord < wordCheck):
                disp_tf.insert(0,f'{Word}: NOT ENOUGH LETTERS!                                                   ')
                points += 1
            elif(splitWord == wordCheck):
                none_hints_entry.place_forget()
                disp_tf.insert(0,f'{Word}: You Found the Correct Number!                                           ')
                disp_numbers = Entry(
                    ws,
                    bg='#0f4b6e',
                    fg='white',
                    width=38,
                    font=('Arial', 15),
                    justify='center'
                    )
                disp_numbers.pack()
                disp_numbers.insert(0,f'   {splitWord} LETTERS IN FINAL ANSWER!')
                checkNumber = 1
                points += 1
            
            else:
                disp_tf.insert(0,f'Unknown error encountered, goodbye!')
                time.sleep(3)
                sys.exit("Unknown Error was Encountered, please contact the coders of this game with a screenshot of this screen! Sorry for the inconvenience!")

        elif(data2[0] == Word):
            disp_tf.insert(0,f'{Word} is correct!! Good job!                                              ')
            
        else:
            disp_tf.insert(0,'                                                                              ')
            disp_tf.insert(0,f'{Word} is incorrect!                          ')
            points += 1

        guess_disp.insert(0,f'{points} GUESSES                                           ')
        

ws = Tk()
ws.title("Wordable")
ws.geometry('500x500')
ws.config(bg='#0f4b6e')

blank_label = Label(
    ws,
    bg='#0f4b6e',
    text="Letter List"
    )

disp_let = Entry(
    ws,
    bg='#0f4b6e',
    fg='black',
    font=('Arial', 12),
    justify='center',
    width=50
    )

blank_label.pack()
disp_let.pack()

wordEntry = Entry(ws)

wordEntry.pack()

confirm_button = Button(
    ws,
    text='Check the Word',
    relief=SOLID,
    command=checkWord,
    )

disp_tf = Entry(
    ws,
    bg='#0f4b6e',
    fg='white',
    width=38,
    font=('Arial', 14),
    justify='center'
    )


point_label = Label(
    ws,
    bg='#0f4b6e',
    fg='white',
    text='GUESSES',
    font=('Arial', 25)
    )



confirm_button.pack()

disp_tf.pack(pady=5)

Label(bg='#0f4b6e').pack()
Label(bg='#0f4b6e').pack()

point_label.pack()

guess_disp = Entry(
    ws,
    bg='#0f4b6e',
    fg='white',
    font=('Arial',25),
    justify='center'
    )

guess_disp.pack()

hint_label = Label(
    ws,
    bg='#0f4b6e',
    fg='red',
    text='HINTS',
    font=('Arial', 18),
    justify='center'
    )

Label(bg='#0f4b6e').pack()

hint_label.pack()

none_hints_entry = Label(
    ws,
    bg='#0f4b6e',
    text='No Hints Yet!',
    font=('Arial', 15),
    justify='center'
    )

none_hints_entry.place(relx=0.38, rely=0.6)

letterList = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ', 'z ']

disp_let.insert(0,''.join(letterList))

ws.mainloop()






