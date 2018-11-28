import subprocess as sp

banned_apps = []

def addban( appToBeBanned ):
    # add ban
    f = open('applist.ban', 'r')
    for line in f:
        banned_apps.append(line)
    banned_apps = [item.split('\n')[0] for item in banned_apps]
    f.close()
    banned_apps.append(appToBeBanned)
    f = open('applist.ban', 'w')
    for item in banned_apps:
        f.write("%s\n" % item)
    f.close()

def removeban( appToBeUnbanned ):
    # remove ban
    f = open('applist.ban', 'r')
    for line in f:
        banned_apps.append(line)
    banned_apps = [i.split('\n')[0] for i in banned_apps]
    f.close()
    f = open('applist.ban', 'w')
    banned_apps.remove(appToBeUnbanned)
    for item in banned_apps:
        f.write("%s\n" % item)
    f.close()

def _addban():
    # add ban
    tmp = sp.call('cls',shell=True)
    print('Please enter the name of the app to be banned.')
    appname = input('App Name: ')
    addban( appname )
    
def _removeban():
    # remove ban
    tmp = sp.call('cls',shell=True)
    print('Please enter the name of the app to be unbanned.')
    appname = input('App Name: ')
    removeban( appname )

def appmanager():
    # app manager menu
    tmp = sp.call('cls',shell=True)
    print('What would you like to do?')
    print('[1] Ban An App')
    print('[2] Unban An App')
    print('[3] Back to Admin Controls')
    amoption = input('Please type the option number: ')
    if amoption == '1':
        _addban()
    elif amoption == '2':
        _removeban()
    elif amoption == '3':
        admincontrol()
    else:
        print('Option does not match the choices!')
        anykey = input('Press Enter to continue.')
        appmanager()
        

def start():
    # start menu
    tmp = sp.call('cls',shell=True)
    print('Please enter the option number you would like.')
    print('i.e. If I wanted to register, I would type 2')
    print('[1] Login')
    print('[2] Register')
    print('[3] Admin Controls')
    option = input('Option number: ') # Get human input
    if option == '1':
        login()
    elif option == '2':
        register()
    elif option == '3':
        adminlogin()
    else:
        print('Option does not match the choices!')
        anykey = input('Press Enter to continue.')
        start()

def login():
    # Get login info
    tmp = sp.call('cls',shell=True)
    print('Enter your login information.')
    name = input('Enter your username: ')
    password_ = input('Enter your password: ')
    logintest( name, password_ )
    
def register():
    # Get registration info
    tmp = sp.call('cls',shell=True)
    print('Enter the information you want to use as your login.')
    name_ = input('Enter your username: ')
    password__ = input('Enter your password: ')
    registerwrite( name_, password__ )

def registerwrite( username, password ):
    # Write registration to file
    n = username+'.txt'
    f = open(n, 'w')
    f.write(username+'\n')
    f.write(password+'\n')
    f.write("Login sys made by Mason Harris")
    f.close()

def logintest( username, password ):
    #logintest
    n = username+'.txt'
    p = password
    try:
        file = open(n, 'r')
        file.close()
        worked = true
        
    except:
        print('File was not able to be opened. Does it exist?')
        yn = input('y/n: ')
        if yn == 'y':
            login()
        elif yn == 'n':
            start()
    
    if worked == true:
        f = open(n, 'r')
        _username_ = f.readline()
        _password_ = f.readline()
        if _password_ == password:
            loginpass( username, password )

def loginpass( un, pw ):
    # Get an app to start
    print('Please give the name of an app to start.')
    print('This wont work if the app isnt in the apps folder!')
    appinput = input('App Name:')
    appstart( appinput )

def adminlogin():
    # Admin logij
    pc = input('Primary Code: ')
    sc = input('Secondary Code: ')
    tc = input('Tertiary Code: ')
    adminpass = input('Password: ')
    if pc == '1337':
        if sc == '0138':
            if tc == '1975':
                admincontrol()
            else:
                print("Code(s) is/are incorrect!")
        else:
            print('Code(s) is/are incorrect!')
    else:
        print('Code(s) is/are incorrect!')
            

def admincontrol():
    # Admin Control
    tmp = sp.call('cls',shell=True)
    print('Welcome to Admin Control!')
    print('This is a WIP feature, and will be coming soon...')
    print('But glad to see you know the login!')
    ai = input('Press enter to go back to the start screen.')
    if ai != 'lfedusheyufy':
        start()
    else:
        start()
    
def appstart( appToBeOpened ):
    # This starts an app
    f = open('applist.ban', 'r')
    for line in f:
        banned_apps.append(line)
    banned_apps = [item.split('\n')[0] for item in banned_apps]
    f.close()
    for item in banned_apps:
        if item == appToBeOpened:
            print('App is banned; cannot open! Contact your app administrator.')
            entertocontinue = input('Press Enter to continue.')
            login()
        
start()
print('lets go')