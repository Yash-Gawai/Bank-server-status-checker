from subprocess import PIPE,Popen
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def execute_return(cmd):
    args = cmd.split(" ")
    proc = Popen(args,stdout=PIPE,stderr=PIPE)
    out,err = proc.communicate()
    return out

out = execute_return("python ping_test.py")
input_message = out.decode("utf-8").strip()
print(input_message)

URLS = {"SBI":"https://www.onlinesbi.com","HDFC":"https://netbanking.hdfcbank.com/netbanking/","AXIS":"https://axisbank.com"}

if input_message in URLS:    
    req = Request(URLS[input_message])
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print ('Website is working fine')
