from subprocess import run

def run_file(dataset_path):
    # Load the dataset
    import pandas as pd
    dataset = pd.read_csv(dataset_path)

    # Model implementation steps:
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=3, random_state=5)
    features = dataset[['age', 'Medu', 'Fedu', 'studytime', 'failures', 'absences']]
    kmeans.fit(features)
    cluster_counts = pd.Series(kmeans.labels_).value_counts()    
    cluster_counts.to_csv('k.txt', header=False)

# Call final.sh script
run(["bash", "final.sh"])