from pygame.mixer import init,music,quit 
import gtts as ai
import os
import threading 
import time

def text(aitext):
    if os.path.exists("Story.mp3"):
        time.sleep(1)
        try:
            os.remove("Story.mp3")
        except PermissionError:
            print("Could not remove the previous audio file. It might still be in use.")
            return
    language = "en"
    voice = ai.gTTS(text=aitext, lang=language, slow=False)
    voice.save("Story.mp3")
    print(aitext)
    try:
        init()
        music.load("Story.mp3")
        music.play()
    except Exception as e:
        print(f"Error playing audio: {e}")

def story(name, gender):
    with open("Story.txt", "r", encoding="utf-8") as s:
        story_text = s.read()
    
    tik = "her" if gender.lower() in ["girl", "woman", "women"] else "his"
    story_text = story_text.replace("Name", name).replace("gender", gender).replace("tik", tik)
    
    with open("Story2.txt", "w") as s1:
        s1.write(story_text)
    
    t1 = threading.Thread(target=text, args=(story_text,))
    t1.start()
    
    time.sleep(95)
    quit()
if __name__ == "__main__":
    name = input("Enter your name:\n")
    gender = input("Enter your gender like boy if ur male kid or women if your grown female\n")
    story(name, gender)
