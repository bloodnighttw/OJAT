#!/usr/bin/python3

import subprocess
from subprocess import Popen,STDOUT,PIPE
from ojatlib import ojat_start,LanguageAction
from threading import Timer

class gccAction(LanguageAction):
    def del_file(self, file_name):
        del_compiled_file_linux()        
    def run(self, file_name):
        gcc_run(file_name)
    def compiler(self, file_name):
        gcc_compiler(file_name)

def gcc_run(stdin_path:str):
    command = ["timeout","5","./a.o"]
    in_file = open(stdin_path,'r').read()
    proc = Popen(command,stdin=PIPE)
    proc.communicate(str.encode(in_file))

def gcc_compiler(file_name:str):
    print("[+] start compiling !")
    command = ["g++",file_name,"-o","a.o"]
    subprocess.check_output(command,timeout=60)
    print("[+] compilered finished!")
def del_compiled_file_linux():
    # command = ["rm","a.out"]
    # subprocess.check_output(command)
    pass

if __name__ == "__main__":
    instance = gccAction()
    ojat_start(instance)

