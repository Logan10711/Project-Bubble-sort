import gradio as gr
import matplotlib.pyplot as plt
import io
from PIL import Image
import time

def bubble_sort_frames(arr):
    a = arr[:]
    n = len(a)
    frames = []
    for i in range(n):
        for j in range(0, n - i - 1):
            # Highlight the two bars being compared
            colors = ['skyblue'] * n
            colors[j] = 'red'
            colors[j+1] = 'red'
            
            fig, ax = plt.subplots(figsize=(4,2.5))
            bars = ax.bar(range(n), a, color=colors)
            
            # Add numbers on top of bars
            for bar, num in zip(bars, a):
                ax.text(
                    bar.get_x() + bar.get_width()/2,
                    num + 0.1,
                    str(num),
                    ha='center',
                    va='bottom',
                    fontsize=10,
                    color='black'
                )
            
            ax.set_title(f"Comparing indices {j} and {j+1}")
            ax.set_xticks([])
            ax.set_ylim(0, max(arr) * 1.1)
            
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)
            frames.append(Image.open(buf))
            
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
                # After swap frame
                fig, ax = plt.subplots(figsize=(4,2.5))
                bars = ax.bar(range(n), a, color=colors)
                
                # Add numbers on top of bars
                for bar, num in zip(bars, a):
                    ax.text(
                        bar.get_x() + bar.get_width()/2,
                        num + 0.1,
                        str(num),
                        ha='center',
                        va='bottom',
                        fontsize=10,
                        color='black'
                    )
                
                ax.set_title(f"Swapped {j} and {j+1}")
                ax.set_xticks([])
                ax.set_ylim(0, max(arr) * 1.1)
                
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                plt.close(fig)
                buf.seek(0)
                frames.append(Image.open(buf))
    # final sorted frame
    fig, ax = plt.subplots(figsize=(4,2.5))
    bars = ax.bar(range(n), a, color='lightgreen')
    
    for bar, num in zip(bars, a):
        ax.text(
            bar.get_x() + bar.get_width()/2,
            num + 0.1,
            str(num),
            ha='center',
            va='bottom',
            fontsize=10,
            color='black'
        )
    
    ax.set_title("Sorted")
    ax.set_xticks([])
    ax.set_ylim(0, max(arr) * 1.1)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    frames.append(Image.open(buf))
    return frames

def visualize(arr_text):
    try:
        arr = [int(x.strip()) for x in arr_text.split(",") if x.strip() != ""]
    except:
        return "Invalid input — enter commas", None
    frames = bubble_sort_frames(arr)
    return None, frames

with gr.Blocks() as demo:
    gr.Markdown("## Bubble Sort Visualizer")
    inp = gr.Textbox(label="Enter numbers separated by commas", value="5,3,8,1,2")
    btn = gr.Button("Visualize Sort")
    gallery = gr.Gallery(label="Sorting Steps", elem_id="gallery", show_label=True, columns=1, height=300)
    msg = gr.Textbox(label="Messages")
    
    btn.click(visualize, inp, [msg, gallery])

demo.launch()
