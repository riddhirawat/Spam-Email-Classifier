# 📩 SMS Spam Detection System

## Overview

An end-to-end Natural Language Processing (NLP) project that classifies SMS messages as Spam or Ham using machine learning techniques.

## Features

* Text Cleaning and Preprocessing
* Stopword Removal
* Stemming
* TF-IDF Vectorization
* Model Comparison
* Cross Validation
* Error Analysis
* Feature Importance Analysis
* Streamlit Deployment

## Dataset

* SMS Spam Collection Dataset
* Binary Classification:

  * Ham (Legitimate Message)
  * Spam (Unwanted Message)

## Models Evaluated

* Multinomial Naive Bayes
* Logistic Regression
* Linear SVM
* Random Forest

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Cross Validation

## Key Findings

* Promotional words such as "free", "win", "claim", and "prize" strongly indicate spam.
* Logistic Regression achieved the best balance between precision and recall.
* Error analysis revealed that some promotional ham messages were misclassified due to overlapping vocabulary.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Streamlit

## Future Improvements

* Deep Learning based text classification
* BERT-based spam detection
* Multi-language support

## Run Locally

pip install -r requirements.txt

streamlit run app.py
