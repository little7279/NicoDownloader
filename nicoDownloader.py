import ffmpeg, moviepy.editor as mp
from nicotools.download import Video
import getpass, os, sys, time, logging
'''
required packages:
    1. nicotools
    2. moviepy
    3. ffmpeg
'''

'''
/search/검색어
/watch/sm34388038
'''
# -> 고유번호 : sm5865063, sm34503384

dir_path = "./Downloads/"
converted_path = "./Converted/"
count = 0
clearchang = lambda: os.system('cls') if sys.platform is "win32" else os.system("clear")


def VideoDownload():
    print('[Login]')
    mail = input('EMAIL : ')
    password = getpass.getpass('PW : ')

    clearchang()
    sm = input("SM number (without 'sm') : ") # TODO : give 3 attempts

    # Video(["sm"+input("SM number (without 'sm') : "),"sm5865063"], save_dir=dir_path, mail=mail, password=password).start() # RuntimeError: Session is closed.
    # TODO : get target vid name, compare it to directory files, if overlaps, dont download

    os.system('nicotools  download --mail "{0}" --pass "{1}" -v "sm{2}" -d "{3}"'.format(mail, password, sm, dir_path));print("")

def VideoToMusic():
    file_list = [e for e in os.listdir(dir_path) if not e.startswith('.')]
    clearchang()
    print('== FileList ==')
    for i,list in enumerate(file_list):
        print('{0}. {1}'.format(i+1,list))
    print("q : quit")

    n = input('NUMBER : ')
    if n=="q":
        return

    n=int(n)-1
    clip = mp.VideoFileClip(dir_path+file_list[n]).subclip(0, -1)
    music = file_list[n].replace(file_list[n].split(".")[1], 'mp3')

    try:  
        os.mkdir(converted_path)
    except OSError:  
        logging.warning("!! Directory Path Exists. !!")

    if not os.path.isfile(converted_path+music):
        clip.audio.write_audiofile(converted_path+music)
    else:
        logging.warning("!! File already Exists. !!")
        time.sleep(2)
        return
    
    if input("Delete the Original file downloaded? (Y/N)").lower() == "y":
        # try:
        os.remove(dir_path+file_list[n])
        # except OSError:
        #     logging.warning("Original file does not exist.") # will this ever happen..
        # else:
        logging.info("Original file Successfully removed.")

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
    logging.basicConfig(level=logging.DEBUG)
    while True:
        count+=1
        selections = {'1': VideoDownload, '2': VideoToMusic, 'q':Press_B_to_Blow, }
        print('[MENU]\n'
          '1. Video Download\n'
          '2. Video -> Music\n'
          '3. MyList\n'
          'q. Exit\n')
        try:
            selections.get( input('SELECT[1-3] : '))()
        except TypeError:
            pass

#     # os.rename(DIR+file_list[n], DIR_M+file_list[n])
#     os.mkdir('./Music')
#     shutil.move(name , DIR_M+name)
#     print('Video -> Music Complete')
