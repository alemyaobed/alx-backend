# 0x01. Caching

## Back-end

This repository contains the implementation of a caching system. In this README, we will cover the following topics:

- What is a caching system?
A caching system is a mechanism used to store frequently accessed data in a temporary storage area, called a cache. It helps improve the performance and efficiency of a system by reducing the need to fetch data from the original source repeatedly.

- Understanding FIFO (First-In, First-Out)
FIFO, also known as First-In, First-Out, is a caching algorithm that evicts the oldest item from the cache when it is full. It follows the principle of "first come, first served."

- Understanding LIFO (Last-In, First-Out)
LIFO, also known as Last-In, First-Out, is a caching algorithm that evicts the most recently added item from the cache when it is full. It follows the principle of "last come, first served."

- Understanding LRU (Least Recently Used)
LRU, also known as Least Recently Used, is a caching algorithm that evicts the least recently used item from the cache when it is full. It assumes that the least recently used item is less likely to be used again in the near future.

- Understanding MRU (Most Recently Used)
MRU, also known as Most Recently Used, is a caching algorithm that evicts the most recently used item from the cache when it is full. It assumes that the most recently used item is more likely to be used again in the near future.

- Understanding LFU (Least Frequently Used)
LFU, also known as Least Frequently Used, is a caching algorithm that evicts the least frequently used item from the cache when it is full. It assumes that the least frequently used item is less likely to be used again in the near future.

- The purpose of a caching system
The purpose of a caching system is to improve the performance and efficiency of a system by reducing the time and resources required to fetch data from the original source. It helps to minimize latency and improve overall user experience.

- Limitations of a caching system
Caching systems have certain limitations. Some of the common limitations include cache size limitations, cache eviction policies, cache consistency issues, and cache invalidation challenges. It is important to consider these limitations while designing and implementing a caching system.

Let's dive into each topic to gain a better understanding of caching systems and their functionalities.

