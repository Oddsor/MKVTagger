import requests
import tempfile
import shutil
from scrapers import themoviedb
import subprocess

__author__ = 'Odd'

mkvprop_path = '"C:\\Program Files\\MKVToolNix\\mkvpropedit.exe"'
mkvextract_path = '"C:\\Program Files\\MKVToolNix\\mkvextract.exe"'

def download_file(name, dir, url):
    response = requests.get(url, stream=True)
    with open(dir + '/' + name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return dir + '/' + name

def attach_files(attachments, file):
    directory = tempfile.mkdtemp('attachment')
    print(directory)
    for attachment in attachments:
        print(subprocess.getoutput(mkvprop_path + ' "' + file + '"' + ' --add-attachment "' + download_file(attachment, directory, attachments[attachment]) + '"'))

if __name__ == '__main__':
    attach_files(themoviedb.get_info('100402')['attachments'], "C:\\Users\\Odd\\Desktop\\XL-TT.mka")
    #print(download_file('/cover.jpg', tempfile.mkdtemp('attachment'), 'https://image.tmdb.org/t/p/w185/gdTfrLPWhWiWFn9BEM0pPCrQrrn.jpg'))