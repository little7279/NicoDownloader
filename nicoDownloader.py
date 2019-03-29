import nicotools, getpass, os, ffmpeg

# File Directory
DIR = "./Downloads"


# NicoVideo의 비디오 고유번호
# Ex
# https://www.nicovideo.jp/watch/sm5865063
# -> 고유번호 : sm5865063
SM = ''


# 니코동에 로그인
EMAIL = input('EMAIL:')
PW = getpass.getpass('PW:')


def VideoDownload(EMAIL, PW, SM):

    print('if [nico URL]/sm32492001\n TYPE : 32492001  ')
    SM = input('sm')
    os.system('nicotools  download --mail "{0}" --pass "{1}" -v "sm{2}" -d "{3}"'.format(EMAIL, PW, SM, DIR))

# 0. ./Downloads 폴더 안에 있는 파일 나열
# 1.  변환할 파일 선택
# 2.  변환후 ./Music로 이동

def VideoToMusic():
    file_list = os.listdir(DIR)
    print('FileList')
    for list in file_list:
        print('{0}'.format(list))

while True:
    print('[MENU]\n1. Video Download\n2. movie -> music\n3. EDIT your MYLIST\n4. press q -> exit')
    menu = input('SELECT[1-3]: ')
    os.system('cls')

    if menu == '1':
        VideoDownload(EMAIL, PW, SM)

    elif menu == '2':
        VideoToMusic()

    elif menu == 'q':
        print('exit nicoDownloader')
        exit(0)

'''

/search/검색어

/watch/sm34388038
'''
