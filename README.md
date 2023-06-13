# Generalized Distributed Computation Approach for Parameter Scanning

**Author**: Akash Yadav 
**Email**: akashyadav23@iisertvm.ac.in

---

## General Description

The Generalized Distributed Computation Approach for Parameter Scanning is a utility script that enables distributed computing for parameter scanning tasks. It provides a generalized framework that can be used for various applications and can be easily integrated into other projects.

The script utilizes SSH and SFTP protocols to distribute tasks among multiple systems in a cluster. It supports parallel execution of tasks and provides progress monitoring capabilities. The script is designed to be user-friendly and can be configured with the necessary system details.

---

## Features

- Distributed computation for parameter scanning tasks
- Support for parallel execution using multiple systems
- Progress monitoring and status updates
- Easy configuration of cluster details
- Generalized framework for various applications
- Importable as a module for integration into other projects

---

## Getting Started

### Dependencies

The script requires the following dependencies:

- paramiko
- numpy
- multiprocessing
- tqdm

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

1. Open the script file `distributed_computation.py` in a text editor.
2. Modify the `users`, `pwds`, and `hosts` lists to include the details of your systems.
3. Save the changes.

---

## Usage

1. Import the script as a module in your project:

    ```python
    import distributed_computation
    ```

2. Call the `deploy` function, passing the name of the code file to be executed:

    ```python
    distributed_computation.deploy("code_file.py")
    ```

3. Monitor the progress of the distributed computation and retrieve the output files from the cluster.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

For any inquiries or support, please contact:

- Akash Yadav PHD232006
- Email: akashyadav23@iisertvm.ac.in

Feel free to reach out with any questions or feedback.

---

## References

If there are any references or external sources used in the project, they can be mentioned here.
