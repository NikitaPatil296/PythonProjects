
print('Imported my module...')

test = 'Test String'

def find_index(dataString,target):
    for i ,value in enumerate(dataString):
        if value == target:
            return i
        
    return -1
