# Martian-Core-Analysis

This project is the final submission and sums up all the work done under the Kriti 2025 Astronomy Project, titled **"Martian Core Analysis"**. The project focuses on the theoretical and conceptual understanding of P and S waves, their propagation, behavior, shadow zones, and the overall implementation of a huge dataset and simulations to determine the state and size of Mars' core.

The project consists of 9 modules in total:
- **5 theoretical modules** focusing on material physics and seismic wave behaviors.
- **4 practical modules** based on machine learning, using regression models to predict the core radius, detecting anomalies in seismic data, and finally creating a 3D simulation of Mars.

Reports, visualizations, and simulations are uploaded in the respective modules. You can navigate through the modules via the **File Structure.md** file, which should be located just above this `README.md` file.

---

## Documentation for Running the Code

### Module 1: Wave Simulation (2D)
- **Files Included**: 2 `.py` files
- **How to Run**: 
    1. Run the script in **VS Code**.
    2. A **Tkinter window** will open, showing the simulation of seismic waves across Mars.
    3. The simulation will visualize the propagation of P and S waves.

---

### Module 2: Interactive Wave Simulation
- **How to Run**: 
    1. Run the Python script.
    2. A **Pygame window** will open.
    3. Click on the cutaway to generate a circular waveform, and interact with it.

---

### Reusable Code for the Simulation:
These functions are reused across multiple modules. 

- `get_slowness(position)`:
    - This function returns the **slowness** (analog of refractive index) for a given 2D Cartesian position on Mars.
    - Modify this function to adjust the model for your custom **P & S wave velocity** model.

- `trace_ray(origin, direction, max_steps=1000)`:
    - This function traces the ray across the 2D cutaway of Mars, starting from the **origin** and propagating in the **direction** provided.
    - The **Mathematics is implemented exactly**, so do not modify this unless you are adding more complexity to the ray tracing.

- `plot_mars_cutaway_with_rays(raypaths, mars_radius=3389.5, core_mantle_boundary=1550.0)`:
    - This function plots the ray paths on a **matplotlib** cutout of Mars.
    - **Do not modify** this function.

The mainline code calls these functions, rendering rays starting at a specific origin and across a range of directions. You can edit the range of directions as needed.

---

### Module 6: Seismic Signal Processing Using ML
- **Task 1**: 
    1. Open the `.ipynb` file on **Kaggle**.
    2. The dataset is public and contains 11 waves; the code runs on only 2 waves by default.
    3. Change the **file_path** with the dataset path provided in the Kaggle input window to process more waves.

- **Task 2**:
    1. This needs to be run in **VSCode**.
    2. Download the dataset from second link in  `Datasets` file where there are two links into the current directory.
    3. Extract the zip file.
    4. Bring `LSL_Models` in the current directory.
    5. Modify the **input_folder** and **output_folder** variables as necessary.
    6. Adjust the **folder_path** to the output folder.
    7. **Do not modify** the `out_subtends` variable (it stores ray termination points).
    8. `depthmodels = dataframes` assigns the Martian volume models in **pandas DataFrame format**.
    9. You can adjust the **range of angles** for initial ray paths or modify the **origin**.

---

### Module 7: Regression Model for Core Radius Prediction
- **How to Run**: 
    1. Ensure `LSL_models` is in the current directory.
    2. Run the provided code on VS Code.
    3. The results will be stored in `.csv` files.

---

### Module 8: Anomaly Detection in Seismic Data
- **How to Run**: 
    1. Open the file on **Kaggle** and run it directly.
    2. The dataset is publicly available.
    3. There are four parameters in the `detect_anomalies` function. 1st is file path,2nd is no. of components for KNN,3rd 
    is no. of epochs for autoencoders and last one is accuracy upto which anomaly has to be detected. 

---

### Module 9: Physics-Informed Neural Networks (PINN)
- **How to Run**: 
    1. Open the file on **Kaggle** and run it directly.
    2. The dataset is publicly available.

---

### Conclusion
This project explores the intricacies of seismic wave propagation on Mars, leveraging both theoretical knowledge and advanced machine learning techniques. The core findings regarding the Martian core's state and size are drawn from extensive data simulations and modeling. All necessary files and visualizations are available for further exploration.
