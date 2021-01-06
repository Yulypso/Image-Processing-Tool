# Digital Image

## Author

[Thierry Khamphousone](https://www.linkedin.com/in/tkhamphousone/)

<br>

## Introduction 

This project is about creating a tool that reads an image in a given format (bitmap or jpeg), process this image (enlarge, shrink ...), save the image in an output file different from the one given as input ( same format as input or different) to never corrupt the original files.

## Get Started

__Setup__
```bash
> cd TD1
> python3 -m venv .venv

# for MacOs/Linux
> source .venv/bin/activate

#for Windows
> py -3 -m venv .venv
> .venv\scripts\activate

# to install requirements (here: numpy)
> pip3 install -r requirements.txt
```

__Note__: In Visual Studio Code, don't forget to select the correct Python interpreter. <br>

[CMD + SHIFT + P] > select Interpreter > Python 3.9.0 64-bits ('.venv') [./.venv/bin/python])

<br>

__Run the code__
```bash
> cd TD1
> python3 🐛.py --bmp ../images/<IMAGE_NAME>.bmp
```

__Stop the code__
```bash
#don't forget to deactivate the virtual environement (.venv)
> deactivate
```