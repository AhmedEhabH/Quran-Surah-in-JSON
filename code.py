import os

path = '/media/ahmed/New Volume/World/Quran/Naser El Qatami' #Path
# print(os.listdir(path))
names = ['lec 04', 'lec 05', 'lec 06', 'lec 07', 'lec 08'] #List of new name
for i, filename in enumerate(os.listdir(path)):
    print("{} - {}\n".format(i, filename))
    os.rename(path + '/' + filename, path + '/' + names[i])
