# Allergies Finder

A simple Python script for detecting previously specified food allergies on an input list.

## Installation

On this [this project's page](https://github.com/rafagarci/AllergiesFinder) click on the `code` button, save and unzip the project on the directory you believe is most appropriate.

<img
    src="https://i.ibb.co/4YS6P3Q/Screenshot-2021-05-28-192306.png"
    alt="Download Code"
    class ="center"
    style="
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;}">

## Running the Program

You must have `Python 3`'s interpreter installed on your computer. You can download the latest `Python` version [here](https://www.python.org/downloads/).

### Windows

Right click the `Scrapper.py` file and select `Open with` then click on then select the `Python` interpreter of choice (must be version 3 or higher).

<img
    src="https://i.ibb.co/G2n8gXK/windows.png"
    alt="Running on Windows"
    class ="center"
    style="
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;}">

### Mac

Right click the `Scrapper.py` file and select `Open With` then click on `Python Launcher` (version 3 or higher).

<img
    src="https://i.ibb.co/kQMSNPL/MacOS.png"
    alt="Running on Mac"
    class ="center"
    style="
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;}">

### Linux

Navigate to the project's directory using the command line and run the following command:

```bash
python3 Scrapper.py
```

## Usage

### Finding Allergic Ingredients

Simply type a list of ingredients separated by commas. The program will output the previously specified allergies that the list contains and will classify them according to previously specified categories.

<img
    src="https://i.ibb.co/g6z3P88/sample-program1.png"
    alt="Sample Output"
    class ="center"
    style="
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;}">

### Adding New Allergic Ingredients and Categories

Open the `Scrapper.py` file using your text editor of choice. For example

> Windows: right click `Scrapper.py` -> `Open with` -> `Notepad`
>
> Mac: right click `Scrapper.py` -> `Open With` -> `TextEdit`
>
> Linux: `vim FolderWithProject/Scrapper.py`

There are two main global categories to which more subcategories can be added. `Do Not Use` and `Avoid`. New subcategories and their corresponding ingredients can be added to each of them.

Both lists follow a similar process when it comes to adding new subcategories and ingredients.

<img
    src="https://i.ibb.co/J30YzxM/categories.png"
    alt="Categories format"
    class ="center"
    style="
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;}">

As seen in the picture above each category is a list of lists (each enclosed with `[]`). The first inner list contains the subcategory names while the remaining lists contain the ingredients to each of these subcategories. In order to add a subcategory it is just needed to first, add the name of the subcategory in the first list and then include its ingredients, as a list, at the end. This process could be further simplified in the future upon request.

### Exiting the Program

Type `quit` and press `enter`.

## License

GNU GPLv3 © Rafael García
