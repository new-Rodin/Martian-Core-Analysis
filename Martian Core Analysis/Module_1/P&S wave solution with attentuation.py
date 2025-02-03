import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define parameters based on research paper
num_points = 200  # More points for better resolution
num_frames = 300  # More frames for smoother animation
wave_length = 10
wave_speed_p = 3574  # P-wave velocity from research paper
wave_speed_s = 1825  # S-wave velocity from research paper
frequency = 1
attenuation = 0.1  # Increased energy decay for visibility

def generate_wave(x, t, speed, wave_type='P'):
    """Generates displacement for P and S waves with attenuation"""
    k = 2 * np.pi / wave_length  # Wave number
    omega = 2 * np.pi * frequency  # Angular frequency
    phase = k * x - omega * t
    decay = np.exp(-attenuation * x)  # Amplitude decay
    
    if wave_type == 'P':
        return x, decay * np.sin(phase), np.zeros_like(x)  # Longitudinal motion
    elif wave_type == 'S':
        return x, np.zeros_like(x), decay * np.sin(phase)  # Transverse motion

def update(frame):
    """Updates animation frames"""
    t = frame / num_frames * 4 * np.pi  # Normalize time
    
    xp, yp, zp = generate_wave(x, t, wave_speed_p, 'P')
    xs, ys, zs = generate_wave(x, t, wave_speed_s, 'S')
    
    line_p.set_data(xp, yp)
    line_p.set_3d_properties(zp)
    line_p.set_alpha(0.7)  # Transparency to visualize fading
    
    line_s.set_data(xs, ys)
    line_s.set_3d_properties(zs)
    line_s.set_alpha(0.7)  # Transparency to visualize fading
    
    return line_p, line_s

# Create Tkinter window
root = tk.Tk()
root.title("P-Wave and S-Wave Simulation with Energy Decay")
frame = tk.Frame(root)
frame.pack()

# Initialize figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(0, wave_length * 2, num_points)
ax.set_xlim(0, 2 * wave_length)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_title("P-Wave vs S-Wave Animation with Energy Decay")
ax.set_xlabel("Wave Propagation")
ax.set_ylabel("P-Wave Displacement")
ax.set_zlabel("S-Wave Displacement")
ax.grid(True)

xp, yp, zp = generate_wave(x, 0, wave_speed_p, 'P')
xs, ys, zs = generate_wave(x, 0, wave_speed_s, 'S')
line_p, = ax.plot(xp, yp, zp, color='blue', linewidth=2, alpha=0.7, label="P-Wave (Longitudinal)")
line_s, = ax.plot(xs, ys, zs, color='red', linewidth=2, linestyle='dashed', alpha=0.7, label="S-Wave (Transverse)")
ax.legend()

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=False)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()

tk.Button(root, text="Exit", command=root.quit).pack()
root.mainloop()
