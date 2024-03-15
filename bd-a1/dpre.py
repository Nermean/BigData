import eda  # Import the next file

def run_file(dataset_path):
    # Load the dataset
    import pandas as pd
    dataset = pd.read_csv(dataset_path)


    # Data preprocessing steps:
    
    # (1) Data Cleaning
    # Task 1: Remove irrelevant columns 
    dataset_modified = dataset.drop(columns=['address', 'famsize'])
    # Task 2: Impute missing values in the "age" column
    dataset_modified['age'].fillna(dataset_modified['age'].median(), inplace=True)
    # Task 3: Remove duplicate rows
    dataset_modified.drop_duplicates(inplace=True)
    
    # (2) Data Transformation
    # Task 1: Encode categorical variables using one-hot encoding
    dataset_modified = pd.get_dummies(dataset_modified, columns=['sex', 'school', 'Pstatus'])
    # Task 2: Scale numerical variables using Min-Max scaling
    from sklearn.preprocessing import MinMaxScaler, LabelEncoder
    scaler = MinMaxScaler()
    dataset_modified[['age', 'Medu', 'Fedu']] = scaler.fit_transform(dataset_modified[['age', 'Medu', 'Fedu']])
    # Task 3: Perform label encoding for categorical variables
    label_encoder = LabelEncoder()
    columns = ['Mjob', 'Fjob', 'reason', 'guardian']
    for col in columns:
        dataset_modified[col] = label_encoder.fit_transform(dataset_modified[col])
    # Task 4: Replace 'yes' with 1 and 'no' with 0 
    columns = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
    dataset_modified[columns] = dataset_modified[columns].replace({'yes': 1, 'no': 0})

    # (3) Data Reduction
    # Task 1: Use SelectKBest to select the top 5 features   
    from sklearn.feature_selection import SelectKBest, chi2
    X = dataset_modified.drop('G3', axis=1) # exclude G3 (student final grade) as it is the target variable # I will need the gender(sex) of the students later on
    y = dataset_modified['G3']
    selector = SelectKBest(chi2, k=15)
    X_new = selector.fit_transform(X, y)
    # Task 2: Perform Principal Component Analysis (PCA) for dimensionality reduction
    from sklearn.decomposition import PCA
    pca = PCA(n_components = 3)
    X_pca = pca.fit_transform(X)

    # Data Discretization
    # Task 1: Discretize "age" into 2 age groups
    bins = [15, 16, 18, 20, 22]
    labels = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    dataset_modified['AgeGroup'] = pd.cut(dataset_modified['age'], bins=bins, labels=labels)
    # Task 2: Discretize 'Medu' into education levels using equal frequency binning
    dataset_modified['Medu_level'] = pd.qcut(dataset['Medu'], q=5, labels=['low', 'medium', 'high', 'very high'], duplicates='drop')


    # Save the resulting dataframe as a new CSV file named res_dpre.csv
    dataset_modified.to_csv('res_dpre.csv', index=False)


    # Invoke the next file
    eda.run_file(dataset_path)