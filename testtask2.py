import os, filecmp, time, shutil

while True:
    source = input('Enter path to source directory: ')
    if os.path.isdir(source):
        break
    print('Input correct path, please')
while True:
    target = input('Enter path to target directory: ')
    if os.path.isdir(target) and target != source:
        break
    print('Input correct path, please')
while True:
    interval = input('input interval for check (sec): ')
    if interval.isdecimal():
        interval = int(interval)
        break
    print('Input correct interval, please')

def sync_dirs(source, target):
    dirsSrc = [o for o in os.listdir(source) if os.path.isdir(os.path.join(source, o))]
    filesSrc = [o for o in os.listdir(source) if os.path.isfile(os.path.join(source, o))]
    dirsTar = [o for o in os.listdir(target) if os.path.isdir(os.path.join(target, o))]
    filesTar = [o for o in os.listdir(target) if os.path.isfile(os.path.join(target, o))]

    for dir in dirsTar:
        if dir not in dirsSrc:
            dirPath = os.path.join(target, dir)
            print('remove target dir \'{}\''.format(dirPath))
            shutil.rmtree(dirPath)
    for file in filesTar:
        if file not in filesSrc:
            filePath = os.path.join(target, file)
            print('remove target file \'{}\''.format(filePath))
            os.remove(filePath)
    for dir in dirsSrc:
        if dir not in dirsTar:
            dirPathSource = os.path.join(source, dir)
            dirPathTarget = os.path.join(target, dir)
            print('copy dir \'{}\' to \'{}\''.format(dirPathSource, dirPathTarget))
            shutil.copytree(dirPathSource, dirPathTarget)
        else:
            newSource = os.path.join(source, dir)
            newTarget = os.path.join(target, dir)
            sync_dirs(newSource, newTarget)
    for file in filesSrc:
        if file not in filesTar:
            filePath = os.path.join(source, file)
            print('copy file \'{}\' to \'{}\''.format(filePath, target))
            shutil.copy2(filePath, target)
        else:
            newSource = os.path.join(source, file)
            newTarget = os.path.join(target, file)
            if not filecmp.cmp(newSource, newTarget):
                print('replace file \'{}\' with \'{}\''.format(newTarget, newSource))
                shutil.copy2(newSource, newTarget)

while True:
    sync_dirs(source, target)
    print('sleeping {} sec'.format(interval))
    time.sleep(interval)
