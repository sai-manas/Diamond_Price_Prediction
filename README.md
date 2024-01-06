## Diamond Price Prediction


## 
1. **Clone the GitHub Repository:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
    ```bash
    cd path/to/your/directory
    
    # Run the following command to clone the GitHub repository:
    git clone https://github.com/sai-manas/Diabetes_Predictor_ML.git
    cd Diabetes_Predictor_ML
    ```

3. **Install Git (if not already installed):**
   - If you don't have Git installed, you can download and install it from the [official Git website](https://git-scm.com/).

4. **Delete Artifacts:**
    - Before running the training pipeline, delete all the files from the artifacts folder:
    ```bash
    rm -rf artifacts/*
    ```

5. **Install Python and/or Conda (if not already installed):**
    - If you haven't already, make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

    - Alternatively, if you prefer using Conda, you can install it from the [official Conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

6. **Open Terminal or Command Prompt (or VS Code):**
    - Open your terminal or command prompt. If you prefer using Visual Studio Code (VS Code), you can open it in the project directory:
    ```bash
    code .
    ```

7. **Navigate to the Directory:**
    - Navigate to the cloned repository:
    ```bash
    cd Diabetes_Predictor_ML
    ```

8. **Create and Activate Virtual Environment (Optional but recommended):**
    - It's a good practice to create a virtual environment to isolate the dependencies of your project. You can create a virtual environment using the following command:
    ```bash
    # Using conda (if you have conda installed):
    conda create --name your_env_name python=3.8
    conda activate your_env_name

    # OR using Python's built-in venv (if you prefer):
    python -m venv your_env_name
    # On Windows:
    your_env_name\Scripts\activate
    # On macOS and Linux:
    source your_env_name/bin/activate
    ```

9. **Install Required Packages using setup.py:**
    - Navigate to the root folder of your cloned repository and run the following command to install the required Python packages listed in the setup.py file:
    ```bash
    python setup.py install
    ```

10. **Run Training Pipeline:**
    - Run the training pipeline script in the terminal. This process will generate necessary files, such as pickles and CSVs, inside the artifacts folder:
    ```bash
    python src/training_pipeline.py
    ```

    *Running the training pipeline will generate files, including pickles and CSVs, inside the artifacts folder.*

11. **Run Flask Application:**
    - Once the training is complete, you can start the Flask application. In your repository's root folder, you should typically have a file named `application.py`, which is the main Flask application file:
    ```bash
    python application.py
    ```

12. **Access the Application:**
    - Your Flask application should now be running. You can access it in your web browser by navigating to [http://localhost:5000](http://localhost:5000) or the URL provided by your application.
