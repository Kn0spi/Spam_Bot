import pyautogui, time
print("A simple text spam bot that types a massage and presses enter")
print("word mode =w copy and paste mode =c self enter mode =t")
mode = input("word or copy and paste mode? ")

def modet():
    text = input("Entere a text to spam: ")
    num = int(input("Enter a num:"))
    time.sleep(5)
    for num in range(num):
        pyautogui.typewrite(text)
        pyautogui.press("enter")

def modec():
    num = int(input("Enter a num:"))
    time.sleep(5)
    f = open("copy_and_paste.txt")
    fa = f.read()
    for num in range(num):
        pyautogui.typewrite(fa)
        pyautogui.press("enter")

def modep():
    time.sleep(5)
    f = open("word.txt")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")    

if mode == "c":
   modec()
elif mode == "w":
     modep()
elif mode == "t":
    modet()     
else:
    print("Only type c or w")   
 







  










 

    








  









 
 

    








  









