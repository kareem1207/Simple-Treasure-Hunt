import random 
from pygame.mixer import init,music,quit
def rooms(key=1):
    init()
    rooms={2:2,3: 3,4: 4, 5:5,6: 6,7: 7, 8:8, 9:9, 10:10, 11:11, 12:12,13: 13,14: 14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25, 26:26, 27:27,28:28}
    game=True
    while game:
        key_up = False
        key_down = False
        key_left = False
        key_right = False
        key_look_around = False
        look_around = False
        help = False
        key_map = False
        # key_quit = False
        map_open = False
        direction=input().lower()
        match direction:
            case 'w':
                key_up=True
            case 'a':
                key_left=True
            case 's':
                key_down=True
            case 'd':
                key_right=True
            case 'l':
                key_look_around=True
            case 'm':
                key_map=True
            case'h':
                help=True
            case _:
                print("Wrong input")
        if key_up:
            if key==1 or (key>=20 and key<=28):
                music.load("snippet-bass-drum-64374-94129.mp3")
                music.play()
                print("Not Possible")
            else :
                music.load("open-and-closed-door-156814.mp3")
                music.play()
                key+=9
            game=False
        elif key_right:
            if key== 10 or key==19 or key==28:
                music.load("snippet-bass-drum-64374-94129.mp3")
                music.play()
                print("Not Possible")
            else :
                music.load("open-and-closed-door-156814.mp3")
                music.play()
                # sleep(4)
                key+=1
            game=False
        elif key_down:
            if key >=1 and key<=10:
                music.load("snippet-bass-drum-64374-94129.mp3")
                music.play()
                print("Not Possible")
            else :
                music.load("open-and-closed-door-156814.mp3")
                music.play()
                # sleep(4)
                key-=9
            game=False
        elif key_left:
            if key==11 or key==20 or key==1:
                music.load("snippet-bass-drum-64374-94129.mp3")
                music.play()
                print("Not Possible")
            else:
                music.load("open-and-closed-door-156814.mp3")
                music.play()
                # sleep(4)
                key-=1
            game=False
        elif key_look_around:
            look_around=True
            game=False
        elif key_map:
            map_open=True
            game=False
        elif help:
            #w-up a-left s-down d-right l-look around
            print("Enter\nw:To move up\na:To move left\ns:To move down\nd:To move right side\nl:To look around\nq:To quit\n")
        if key<1:
            raise ValueError("Value is too low ")
    # quit()
    return [key,look_around,map_open]
def rooms_def():
    clues=random.randint(1,5)
    death_traps=random.randint(0,7)
    total_rand=4+clues+death_traps
    rooms_items=[]
    extra_life=random.randint(0,1)
    c,d,t,i1,i2=0,0,0,0,0
    while len(rooms_items)!=total_rand:
        items=random.randint(6,28)
        if items not in rooms_items :
            rooms_items.append(items)
    random.shuffle(rooms_items)
    clues_roomNo,death_trap_roomNo,items_roomNo=[],[],[]
    while c!=clues:
        clues_roomNo.append(rooms_items.pop())
        c+=1
    while d!=death_traps:
        death_trap_roomNo.append(rooms_items.pop())
        d+=1  
    items_roomNo=rooms_items
    random.shuffle(items_roomNo)
    note=[clues,death_traps]
    treasure=items_roomNo[1]
    friendly_ghost_count=random.randint(0,1)
    ghost_death_count=random.randint(3,9)-friendly_ghost_count
    ghost_death_room,extra_life_roomNo,friendly_ghost_roomNo=[],[],[]
    i=0
    if treasure%2==0:
        while i != ghost_death_count:
            rand=random.randint(2,28)
            if rand%2!=0 and rand not in ghost_death_room and rand not in death_trap_roomNo and rand not in items_roomNo :
                ghost_death_room.append(rand)
                i+=1
    else :
        while i != ghost_death_count:
            rand=random.randint(2,28)
            if rand%2!=0 and rand not in ghost_death_room and rand not in death_trap_roomNo and rand not in items_roomNo  :
                ghost_death_room.append(rand)
                i+=1   
    rand=random.randint(2,28)
    if extra_life!=0 and rand not in ghost_death_room and rand not in death_trap_roomNo and rand not in items_roomNo :
        extra_life_roomNo.append(rand)
    rand=random.randint(2,28)
    if friendly_ghost_count!=0 and rand not in extra_life_roomNo and rand not in ghost_death_room and rand not in death_trap_roomNo and rand not in items_roomNo :
        friendly_ghost_roomNo.append(rand)
    return [clues_roomNo,death_trap_roomNo,items_roomNo,note,ghost_death_room,ghost_death_count,extra_life_roomNo,friendly_ghost_roomNo]
if __name__=="__main__":
    k=rooms(1)      