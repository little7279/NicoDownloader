import nicotools, getpass, os 


email = input('email : ')
pw = getpass.getpass('pw : ')
sm = input("sm : ")

os.system('nicotools --mail "%s" --pass "%s" download -v  %s ' %(email, pw, sm))

