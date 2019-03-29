import nicotools, getpass, os, ffmpeg

# Login niconico
EMAIL = input('EMAIL:')
PW = getpass.getpass('PW:')

# File Directory
DIR = "./Downloads"


# Exam input : '27905394'
print('IF [nico URL]/sm32492001\n JUST TYPE : 32492001  ')
SM = input()
# download -v "{2}"
# os.system('nicotools  download --mail "{0}" --pass "{1}" -v "sm{2}" -d "{3}" '.format(EMAIL, PW, sm, DIR))

def VideoDownload(EMAIL, PW, SM):
    os.system('nicotools  download --mail "{0}" --pass "{1}" -v "sm{2}" -d "{3}" '.format(EMAIL, PW, sm, DIR))

def VideoToMusic():
    # Soon
while True:
    print('[MENU]\n1. Video or music Download\n2. movie -> music\n3. EDIT your MYLIST')
    menu = input('SELECT[1-3]: ')
    os.system('cls')

    if menu == '1':
        VideoDownload(EMAIL, PW, SM)
    elif menu == '2':
        print('Soooooooooooooooooooooon')
    elif menu == 'q':
        print('exit nicodownloader')
        exit(0)
'''

/search/검색어

/watch/sm34388038
'''
