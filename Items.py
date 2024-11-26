def decoder(code):
    decode_dict={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', ' -----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}
    decoded_data=""
    for i in code:
        decoded_data+=decode_dict[i]
    return decoded_data
def room_teller(key):
    print(f"Your in {key} room")
def map(key):
    row1,row2,row3,map=[],[],[],""
    map_rooms={2:"2 ",3:"3 ",4:"4 ",5:"5 ",6:"6 ",7:"7 ", 8:"8 ", 9:"9 ", 10:"10 ", 11:"11 ", 12:"12 ",13:"13 ",14:"14 ", 15:"15 ", 16:"16 ", 17:"17 ", 18:"18 ", 19:"19 ", 20:" 20 ", 21:"21 ", 22:"22 ", 23:"23 ", 24:"24 ", 25:"25 ", 26:"26 ", 27:"27 ",28:"28 "}
    map_key={2:'2️⃣',3:'3️⃣',4:'4️⃣', 5:'5️⃣',6:'6️⃣',7:'7️⃣', 8:'8️⃣', 9:'9️⃣', 10:'🔟', 11:'1️⃣ 1️⃣ ', 12:'1️⃣2️⃣',13:'1️⃣ 3️⃣',14:'1️⃣ 4️⃣', 15:'1️⃣ 5️⃣', 16:'1️⃣ 6️⃣', 17:'1️⃣ 7️⃣', 18:'1️⃣ 8️⃣', 19:'1️⃣ 9️⃣', 20:'2️⃣ 0️⃣',21:'2️⃣ 1️⃣',22:'2️⃣ 1️⃣',23:'2️⃣ 3️⃣', 24:'2️⃣ 4️⃣', 25:'2️⃣ 5️⃣', 26:'2️⃣ 6️⃣', 27:'2️⃣ 7️⃣',28:'2️⃣ 8️⃣'}
    for i in range(28,1,-1):
        if i<=28 and i>=20:
            row1.append(str(i))
        elif i<=19 and i>=11:
            row2.append(str(i))
        elif i>=2 and i<=10:
            row3.append(str(i))
    row1.reverse(),row2.reverse(),row3.reverse()
    if key<=28 and key>=20:
        row1[row1.index(str(key))]=map_key[key]
    elif key<=19 and key>=11:
        row2[row2.index(str(key))]=map_key[key]
    elif key>=2 and key<=10:
        row3[row3.index(str(key))]=map_key[key]
    for i in row1:
        map+=i+" "
    map+='\n'
    for i in row2:
        map+=i+" "
    map+='\n'
    for i in row3:
        map+=i+"  "
    return map
if __name__=='__main__':
    code=input("Enter data you want to convert\n")
    code_list=code.split(" ")
    print(decoder(code_list))
    m=map(11)
    print(m)
    