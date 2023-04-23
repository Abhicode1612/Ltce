# macro with more positional arguments &amp; label argument, expansion of macro &amp; generating expanded source code.


# Define macro names and opcodes
macro_names = ["MACRO"]
opcodes = ["MOV", "ADD", "SUB", "MUL", "DIV", "AND", "OR", "LOAD", "STORE", "DCR", "INC", "JMP", "JNZ", "HALT"]

# Take input from user
macro_code = []
source_code = []
num_macro_def = int(input("Enter the number of macro definition lines: "))
for i in range(num_macro_def):
    macro_code.append(input("Enter Macro code instruction {} : ".format(i + 1)).upper())

num_source_code = int(input("Enter the number of source code lines: "))
for i in range(num_source_code):
    source_code.append(input("Enter Source code instruction {} : ".format(i + 1)).upper())

# Parse the macro code to get macro names and arguments
macros = {}
for code in macro_code:
    if code.startswith("MACRO"):
        macro_name, *args = code.split()[1:]
        macros[macro_name] = args

# Process the source code
num_instr_src = 0
num_macro_calls = 0
num_instr_mc = 0
expanded_code = []
for code in source_code:
    if any(macro_name in code for macro_name in macro_names):
        num_macro_calls += 1
        macro_name, *args = code.split()
        if macro_name in macros:
            num_instr_mc += 1
            mapping = dict(zip(macros[macro_name], args))
            for macro_code in macro_code[1:-1]:
                for arg_name, arg_value in mapping.items():
                    macro_code = macro_code.replace(arg_name, arg_value)
                expanded_code.append(macro_code)
        else:
            expanded_code.append(code)
    else:
        num_instr_src += 1
        expanded_code.append(code)

# Print the output
print("Expanded Source Code is : ")
for code in expanded_code:
    print(code)

print("No of instructions in input source code : {}".format(num_instr_src))
print("No of macro call : {}".format(num_macro_calls))
print("No of instructions defined in macro call : {}".format(num_instr_mc))
print("Total number of instructions in expanded code : {}".format(len(expanded_code)))








# Enter the number of macro definition lines: 3
# Enter Macro code instruction 1 : MACRO ADD2
# Enter Macro code instruction 2 : ADD &1, &1
# Enter Macro code instruction 3 : MEND
# Enter the number of source code lines: 5
# Enter Source code instruction 1 : LOAD A
# Enter Source code instruction 2 : ADD2 B
# Enter Source code instruction 3 : ADD2 C
# Enter Source code instruction 4 : STORE A
# Enter Source code instruction 5 : HALT
