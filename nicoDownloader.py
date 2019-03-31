import ffmpeg, moviepy.editor as mp
from nicotools.download import Video
import getpass, os, sys, time, asyncio, shutil
'''
required packages:
    1. nicotools
    2. moviepy
    3. ffmpeg
'''

# -> 고유번호 : sm5865063

dir_path = "./Downloads/"
converted_path = "./Converted/"
count = 0
clearchang = lambda: os.system('cls') if sys.platform is "win32" else os.system("clear")

def VideoDownload():
    clearchang()
    mail = input('EMAIL : ')
    password = getpass.getpass('PW : ')
    # Video(["sm"+input("SM number (without 'sm') : "),"sm5865063"], save_dir=dir_path, mail=mail, password=password).start() # RuntimeError: Session is closed.
    os.system('nicotools  download --mail "{0}" --pass "{1}" -v "sm{2}" -d "{3}"'.format(mail, password, input("SM number (without 'sm') : "), dir_path));print("")

def VideoToMusic():
    """
    0. ./Downloads 폴더 안에 있는 파일 나열
    1.  변환할 파일 선택
    2.  변환후 ./Music로 이동
    """
    file_list = [e for e in os.listdir(dir_path) if not e.startswith('.')]
    clearchang()
    print('== FileList ==')
    for i,list in enumerate(file_list):
        print('{0}. {1}'.format(i+1,list))

    n = int(input('NUMBER : '))-1

    clip = mp.VideoFileClip(dir_path+file_list[n]).subclip(0, -1)
    music = file_list[n].replace(file_list[n].split(".")[1], 'mp3')

    try:  
        os.mkdir(converted_path)
    except OSError:  
        print("!! Directory Exists. !!") # TODO : USE LOGGER INSTEAD OF PRINT FUNCTION

    clip.audio.write_audiofile(converted_path+music)

    try:
        os.remove(dir_path+file_list[n])
    except OSError:
        print("Original file does not exist.") # TODO : USE LOGGER INSTEAD OF PRINT FUNCTION
    else:
        print("Original file Successfully removed.") # TODO : USE LOGGER INSTEAD OF PRINT FUNCTION

    print('Video -> Music Complete')
    time.sleep(3)
    clearchang()

def Press_B_to_Blow():
    clearchang()
    for c in ("now exiting "+"nico "*count+"douga downloader."):
        time.sleep(0.1)
        print(c, end='', flush=True)
    time.sleep(3)
    clearchang()
    exit(0)


if __name__ == "__main__":
    while True:
        count+=1
        selections = {'1': VideoDownload, '2': VideoToMusic, 'q':Press_B_to_Blow, }
        print('[MENU]\n'
          '1. Video Download\n'
          '2. Video -> Music\n'
          '3. MyList\n'
          '4. Exit\n')
        try:
            selections.get( input('SELECT[1-3] : '))()
        except TypeError:
            pass

#     # os.rename(DIR+file_list[n], DIR_M+file_list[n])
#     os.mkdir('./Music')
#     shutil.move(name , DIR_M+name)
#     print('Video -> Music Complete')

'''
/search/검색어
/watch/sm34388038
'''