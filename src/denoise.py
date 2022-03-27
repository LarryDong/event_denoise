
# denoise events based on correlation

from math import exp
import numpy as np
import argparse
import os
import cv2
import pandas as pd
import math

WIDTH = 346
HEIGHT = 260

# denoise based on correlation.
# Noise: k * k window has < N events
def denoise(points, k=5, N=3):
    src = np.zeros(shape=(HEIGHT, WIDTH), dtype='uint8')
    src_conv = np.zeros(shape=(HEIGHT, WIDTH), dtype='float32')
    dst = np.zeros(shape=(HEIGHT, WIDTH), dtype='uint8')
    for p in points:                    # draw points
        src[p[1], p[0]] = 255

    kernel = np.ones(shape=(k,k), dtype='float32') / (k*k)
    src_conv = cv2.filter2D(src, -1, kernel)
    dst[src_conv>255*N/(k*k)] = 255
    dst = dst & src

    cv2.imshow('src', src)
    cv2.imshow('denoised', dst)
    key = cv2.waitKey(0)
    if key == ord('q'):
        os.abort()
    return dst


if __name__ == '__main__':
    parser = argparse.ArgumentParser('denoise')
    parser.add_argument('--root_path', type=str, default='./data')
    parser.add_argument('--show_image', type=int, default=1)
    parser.add_argument('--begin', type=int, default=0)
    parser.add_argument('--K', type=int, default=5, help='windows size')
    parser.add_argument('--N', type=int, default=3, help='neighbor number (threshold)')
    args = parser.parse_args()
    
    # load dirs
    events_file = os.path.join(args.root_path, 'data.txt')
    ts_file_data = np.loadtxt(os.path.join(args.root_path, "data_ts.txt"), delimiter=' ', dtype=np.float)
    ts_list = ts_file_data[:,1]

    idx = args.begin    # begin from input index.
    point_list = []
    for df in pd.read_csv(events_file, names=['ts', 'x', 'y', 'p'], delimiter=' ', chunksize=10**6):   # processing in chunk=
        for x,y,t,p in zip(df['x'],df['y'],df['ts'],df['p']):        
            if idx != 0 and t < ts_list[idx-1]:     # skip before index
                continue
            point_list.append((x,y))

            if idx < len(ts_list) and t > ts_list[idx] :
                img = denoise(point_list, args.K, args.N)
                idx = idx + 1
                point_list = []

