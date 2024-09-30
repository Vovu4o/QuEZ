# MaLkuTeam presents: QuEZ - Fast Keyphrase Extraction and Clustering from Reviews

This project implements a Python script for extracting keyphrases from customer reviews and clustering them to generate a meaningful word cloud. 

## Features

- **Keyphrase Extraction:** Uses the YAKE algorithm for extracting keyphrases from text.
- **Lemmatization:** A method from the PyMystem3 determines the initial form of a word.
- **Word Embedding:** Leverages the NaVec pre-trained word embedding model for representing words as vectors.
- **Clustering:** Employs KMeans clustering to group similar keyphrases together.
- **Result Visualization:** Generates a concise output summarizing the extracted keyphrases and their clusters in a JSON file.

## Requirements

- Python 3.6+
- [YAKE](https://pypi.org/project/yake/) 
- [NaVec](https://github.com/natasha/navec) 
- [PyMystem3](https://pypi.org/project/pymystem3/)
- [Joblib](https://pypi.org/project/joblib/)
- [Scikit-learn](https://pypi.org/project/scikit-learn/)
- [NLTK](https://pypi.org/project/nltk/)

## Setup

1. **Install required packages:**
   - !pip install yake
   - !pip install navec
   - !pip install pymystem3
   - !pip install tqdm
   - !pip install joblib
   - !pip install sklearn
   - !pip install numpy
   - !pip install csv
   - !pip install json
   
3. **Download the NaVec model:**
   !wget https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar
   
4. **Import required packages and load the NaVec model**:
   - import yake
   - from pymystem3 import Mystem
   - from tqdm import tqdm
   - from joblib import Parallel, delayed
   - from sklearn.cluster import KMeans
   - import numpy as np
   - import csv
   - import json
   - from navec import Navec
   - path = '/content/navec_hudlit_v1_12B_500K_300d_100q.tar'
   - navec = Navec.load(path)

## Usage

1. **Prepare your review data:** Create a CSV file named reviews.csv with one review per line.
2. **Run the script:**
   python QuEZ.py
3. **Output:** The script will output a JSON file named QuEZ.json containing the main words from the clusters and the number of words in each.

## Example

**Input (sentences.csv):**
    Меня мотивирует возможность работать в команде профессионалов.
    Я стремлюсь к профессиональному развитию, которое ваша компания предлагает.
    Я ценю возможность внести свой вклад в успешное будущее компании.
    Меня привлекает динамичная и творческая атмосфера в вашей компании.
    Ваши ценности и миссия совпадают с моими личными ценностями.
    Я верю в потенциал компании и хочу быть частью ее роста.
    Ваша компания известна своим инновационным подходом, что меня вдохновляет.
    Мне нравится, что компания фокусируется на [отрасль/сфера деятельности].
    Я впечатлен вашим вниманием к сотрудникам и созданием благоприятной рабочей среды.
    Ваша компания предоставляет отличные возможности для обучения и развития.

**Output (QuEZ.json):**
    {'ценность': 1, 
     'компания': 2, 
     'подход': 1, 
     'рост': 1, 
     'среда': 1, 
     'отрасль': 1, 
     'профессионал': 1, 
     'развитие': 1}
