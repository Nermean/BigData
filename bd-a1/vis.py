import model  # Import the next file

def run_file(dataset_path):
    # Load the preprocessed dataset
    import pandas as pd
    dataset = pd.read_csv(dataset_path)

    # Data visualization steps:
    import matplotlib.pyplot as plt
    import seaborn as sns  

    # Create a visualization
    plt.figure(figsize=(12, 8))
    sns.countplot(x='school', data=dataset)
    plt.title('Distribution of Students by school')
    plt.xlabel('school')
    plt.ylabel('Count')
    plt.savefig('vis.png')  # Save the visualization as vis.png



    # Invoke the next file
    model.run_file(dataset_path)
