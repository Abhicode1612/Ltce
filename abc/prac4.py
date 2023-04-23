# macro without argument, expanding macro calls &amp; generating expanded source

macro_def = [] 
source_code = [] 
extended_source_code = []

print("Enter Macro Command: ") 
macro_cmd = input() 
macro_def.append(macro_cmd)
while macro_def[len(macro_def)-1] != 'MEND':
    macro_cmd = input() 
    macro_def.append(macro_cmd)

print("Enter Source Code: ") 
command = input("") 
source_code.append(command)

while source_code[len(source_code)-1] != 'HALT': 
    command = input()
    source_code.append(command) 
macro_name = macro_def[1]

for ext_cmd in range(0, len(source_code)): 
    if (source_code[ext_cmd] == macro_name):
        macro_cmd = 0
        for mac_cmd in range(0, len(macro_def)):
            if macro_def[mac_cmd] == 'MACRO' or macro_def[mac_cmd] == 'MEND' or macro_def[mac_cmd] == macro_name:
                pass 
            else:
                extended_source_code.append(macro_def[mac_cmd])
    else:
        extended_source_code.append(source_code[ext_cmd]) 
print('**********Extended Source Code**************')
 
for code in range(0, len(extended_source_code)): 
    print(extended_source_code[code], end='\n')









# output
# Enter Macro Command:
# MACRO SUB1 &A,&B
# SUB &A,&B
# MEND
# Enter Source Code:
# LDA X
# SUB1 X,Y
# STA Z
# HALT