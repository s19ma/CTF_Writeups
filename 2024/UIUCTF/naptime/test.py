def subset(array, num):
    result = []
    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
        find(arr[1:], num, path)
    find(array, num)
    return result
a =  [66128, 61158, 36912, 65196, 15611, 45292, 84119, 65338]
ct = [273896, 179019, 273896, 247527, 208558, 227481, 328334, 179019, 336714, 292819, 102108, 208558, 336714, 312723, 158973, 208700, 208700, 163266, 244215, 336714, 312723, 102108, 336714, 142107, 336714, 167446, 251565, 227481, 296857, 336714, 208558, 113681, 251565, 336714, 227481, 158973, 147400, 292819, 289507]

for su in ct:
    res = subset(a, su)[0]
    check = ""
    i=0
    for r in res:
        while r != a[i]:
            check+="0"
            i+=1
        check+="1"
        i+=1

    while len(check)<8:
        check+="0"
    # check = "01110101"
    print(chr(int(check, 2)),end ="")

    #uiuctf{i_g0t_sleepy_s0_I_13f7_th3_fl4g}