# Partitioner for iOS Dual-Booting :D

import math
import shutil
import subprocess
import sys, os, argparse
from appscript import app
from collections import namedtuple
from MobileDevice import *

def connect():



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', help='Lists available commands')
    parser.add_argument('-b', help='Blocksize of your device')
    parser.add_argument('-r', help='Resizes primary os Data partition. Use with -g')
    parser.add_argument('-a', help='Adds how many partitions to be used')
    parser.add_argument('-g', help='This is your input of GB')
    return parser.parse_args()

class gptfdisk(object):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg


    def resize_os(path):
        df = namedtuple('usage', 'total')
        st = os.statvfs(path)
        total = st.f_blocks * st.f_frsize
        return _ntuple_diskusage(total)
    gigabytes = int(args.gigabytes)
    new_size = _ntuple_diskusage(total) - args.gigabytes
    subprocess.call(['hfs_resize', '/private/var', new_size])
    subprocess.call(['gptfdisk', '/dev/rdisk0s1'])
    subprocess.call(['i', '2',])
    GUID = subprocess.check_output('Partition unique GUID: %s')
    subprocess.call(['d', '2', 'n'])
    app('System Events').keystroke('\r')
    subprocess.check_output('First Sector (%s-%s), default = %s')
    


    def
