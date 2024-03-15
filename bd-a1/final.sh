'''
The line (#!/bin/bash) is called a shebang or hashbang. 
It is a special syntax at the beginning of a script file that tells the OS what interpreter to use to execute the script.
Here: the script should be interpreted and executed using the Bash shell.

echo: use "&&" to execute the next command only if the previous one was successful, and "||" to execute the next command only if the previous one failed.
'''
# ======================================================================================================

#!/bin/bash

# Define container name
container_name="bd-a1_docker-container"

# Define the file paths within the container
file1="/home/doc-bd-a1/eda-in-1.txt"
file2="/home/doc-bd-a1/eda-in-2.txt"
file3="/home/doc-bd-a1/eda-in-3.txt"
file4="/home/doc-bd-a1/k.txt"
file5="/home/doc-bd-a1/res_dpre.csv"
file6="/home/doc-bd-a1/vis.png"

# Define the local directory path where you want to copy the file
path="G:\0 Nermean\NU\4th Year\Semester 8\CSCI461 - Intro to Big Data\Assignment 1\bd-a1\service-result"

# Create the local directory if it doesn't exist
mkdir -p $path

# Copy the file from the Docker container to the local directory
echo "Copying files..." 
docker cp $container_name:$file1 $path && echo "File 1 copied successfully from the Docker container to your local PC." || echo "Failed to copy file from the Docker container to your local pc!" 
docker cp $container_name:$file2 $path && echo "File 2 copied successfully from the Docker container to your local PC." || echo "Failed to copy file from the Docker container to your local pc!" 
docker cp $container_name:$file3 $path && echo "File 3 copied successfully from the Docker container to your local PC." || echo "Failed to copy file from the Docker container to your local pc!" 
docker cp $container_name:$file4 $path && echo "File 4 copied successfully from the Docker container to your local PC." || echo "Failed to copy file from the Docker container to your local pc!" 
docker cp $container_name:$file5 $path && echo "File 5 copied successfully from the Docker container to your local PC." || echo "Failed to copy file from the Docker container to your local pc!" 
docker cp $container_name:$file6 $path && echo "File 6 copied successfully from the Docker container to your local PC." || echo "Failed to copy file from the Docker container to your local pc!" 

# Stop the Docker container
docker stop $container_name && echo "Docker container stopped." || echo "Failed to stop the Docker container!"

# ======================================================================================================

# #!/bin/bash

# # Copy output files from container to local machine
# docker cp bd-a1_docker-container:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
# docker cp bd-a1_docker-container:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
# docker cp bd-a1_docker-container:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
# docker cp bd-a1_docker-container:/home/doc-bd-a1/vis.png bd-a1/service-result/
# docker cp bd-a1_docker-container:/home/doc-bd-a1/k.txt bd-a1/service-result/

# # Stop the container
# docker stop bd-a1_docker-container

# ======================================================================================================
