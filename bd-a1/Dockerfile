# Define the environment as ubunto
FROM ubuntu

# Install Python3, Pandas, Numpy, Seaborn, Matplotlib, scikit-learn, and Scipy packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container at '/home/doc-bd-a1/''
RUN mkdir /home/doc-bd-a1/

# Copy the dataset files to the container
COPY students.csv /home/doc-bd-a1/

# Define the default command to run when the container starts >> Open the bash shell upon container startup.
CMD ["/bin/bash"]
