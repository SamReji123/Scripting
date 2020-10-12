import os
import fileinput
import shutil

from subprocess import Popen, PIPE, STDOUT
#/home/sjoseph8/Desktop/Thesis_Final/library_extraction
path = raw_input("Enter path where the liberty files are presented : ") 

p = Popen(['lc_shell'], stdout=PIPE, stdin=PIPE, stderr=STDOUT,cwd=path)    

grep_stdout = p.communicate(input=b'read_lib asap7sc7p5t_24_SIMPLE_LVT_TT.lib\nwrite_lib asap7sc7p5t_22b_SIMPLE_LVT_TT_170906 -format db -output asap7sc7p5t_LVT_TT.db\n\nexit')[0]

p.terminate()
p.kill()
print(grep_stdout)
