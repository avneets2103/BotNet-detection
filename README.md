# IoT Botnet Detection Using Ensemble Machine Learning

## Abstract

This research proposes an innovative approach to detect IoT botnet attacks using a variation of ensemble stacking. The study focuses on the Mirai and BASHLITE botnets, utilizing the NBAIoT dataset. By combining multiple machine learning models and leveraging prediction confidence, the approach achieves high accuracy in both binary classification (benign vs. malicious) and multi-class classification (attack types). The methodology demonstrates the potential of using prediction confidence as a more precise parameter compared to predictions alone.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Contributing](#contributing)

## Introduction

The Internet of Things (IoT) has become increasingly vulnerable to botnet attacks, posing significant security risks. This study addresses the urgent need for reliable detection and mitigation models, focusing on the notorious Mirai and BASHLITE botnets. By developing a sophisticated program for early identification and reporting of IoT botnet attacks, the research aims to enhance the security of these devices and strengthen the resilience of the IoT ecosystem.

## Dataset

The NBAIoT dataset comprises 7,062,606 instances with 115 features each, collected from 9 commercial IoT devices infected by Mirai and BASHLITE. The data includes various attack types and benign traffic. After preprocessing, the dataset was divided into two subsets: one for binary classification (danger vs. benign) and another for multi-class classification (attack types). The data was scaled, dimensionality reduced using PCA, and split into training, testing, and validation sets.

## Methodology

The methodology involves a two-stage approach:

1. **Individual Models**: Five models (XGBoost, SVM, Random Forests, ANN, and RNN) were trained on the preprocessed data for both binary and multi-class classification tasks.

2. **Ensemble Model**: The prediction probabilities from individual models were used to train a final neural network, creating a "neural network of models." This approach allows for dynamic weighting of individual model outputs.

Hyperparameter tuning was performed using techniques like Randomized Search CV and Keras-tuner to optimize model performance.

## Results

The ensemble model achieved remarkable accuracy:

- Binary Classification (Benign vs. Malicious): 99.9025%
- Multi-class Classification (Attack Types): 99.8543%

These results demonstrate the effectiveness of the proposed ensemble approach in detecting and classifying IoT botnet attacks.

## Conclusion

The study showcases the potential of using prediction confidence in ensemble stacking for improved accuracy in IoT botnet detection. The final ensemble model outperformed individual models, even though they already had high accuracies. This approach proves promising for enhancing security in IoT ecosystems.

## Future Work

Future research will focus on:

1. Applying this ensemble stacking variation to other datasets and domains.
2. Experimenting with different individual models and model combinations.
3. Exploring the effectiveness of this approach in real-time detection scenarios.
4. Investigating the model's adaptability to emerging botnet attack patterns.

## Contributing

To clone this repository and set up the project locally, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command: `git clone https://github.com/yourusername/iot-botnet-detection.git`
4. Change into the project directory: `cd iot-botnet-detection`
5. Install the required dependencies: `pip install jupyter numpy pandas seaborn warnings sklearn tensorflow matplotlib xgboost kerastuner keras joblib pickle`
6. Open the directory in Jupyter Notebook or Google Colab, and get the data from `https://www.kaggle.com/datasets/mkashifn/nbaiot-dataset` or preprocessed data by me from `https://www.kaggle.com/datasets/avneets2103/type-data-nbaiot-processed` and `https://www.kaggle.com/datasets/avneets2103/prerocessed-danger-nbaiot`
