from microbit import *
import audio
import music

def welcome():
    display.scroll('Hello Chloe!')
    display.show(Image.HEART)
    sleep(1000)
    
def work():
    while True:
        display.clear()
        for y in range(0, 5):
            for x in range(0, 5):
                display.set_pixel(x, y, 9)
                if button_a.is_pressed() or button_b.is_pressed():
                    return  # Exit the work function
        for y in range(0, 5):
            sleep(60000)
            for x in range(0, 5):
                display.set_pixel(x,y,0)
                if button_a.was_pressed() or button_b.was_pressed():
                    return  # Exit the work function
                sleep(60000)
        audio.play(Sound.HAPPY)
        
        display.scroll('Take a Break')
        
        for y in range(0, 5):
            for x in range(0, 5):
                display.set_pixel(x, y, 9)
                sleep(12000)
                if button_a.is_pressed() or button_b.is_pressed():
                    return  # Exit the work function
            
            if button_a.is_pressed() or button_b.is_pressed():
                return  # Exit the work function
        audio.play(Sound.TWINKLE)
        

def meeting():
    while True:
        display.scroll('Meeting time!')
        display.show(Image.HEART)
        sleep(2000)
        if button_a.was_pressed() or button_b.was_pressed():
                    return  # Exit the work function
    
display.clear()
music.play(music.NYAN)

while True:
    if button_a.was_pressed():
        work()
    elif button_b.was_pressed():
        meeting()
        
    else:
        welcome()
    sleep(100)
        
    