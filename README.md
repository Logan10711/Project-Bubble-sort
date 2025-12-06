---
title: Project Bubble Sort
emoji: 🏢
colorFrom: blue
colorTo: gray
sdk: gradio
sdk_version: 6.0.2
app_file: app.py
pinned: false
---
Demo

photos of code running down below

<img width="1498" height="746" alt="" src="https://github.com/user-attachments/assets/73a71e63-a3f5-4b11-8ee6-87c380cd50f1" />
<img width="1471" height="709" alt="" src="https://github.com/user-attachments/assets/96ee3958-a7ac-4d2b-8c28-4ec7e514063c" />
<img width="1487" height="719" alt="Screenshot 2025-12-06 at 3 27 46 PM" src="https://github.com/user-attachments/assets/4f691c5f-81b2-4769-acdd-dcfb1ca15dd3" />



Problem Breakdown and Computational Thinking

Bubble sort is a simple comparison-based algorithm. It looks at pairs of numbers, swaps them if they’re out of order, and keeps looping until everything is sorted. It’s not the fastest algorithm, but it’s easy to trace and great for learning how sorting works.

How the thinking breaks down:

Decomposition: Separate the task into small steps: compare, swap, repeat until no changes happen.

Pattern Recognition: Each pass pushes the largest value to the end, so the list gets more sorted with every loop.

Abstraction: Focus only on the comparisons and swaps. Ignore anything that doesn’t affect the order.

Algorithm Design: Loop through the list, check neighbors, swap if needed, and stop when a full pass has no swaps.

Steps to Run

first, input a list of numbers seperated by commas next click "visualize sort" if you inputed incorrectly, it will wait until the input fits the criteria and output a message saying to fix it if you inputed correctly, it will output a visualization of what bubble sort looks like and each step in sorting the array

Hugging Face Space

You can use the app directly here: https://huggingface.co/spaces/Logan1107/Project-Bubble-sort

Author and Acknowledgment

Made by Logan Walter. ChatGPT (level 4) helped me figure out how to set up Gradio for the Space and walked me through adding things like matplotlib.pyplot as plt for the plots and Pillow for handling image processing behind the scenes. All code was written by me and ChatGPT just walked me through how to implement and improve the visuals of my code.
