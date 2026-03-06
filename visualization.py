import matplotlib.pyplot as plt
import random


def plot_all_gantt(fcfs_timeline, sjf_timeline, rr_timeline):
    fig, axs = plt.subplots(3, 1, figsize=(12, 6), sharex=True)

    algorithms = [
        ("FCFS", fcfs_timeline),
        ("SJF", sjf_timeline),
        ("Round Robin", rr_timeline)
    ]

    for ax, (title, timeline) in zip(axs, algorithms):
        process_colors = {}

        for entry in timeline:
            pid = entry[0]
            if pid not in process_colors:
                process_colors[pid] = (random.random(), random.random(), random.random())

        for entry in timeline:
            pid, start, end = entry
            ax.broken_barh([(start, end - start)], (10, 8),
                           facecolors=process_colors[pid])
            ax.text(start + (end - start)/2,
                    14,
                    pid,
                    ha='center',
                    va='center',
                    color='white',
                    fontweight='bold')

        ax.set_yticks([])
        ax.set_title(title)
        ax.grid(True)

    axs[-1].set_xlabel("Time")

    plt.tight_layout()
    plt.show()

def plot_comparison_bar(fcfs_avg, sjf_avg, rr_avg):
    import matplotlib.pyplot as plt
    import numpy as np

    labels = ["Waiting Time", "Turnaround Time", "CPU Utilization"]

    fcfs = fcfs_avg
    sjf = sjf_avg
    rr = rr_avg

    x = np.arange(len(labels))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(x - width, fcfs, width, label="FCFS")
    ax.bar(x, sjf, width, label="SJF")
    ax.bar(x + width, rr, width, label="Round Robin")

    ax.set_ylabel("Values")
    ax.set_title("Algorithm Performance Comparison")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.tight_layout()
    plt.show()
    
def plot_scalability(process_counts, fcfs_wait, sjf_wait, rr_wait):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8,5))

    plt.plot(process_counts, fcfs_wait, marker='o', label="FCFS")
    plt.plot(process_counts, sjf_wait, marker='o', label="SJF")
    plt.plot(process_counts, rr_wait, marker='o', label="Round Robin")

    plt.xlabel("Number of Processes")
    plt.ylabel("Average Waiting Time")
    plt.title("Scalability Analysis")
    plt.legend()

    plt.tight_layout()
    plt.show()
