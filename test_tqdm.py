from GPCR.utils import tqdm
import time
import requests

for _ in tqdm(range(10000), ascii=True):
    time.sleep(0.1)

def downloader():
    start = time.time()
    size = 0
    respose = req