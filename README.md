## BigData Assignment 1:

### 1- creating a directory on local machine named bd-a1
### 2- Download and place the dataset students.csv in the bd-a1/ directory
### 3- Create the docker file in Dockerfile in vs for the ubunto (in the zip file)
### 4- To build the image use this command:
- docker build -t bd-a1-image (-t here is short --tag which is used to tag the Docker image with a specific name) 
### 5- To run the container from the image use this command:
- docker run -it --name bd-a1-container1 bd-a1-image
- (-it flags  indicates that you want to run an interactive session inside the container, allowing you to interact with its command-line interface.)
### 6- To move the Python files to the Docker container use this command: (cp here is a subcommand used to copy files)
#### The load.py file is responsible for loading a dataset from a specified path and then running the dpre module or script, likely for performing some data preprocessing tasks on the loaded dataset.
- docker cp load.py bd-a1-container:/home/doc-bd-a1/load.py
#### The dpre.py file handles various data preprocessing tasks such as:
- docker cp dpre.py bd-a1-container:/home/doc-bd-a1/dpre.py 
1. Data Cleaning
   - Removing irrelevant columns
   - Removing dublicates
   - Filling missing values
2. Data Transformation
   - Encodeing categorical values by hot enconding
   - Scaling numerical values
   - Performing label encoding for categorical variables
   - Replacing 'yes' with 1 and 'no' with 0 in specific columns
3. Data Reduction
   - Using SelectKBest feature selection technique with chi-square test to select the top 15 features based on the target variable
   - Performing Principal Component Analysis (PCA) to reduce the dimensionality of the dataset to 3 components.
4. Data Discretization
   - Discretizing the age column into 4 age groups
   - Discretizing the Medu column into education levels (low, medium, high, very high) using equal frequency binning.

To prepare the dataset for further analysis. Saves the resulting modified dataset as a new CSV file named res_dpre.csv. Then,go to the next file (eda.py) to perform exploratory data analysis on the modified dataset.
#### Conduct exploratory data analysis by extracting insights from the dataset:
- docker cp eda.py bd-a1-container:/home/doc-bd-a1/eda.py 
1. Insight 1: Calculates the mean age of students and writes it to a file named eda-in-1.txt.
2. Insight 2: Calculates the percentage of male and female students and writes it to a file named eda-in-2.txt.
3. Insight 3: Calculates the average absence rate of students and writes it to a file named eda-in-3.txt.

Afterwards, go to the next file (vis.py) to perform further visualization tasks on the dataset.

#### Create a countplot to visualize the distribution of students by school, then save the visualization as an image file named vis.png.
- docker cp vis.py bd-a1-container:/home/doc-bd-a1/vis.py
  
Go to the next file (model.py) to continue with further modeling tasks.

#### Implement a clustering model using the K-means algorithm from the sklearn library: Configures the K-means algorithm with 3 clusters and a random state of 5, Selects specific features (age, Medu, Fedu, studytime, failures, absences) from the dataset for clustering, Fit the K-means model to the selected features, count the number of data points in each cluster and saves the cluster counts to a file named k.txt. 
- docker cp model.py bd-a1-container:/home/doc-bd-a1/model.py 

Then, call the shell script named final.sh using the subprocess.run function from the subprocess module.

#### This file copies the output files generated by dpre.py, eda.py, vis.py, and model.py from the container to your local machine in bd-a1/service-result/. Finally, the script should stop the container.
- docker cp final.sh bd-a1-container:/home/doc-bd-a1/final.

### Note that: each Python file responsible for updating the data frame will invoke the next Python file and transmit the data frame path to it. Subsequently, read the CSV file as a data frame and continue processing.

### 7- To access the terminal of the running container use the following command:
- docker exec -it bd-a1-container /bin/bash (docker exec here is as docker run & /bin/bash it is starting an iterative bash shell)

### 8- To navigate to the directory containing load.py use this command:
- cd /home/doc-bd-a1/

### 9- To run the load.py file use this command:
- python3 load.py students.csv


### Dataset Link:
https://www.kaggle.com/datasets/larsen0966/student-performance-data-set?select=student-por.csv

### Docker Hub Link:
https://hub.docker.com/r/nermean/big_data

### GitHub Link:
https://github.com/Nermean/BigData.git
