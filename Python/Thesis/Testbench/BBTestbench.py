


from random import *
import json
f = open("synthesized_RTL.v","r")

lines = f.readlines()

module_name = ""
X = ""
Y = ""

for l in lines:
    if("module" in l):
        if("endmodule" not in l):
            module_name = l.split(" ")[1]


input_flag = 0

for l in lines:
    if("input" in l):
        X = l.replace("input","").replace(" ","").replace(";","")
	input_flag = 1
	continue
    if("output" in l):
	input_flag = 0
	break
    if(input_flag == 1):
	X += l.replace(" ","").replace(";","")
X = X.replace("\n","")


output_flag = 0
for l in lines:
    if("output" in l):
	Y = l.replace("output","").replace(" ","").replace(";","")
        output_flag = 1
        continue
    if("wire" in l):
	output_flag = 0
	break
    if(output_flag == 1):
	Y += l.replace(" ","").replace(";","")

Y = Y.replace("\n","")



X = X.rstrip()
Y = Y.rstrip()



x_values = X.split(",")
x_values_text = ""
y_values = X.split(",")
y_values_text = ""
z_values = X.split(",")
z_values_text = ""


OPCODE_DICT_X = {}
OPCODE_DICT_Y = {}
OPCODE_DICT_Z = {}


for x1 in x_values:
    rand_int = str(randint(0, 1))
    OPCODE_DICT_X[""+x1.lower()] = rand_int
    x_values_text += x1 +"="+rand_int+";\n"
for y1 in y_values:
    rand_int = str(randint(0, 1))
    OPCODE_DICT_Y[""+y1.lower()] = rand_int
    y_values_text += y1 +"="+rand_int+";\n"
for z1 in y_values:
    rand_int = str(randint(0, 1))
    OPCODE_DICT_Z[""+z1.lower()] = rand_int
    z_values_text += z1 +"="+rand_int+";\n"

master_opcode = {}
master_opcode['x'] = OPCODE_DICT_X
master_opcode['y'] = OPCODE_DICT_Y
master_opcode['z'] = OPCODE_DICT_Z

with open("opcode.json","w") as fp:
    json.dump(master_opcode,fp)


v_file = "`timescale 1ns/1ps\n""module verilog_tb;\nreg "+X+";\nwire "+Y+";\n"+module_name+" tb ("+X+","+Y+");\ninitial\nbegin\n""#500\n"""+x_values_text+"\n#1000\n"+y_values_text+"\n#1500\n"+z_values_text+"end\nendmodule";



fo = open("verilog_tb.v","w")
fo.write(v_file)
