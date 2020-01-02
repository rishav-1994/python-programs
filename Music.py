Notes=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
#for Major scale
n=input("Enter root note of the scale: ")
index=Notes.index(n)
for i in range(1,9):
    if index>11:
        index-=12
    if i==3 or i==7:
        print(Notes[index],end=" ")
        index+=1
    else:
        print(Notes[index],end=" ")
        index+=2