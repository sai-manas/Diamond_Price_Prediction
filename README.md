# Diamond Price Predictor - Web Application

## Overview

Diamond Price Predictor web application predicts diamond price using Regression models. The implementation includes Linear Regression, Lasso, Ridge, ElasticNet, DecisionTree Regressor, RandomForest Regressor and KNeighbors Regressor. The selection process involved a comprehensive comparison, evaluation, and cross-validation to identify the most effective model. After rigorous cross-validation and metric analysis, the Random Forest Regressor model emerged as the optimal choice, exhibiting superior performance with an accuracy of 97%.

The Random Forest Regressor model, deemed the most reliable, has been deployed in a flask web application using AWS. The web application utilizes the `model.pkl` file, which contains the trained Random Forest Regressor model, offering a user-friendly interface for diamond price prediction.

## Screen Recording of Diamond Price Predictor Application
https://github.com/sai-manas/Diamond_Price_Prediction/assets/106865226/f8f56bf7-e8cc-4792-a29c-8631983be4f6

## Dataset Information

- **Instances:** 193573
- **Attributes:** 10 Diamonds-related attributes and 1 output attribute (Price)
- **Dataset Source Link:** https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv

## Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn , Pickle, Warnings
- **Web Framework:** Flask
- **Frontend:** HTML, CSS
- **Deployment:** AWS Elastic Beanstalk, AWS CodePipeline
  
## How to use
> Hosted this web application using Flask and deployed on AWS

### I. Flask
1. **Clone the GitHub Repository:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
    ```bash
    cd path/to/your/directory
    
    # Run the following command to clone the GitHub repository:
    git clone https://github.com/sai-manas/Diamond_Price_Prediction.git
    cd Diabetes_Predictor_ML
    ```

3. **Install Git (if not already installed):**
   - If you don't have Git installed, you can download and install it from the [official Git website](https://git-scm.com/).

4. **Delete Artifacts:**
   - Before initiating the training pipeline, it's important to ensure a clean slate by deleting all files from the 'artifacts' folder. This step helps prevent any conflicts or issues during the training process.

    **Option 1: Manual Deletion**
    - Manually delete all files inside the 'artifacts' folder. You can do this through your file explorer or terminal.

    **Option 2: Delete Using Command Line (Linux/Mac):**
    ```bash
    rm -rf artifacts/*
    ```
    
    **Option 3: Delete Using Command Prompt (Windows):**
    ```bash
    del /Q artifacts\*
    ```

    Note: The 'model.pkl' file will be generated during the training pipeline and is not uploaded to GitHub due to its large size (1.8 GB). Therefore, it is advisable to delete all files from the 'artifacts' folder and generate the files locally by following these steps

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
    cd Diamond_Price_Prediction
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

11. **Run Flask Application:**
    - Once the training is complete, you can start the Flask application. In your repository's root folder, you should typically have a file named `application.py`, which is the main Flask application file:
    ```bash
    python application.py
    ```
    
12. **Access the Application:**
    - Your Flask application should now be running. You can access it in your web browser by navigating to [http://localhost:5000](http://localhost:5000) or the URL provided by your application.

### II. AWS (ELastic Beanstalk,Code Pipeline)
1. Follow the above-mentioned steps from 1 to 10 and push your files to GitHub, then proceed to the next step outlined below.
   
2. **Deploy application using ELastic Beanstalk and Code Pipeline in AWS**
   - Refer to the steps outlined in this article for deploying a web application on AWS from GitHub as the source. URL - https://dev.to/wardaliaqat01/cicd-pipeline-hands-on-aws-code-pipeline-elastic-beanstalk-github-35n3
