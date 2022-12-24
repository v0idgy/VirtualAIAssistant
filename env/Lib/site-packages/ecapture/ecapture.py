
import logging
import time
import cv2

allowedFileTypes =  ["png","jpg","jpeg"]

def capture(cameraIndex, windowName,saveName):
    if (saveName == False and windowName == False):
        logging.warning("As the parameters WindowName and SaveName are both set to false, it renders this function call redundant")
        return

    cam = cv2.VideoCapture(cameraIndex,apiPreference=cv2.CAP_ANY, params=[    cv2.CAP_PROP_FRAME_WIDTH, 10000,    cv2.CAP_PROP_FRAME_HEIGHT, 10000])
    if cam is None or not cam.isOpened():
       logging.error('Unable to open image source: ' + str(cameraIndex))
       return
    ret, frame = cam.read()
    if ret:
        if(saveName != False):
            if(isinstance(saveName, str)):
                SaveNameFormatCheck = saveName.split('.')
                if(SaveNameFormatCheck[len(SaveNameFormatCheck)-1] in allowedFileTypes):
                    cv2.imwrite(saveName, frame)
                else:
                    logging.error("The specified file format is not allowed. Only the following formats are allowed: " + str(allowedFileTypes))
                    return
            else:
                logging.error("Save Name argument is not a string")
                return

        if(windowName != False):
            if(isinstance(windowName, str)):
                cv2.namedWindow(windowName)
                cv2.imshow(windowName, frame)
                cv2.waitKey(0)
            else:
                logging.error("Window Name argument is not a string")
                return
    cam.release()
    cv2.destroyAllWindows()

def captureCustomRes(cameraIndex, windowName,saveName, imageWidth = 1920, imageHeight = 1080):
    if (saveName == False and windowName == False):
        logging.warning("As the parameters WindowName and SaveName are both set to false, it renders this function call redundant")
        return
    
    cam = cv2.VideoCapture(cameraIndex,apiPreference=cv2.CAP_ANY, params=[    cv2.CAP_PROP_FRAME_WIDTH, imageWidth,    cv2.CAP_PROP_FRAME_HEIGHT, imageHeight])

    if cam is None or not cam.isOpened():
       logging.error('Unable to open image source: ' + str(cameraIndex))
       return
    ret, frame = cam.read()
    if ret:
        if(saveName != False):
            if(isinstance(saveName, str)):
                SaveNameFormatCheck = saveName.split('.')
                if(SaveNameFormatCheck[len(SaveNameFormatCheck)-1] in allowedFileTypes):
                    cv2.imwrite(saveName, frame)
                else:
                    logging.error("The specified file format is not allowed. Only the following formats are allowed: " + str(allowedFileTypes))
                    return
            else:
                logging.error("Save Name argument is not a string ")
                return

        if(windowName != False):
            if(isinstance(windowName, str)):
                cv2.namedWindow(windowName)
                cv2.imshow(windowName, frame)
                cv2.waitKey(0)
                cv2.destroyWindow(windowName)
            else:
                logging.error("Window Name argument is not a string")
                return
    cam.release()
    cv2.destroyAllWindows()

def vidCapture(cameraIndex,windowName,saveName,exitKey):
    if (saveName == False and windowName == False):
        logging.warning("As the parameters WindowName and SaveName are both set to false, it renders this function call redundant")
        return

    vid_capture = cv2.VideoCapture(cameraIndex)
    
    vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

    validSaveName = False
    validWindowName = False

    if vid_capture is None or not vid_capture.isOpened():
       logging.warning('Unable to open image source: ' + str(cameraIndex))
       return

    width= 1920 
    height= 1080

    if saveName != False:
        if(isinstance(saveName, str)):
            SaveNameFormatCheck = saveName.split('.')
            if(SaveNameFormatCheck[len(SaveNameFormatCheck)-1] == "avi"):
                writer = cv2.VideoWriter(saveName, cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
                validSaveName = True
            else:
                logging.error("The specified file format is not allowed. Only the following formats are allowed: avi ")
                return
        else:
            logging.error("Save Name argument is not a string")
            return

  
    if(not isinstance(exitKey, str)):
        logging.error("Exit Key must be a string of length 1")
        return
        

    if(windowName != False):
        if(isinstance(windowName, str)):
            cv2.namedWindow(windowName)
            validWindowName = True
        else:
            logging.error("Window Name argument is not a string")
            return

    while True:
        ret,frame= vid_capture.read()
        if ret:
            if(validSaveName  == True):
                writer.write(frame)
            
            if(validWindowName == True):
                cv2.imshow(windowName, frame)

        if cv2.waitKey(1) & 0xFF == ord(exitKey):
            break


    vid_capture.release()
    if(validSaveName  == True):
        writer.release()
    cv2.destroyAllWindows()

def vidCaptureCustomRes(cameraIndex,windowName,saveName,exitKey, imageWidth = 640, imageHeight = 480 ):
    if (saveName == False and windowName == False):
        logging.warning("As the parameters WindowName and SaveName are both set to false, it renders this function call redundant")
        return

    vid_capture = cv2.VideoCapture(cameraIndex)
    
    vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, imageWidth)
    vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, imageHeight)

    validSaveName = False
    validWindowName = False

    if vid_capture is None or not vid_capture.isOpened():
       logging.warning('Unable to open image source: ' + str(cameraIndex))
       return

    width= imageWidth 
    height= imageHeight

    if saveName != False:
        if(isinstance(saveName, str)):
            SaveNameFormatCheck = saveName.split('.')
            if(SaveNameFormatCheck[len(SaveNameFormatCheck)-1] == "avi"):
                writer = cv2.VideoWriter(saveName, cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
                validSaveName = True
            else:
                logging.error("The specified file format is not allowed. Only the following formats are allowed: avi ")
                return
        else:
            logging.error("Save Name argument is not a string")
            return

  
    if(not isinstance(exitKey, str)):
        logging.error("Exit Key must be a string of length 1")
        return
        

    if(windowName != False):
        if(isinstance(windowName, str)):
            cv2.namedWindow(windowName)
            validWindowName = True
        else:
            logging.error("Window Name argument is not a string")
            return

    while True:
        ret,frame= vid_capture.read()
        if ret:
            if(validSaveName  == True):
                writer.write(frame)
            
            if(validWindowName == True):
                cv2.imshow(windowName, frame)

        if cv2.waitKey(1) & 0xFF == ord(exitKey):
            break


    vid_capture.release()
    if(validSaveName  == True):
        writer.release()
    cv2.destroyAllWindows()

def timedVidCapture(cameraIndex,windowName,saveName,timer):

    if (saveName == False and windowName == False):
        logging.warning("As the parameters WindowName and SaveName are both set to false, it renders this function call redundant")
        return

    vid_capture = cv2.VideoCapture(cameraIndex)
    
    vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

    validSaveName = False
    validWindowName = False

    if vid_capture is None or not vid_capture.isOpened():
       logging.warning('Unable to open image source: ' + str(cameraIndex))
       return

    width= 640 
    height= 480

    if saveName != False:
        if(isinstance(saveName, str)):
            SaveNameFormatCheck = saveName.split('.')
            if(SaveNameFormatCheck[len(SaveNameFormatCheck)-1] == "avi"):
                writer = cv2.VideoWriter(saveName, cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
                validSaveName = True
            else:
                logging.error("The specified file format is not allowed. Only the following formats are allowed: avi ")
                return
        else:
            logging.error("Save Name argument is not a string")
            return

    if(windowName != False):
        if(isinstance(windowName, str)):
            cv2.namedWindow(windowName)
            validWindowName = True
        else:
            logging.error("Window Name argument is not a string")
            return
    t1 = time.time()
    while True:
        ret,frame= vid_capture.read()
        if ret:
            if(validSaveName  == True):
                writer.write(frame)
            
            if(validWindowName == True):
                cv2.imshow(windowName, frame)

        if time.time() - t1 > timer or cv2.waitKey(1) & 0xFF == 27:
            break


    vid_capture.release()
    if(validSaveName  == True):
        writer.release()
    cv2.destroyAllWindows()

def timedVidCaptureCustomRes(cameraIndex,windowName,saveName,timer, imageWidth = 1920, imageHeight = 1080):

    if (saveName == False and windowName == False):
        logging.warning("As the parameters WindowName and SaveName are both set to false, it renders this function call redundant")
        return

    vid_capture = cv2.VideoCapture(cameraIndex)
    
    vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, imageHeight)
    vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, imageWidth)

    validSaveName = False
    validWindowName = False

    if vid_capture is None or not vid_capture.isOpened():
       logging.warning('Unable to open image source: ' + str(cameraIndex))
       return

    width= imageWidth 
    height= imageHeight

    if saveName != False:
        if(isinstance(saveName, str)):
            SaveNameFormatCheck = saveName.split('.')
            if(SaveNameFormatCheck[len(SaveNameFormatCheck)-1] == "avi"):
                writer = cv2.VideoWriter(saveName, cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
                validSaveName = True
            else:
                logging.error("The specified file format is not allowed. Only the following formats are allowed: avi ")
                return
        else:
            logging.error("Save Name argument is not a string")
            return

    if(windowName != False):
        if(isinstance(windowName, str)):
            cv2.namedWindow(windowName)
            validWindowName = True
        else:
            logging.error("Window Name argument is not a string")
            return
    t1 = time.time()
    while True:
        ret,frame= vid_capture.read()
        if ret:
            if(validSaveName  == True):
                writer.write(frame)
            
            if(validWindowName == True):
                cv2.imshow(windowName, frame)

        if time.time() - t1 > timer or cv2.waitKey(1) & 0xFF == 27:
            break


    vid_capture.release()
    if(validSaveName  == True):
        writer.release()
    cv2.destroyAllWindows()

def delay_imcapture(cameraIndex, windowName,saveName, delay):
    logging.warning("delay_imcapture is no longer supported")

def vidcapture(cameraIndex,windowName,saveName,exitKey):
    logging.warning("vidcapture is no longer supported, use vidCapture instead")

def auto_vidcapture(cameraIndex,windowName,saveName,timer):
    logging.warning("vidcapture is no longer supported, use timedVidCapture instead")
capture(0,"window","False.png")