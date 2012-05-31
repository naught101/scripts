#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cleans music directory folder structure. Moves music from directories with
# only a couple of files to the parent, then deletes empty dirs.

import os, commands, string, sys, shutil, glob

basepath = "/home/music"

# list directories
def GetSubDirs(dirname):
    if os.path.isdir(dirname):
        dirList = os.listdir(dirname)
        subDirs = []
        for item in dirList:
            fullpath = os.path.join(dirname, item)
            if os.path.isdir(fullpath):
                subDirs = subDirs + [fullpath]
        return subDirs
    else:
        msg = dirname + " is not a directory, can't have subdirectories"
        return  msg

def GetFiles(dirname):
    if os.path.isdir(dirname):
        dirList = os.listdir(dirname)
        files = []
        for item in dirList:
            fullpath = os.path.join(dirname, item)
            if not os.path.isdir(fullpath):
                files = files + [fullpath]
        return files
    else:
        msg = dirname + " is not a directory, so it doesn't contain files"
        return  msg

def RecurseSubdir(dirname):
    subdirs = GetSubDirs(dirname)
    directorylist = []
    for directory in subdirs:
        sublist = RecurseSubdir(directory)
        directorylist = directorylist + sublist
    return directorylist

def MoveFewToParent(dirname):
    movedNum = 0
    for (path,dirs,files) in os.walk(dirname):
        if len(dirs) == 0 :
            if len(files) < 2 :
                for file in files:
                    oldpath = os.path.join(path, file)
                    newpath = os.path.join(os.path.split(path)[0], file)
                    shutil.move( oldpath , newpath)
                    movedNum += 1
    return "moved " + str(movedNum) + " files."

def DeleteEmptySubDirs(dirname):
    deletedNum = 0
    for (path,dirs,files) in os.walk(dirname):
        if len(dirs) == 0 :
            if len(files) == 0:
                os.rmdir(path)
                deletedNum = deletedNum + 1
    return "deleted " + str(deletedNum) + " empty directories."
