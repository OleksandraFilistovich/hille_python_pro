import os
from multiprocessing import Process
from threading import Thread, current_thread
from time import perf_counter as perf

from requests import get as get_img


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing file {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    name = current_thread().name
    print(f"Downloading image from {image_url} in thread {name}")
    response = get_img(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


def main():
    img_url = "https://apod.nasa.gov/apod/image/2304/NGC1333HST33rd_800.png"

    print(f"=== Current thread: {current_thread().name} ===")
    print(f"=== Current process: {os.getpid()} ===\n")

    # REGULAR LOAD
    start_down = perf()
    download_image(img_url)
    download_counter = round(perf() - start_down, 2)

    start_encr = perf()
    encrypt_file("rock.txt")
    encryption_counter = round(perf() - start_encr, 2)

    regular_total = round(perf() - start_down, 2)

    print(
        f"= Regular I/O task time: {download_counter} sec =",
        f"\n= Regular CPU task time: {encryption_counter} sec =",
        f"\n= Regular total: {regular_total} sec =\n",
    )

    # THREADS & PROCESSES LOAD
    thread_1 = Thread(target=download_image, args=(img_url,))
    thread_2 = Thread(target=download_image, args=(img_url,))

    process_1 = Process(target=encrypt_file, args=("rockyou.txt",))
    process_2 = Process(target=encrypt_file, args=("rockyou.txt",))

    start_down = perf()
    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()
    download_counter = round(perf() - start_down, 2)

    start_encr = perf()
    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
    encryption_counter = round(perf() - start_encr, 2)

    total = round(perf() - start_down, 2)

    print(
        f"= I/O task with threading time: {download_counter} sec =",
        f"\n= CPU task with multiprocessing time: {encryption_counter} sec =",
        f"\n= Total: {total} sec =\n",
    )


if __name__ == "__main__":
    main()
