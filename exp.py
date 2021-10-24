import base64

arrayOfByte2=[78, 106, 73, 49, 79, 122, 65, 51, 89, 71, 65, 117, 78, 106, 78, 109, 78, 122, 99, 55, 89, 109, 85, 61]
arrayOfByte1=[89, 87, 66, 108, 79, 109, 90, 110, 78, 106,65, 117, 79, 109, 74, 109, 78, 122, 65, 120, 79, 50, 89, 61]

def Decode(arr):
    res = base64.b64decode(bytes(arr))
    j = len(res)
    result=[]
    for i in range(0,j):
        result.append(res[i] ^ 3)
    return result

arr1=Decode(arrayOfByte1)
arr2=Decode(arrayOfByte2)

print(arr2)
print(bytes(arr2))

print(arr1)
print(bytes(arr1))

print('flag 5 is :  '+(str(bytes(arr2))).replace('b\'','').replace('\'','')+'-'+(str(bytes(arr1))).replace('b\'','').replace('\'',''))
