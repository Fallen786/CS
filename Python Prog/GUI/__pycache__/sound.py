import multiprocessing
from playsound import playsound
playsound('C:\\Users\\USER\\Downloads\\Shovel.mp3')
p = multiprocessing.Process(target=playsound, args=("shovel.mp3",))
p.start()
input("press ENTER to stop playback")
p.terminate()