#Herovision
import PySimpleGUI as sg
try:
    from PIL import Image
except ImportError:
    import Image

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Herovision')],
            [sg.Text('Please select the location of the screenshot you\'d like to analyse'), sg.FileBrowse(key="-IN-")],
            [sg.Button('Upload'), sg.Button('Cancel')] ],
            #[sg.Image('''C:\Users\MatthewH\Documents\GitHub\herovision\herovision\resources''')] #image preview

# Create the Window
window = sg.Window('Herovision', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values["-IN-"])

window.close()

#TODO: ask for a screenshot
print("To analyse a screenshot, drop it into the /screenshots folder")
screenshotPath = input("Please enter the filename of the screenshot you'd like to analyse:\n")

#TODO: analyse with google automl
print("Image analysis not yet implemented. defaulting to hero \'Sniper\' as a fallback.")
hero = "sniper"

#TODO: reach out to fandom wiki for data
print("Fandom API call not yet implemented.")
hero_bio = "Kardel Sharpeye, the Sniper, is a ranged agility hero who excels at dealing moderate to heavy damage from an incredible range."

#TODO: print this out to the console
print("HERO DETECTED: " + hero + "\nbio:" + hero_bio)
#TODO: present this in a nice UI

