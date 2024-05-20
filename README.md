# Voice Translator
## Tech Stack
- HuggingFace: Translation
- Whisper: Speech-to-text
- Speechrecognition: Microphone recording
- Google Text-to-Speech: Text-to-Speech
- Gradio: Interface
- Docker: Containerization

## Description
This project leverages open-source models to provide real-time speech translation capabilities. Using advanced speech recognition algorithms, it can accurately detect the language spoken in real-time, whether from a microphone input or an audio file. The system then generates synthetic audio and text translations in the target language, all with minimal latency.

Accessible through a user-friendly web interface, this solution offers seamless integration into various applications and workflows. Whether for multilingual communication, language learning, or accessibility purposes, our platform delivers efficient and reliable speech translation services to meet diverse needs.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

To install and set up this project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Artachtron/Voice-Translation.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Voice-Translation
    ```

3. **Install dependencies:**

    ```bash
    # Note: Poetry is required to manage dependencies. 
    # If you don't have Poetry installed, follow the installation guide at https://python-poetry.org/docs/#installation
    poetry install
    ```


## Usage

### From Terminal

1. **Navigate to the source directory:**

    ```bash
    cd src
    ```

2. **Run the Gradio interface:**

    ```bash
    poetry run python main.py
    ```

3. **Open the Gradio demo:**

   Click on the gradio link shown in your terminal or copy and paste in your browser.


### From container

To use this project from a Docker container, follow these steps:

1. **Ensure Docker is installed and running on your system.**

2. **Navigate to the root folder of the project:**

    ```bash
    cd Voice-Translation
    ```

3. **Build the Docker image:**

    ```bash
    docker build -t voice-translation .
    ```

4. **Run the Docker container:**

    ```bash
    docker run -p 8080:8080 voice-translation
    ```

After completing these steps, the project will be running in a Docker container, accessible on port 8080.
