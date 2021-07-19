# Simple read/write images using OpenCV

A simple code snippet to read, and write images using the Python OpenCV library.
**Python >= 3.6**

## Windows

### Step 1 - Clone repository

    git clone https://github.com/BehzadRp98/ReadWriteImage_Python_Component.git

### Step 2 - Optional step
It is recommended that a virtual environment be enabled to install and test the code snippet.

##### 1 - Install python virtual enviroment

    python -m pip install virtualenv

##### 2 - Create a virtual enviroment

    python -m venv rwImages

##### 3 - Activate virtual enviroment

    rwImagesEnv\Scripts\activate

### Step 3 - Install requirements

    python -m pip install -r requirements.txt

### Step 4 - Quick start
To test the repository quickly there is a flower photo in "images" folder:

    python rwImages.py --input images\flower.jpg --output out.png

All options:

    python rwImages.py --help
    usage: rwImages.py [-h] --input INPUT --output OUTPUT
    
    Read and write images
    
    optional arguments:
      -h, --help       show this help message and exit
      --input INPUT    [REQUIRED] Source image path
      --output OUTPUT  [REQUIRED] Destination image path like: output.jpg

## Unbutu
### Step 1 - Clone repository

    git clone https://github.com/BehzadRp98/ReadWriteImage_Python_Component.git

### Step 2 - Optional step
It is recommended that a virtual environment be enabled to install and test the code snippet

##### 1- Install python virtual enviroment

    python3 -m pip install virtualenv

##### 2 - Create a virtual enviroment

    python3 -m venv rwImages

##### 3 - Activate virtual enviroment

    source ./rwImages/bin/activate

##### NOTE: If virtual enviroment activated use "python" instead of "python3"

### Step 3 - Install requirements

    python3 -m pip install -r requirements.txt

### Step 4 - Quick start
To test the repository quickly there is a flower photo in "images" folder:

    python3 rwImages.py --input ./images/flower.jpg --output ./out.png

All options:

    python3 rwImages.py --help
    usage: rwImages.py [-h] --input INPUT --output OUTPUT
    
    Read and write images
    
    optional arguments:
      -h, --help       show this help message and exit
      --input INPUT    [REQUIRED] Source image path
      --output OUTPUT  [REQUIRED] Destination image path like: output.jpg

## Raspberry Pi 4

### Step 1 - Clone repository

    git clone https://github.com/BehzadRp98/ReadWriteImage_Python_Component.git

### Step 2 - Optional step
It is recommended that a virtual environment be enabled to install and test the code snippet

##### 1 - Install python virtual enviroment

    python3 -m pip install virtualenv

##### 2 - Create a virtual enviroment

    python3 -m venv rwImages

##### 3 - Activate virtual enviroment

    source ./rwImages/bin/activate

##### NOTE: If virtual enviroment activated use "python" instead of "python3"

### Step 3 - Install requirements
OpenCV is the only requirement of this repository. To install it on Raspberry Pi 4, follow steps in https://qengineering.eu/install-opencv-4.3-on-raspberry-pi-4.html

### Step 4 - Quick start
To test the repository quickly there is a flower photo in "images" folder:

    python3 rwImages.py --input ./images/flower.jpg --output ./out.png

All options:

    python3 rwImages.py --help
    usage: rwImages.py [-h] --input INPUT --output OUTPUT
    
    Read and write images
    
    optional arguments:
      -h, --help       show this help message and exit
      --input INPUT    [REQUIRED] Source image path
      --output OUTPUT  [REQUIRED] Destination image path like: output.jpg
