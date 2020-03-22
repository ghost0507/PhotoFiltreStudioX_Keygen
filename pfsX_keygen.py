#
# * Program: PhotoFiltre Studio X v10.x
# * Release: Simple Keygen
# * Created with: Python 3.8.x
#

def GenerateRegCode(name : str):
  Data = [0x7B, 0x4D, 0x86, 0x4E, 0x63, 0x45, 0xBC]
  Result = ''
  if(len(name)>=5):
      S = name.lower().replace(' ', '')
      T = 0
      for i in range(len(S)-1,-1, -1):
          T += ord(S[i]) - i - 1
      S = '{:3d}{:02d}01234'.format(T % 0x3E8, len(S) % 0x64)
      for i in range(10):
          Result += '{0:02X}'.format(Data[(i + 1) % 7] ^ ord(S[i]))
      Result = Result[:5] + '-' + Result[5:10] + '-' + Result[10:15] + '-' + Result[15:20]
      return Result
  else:
      return ''
    
name = input("Enter registration name: ")
if(name.strip()==""):
  print("-> Name can't be empty!")
else:
    if(len(name)<5):
        print("-> Name must have at least 5 characters!")
    else:
        print('Registration key: ' + GenerateRegCode(name))