import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json
import numpy as np
import cv2
from urllib.request import urlopen
import ftplib
import time
import rpyc


subscription_key = '1a2dddbfe8984367816892a32dd4f812'
uri_base = 'https://westcentralus.api.cognitive.microsoft.com'
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}


conn = rpyc.classic.connect('ev3dev')  # host name or IP address of the EV3
subprocess = conn.modules['subprocess']
ev3 = conn.modules['ev3dev.ev3']
us = ev3.UltrasonicSensor('in2')
url='http://10.73.32.151:8080//photoaf.jpg'
#ts = ev3.TouchSensor('in')
us.mode='US-DIST-CM'
DISTANCE_DETECT=True
motor = ev3.MediumMotor('outD')
m= ev3.LargeMotor('outC')

def ImageProcessing():
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    #cv2.imwrite("opencv.jpg", img)
    time.sleep(1)

    if 'a.jpg' in open('example.txt','r').read():
        cv2.imwrite("b.jpg", img)
        session = ftplib.FTP('ftp.yensan0512.com','yensan0512','DcfD43H-7y')
        file = open('C:/Users/ASUS/Downloads/robot/b.jpg','rb')                  # file to send
        session.storbinary('STOR /public_html/image/b.jpg', file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
        body={'url':'http://yensan0512.com/image/b.jpg'}
        with open('example.txt', 'w') as myfile:
            myfile.write("b.jpg")

    else:
        cv2.imwrite("a.jpg",img)
        session = ftplib.FTP('ftp.yensan0512.com','yensan0512','DcfD43H-7y')
        file = open('C:/Users/ASUS/Downloads/robot/a.jpg','rb')                  # file to send
        session.storbinary('STOR /public_html/image/a.jpg', file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
        body={'url':'http://yensan0512.com/image/a.jpg'}
        with open('example.txt', 'w') as myfile:       
            myfile.write("a.jpg")

    time.sleep(3)

    try:
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)
    
        print ('Response:')
        parsed = json.loads(response.text)
        print (json.dumps(parsed, sort_keys=True, indent=2))
    
        print(parsed[0]['faceAttributes']['gender'])
        a = parsed[0]['faceAttributes']['gender']
        return a
        time.sleep(5)


    
    except Exception as e:
        print('Error:')
        print(e)

def female():
    subprocess.call("python3 robot/female.py", shell=True)

def male():
    subprocess.call("python3 robot/male.py", shell=True)





while DISTANCE_DETECT:    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
    
    #if(ts.value == 1):
    if (us.value() < 100):
        print("----------Start Face Detection--------------")
        time.sleep(5)
        result=ImageProcessing()
        time.sleep(1)   
        if result == 'female':
           print("detect female")
           female()
        elif result =='male':
            print('detect male')
            male() 
    else:
        break
#result = ImageProcessing()
#print(result)      