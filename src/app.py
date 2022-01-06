import pyautogui as robots
import time 
# robots.displayMousePosition()

list_song = ['flaca','hoy te toca ser feliz']
brave_position = 56,164
direct = 2401,45
find = 2541,127
song = 2850,236 
exit_n =3809,26 

def abrir(pos,click=1):
    robots.moveTo(pos)
    robots.click(clicks=click)
    
def maximize():
    time.sleep(2)
    robots.hotkey('alt','space')
    time.sleep(0.5)
    robots.typewrite('x')
    
def search_nave(position):
    time.sleep(4)
    abrir(position)
    robots.typewrite('youtube.com')
    time.sleep(2)
    robots.hotkey('enter')
    time.sleep(5)
    
def search_song(position,song):
    abrir(position)
    robots.hotkey('ctrl','a')
    robots.typewrite(song)
    time.sleep(2)
    robots.hotkey('enter')
    time.sleep(5)

def select_song(position):
    abrir(position) 
    time.sleep(15)

def close(position):
    abrir(position)
    
def main():
    #abrir navegador
    time.sleep(2)
    abrir(brave_position,click=2)
    
# maximizar pantalla
    #maximize()
    
    # ubicarse en el buscardor
    search_nave(direct)
    
    # ubicarse buscador youtube
    search_song(find,list_song[0])
    
    # seleccionar cancion
    select_song(song)
    
    search_song(find,list_song[1])
    
    select_song(song)
    
    close(exit_n)
    
    
if __name__ == '__main__':
    main()