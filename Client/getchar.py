import keyboard

def inputNoEnter():
    keys = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0",".","-","_","@","!","?","(",")","[","]","{","}","<",">","/","\\","|","=","+","*","&",",",";","´","`","^","¨","~","$","#","%","'","\"",":"]
    key = 0
    i = 0
    text = ""
    while key != "enter":
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            for k in keys:
                if key == k:
                    text += key
                    i += 1
            if key == "backspace":
                i-=2 if i > 0 else 0
                text = text[:i]
            if key == "space":
                i-=1 if i > 0 else 0
                text = text[:i] + " "
                i+=1
            if key == "enter":
                text = ""
                i = 0
                return(text)
