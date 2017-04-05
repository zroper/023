import os
filenames = os.listdir('/Users/zroper/Desktop/TEMPO_protcode/Proclib_Jan2017')
os.chdir('/Users/zroper/Desktop/TEMPO_protcode/Proclib_Jan2017')
with open('/Users/zroper/Desktop/TEMPO_protcode/Proclib_Jan2017/Proclib_Jan2017compiled.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)