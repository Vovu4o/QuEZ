# MaLkuTeam presents: QuEZ - Fast Keyphrase Extraction and Clustering from Reviews
![Logo](https://github.com/Vovu4o/QuEZ/blob/main/readme_white_red.png)

## Description
Raw data from **survey** results are often redundant and include many synonyms, colloquialisms, or even obscene language. This project implements an algorithm for analyzing the totality of survey results, converting raw data into an interpreted **word cloud** to facilitate their analysis. A distinctive feature of the presented solution is that the algorithm does **not use neural networks**, which significantly speeds up its work. In addition, a **web service** has been implemented that can accept a **csv file** with survey results for processing and output a **json file** with a cloud of words (of the form: "main words of the cluster" - <number_of_words_in_the_cluster>).

## Creators (MaLkuTeam):
- Konstantin Kislov (telegram: @Kislov_Konstantin) - AI
- Kovalenko Vladimir (telegram: @username_049) - backend, fronted
- Timokhin Ivan (telegram: @ssstrudel) - fronted, design

## Features

- **Keyphrase Extraction:** Uses the YAKE algorithm for extracting keyphrases from text.
- **Lemmatization:** A method from the PyMystem3 determines the initial form of a word.
- **Word Embedding:** Leverages the Navec pre-trained word embedding model for representing words as vectors.
- **Clustering:** Employs KMeans clustering to group similar keyphrases together.
- **Result Visualization:** Generates a concise output summarizing the extracted keyphrases and their clusters in a JSON file.
- **Speed:** The API-wrapped solution processes 1000 reviews in 5 seconds or less, with local use of the script, the running time is reduced to 2-3 seconds.

## Requirements

- Python 3.6+
- [YAKE](https://pypi.org/project/yake/) 
- [Navec](https://github.com/natasha/navec) 
- [PyMystem3](https://pypi.org/project/pymystem3/)
- [Joblib](https://pypi.org/project/joblib/)
- [Tqdm](https://pypi.org/project/tqdm/)
- [Scikit-learn](https://pypi.org/project/scikit-learn/)
- [NLTK](https://pypi.org/project/nltk/)

## Usage via the website
...

## Local Usage

1. **Install required packages:**
   ```python
   !pip install yake
   !pip install navec
   !pip install pymystem3
   !pip install tqdm
   !pip install joblib
   !pip install sklearn
   !pip install numpy
   ```
3. **Download the NaVec model:**
   ```python
   !wget https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar
   ```
5. **Import required packages and load the NaVec model**:
   ```python
   import pandas as pd
   import yake
   from pymystem3 import Mystem
   from tqdm import tqdm
   from joblib import Parallel, delayed
   from sklearn.cluster import KMeans
   import numpy as np
   import pandas as pd
   import csv
   import json
   from navec import Navec
   path = '/content/navec_hudlit_v1_12B_500K_300d_100q.tar'
   navec = Navec.load(path)
   ```
6. **Prepare your review data:** Create a CSV file named reviews.csv with one review per line.

7. **Run the script:**
   ```python
   #Reading reviews from a csv file:
   def read_sentences_from_csv(content):
      sentences = []
      with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
         reader = csv.reader(csvfile)
         for row in reader:
            sentences.append(row[0])
      return sentences

   #Defining the initial form of keywords:
   def lemmatize(text):
      m = Mystem()
      merged_text = "|".join(text)
      doc = []
      res = []
      for t in m.lemmatize(merged_text):
         if t != '|':
            doc.append(t)
         else:
            res.append(doc)
            doc = []
      return res
   
   #Clustering of keywords using the K-means algorithm and vector representations of words from the NaVec model:
   def cluster_words_with_vectors(words,n, navec):
      vectors = [navec[word[0]] for word in words if word[0] in navec]
      kmeans = KMeans(n_clusters=n, random_state=0)
      clusters = kmeans.fit_predict(vectors)
      clustered_words = {}
      for i, cluster_id in enumerate(clusters):
         if cluster_id not in clustered_words:
            clustered_words[cluster_id] = []
         clustered_words[cluster_id].append(words[i])
      return clustered_words

   #Converting the dictionary of the received clusters into the dictionary of the interpreted word cloud:
   def cluster_dict_to_compact_dict(cluster_dict,n_clusters):
      compact_dict = {}
      for cluster_id in range(n_clusters):
      cluster = cluster_dict[cluster_id]
      all_words = [word for sublist in cluster for word in sublist]
      uniq = []
      sorted_words = sorted(all_words, key=all_words.count, reverse=True)
      for i in range(len(sorted_words)):
         if not(sorted_words[i] in uniq) and len(uniq)<3:
            uniq.append(sorted_words[i])
         if len(uniq)==3:
            break
      key = '/'.join(uniq[:3])
      if len(key.split('/')) < 3:
         key = '/'.join(uniq[:2])
      if len(key.split('/')) < 2:
         key = uniq[0]
      compact_dict[key] = len(all_words)
      return compact_dict
   
   #Pipeline:
   def kw_from_file(file, navec):
      newlst = read_sentences_from_csv(file)
      extractor = yake.KeywordExtractor(
         lan="ru",
         n=1,
         dedupLim=0.3,
         top=1
      )
      for i in range(len(newlst)):
         newlst[i] = newlst[i].lower()
      ans = []
      for i in range(len(newlst)):
         ans.append(extractor.extract_keywords(newlst[i])[0][0])
      batch_size = 1000
      text_batch = [ans[i: i + batch_size] for i in range(0, len(ans), batch_size)]
      processed_texts = Parallel(n_jobs=-1)(delayed(lemmatize)(t) for t in tqdm(text_batch))[0]
      ans = [processed_texts[i] for i in range(len(processed_texts))]
      lst_for_check_len = [word for sublist in ans for word in sublist]
      n_clusters = len(set(lst_for_check_len))
      if n_clusters > 10:
         n_clusters = 10
      clusters = cluster_words_with_vectors(ans, n_clusters, navec)
      ans = cluster_dict_to_compact_dict(clusters,n_clusters)
      return ans

   #Main:
   file = "input_your_csv_file_path.csv"
   key_dict = kw_from_file(file,navec)
   with open("QuEZ.json", 'w', encoding='utf-8') as f:
      json.dump(key_dict, f, ensure_ascii=False, indent=4)
   #End of the script
   ```
4. **Output:** The script will output a JSON file named QuEZ.json containing the main words from the clusters and the number of words in each.

## Example

**Input (input.csv):**
   ```
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
   ```

**Output (QuEZ.json):**
   ```
    {'ценность': 1, 
     'компания': 2, 
     'подход': 1, 
     'рост': 1, 
     'среда': 1, 
     'отрасль': 1, 
     'профессионал': 1, 
     'развитие': 1}
   ```
