filepath = 'password.txt'

valid_count = 0

def parseline(line):

    parsed_line = line.split(' ')

    nums = (parsed_line[0]).split('-')
    letter = (parsed_line[1])[0]
    password = parsed_line[2].rstrip()

    index1 = int(nums[0])
    index2 = int(nums[1])

    if(not((password[index1- 1] == letter and password[index2 - 1] == letter) or (password[index1-1] != letter and password[index2 - 1] != letter ))):
        return True
    else:
        return False


    '''count = 0
    for letters in password:
        if(letter == letters):
            count+=1

    if(count >= int(nums[0]) and count <= int(nums[1])):
        return True
    else: 
        return False
    '''

with open(filepath) as fp:
   for line in fp:
       result = parseline(line)
       if(result):
           valid_count += 1

print(valid_count)
