"""Concurrency Example"""

#threading
# import threading 
# import time



# def print_numbers():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         time.sleep(1)
        


# # # Create two threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# #Start the threads
# thread1.start()
# thread2.start()

# #Wait for both threads to finish
# thread1.join()
# thread2.join()

# print("Done")


# #Asynchronous Programming with asyncio
import asyncio

async def print_numbers():
    for i in range(5):
        print(i)
        # await asyncio.sleep(1)

async def print_letters():
    for letter in 'ABCDE':
        print(letter)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(print_numbers(), print_letters())

asyncio.run(main())
print("Done")


