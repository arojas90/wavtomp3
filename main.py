import sys
from pydub import AudioSegment as au


sound = au.from_wav(sys.argv[1])
sound.export(sys.argv[2], format="mp3")



