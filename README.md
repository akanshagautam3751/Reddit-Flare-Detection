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
Flares like `AskIndia`, `Scheduled`, `Photography`, `Food`, `Business/Finance`, `Politics`, `Non-Political`, `AMA`, `Policy/Economics`, `Science/Technology`, `Sports` have 100 posts each whereas `[R]eddiquette` flare has only 18 posts.

### Basic Pre-processing
* **Lowercase**: transform the text into lowercase
* **Remove Stopwords:** remove commonly occurring words as they do not add much value to the meaning of the data
* **Spelling correction:** it helps in understanding the semantics of the text better
* **Lemmatization:** it converts the word into it's root word vocalbulary
**Note:** Removal of punctuations and common occurring words with respect to the data leads to decrease in the model accuracy by 10% 

## Analysis

### Split the dataset
The data is split into `train` and `test` set. The `train` data consists of the 70% posts samples while `test` data consists 30% posts samples. 

## Results

## Reference
