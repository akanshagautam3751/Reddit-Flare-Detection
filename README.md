# Reddit-Flare-Detection
Reddit Flare Detection is a web application that predicts the flares of India subreddit. This application is deployed on Heroku Servers and here's the link for the same. 

## Directory Structure
* requirements.txt : It contains all the required dependencies
* Procfile.txt : It requires to set-up Heroku
* app.py : It contains the main function to run the Flask web-application.
* data.csv : It contains all the collected data from India subreddit. 
* Notebooks : There are 2 Jupyter Notebooks in this folder. 
  * `Reddit_flare_detector_2_part_1.ipynb` contains the script required to collect the data
  * `Reddit_flare_detector_2_part_2_3_ipynb.ipynb` contains the script required to perform EDA on the collected data and then used the inferences to build a Flare Detector.  
* trained_variables : It contains the trained XGBoost Classifier Model and the trained TFIDF instance. 
* templates : It contains the main html file that will render when running the application.
* test.py: It contains the script requires to test the performance of the classifier.
* sample_test_file.txt: It contains a link of a r/india post in every line.

## Codebase
The entire code has been developed using Python programming language, utilizing it's powerful text processing and machine learning modules. The application has been developed using Flask web framework and hosted on Heroku web server.

## Project Execution
* Open the terminal
* Clone this repository using https://github.com/akanshagautam3751/Reddit-Flare-Detection.git
* Create a virtual environment for the application to work
* Activate the virtual environment
* Make sure your system has pip and python installed
* Download all the dependencies in requirements.txt using `pip install -r requirements.txt`
* Don't forget to import nltk.
* To run the application, hit `python app.py`. It will take you to http://127.0.0.1:5000/

## Approach

### Data Collection
Collect `1118` Reddit posts of `12` flares using the Reddit API `praw`. 

![sample](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/samples.JPG)


Flares like `AskIndia`, `Scheduled`, `Photography`, `Food`, `Business/Finance`, `Politics`, `Non-Political`, `AMA`, `Policy/Economics`, `Science/Technology`, `Sports` have 100 posts each whereas `[R]eddiquette` flare has only 18 posts.

### Basic Pre-processing
* **Lowercase**: transform the text into lowercase
* **Remove Stopwords:** remove commonly occurring words as they do not add much value to the meaning of the data
* **Spelling correction:** it helps in understanding the semantics of the text better
* **Lemmatization:** it converts the word into it's root word vocalbulary
**Note:** Removal of punctuations and common occurring words with respect to the data leads to decrease in the model accuracy by 10% 

### Analysis
Use `tokenizer` to generate a `WordCloud`. In `WordCloud`, the font of the word is directly proportional to the frequency of the word in the text data.

* ![wordcloud_title](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/wordclound_title.JPG)

Words like `political`, `india`, `indian food`, `photography`, `science` are the most used words in the `title` feature.

* ![wordcloud_body](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/wordcloud_body.JPG)

Words like `indian`, `india`, `https`, `people`, `government` are the most used words in the `body` feature.

* ![wordcloud_comments](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/wordcloud_comments.JPG)

Words like `people`, `india`, `time`, `good` are the most used words in the `comments` feature.

### Advance text processing

Use bi-grams to return the frequency of the sequence of two words using corpus

![bigram_title](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/bigrams_title.JPG)

![bigram_body](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/bigrams_body.JPG)

![bigram_comments](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/bigrams_comments.JPG)

### Split the dataset
The data is split into `train` and `test` set. The `train` data consists of the 70% posts samples while `test` data consists 30% posts samples. 

### Convert the textual data into meaningful features
Machines do not understand raw text data. So, to convert the text data into numeric data, Sci-kit offers powerful processing tools such as the CountVectorizer and the TFIDF Vectorizer.
The text was fed into these vectors and analysed further that proves that TFIDF Vectorizer performs better on classifier than the CountVectorizer.

### Train the model
To find the suitable model with respect to the features, the models used to fit the data are as follows: 
* Logistic Regression 
* Linear SVC 
* Naive Bayes Classifier
* Decision-Tree Classifier
* Random forest Classifier
* XGBoost Classifier 
I have obtained test accuracies simultaneously which can be found in the later section. 

## Results

The results are as follows:

* Post `title` as the only feature

  ![Result Image 1](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/results_title.JPG)


* Post `body` as the only feature

  ![Result Image 1](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/results_body.JPG)


* Post `comments` as the only feature

  ![Result Image 1](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/results_comments.JPG)


* Concatenation of post `title` and `body` as features

  ![Result Image 1](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/results_title_body.JPG)


* Concatencation of post `body` and `comments` as features

  ![Result Image 1](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/results_body_comments.JPG)


* Concatenation of post `title` and `comments` as features

  ![Result Image 1](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/results_title_comments.JPG)


* Concatenation of post `title`, `body` and `comments` as features

  ![Result Image 1](https://github.com/akanshagautam3751/Reddit-Flare-Detection/blob/master/Images/results_title_body_comments.JPG)


## Inference
It was observed that the XGBoost Classifier gave the highest accuracy of 86% using the concatenation of `title`, `body` and `comments` as features. Thus, it was used to predict the flare correctly.  
Also, using the post `body` as the only feature gave the worst accuracies on all classifiers.

## References 
* https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
* https://towardsdatascience.com/machine-learning-text-processing-1d5a2d638958
* https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
* https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b




