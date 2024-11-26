from story import story
import game
import time 
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60 
    return "%d:%02d:%02d" % (hour, minutes, seconds)
def main_game():
    game_time_start=time.time()
    print("Use Head phones for better experience")
    name=input("Enter your name:\n")
    gender=input("Enter your gender like boy if ur male kid or women if your grown female\n")
    g=True
    while g:
        game_choice=int(input("Enter\n1:For story\n2:To know about game\n3:To start game\n4:To quit\n"))
        g=True
        match game_choice :
            case 1:
                print("Loading.....")
                story(name,gender)                 
            case 2:
                with open("game_details.txt", 'r') as f:
                    contents = f.read()
                    print(contents)
                f.close()
            case 3 :    
                #g=False
                print("Enter\nw:To move up\na:To move left\ns:To move down\nd:To move right\nl:To look around\nh:For help\n")
                easter_egg=game.game()
                if easter_egg :
                    print("You found gold successfully now ypu have a choice you can either go with all the gold or since you made a deal go back to him what you think\n")
                    print("press r to run will gold or press b for going back\n")
                    easter_egg_choice=input().lower()
                    if easter_egg_choice=='r':
                        print("You ran away with all the gold and people labeled you as greedy and not trustworthy\n")
                    elif easter_egg_choice=='b':
                        print("You went back with gold and as promised , old man gave you 60% of gold and people labeled you as courageous and trustworthy "+gender+"\n")
                    else :
                        raise TypeError("Wrong Input")
                game_time_end=time.time()
                print(f"Thank you for playing and you played game for {convert(game_time_end-game_time_start)}\nYou are going back to the menu\n")        
            case 4:
                exit
                g=False
            case _ :
                raise TypeError("Wrong Input")
if __name__=="__main__":
    main_game()