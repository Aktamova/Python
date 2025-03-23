Threads Homewrok 12
Exercise 1: Threaded Prime Number Checker

Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.
import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, primes, lock):
    local_primes = [n for n in range(start, end) if is_prime(n)]
    with lock:
        primes.extend(local_primes)

def threaded_prime_checker(start, end, num_threads):
    threads = []
    primes = []
    lock = threading.Lock()
    step = (end - start) // num_threads

    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step if i < num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, primes, lock))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("Prime numbers:", sorted(primes))

if __name__ == "__main__":
    start_range = 10
    end_range = 100
    num_threads = 4
    threaded_prime_checker(start_range, end_range, num_threads)

Exercise 2: Threaded File Processing

Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.
import threading
from collections import Counter

def count_words(lines, word_count, lock):
    local_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_count.update(words)
    with lock:
        for word, count in local_count.items():
            word_count[word] = word_count.get(word, 0) + count

def threaded_word_count(file_path, num_threads):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    chunk_size = len(lines) // num_threads
    threads = []
    word_count = {}
    lock = threading.Lock()
    
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[start:end], word_count, lock))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("Word frequencies:")
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = "../info.txt"  
    num_threads = 4
    threaded_word_count(file_path, num_threads)
