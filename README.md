[![GitHub license](https://img.shields.io/github/license/SINGHxTUSHAR/EmotionDetection-Cyfuture.svg)](https://github.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/SINGHxTUSHAR/EmotionDetection-Cyfuture.svg)](https://GitHub.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/SINGHxTUSHAR/EmotionDetection-Cyfuture.svg)](https://GitHub.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/SINGHxTUSHAR/EmotionDetection-Cyfuture.svg)](https://GitHub.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/SINGHxTUSHAR/EmotionDetection-Cyfuture.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/SINGHxTUSHAR/EmotionDetection-Cyfuture.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/network/)
[![GitHub stars](https://img.shields.io/github/stars/SINGHxTUSHAR/EmotionDetection-Cyfuture.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/stargazers/)

[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/SINGHxTUSHAR/EmotionDetection-Cyfuture)

# EmotionDetection - Cyfuture
![Preview Image](https://github.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/blob/main/preview.jpg)

#### Project Overview:
This project focuses on developing a machine learning model to detect human emotions from facial expressions. Using advanced computer vision techniques and deep learning algorithms, the model identifies emotions such as happiness, sadness, anger, and more in real-time. The application is designed to be user-friendly and can be integrated into various platforms to enhance user interaction.

Developed for Cyfuture, this emotion detection system provides valuable insights into user sentiments, enabling improved customer engagement and personalized experiences.

## Workflow Description
The project follows a structured workflow consisting of six key steps:

1. **Data Collection**: We utilize the FER2013 dataset, which contains thousands of labeled facial expressions, to train our model.

2. **Data Preprocessing**: The images are preprocessed by resizing them to a uniform size, normalizing pixel values, and applying data augmentation techniques to increase the diversity of the training set.

3. **Model Building**: A convolutional neural network (CNN) is constructed with multiple layers to extract features from facial images and classify them into different emotion categories.

4. **Model Training**: The model is trained using the prepared dataset, with techniques like cross-validation and early stopping to optimize performance and prevent overfitting.

5. **Model Evaluation**: The model's accuracy is evaluated using a separate test set, with performance metrics such as precision, recall, and F1-score calculated.

6. **Deployment**: A Streamlit web application is developed to allow users to upload images or use their webcam to detect emotions in real-time.

## Requirements💻 :
Ensure you have the following dependencies installed:

- Python (version 3.11.x || 3.12.x)
- IDE: VS-CODE or Colab
- Virtual-environment (venv)
- Other dependencies (refer to the requirements.txt)

You can install the required Python packages using:

```bash
pip install -r requirements.txt
```


## Setup 💿:

- Clone the repository:
```bash
git clone https://github.com/SINGHxTUSHAR/EmotionDetection-Cyfuture.git
cd EmotionDetection-Cyfuture
```
- Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
- Activate the virtual environment:
  - On Windows:
   ```bash
   venv\Scripts\activate
   ```
  - On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```


## Contributing 📌:
If you'd like to contribute to this project, please follow the standard GitHub fork and pull request process. Contributions, issues, and feature requests are welcome!

## Suggestion 🚀: 
If you have any suggestions for me related to this project, feel free to contact me at tusharsinghrawat.delhi@gmail.com or <a href="https://www.linkedin.com/in/singhxtushar/">LinkedIn</a>.

## License 📝:
This project is licensed under the <a href="https://github.com/SINGHxTUSHAR/EmotionDetection-Cyfuture/blob/main/LICENSE">MIT License</a> - see the LICENSE file for details.
