import cv2 as cv
import os

def rescale(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    return cv.resize(frame, (width, height), cv.INTER_AREA)

def frame_per_second(path_video, path_save=None, n=3):
    folder_save = 'Results'
    if path_save != None:
        os.chdir(path_save)
    else:
        os.mkdir(folder_save)
        os.chdir(folder_save)
    capture = cv.VideoCapture(path_video)
    frame_rate = capture.get(cv.CAP_PROP_FPS)
    frame_counts = capture.get(cv.CAP_PROP_FRAME_COUNT)

    print('--------------------------------------------------')
    print('| Informations of Video:                         |')
    print('|   *Frame_rate:     {0:10.3f}                  |'.format(frame_rate))
    print('|   *Frame_counts:   {0:10.3f}                  |'.format(frame_counts))
    print('|   *Time videos:    {0:10.3f}                  |'.format(frame_counts/frame_rate))
    print('{0:-^50}'.format('-'))

    frame_index,n = 1,n
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        if frame_index % int(frame_rate/n) == 0:
            file_save_frame = '{}_{}.jpg'.format('frame_image', frame_index)
            cv.imwrite(file_save_frame, frame)
        frame_index += 1
    capture.release()
    cv.destroyAllWindows()