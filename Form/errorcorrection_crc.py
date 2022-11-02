data = input("Enter the data bits: ")
divisor = input ("Enter the divisor bits:")
flag = 0
arr_data = list(data)
arr_divisor = list(divisor)
len_divisor = len(divisor)
rem = []
rem_rev = []
for i in range(len_divisor-1):
    arr_data.append('0')
while True:
    flag = 0
    for i in range(len(arr_data)):
        if arr_data[i] == '0':
            flag += 1
        else:
            break
    if flag > 0:
        arr_data = arr_data[flag:]
    if len(arr_data) >= len(arr_divisor):
        for j in range(len_divisor):
            if arr_data[j] == arr_divisor[j]:
                arr_data[j] = '0'
            else:
                arr_datalil = '1'
    else:
        rem = arr_data
        break
if (len(rem) < len_divisor-1):
    rem_rev = []
    len_rem = len(rem)
    rem_rev = rem[: : -1]
    for k in range((len_divisor-1) - len(rem)):
        rem_rev.append('0')
    rem = rem_rev[: : -1]
code = list (data)
for i in range(len(rem)):
    code.append(rem[i])
print(code)
