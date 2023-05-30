# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:25:49 2023

@author: nomanmustafa7@yahoo.com
"""
import gwy
import gtk

plugin_menu = "/horizontal Pile1 (python)"
plugin_type = "PROCESS"
plugin_desc = "Implements horizontal Pile for wsf image files"
# Define keys for storing data in gwyddion
SPARSE_MOD_NAME = "horizontal Pile1"
DEBUG = False
SPARSE_MOD_NAME = "horizontal Pile1"
defaults = {}
PREVIEW_SIZE = 400
###########################################
# START FUNCTIONS
###########################################         
def dir_folder(filename):
    lista = filename.split('\\')
    filename  = lista.pop()
    temp = ''
    for i in range(len(lista)):
        temp = temp + lista[i] + '\\'
    #print temp
    return temp
def load112( filename):
   #print 'filename' + filename 
   load(filename) 
def load(filename):
    folder = dir_folder(filename)
    print "parent folder = ",folder
    import glob
    list_files = glob.glob(folder+"*.wsf")
    #print list_files
    list_files.sort()
    #print list_files
    img_count = len(list_files)
    print "length of files = ",len(list_files)
    import os
    import shutil
    if (os.path.isdir(folder+"output")):
        shutil.rmtree(folder+"output")
    os.mkdir(folder+"output")
    
    path = list_files[0]#'D:\\imgs2\\AFM_scan_2019-11-26_14.19.49, 5um, 256 pixels, Right(1).wsf'
    g = open(path)
    g1 = g.read()
    g2 = g1.split('\n')
    new_lines = []
    for i in range(2):
        new_lines.append(g2.pop(0))
    #print( new_lines)
    
    Line = g2.pop(0)
    Line_list = Line.split(':')
    Line_list_data = int(Line_list[len(Line_list)-1])
    #print "L100 = ",type(Line_list_data),Line_list_data* img_count
    new_lines.append("Pixels in X:    "+str(Line_list_data * img_count))
    #print("L102 = ",new_lines)
    
    for i in range(1):
        new_lines.append(g2.pop(0))
    #print(new_lines)
    Line1 = g2.pop(0)
    Line_List1 = Line1.split(':')
    Line_List_data1 = float(Line_List1[len(Line_List1)-1])
    #str(Line_List_data* img_count)
    
    new_lines.append("X Range: 	"+str(Line_List_data1 * img_count))
    #new_lines.append("X Range: 	10.000")
    #print(new_lines)
    for i in range(28):
        new_lines.append(g2.pop(0))
    #print(new_lines)
    #print(len(g2))

    list_files_new = []
    for i in range(len(list_files)-1):
        i = i+1
        filename_ = list_files[i]
        g_ = open(filename_)
        g1_ = g_.read()
        g2_ = g1_.split('\n')
        #new_lines = []
        for i in range(33):
            g2_.pop(0)
        #print "L193 = " ,g2.pop(0)
        list_files_new.append(g2_)
    #print "L194 = ",len(list_files_new)
       
    for i in range(len(g2)-1):
        temp_line = g2.pop(0)
        for file in range(len(list_files_new)):
            temp_line = temp_line+" "+list_files_new[file].pop(0)
        new_lines.append(temp_line)
    lines =new_lines# ['Readme', 'How to write text files in Python']
    print "processing completed"
    with open(folder+"output\\"+'readme123.wsf', 'w') as f:
        for line in lines:
            f.write(str(line))
            f.write('\n')
    print "file write finished"
def run():
    gwy_container = gwy.gwy_app_settings_get()
    data_container = gwy.gwy_app_data_browser_get_current(gwy.APP_CONTAINER)
    gwydata = {'container': gwy_container}    
    filename = gwy.gwy_file_get_filename_sys(data_container)
    print 'filename = ',filename 
    load112(filename)




            

