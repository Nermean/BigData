import vis  # Import the next file

def run_file(dataset_path):
    # Load the preprocessed dataset
    import pandas as pd
    dataset = pd.read_csv(dataset_path)

    # Exploratory data analysis steps:
    # Exploratory Data Analysis
    # Insight 1: Calculate the mean age of students
    x = dataset['age'].mean()
    with open('eda-in-1.txt', 'w') as file:
        file.write(f"Mean age of students: {x}\n")

    # Insight 2: % of male and female students
    y = dataset['sex'].value_counts(normalize=True) * 100
    with open('eda-in-2.txt', 'w') as file:
        file.write(f"Percentage of male students: {y['M']} %\n")
        file.write(f"Percentage of female students: {y['F']} %\n")

    # Insight 3: Calculate the average absence rate
    x = dataset['absences'].mean()
    with open('eda-in-3.txt', 'w') as file:
        file.write(f"Average absence rate: {x}\n")


    # Invoke the next file
    vis.run_file(dataset_path)