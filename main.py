# Task 1 

import threading

def even():
    for i in range(30, 51):
        if i % 2 == 0:
            print("Even:", i)

def odd():
    for i in range(30, 51):
        if i % 2 != 0:
            print("Odd:", i)




# Task 2 

import os
import requests


def mp3_downloader(url, dest):
    try:
        response = requests.get(url, stream=True)
        
        with open(dest, 'wb') as f:
            for data in response.iter_content(chunk_size=1024):
                
                if data:
                    f.write(data)
        print(f"Downloaded {url} to {dest}")
        
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def downloader():
    urls = [ "url_1", "url_2", "url_3", "url_4"]

    if not os.path.exists('Downloaded Files'):
        os.makedirs('Downloaded Files')

    threads = []
    
    for url in urls:
        filename = f"mp3_files/file_{url}.mp3"
        thread = threading.Thread(target=mp3_downloader, args=(url, filename))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Files Have Been Downloaded")

if __name__ == "__main__":
    
    thr1 = threading.Thread(target=even)
    thr2 = threading.Thread(target=odd)

    thr1.start()
    thr2.start()

    thr1.join()
    thr2.join()
    
    downloader()
