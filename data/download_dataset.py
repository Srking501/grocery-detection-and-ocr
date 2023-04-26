import os
import requests
import tarfile
from tqdm import tqdm

url = "http://trax-geometry.s3.amazonaws.com/cvpr_challenge/SKU110K_fixed.tar.gz?ref=blog.roboflow.com"
filename = "SKU110K_fixed.tar.gz"

if os.path.exists(filename):
    print(f"{filename} already exists. Skipping download.")
else:
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)
        with open(filename, "wb") as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        print(f"Downloaded {filename} from {url}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

if os.path.exists(filename):
    extract_file = input("Do you want to extract the contents of the tar file to the current directory? (y/n) ")
    if extract_file.lower() == "y":
        with tarfile.open(filename, "r:gz") as tar_ref:
            members = tar_ref.getmembers()
            progress_bar = tqdm(total=len(members), unit="file")
            for member in members:
                tar_ref.extract(member)
                progress_bar.update(1)
        progress_bar.close()
        print(f"Extracted contents of {filename} to current working directory")
    else:
        print("Skipping extraction of tar file.")
