# Implementation of 2-levels nested macro &amp; its expansion.

macro_def = []
source_code = []
macro_outer = []
extended_macro_code = []
extended_source_code = []
print("Enter Macro Command(inner): ")
macro_cmd=input()
macro_def.append(macro_cmd)
while macro_def[-1] != 'MEND':
    macro_cmd=input()
    macro_def.append(macro_cmd)
macro_name = macro_def[1].split()[0]
params = macro_def[1].split() [1:]
print("Enter Macro Command(outer): ") 
macro_cmd = input() 
macro_outer.append(macro_cmd)
while macro_outer[len(macro_outer)-1] != 'MEND':
    macro_cmd = input() 
    macro_outer.append(macro_cmd)
print("Enter Source Code: ")
command=input("")
source_code.append(command)
while macro_outer [-1] != 'MEND':
    command=input()
    macro_outer.append(command)
for ext_cmd in range (len (macro_outer)):
    if macro_outer [ext_cmd].startswith (macro_name):
        macro_args = macro_outer [ext_cmd].split() [1:]
        macro_dict = {param: arg for param, arg in zip(params, macro_args)} 
        macro_cmd = 0
        for mac_cmd in range (len (macro_def)):
            if macro_def[mac_cmd] == 'MACRO' or macro_def[mac_cmd] == 'MEND' or macro_def[mac_cmd].startswith (macro_name):
                pass
            else:
                expanded_cmd = macro_def[mac_cmd]
                for param, arg in macro_dict.items():
                    expanded_cmd = expanded_cmd.replace(param, arg)
                extended_macro_code.append(expanded_cmd)
    else:
        extended_macro_code.append(macro_outer [ext_cmd])

while source_code[len(source_code)-1] != 'HALT': 
    command = input()
    source_code.append(command) 
macro_name = extended_macro_code[1]

for ext_cmd in range(0, len(source_code)): 
    if (source_code[ext_cmd] == macro_name):
        macro_cmd = 0
        for mac_cmd in range(0, len(macro_def)):
            if extended_macro_code[mac_cmd] == 'MACRO' or extended_macro_code[mac_cmd] == 'MEND' or extended_macro_code[mac_cmd] == macro_name:
                pass 
            else:
                extended_source_code.append(extended_macro_code[mac_cmd])
    else:
        extended_source_code.append(source_code[ext_cmd]) 


print('**********MACRO EXTENDED CODE**************')
for code in extended_macro_code:
    print (code)

print('**********Extended Source Code**************')
 
for code in range(0, len(extended_source_code)): 
    print(extended_source_code[code], end='\n')









# Enter Macro Command(inner):
# MACRO
# ADD &A, &B
# SUB &A, &B
# MEND
# Enter Macro Command(outer):
# LOOP LDA &X
# ADD &Y
# STA &X
# CMP &X, &Z
# JLT LOOP
# HLT
# MEND
# Enter Source Code:
# LOOP
# ADD A, B
# SUB A, B
# HALT