import keyboard

def inputNoEnter(msg):
    keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ñ', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-', '_', '@', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '=', '+', '*', '&', ',', ';', '´', '`', '^', '¨', '~', '$', '#', '%', "'", '"', ':', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    i = len(msg)
    text = msg
    event = keyboard.read_event()
    if event.event_type == "down":
        key = event.name
        for k in keys:
            if key == k:
                text += key
                return text,False,False,True
        if key == "backspace":
            i-=1 if i > 0 else 0
            text = text[:i]
            return text,False,True,True
        if key == "space":
            text += " "
            return text,False,False,True
        if key == "enter":
            return text,True,False,True
        return text,False,False,False
    else:
        return text,False,False,False