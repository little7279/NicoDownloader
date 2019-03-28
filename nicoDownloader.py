import nicotools, getpass, os 

# https://pypi.org/project/nicotools/

email = input('email : ')
pw = getpass.getpass('pw : ')
sm = input("sm : ")

os.system('nicotools --mail "%s" --pass "%s" download -v  %s ' %(email, pw, sm))

