from random import shuffle
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
#prefs.hardware['audioLib'] = ['pyo']
from psychopy import visual, core, sound, event, gui, logging
import os
import numpy as np
from sys import argv
import pandas as pd

#from triggers import setParallelData
#setParallelData(0)
#### function to quit the experiment and save log file:
def quit_and_save():
    logfile.close()
    logging.flush()
    core.quit()
    
event.globalKeys.add(key='escape', func=quit_and_save, name='shutdown')

csid = ''
if len(argv)>1:
    csid = argv[1]

#### Collect participant identity:
border = np.random.choice([0, 1], size=1)
ID_box = gui.Dlg(title = 'Subject identity')
ID_box.addField('ID: ', csid)
ID_box.addField('Block Order (0/1): ', border[0])
sub_id = ID_box.show()
border = int(sub_id[1])
#create a window
win = visual.Window(fullscr=True, color='black')
fixationCross = visual.TextStim(win, text='+', color='white', height=0.2)
fixationCross.draw()
win.flip()
core.wait(2)

# set project directory:
my_path = os.path.abspath(os.path.dirname(__file__))
os.chdir(my_path)
print(os.getcwd())

df = pd.read_csv("Homophone_judgement_task_stimuli_Sheet1.csv")
col = 'white'
log_dir = 'logs'

shuffled = df.sample(frac=1).reset_index(drop=True)

yes = shuffled[shuffled["Homophones? (Y/N)"] == 'Y']
no = shuffled[shuffled["Homophones? (Y/N)"] == 'N']
listen_words_yes = yes[0:10]
listen_words_no = no[0:10]
listen_words = listen_words_yes.append(listen_words_no)
listen_words = listen_words.sample(frac=1).reset_index(drop=True)
listen_words1 = listen_words["Word 1"].values.tolist()
listen_words2 = listen_words["Word 2"].values.tolist()
listen_corrects = listen_words["Homophones? (Y/N)"].values.tolist()

imagine_words_yes = yes[11:20]
imagine_words_no = no[11:20]
imagine_words = imagine_words_yes.append(imagine_words_no)
imagine_words = imagine_words.sample(frac=1).reset_index(drop=True)
imagine_words1 = imagine_words["Word 1"].values.tolist()
imagine_words2 = imagine_words["Word 2"].values.tolist()
imagine_corrects = imagine_words["Homophones? (Y/N)"].values.tolist()

speaking_words_yes = yes[21:30]
speaking_words_no = no[21:30]
speaking_words = speaking_words_yes.append(speaking_words_no)
speaking_words = speaking_words.sample(frac=1).reset_index(drop=True)
speaking_words1 = speaking_words["Word 1"].values.tolist()
speaking_words2 = speaking_words["Word 2"].values.tolist()
speaking_corrects = speaking_words["Homophones? (Y/N)"].values.tolist()


instructions1 = visual.TextStim(win, text = "In the following block, you will see two words. \n\n"
                                            "Please listen to someone speaking the two words. \n\n"
                                           "If the words sound the same, press 1. \n\n "
                                           "If the words sound different, press 2. \n\n"
                                           "Press a key to begin.",
                                         wrapWidth=1.8, color = col)

instructions2 = visual.TextStim(win, text = "In the following block, you will see two words. \n\n"
                                            "Please try to imagine speaking the two words in your head. \n\n"
                                           "If the words sound the same, press 1. \n\n "
                                           "If the words sound different, press 2. \n\n"
                                           "Press a key to begin.",
                                         wrapWidth=1.8, color = col)
                                         
instructions3 = visual.TextStim(win, text = "In the following block, you will see two words. \n\n"
                                            "Please try to speak the two words out loud. \n\n"
                                           "If the words sound the same, press 1. \n\n "
                                           "If the words sound different, press 2. \n\n"
                                           "Press a key to begin.",
                                         wrapWidth=1.8, color = col)
                                         
instructions4 = visual.TextStim(win, text = "In the following block, you will see two words. \n\n"
                                            "Please listen to someone singing the two words. \n\n"
                                           "If the words sound the same, press 1. \n\n "
                                           "If the words sound different, press 2. \n\n"
                                           "Press a key to begin.",
                                         wrapWidth=1.8, color = col)

instructions5 = visual.TextStim(win, text = "In the following block, you will see two words. \n\n"
                                            "Please try to imagine singing the two words in your head. \n\n"
                                           "If the words sound the same, press 1. \n\n "
                                           "If the words sound different, press 2. \n\n"
                                           "Press a key to begin.",
                                         wrapWidth=1.8, color = col)
                                         
instructions6 = visual.TextStim(win, text = "In the following block, you will see two words. \n\n"
                                            "Please try to sing the two words out loud. \n\n"
                                           "If the words sound the same, press 1. \n\n "
                                           "If the words sound different, press 2. \n\n"
                                           "Press a key to begin.",
                                         wrapWidth=1.8, color = col)
                                         

block_info = {'speak_listen': {'w1': listen_words1, 'w2': listen_words2, 'correct': listen_corrects, 'instructions': instructions1}, \
'sing_listen': {'w1': listen_words1, 'w2': listen_words2, 'correct': listen_corrects, 'instructions': instructions4}, \
'speak_imagine': {'w1': imagine_words1, 'w2': imagine_words2, 'correct': imagine_corrects, 'instructions': instructions2}, \
'sing_imagine': {'w1': imagine_words1, 'w2': imagine_words2, 'correct': imagine_corrects, 'instructions': instructions5}, \
'speak_speak': {'w1': speaking_words1, 'w2': speaking_words2, 'correct': speaking_corrects, 'instructions': instructions3}, \
'sing_sing': {'w1': speaking_words1, 'w2': speaking_words2, 'correct': speaking_corrects, 'instructions': instructions6}}
 
block_order = [['speak_listen', 'speak_imagine', 'speak_speak', 'sing_listen', 'sing_imagine', 'sing_sing'],
['sing_listen', 'sing_imagine', 'sing_sing', 'speak_listen', 'speak_imagine', 'speak_speak']]
endText = visual.TextStim(win, text='That is the end of the task. \n'
                                    'Press a key to finish',
                          wrapWidth=1.8, color = col)
                          
endBlockText = visual.TextStim(win, text='That is the end of the block. \n'
                                    'Rest as much as you need. \n'
                                    'Press a key to continue.',
                          wrapWidth=1.8, color = col)
                          
# start log file:
# Default
filename = log_dir + '/' + sub_id[0] + '_homophones_default.log'
lastLog = logging.LogFile(filename, level=logging.INFO, filemode='w')

# Custom
custom_logfname = log_dir + '/' + sub_id[0] + '_homophones_custom.csv'
logfile = open(custom_logfname,'w')
logfile.write("subject,block_time,experiment_time,block,word1,word2,response,rt\n")

# Set clock
block_time = core.Clock()
trial_time = core.Clock()
experiment_time = core.Clock()

############################# Start the task ###############################

#create trial function
def trials(word1, word2, correct, block='one'):
    trial_time.reset() 
    block_t= block_time.getTime()
    experiment_t = experiment_time.getTime()
    fixationCross.draw()
    win.flip()
    core.wait(1)
    wordText1 = visual.TextStim(win, text= word1,
                          wrapWidth=1.8, color = col, pos=(-.5, 0.0))
    wordText2 = visual.TextStim(win, text= word2,
                          wrapWidth=1.8, color = col, pos=(0.5, 0.0)) 
    wordText1.draw()
    wordText2.draw()
    win.flip()
    event.clearEvents(eventType='keyboard')
    response = None
    while response == None:
        key = event.getKeys(timeStamped=trial_time)
        if len(key) > 0:
            response = key[0][0]
            rt = key[0][1]
    logfile.write("{},{},{},{},{},{},{},{}\n".format(sub_id[0],block_t,experiment_t,block, word1, word2, response, rt))
    

def block(block_name):
    block_time.reset()
    words_1_block = block_info[block_name]['w1']
    words_2_block = block_info[block_name]['w2']
    corrects_block = block_info[block_name]['correct']
    instructions = block_info[block_name]['instructions']
    instructions.draw()
    win.flip()
    event.waitKeys()
    for i in range(len(words_1_block)):
        word1_block = words_1_block[i]
        word2_block = words_2_block[i]
        correct_block = corrects_block[i]
        trials(word1_block, word2_block, correct_block)
    endBlockText.draw()
    win.flip()
    event.waitKeys()
        #split is random and order is random within a block

def experiment(border=0):
    for block_name in block_order[border]:
        block(block_name)
    endText.draw()
    win.flip()
    core.wait(2)
    core.quit()
        
experiment(border=border)


