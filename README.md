# Unified Computing Interface (UCI) for Parameter Scanning

## General Description

The Generalized UCI (Unified Computing Interface) for Parameter Scanning is a utility script that enables distributed computing for parameter scanning tasks. It provides a generalized framework that can be used for various applications and can be easily integrated into other projects.

Parameter scanning tasks often involve running a computational model or algorithm with different input parameters to explore the behavior and output variations. However, running these tasks sequentially on a single machine can be time-consuming and inefficient, especially for large-scale parameter sets.

The UCI script addresses this challenge by leveraging the power of multiple systems in a cluster. It distributes the parameter scanning tasks across the cluster, allowing them to be executed in parallel. This significantly reduces the overall execution time and improves efficiency.

By using the UCI, researchers, scientists, and engineers can accelerate their parameter scanning experiments, enabling them to explore a larger parameter space, optimize models, analyze sensitivity, or conduct parameter-driven simulations more effectively. The script's flexibility and generalization make it suitable for various domains, including scientific research, data analysis, optimization, machine learning, and more.

Furthermore, the UCI script is designed to be user-friendly and easily adaptable. It provides functionalities for task allocation, progress monitoring, and result retrieval, simplifying the management of distributed computations. The script can also be imported as a module, allowing seamless integration into existing projects and workflows.

With the Generalized UCI for Parameter Scanning, researchers can harness the collective computational power of a cluster, unlocking new possibilities and accelerating their parameter-based investigations.

---

## Features

- Distributed computation for parameter scanning tasks
- Support for parallel execution using multiple systems
- Progress monitoring and status updates
- Task allocation based on system resources
- Result retrieval from the cluster
- Generalized framework for various applications
- Importable as a module for integration into other projects

---

## Getting Started

### Dependencies

The script requires the following dependencies:

- `paramiko` for SSH and SFTP communication
- `numpy` for array manipulation
- `multiprocessing` for parallel execution
- `tqdm` for progress monitoring

Please make sure these dependencies are installed before using the script.

### Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/repository-name.git
    ```

2. Install the required dependencies:

    ```
    pip install paramiko numpy tqdm
    ```

### Configuration

1. Open the script file `uci.py` in a text editor.
2. Modify the `users`, `pwds`, and `hosts` lists to include the details of your systems. Each entry in the lists corresponds to a system in the cluster.
3. Save the changes.

---

## Usage

1. Import the script as a module in your project:

    ```python
    import uci
    ```

2. Call the `deploy` function, passing the name of the code file to be executed:

    ```python
    uci.deploy("code_file.py")
    ```

3. Monitor the progress of the UCI computation and retrieve the output files from the cluster.



---
# Job Script 

This documentation provides an overview and usage instructions for the `job.py` script, which is part of the Unified Computing Interface (UCI) framework. The script is responsible for configuring and deploying a distributed parameter scanning computation across a cluster of machines.

## Configuration

The configuration section of the `job.py` script is where you can customize the parameters and settings for your computation. Below are the key elements of the configuration:

### Index File Generation

The index file contains the combinations of parameter values to be scanned during the computation. In this script, the index file is generated based on two parameters: `sigma` and `q`. You can modify the range and step size of these parameters to suit your specific needs.

### Saving Parameter Arrays

The parameter arrays, such as `sigma_vals` and `q_vals`, are saved as separate files using the `np.save()` function. These arrays can be useful for reference or further analysis after the computation is complete.

### Deployment

The `fname` variable specifies the name of the code file that contains the computation logic for each parameter combination. Ensure that you provide the correct file name and that the file exists in the same directory as the `job.py` script.

## Usage

To run the `job.py` script and initiate the parameter scanning computation, follow these steps:

1. Make sure you have installed the necessary dependencies, including NumPy, UCI, and any other dependencies required by your code file.

2. Open a terminal or command prompt and navigate to the directory where the `job.py` script is located.

3. Execute the following command to start the computation:

   ```bash
   python job.py

---
# Simulation Script 

## Overview

The simulation script is designed to perform parallel simulations using the multiprocessing module in Python. It loads a task file, specifies the folder to save the simulation data, and utilizes multiprocessing to process the assigned tasks concurrently.

## Configuration

Before running the script, ensure that you have the necessary dependencies installed, including NumPy and the multiprocessing module.

### Task File

The script expects a task file (`task.npy`) containing the parameter combinations for the simulations. The task file should be a NumPy array where each row represents a set of parameters. Ensure that you have the `task.npy` file available in the same directory as the script.

### Output Folder

The simulation data will be saved in a folder specified by the `path` variable. By default, the folder name is set to `'DATA/'`. If the folder already exists, it will be removed and recreated to ensure a clean output directory for the new simulations. If the folder does not exist, it will be created automatically.

## Simulation Function

The `simulate(params)` function is responsible for executing the simulations. It takes in a set of parameters, `params`, and performs the simulation accordingly. Replace the placeholder code (`...`) within the function with your simulation logic.

The function saves the simulation results in separate NumPy files based on the parameter values. The file name is constructed using the `sigma` and `q` values, and the files are saved in the `path` folder.

## Execution

To execute the simulation script, follow these steps:

1. Ensure that you have the necessary dependencies installed, including NumPy and the multiprocessing module.

2. Place the `task.npy` file in the same directory as the script.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Execute the following command to start the simulation:

   ```bash
   python script.py

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request. Follow the guidelines provided in the repository for contributing.

---

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE). You are free to use, modify, and distribute the code in accordance with the terms of the license.

---

## Contact

For any inquiries or support, please contact:

- Akash Yadav PHD232006
- Email: akashyadav23@iisertvm.ac.in

Feel free to reach out with any questions or feedback.

---

## References

If there are any references or external sources used in the project, they can be mentioned here.
