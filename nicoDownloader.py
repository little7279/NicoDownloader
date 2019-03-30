import nicotools, getpass, os, shutil, moviepy.editor as mp

# JUUUUUUUUUST Login
EMAIL = input('EMAIL:')
PW = getpass.getpass('PW:')
DIR = './Downloads/'
DIR_M = './Music'
SM = ''

def VideoDownload(EMAIL, PW, SM):
    SM = input('sm')
    os.system('nicotools  download --mail "{0}" --pass "{1}" -v "sm{2}" -d "{3}"'.format(EMAIL, PW, SM, DIR))
    
    

# 0. ./Downloads 폴더 안에 있는 파일 나열
# 1.  변환할 파일 선택
# 2.  변환후 ./Music로 이동
def VideoToMusic():
    i = 0

    file_list = os.listdir(DIR)
    print('FileList')
    for list in file_list:
        print('{0}. {1}'.format(i, list))

    n =  int(input('NUMBER :'))

    clip = mp.VideoFileClip(DIR+file_list[n]).subclip(0, -1)
    music = file_list[n].replace('.mp4', '.mp3')
    clip.audio.write_audiofile(music)
    print('Video -> Music Complete')
    
while True:

    print('[MENU]\n'
          '1. Video Download\n'
          '2. Video -> Music\n'
          '3. MyList\n'
          '4. Exit\n')
    menu = input('SELECT[1-3]: ')
    os.system('cls')

    if menu == '1':
        VideoDownload(EMAIL, PW, SM)

    elif menu == '2':
        VideoToMusic()

    elif menu == '4':
        print('exit nicoDownloader')
        exit(0)
