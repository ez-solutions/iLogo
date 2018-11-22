# iLogo
Creates a logo using wordcloud and your own photo.

## Prep Word Cloud Source
* Get the target articl and save it as text, replace `word_data.txt`
* Setup virtual env
    ```bash
    python3.6.5 -m venv venv
    ```
* Install requirements
    ```bash
    source venv/bin/activate
    pip install -r requirements.txt
    ```
* Make sure following file names are up to date:
    ```python
    data_file = "word_data.txt"
    image_file = "batman.jpeg"
    font_file = "Inconsolata for Powerline.otf"
    logo_file = "logo.jpg"
    ```
* Run
    ```bash
    python ilogo.py
    ```