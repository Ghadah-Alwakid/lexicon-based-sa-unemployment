import os

files = os.listdir('lexicons_v4')
print(files)

for f in files:
    file_handle = open(os.path.join('lexicons_v4', f), encoding='utf-8')
    lines = file_handle.read().splitlines()
    file_handle.close()
    clean_lines = list(set(lines))
    file_writer = open(os.path.join('lexicons_v4', f), encoding='utf-8', mode='w')
    file_writer.write('\n'.join(clean_lines))
    file_writer.close()

print('all done')
