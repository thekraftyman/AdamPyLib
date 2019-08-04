# AdamPyLib.py
# By: Adam Kraft
# A library of functions and classes that I find usefull but I won't remember lol
'''
Welcome to AdamPyLib, a package of functions that make life programming with
python a little easier!
Currently built for Python version 3.7.0
To use, import like:
from AdamPyLib import * (or just one single module)
'''
# -----------------------------------------------------------------------------
#Import Packages (Make sure you have all of them!)
import sys
import os
import os.path
from datetime import datetime
if dist == 'Windows':
    import win32com.client
from playsound import playsound
import PyPDF2
import vlc

# -----------------------------------------------------------------------------
# ------------------------------ Functions! -----------------------------------
# -----------------------------------------------------------------------------
# Functions go here
def uprint(st):
    '''prints a string that can be overwritten by the same command
    >>>uprint('test')
    test
    >>>for i in range(3):
            uprint('{}>'.format('='*i))
    >
    ... (through time)
    =>
    ... (through time)
    =>>
    '''
    print(f'\r{st}',end='')
    sys.stdout.flush()

def speak(text):
    '''literally says a passed text
    >>>speak('hello')
    >>>
    (you will hear the computer say 'hello')
    '''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    speaker.Speak(text)

def play_song(path):
    '''plays a mp3 at the given path
    >>>play_song('C:\Users\Adam\Music\FU.mp3')
    >>>
    (you will hear the song FU.mp3 play)
    '''
    playsound(path)

    def play_video(video_path):
        '''plays a video with the VLC package at the given path'''
        player = vlc.MediaPlayer(video_path)
        player.play()
        player.set_fullscreen(True)

def merge_pdfs(folder_path,out_name):
    '''merges an entire folder of PDFs into a single pdf'''
    os.chdir(folder_path)
    pdf2merge = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdf2merge.append(filename)
    pdfWriter = PyPDF2.PdfFileWriter()
    #loop through all PDFs
    for filename in pdf2merge:
        #rb for read binary
        pdfFileObj = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        #Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    #save PDF to file, wb for write binary
    pdfOutput = open(out_name+'.pdf', 'wb')
    #Outputting the PDF
    pdfWriter.write(pdfOutput)
    #Closing the PDF writer
    pdfOutput.close()

# -----------------------------------------------------------------------------
# ------------------------------ Classes! -------------------------------------
# -----------------------------------------------------------------------------
# Classes go here

class Log:
    '''Log class that can be written to and saves itself'''

    # Define Global Variables -------------------------------------------------
    divider = '-----------------------------------------------------------'
    # -------------------------------------------------------------------------

    def __init__(self,path,header):
        '''attempts to open a log and creates one if none exists'''
        if os.path.exists(path):
            self.lg = open(path, mode='a')
        else:
            self.lg = open(path, mode='w', encoding='utf-8')
            self.lg.write(header+'\n')
            self.lg.write(divider+'\n')
        self.path = path
        self.header = header
        self.status = 'OFF'

    def _current_time(self):
        '''returns current time in hour:minute form'''
        return datetime.now().strftime('%H:%M')

    def _day_stamp(self):
        '''returns current day in M/D/Y form'''
        return datetime.now().strftime('%m/%d/%y')

    def _update(self):
        '''saves the document and re-opens it in append mode'''
        self.lg.close()
        self.lg = open(self.path, mode='a')

    def write(self, string):
        '''writes a string to the log and updates it'''
        self.lg.write(string+divider+'\n')
        self._update()

    def iter_sections(self):
        with open(self.path, 'r') as infile:
            data = infile.read().split(divider)

    def __iter__(self):
        for section in self.iter_sections():
            yield section

    def __repr__(self):
        return 'Log("{}","{}")'.format(self.path,self.header)

    def __str__(self):
        print('Log object with header: {}'.format(self.header))

    def __add__(self,other):
        self.lg.write(other)
