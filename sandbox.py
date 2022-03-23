import tkinter as tk

BREAKING_NEWS_LENGTH = 150
NO_OF_SPACES = 4
SCROLL_START = 0

scroll_text_length = BREAKING_NEWS_LENGTH + NO_OF_SPACES

root = tk.Tk()
deli = 100           # milliseconds of delay per character
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=10 )


def shif():
    global BREAKING_NEWS_LENGTH, SCROLL_START
    char_count = len(shif.msg)
    if char_count <= BREAKING_NEWS_LENGTH:
        for _ in range(char_count, BREAKING_NEWS_LENGTH):
            shif.msg += " "
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)


shif.msg = 'Russia and Ukraine agree to temporary ceasefire to let civilians leave two Ukraine cities'
# If news headline is longer than BREAKING_NEWS_LENGTH, add ... at the end
breaking_news_end_index = BREAKING_NEWS_LENGTH - 1
if len(shif.msg) > BREAKING_NEWS_LENGTH:
    shif.msg = shif.msg[:breaking_news_end_index - 3]
    shif.msg += "..."
else:
    shif.msg = shif.msg[:breaking_news_end_index]

for _ in range(NO_OF_SPACES):
    shif.msg += " "  # Adding 4 spaces to show start and end of loop

shif()
labl.pack()
root.mainloop()