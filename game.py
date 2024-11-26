import Items
import Rooms
import art
import random
from pygame.mixer import init,music,quit
def game():
    init()
    clues=[".- .-.. .-- .- -.-- ... .-.. --- --- -.- .- .-. --- ..- -. -..","..- ... . .-. --- --- -- ..-. .. -. -.. . .-. - --- -.- -. --- .-- .. -. .-- .... .. -.-. .... .-. --- --- -- -.-- --- ..- .-. .. -.","- --- -.- -. --- .-- .- -... --- ..- - -.- . -.-- -... .. -. -.. .. -. --. -.-. .-.. .. -.-. -.- ...."]
    rooms=Rooms.rooms_def()
    treasure=rooms[2][0] 
    crn=rooms[0]
    key=1
    lives=3
    dtrn=rooms[1]
    map_room=[rooms[2][3]]
    if treasure%2==0:
        clues.append("- .-. . .- ... ..- .-. . .. ... .. -. . ...- . -. -. ..- -- -... . .-. . -.. .-. --- --- --")
    else :
        clues.append("- .-. . .- ... ..- .-. . .. ... .. -. --- -.. -.. -. ..- -- -... . .-. . -.. .-. --- --- --")
    encode={0:' -----',1:'.----',2: '..---',3: '...--',4: '....-',5: '.....',6: '-....',7: '--...'}
    death=rooms[3][1] 
    death_code=encode[death]
    death_clue="- .... . .-. . - --- - .- .-.. "+death_code+" -. ..- -- -... . .-. --- ..-. .-. --- --- -- ... .-- .... .. -.-. .... -.-. --- -. - .- .. -. ... -.. . .- - .... - .-. .- .--."
    clues.append(death_clue)
    random.shuffle(clues)
    clues_toBe_shown=[]
    map_item=False
    while len(clues_toBe_shown)!=len(crn):
        clues_toBe_shown.append(clues.pop())
    random.shuffle(clues_toBe_shown)
    decoder_roomNo=[rooms[2][1]]
    room_number_finder_roomNo=[rooms[2][2]]
    game=True
    game_won=True
    key=1
    decoder_item,room_teller=False,False
    ghost_death_roomNOs=rooms[4]
    extra_life_roomNo=[rooms[5]]
    friendly_ghost_roomNo=rooms[6]
    while game :
        if lives ==1:
            music.load("heartbeat-79303.mp3")
            music.play()
        key_pressed=True
        while key_pressed:
            rooms_list=Rooms.rooms(key)
            key=rooms_list[0]
            look_around=rooms_list[1]
            map_open=rooms_list[2]
            key_pressed=False
        # w-up a-left s-down d-right l-look around 
        if look_around:
            if key==treasure:
                music.load("insane-funny-scream-199845.mp3")
                music.play()
                print(art.game_won)
                game=False
            elif key in decoder_roomNo:
                print("You found a decoder")
                decoder_item=True
                decoder_roomNo.pop()
            elif key in map_room:
                music.load("insane-funny-scream-199845.mp3")
                music.play()
                print("You found a map\nPress 'm' to open any time ")
                map_item=True
                map_room.pop()
            elif key in room_number_finder_roomNo:
                print("You found a room number finder")
                room_teller=True
                room_number_finder_roomNo.pop()
            elif key in ghost_death_roomNOs:
                music.load("male-scream-in-fear-123079.mp3")
                music.play()
                print("You have encountered an ghost\n")
                print("You lost one life")
                lives-=1
            elif key in extra_life_roomNo:
                music.load("insane-funny-scream-199845.mp3")
                music.play()
                print("You found an extra life \nYou life got added by one\n")
                extra_life_roomNo.pop()
                lives+=1
            elif key in friendly_ghost_roomNo :
                if treasure >=2 and treasure<=10:
                    print("treasure is in between room numbers 2 to 10 ")
                elif treasure >=11 and treasure<=19:
                    print("treasure is in between room numbers 11 to 19 ")
                elif treasure >=28 and treasure<=28:
                    print("treasure is in between room numbers 20 to 28 ")
            elif key in crn :
                if decoder_item:
                    code=clues_toBe_shown.pop()
                    code_list=code.split(" ")
                    print(code)
                    decoded_data=Items.decoder(code_list)
                    print(f"{code}\nSince you have decoder the decoded data is \n{decoded_data}")
                    crn.remove(key)
                else:
                    print(random.choice(clues_toBe_shown))
        if map_item and map_open:
            m=Items.map(key)
            print(m)
        if room_teller:
            music.load("insane-funny-scream-199845.mp3")
            music.play()
            Items.room_teller(key)
        if key in dtrn:
            music.load("male-extreme-scream-123078.mp3")
            music.play()
            print("You entered into a death trap contained room\n")
            lives=0
        if lives==0:
            print(art.game_lost)
            game=False
            game_won=False
    quit()
    return game_won 
if __name__=="__main__":
    k=game()
    print(k)