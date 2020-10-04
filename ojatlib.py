import argparse
import sys
import os,platform
from uuid import uuid4
import glob

if __name__ == "__main__":
    print("This is a lib,not a autotest tool,pls check out the instance which use this lib to use .")
    exit(1)
    pass

a = '/'

if(platform.system() == 'Windows'):
    a = '\\'

compilered_file_name = ""
del_compiled_file = ""
class LanguageAction():
    def del_file(self,file_name:str):
        pass
    def run(self,file_name:str):
        pass
    def compiler(self,file_name:str):
        pass

# Note: I recommand U write a function tha all the code will be compilered into only one name,because it will be more easier to write a run  and deleate function.

def files_load(file_name:str) :
    if not os.path.exists('.ojat'):
        os.makedirs('.ojat')
    path = '.ojat' + a + file_name
    if not os.path.exists(path):
        os.makedirs(path)
    all_file_list = glob.glob(path+a+"*.at") 
    all_file_list.sort(key=os.path.getmtime)
    return all_file_list

def file_create(file_name:str,content:str)->None:
    if not os.path.exists('.ojat'):
        os.makedirs('.ojat')
    if not os.path.exists('.ojat' + a + file_name):
        os.makedirs('.ojat'+a+file_name)
    input_file_name = str(uuid4()) + ".at"
    file_obj = open(".ojat"+a+file_name+a+input_file_name,"w+")
    file_obj.write(str(content))
    file_obj.close()

def read_content_and_run(file_name:str,func):
    files = files_load(file_name)
    for index,file in enumerate(files):
        print("- - -")
        print("[content No."+str(index)+" ]")
        content = open(file,'r').read()
        print(content)
        print("[output  No."+str(index)+" ]")
        func.run(str(file))
        print("- - -\n")

def input_content_get() -> str:
    a = str("")
    try:
        while True:
            a = a + input() + "\n"
    except EOFError:
        pass

    return a

def print_help():
    print("this is the user guide")

def ojat_start(instance:LanguageAction):
    func = instance
    fn = ""
    try:
        fn = sys.argv[1]
    except IndexError:
        print("Please enter the file name")
        exit(1)
    if(fn == "-help"):
        print_help()
        exit(0)

    try:
        option = sys.argv[2]
        if(option == "-input"):
           file_create(fn,input_content_get())
           exit(1)
        elif(option == "-help"):
            print_help()
            exit(0)
        else:
            print("Don't have this option.")
            exit(1)
    except IndexError:
        pass

    instance.compiler(fn)
    read_content_and_run(fn,instance)
    instance.del_file(fn)
