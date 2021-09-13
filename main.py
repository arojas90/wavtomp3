import sys
from pydub import AudioSegment as au
import glob


#sound = au.from_wav(sys.argv[1])
#sound.export(sys.argv[2], format="mp3")

#print(glob.glob("./wav/*.WAV"))

for file in glob.glob("./wav/*.wav"):
    sound = au.from_wav(file)
    sound.export(file.replace('./wav', './mp3').replace('.wav', '.mp3'), format="mp3")



