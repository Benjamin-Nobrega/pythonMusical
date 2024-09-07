import librosa

#don't know how to diferentiate beetween the same instrument being played more than one at once

#still don't know if i'll get all the instruments sheet or only one for now
def getKeyboard(music):
    ...

def getInstruments(music):
    ...

def buildMusicalSheet(instrument_list):
    ...
    
def buildMidi(instrument_list):
    ...

#going to merge all the midi files so there will be only the instrumental
def mergeMidi(instruments_list):
    ...

def main():
    
    y, sr = librosa.load(r"./60 BPM - Metronome.mp3")
    
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(beat_times)
    
if __name__ == "__main__":
    main()