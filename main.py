import os
os.add_dll_directory('C:/Program Files/VideoLAN/VLC')
import vlc
import speech_recognition as sr
from google import google
import pyttsx3


answers = {'name': 'You should already know that, because you called me just now',
           'channelName': 'your channel name is Developers Hub',
           'yourself': 'I am a voice assistent designed by Developers Hub',
           'message': 'Please subscribe to our channel, like this video for me, see you again with lots of fun'}

# Initialize the recognizer
r = sr.Recognizer()
r1 = sr.Recognizer()

# Function to convert text to
# Speech


def googleSearch(searchTerm):

    # if 'calculate' in searchTerm:
    #     calTerm = searchTerm.split("calculate")
    #     result = google.calculate(calTerm[-1])

    #     return result.value+result.unit

    num_page = 1
    search_results = google.search(searchTerm, num_page)
    # for result in search_results:
    #     print(result.description)

    return search_results[0].description


def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def solutionFinder(incomingText):
    answer = ''
    if 'music' in incomingText:
        if 'play music' in incomingText:
            print("2")
            s.playSong()

        if 'next music' in incomingText:
            s.nextSong()

        if 'previous music' in incomingText:
            s.previousSong()

        if 'stop music' in incomingText:
            print("3")
            s.stopSong()

    else:
        if 'your name' in incomingText:
            answer = answers['name']

        if 'channel name' in incomingText:
            answer = answers['channelName']

        if 'yourself' in incomingText:
            answer = answers['yourself']

        if 'message' in incomingText:
            answer = answers['message']

        if 'search for' in incomingText:
            searchTerm = incomingText.split('for')
            answer = googleSearch(searchTerm[-1])

        SpeakText(answer)


class SongOperation():

    def playSong(self):
        # os.startfile('C:/Users/My PC/Downloads/Jim Yosef x ROY KNOX - Sun Goes Down [NCS Release].mp3')
        # subprocess.Popen(['C:/Program Files/VideoLAN/VLC/vlc.exe', 'lost.mp3'])
        # self.p = vlc.MediaPlayer(
        #     "C:/Users/My PC/Downloads/Jim Yosef x ROY KNOX - Sun Goes Down [NCS Release].mp3")
        a1 = vlc.MediaList([vlc.Media("C:/Users/My PC/Downloads/Jim Yosef x ROY KNOX - Sun Goes Down [NCS Release].mp3"),
                            vlc.Media("C:/Users/My PC/Downloads/Diamond Eyes - Everything _NCS Release_.mp3")])
        self.p = vlc.MediaListPlayer()
        self.p.set_media_list(a1)
        self.p.play()

    def stopSong(self):
        if self.p.is_playing():
            # os.system("TASKKILL /F /IM vlc.exe")
            self.p.stop()

    def nextSong(self):
        if self.p.is_playing():
            # os.system("TASKKILL /F /IM vlc.exe")
            self.p.next()

    def previousSong(self):
        if self.p.is_playing():
            # os.system("TASKKILL /F /IM vlc.exe")
            self.p.previous()


# Loop infinitely for user to
# speak
s = SongOperation()

while(1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            print("Call me jessie")
            audio2 = r.listen(source2, phrase_time_limit=4)

            # Using ggogle to recognize audio
            MyText = ''
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)

            if 'hey jessie' in MyText:
                SpeakText('Tell me')
                r1.adjust_for_ambient_noise(source2, duration=0.2)
                print('Listening....')
                audio3 = r1.listen(source2, phrase_time_limit=4)
                # Using ggogle to recognize audio
                MyNewText = ''
                MyNewText = r1.recognize_google(audio3)
                MyNewText = MyNewText.lower()
                print("you said "+MyNewText)
                solutionFinder(MyNewText)

            # SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        pass

    except sr.WaitTimeoutError:
        pass
