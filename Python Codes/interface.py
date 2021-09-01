
import os, PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Col


actionbtn1 = ""
actionbtn2 = ""
actionbtn3 = ""
actionbtn4 = ""
actionbtn5 = ""
actionbtn6 = ""
actionbtn7 = ""
actionbtn8 = ""
actionbtn9 = ""
puerto = ""



sg.ChangeLookAndFeel('Dark')

col1 = [     #Btn6
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn6", default=True, key='btn6carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn6"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn6",key='btn6programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn6"), sg.FileBrowse()]], title='Opciones Boton 6',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno')],

]

col2 = [
    #btn7
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn7", default=True, key='btn7carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn7"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn7",key='btn7programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn7"), sg.FileBrowse()]], title='Opciones Boton 7',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno')],
    
]

col3 = [  
    #btn8
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn8", default=True, key='btn8carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn8"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn8",key='btn8programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn8"), sg.FileBrowse()]], title='Opciones Boton 8',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno')],

]

col4 = [
    #btn9
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn9", default=True, key='btn9carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn9"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn9",key='btn9programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn9"), sg.FileBrowse()]], title='Opciones Boton 9',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno')],
    [sg.Text('_' * 93)],

    [sg.Button('Cambiar',enable_events=True) ,sg.Button('CrearArchivo'), sg.Button('Ejecutar'), sg.Button('Exit')],
    
]

layout = [
    [sg.Text('Arduino', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Inserte puerto COM'), sg.InputText('COM10', key='com'), sg.Button('Set')],
    

    #Btn1
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn1", default=True, key='btn1carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn1"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn1",key='btn1programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn1"), sg.FileBrowse()]], title='Opciones Boton 1',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno'),sg.Column(col1)],
    
    #Btn2
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn2", default=True, key='btn2carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn2"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn2",key='btn2programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn2"), sg.FileBrowse()]], title='Opciones Boton 2',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno'),sg.Column(col2)],

    #Btn3
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn3", default=True, key='btn3carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn3"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn3",key='btn3programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn3"), sg.FileBrowse()]], title='Opciones Boton 3',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno'),sg.Column(col3)],

    #Btn4
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn4", default=True, key='btn4carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn4"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn4",key='btn4programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('',key="archivobtn4"), sg.FileBrowse()]], title='Opciones Boton 4',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno'),sg.Column(col4)],
    
    #Btn5
    [sg.Frame(layout=[
    [sg.Radio('Abrir una Carpeta', "btn5", default=True, key='btn5carpeta',size=(15,1)),
    sg.Text('Seleccionar', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('',key="carpetabtn5"), sg.FolderBrowse()], 
    [sg.Radio('Abrir un Programa', "btn5",key='btn5programa'),
    sg.Text('Seleccionar', size=(17, 1), auto_size_text=False, justification='right'),sg.InputText('', key="archivobtn5"), sg.FileBrowse()]], title='Opciones Boton 5',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Seleccione uno')],

    
    
]
window = sg.Window('Arduino', layout, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'Set':
        puerto = values['com']

    if event == 'Ejecutar':
        os.startfile("run.exe")
        
    if event == 'Cambiar':
                #Boton 1
        if values['btn1carpeta'] == True:
            actionbtn1 = values['carpetabtn1']
            
        elif values['btn1programa'] == True:
            actionbtn1 = values['archivobtn1']
        
        #Boton 2
        if values['btn2carpeta'] == True:
            actionbtn2 = values['carpetabtn2']
            
        elif values['btn2programa'] == True:
            actionbtn2 = values['archivobtn2']

        #Boton 3
        if values['btn3carpeta'] == True:
            actionbtn3 = values['carpetabtn3']
            
        elif values['btn3programa'] == True:
            actionbtn3 = values['archivobtn3']  

        #Boton 4
        if values['btn4carpeta'] == True:
            actionbtn4 = values['carpetabtn4']
            
        elif values['btn4programa'] == True:
            actionbtn4 = values['archivobtn4']

        #Boton 5
        if values['btn5carpeta'] == True:
            actionbtn5 = values['carpetabtn5']
            
        elif values['btn5programa'] == True:
            actionbtn5 = values['archivobtn5']

        #Boton 6
        if values['btn6carpeta'] == True:
            actionbtn6 = values['carpetabtn6']
            
        elif values['btn6programa'] == True:
            actionbtn6 = values['archivobtn6']

        #Boton 7
        if values['btn7carpeta'] == True:
            actionbtn7 = values['carpetabtn7']
            
        elif values['btn7programa'] == True:
            actionbtn7 = values['archivobtn7']
        
        #Boton 8
        if values['btn8carpeta'] == True:
            actionbtn8 = values['carpetabtn8']
            
        elif values['btn8programa'] == True:
            actionbtn8 = values['archivobtn8']

        #Boton 9
        if values['btn9carpeta'] == True:
            actionbtn9 = values['carpetabtn9']
            
        elif values['btn9programa'] == True:
            actionbtn9 = values['archivobtn9']

    if event == 'CrearArchivo':
        f = open("vars.txt", "w")
        f.write(puerto + "," + actionbtn1 + "," + actionbtn2 + "," + actionbtn3 + "," + actionbtn4 + "," + actionbtn5 + "," + actionbtn6 + "," + actionbtn7 + "," + actionbtn8 + "," + actionbtn9)
        f.close()

    