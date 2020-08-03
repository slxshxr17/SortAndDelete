import os
import hashlib
def main(path):
    for count, filename in enumerate(os.listdir(path)):
        dst = str(count) + ".jpg"
        src = path + filename
        dst = path + dst
        os.rename(src, dst)  
   
def md5(f):
    return hashlib.md5(open(f,'rb').read()).hexdigest()

def funkcja(path):
    if not os.path.isdir(path):
        print('Nie ma takiego folderu!')
    else:
        md5_dict={}
        for root, files in os.walk(path):
            for f in files:
                if not md5(os.path.join(root,f)) in md5_dict:
                    md5_dict.update({md5(os.path.join(root,f)):[os.path.join(root,f)]})
                else:
                    md5_dict[md5(os.path.join(root,f))].append(os.path.join(root,f))
        for key in md5_dict:
            while len(md5_dict[key])>1:
                for item in md5_dict[key]:
                    os.remove(item)
                    md5_dict[key].remove(item)
        print('Zrobione!')


path = '/Users/admin/Desktop/tosend/'
a = input("Podaj sciezke, np:" + str(path) + " :")
main(a) 
funkcja(a)