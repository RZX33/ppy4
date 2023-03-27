def caesars_cipher(data, k, arr=['']):
    if arr.__contains__(''):
        text = str(data).lower()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']

        result = ''
        for i in text:
            if alphabet.__contains__(i):
                temp_value = 0
                if ord(i) + k > ord('z'):
                    temp_value = ord(i) + k - ord('z') + ord('a')
                elif ord(i) + k < ord('a'):
                    temp_value = ord(i) + k + ord('z') - ord('a')
                else:
                    temp_value = ord(i) + k
                result += chr(temp_value)
            else:
                result += i
        return result
    else:
        text = str(data)
        result = ''
        for i in text:
            if i.lower() == arr[0]:
                result += arr[1]
            else:
                result += i
        return result



print(caesars_cipher('The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll', 5))
print(caesars_cipher('The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll', 5, ['a', 'B']))
