import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simulate_2d_ion_diffusion(grid_size=100, diffusion_coefficient=0.1, time_step=0.1, num_time_steps=100):
    # Define grid and initial conditions
    concentration = np.zeros((grid_size, grid_size))

    # Set high concentration at multiple centers
    centers = [(15, 15), (15, 35), (25, 25), (35, 15), (35, 35)]
    for center in centers:
        concentration[center] = 1.0

    # Create a figure
    fig, ax = plt.subplots()

    # Initialize the plot
    img = ax.imshow(concentration, cmap='viridis', origin='lower')

    def update(frame):
        nonlocal concentration
        new_concentration = concentration.copy()

        for x in range(1, grid_size - 1):
            for y in range(1, grid_size - 1):
                if (x, y) not in centers:
                    new_concentration[x, y] += (
                            diffusion_coefficient * (concentration[x + 1, y] + concentration[x - 1, y] +
                                                     concentration[x, y + 1] + concentration[x, y - 1] - 4 *
                                                     concentration[x, y])
                            * time_step
                    )
        concentration = new_concentration

        img.set_array(np.array(concentration))
        ax.set_title(f"Time Step {frame + 1}")  # Update the title with the correct time step

        # Stop the animation after a specific number of time steps
        if frame + 1 >= num_time_steps:
            animation.event_source.stop()
            print("Simulation completed.")  # Indicate the end of execution

        return img,

    # Create the animation
    animation = FuncAnimation(fig, update, frames=num_time_steps, interval=1000, blit=True)

    # Display the animation
    plt.show()

    # Save the animation as a video file (optional)
    animation.save('ion_diffusion_animation.mp4', writer='ffmpeg', fps=5)

    print("Simulation completed.")  # Indicate the end of execution

# Example usage
simulate_2d_ion_diffusion(grid_size=50, diffusion_coefficient=2, time_step=0.2, num_time_steps=40)
