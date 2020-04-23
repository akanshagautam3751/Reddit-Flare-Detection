
""" Import libraries """
import flask
import pandas as pd
import numpy as np
""" Import NLTK library to remove the stopwords"""
import nltk 
nltk.download('stopwords') #download stopwords
from nltk.corpus import stopwords #import stopwords
nltk.download('wordnet')
from textblob import Word
import praw #reddit api
import pickle
import request 
import requests
import json # import jsonify #to use json objects

## load the trained model and tfidf variable
model = pickle.load(open('trained_variables/model.pkl','rb'))
tfidf_variable = pickle.load(open('trained_variables/tfidf_variable.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
    	return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
    	link = flask.request.form['link']
    	predicted_flare = fetch(link)
    	return flask.render_template('main.html', original_input={'link':link}, result = predicted_flare[0])

@app.route("/automated_testing", methods=['GET', 'POST'])
def automated_testing():
	if flask.request.method == 'POST':
		file = flask.request.files['upload_file']
		lines = file.readlines()
		dict_links_flares = dict()
		for line in lines:
			link = line.decode()
			flare = fetch(link)
			dict_links_flares[link] = flare[0]
		dict_links_flares = json.dumps(dict_links_flares) #convert the dictionary to string object
		json_links_flares = json.loads(dict_links_flares) #convert the string to dictionary object
		return json_links_flares

def fetch(link):
	client_id = '1jhEvPDMQYI5ZQ'
	client_secret = 'OGids43hs9-E-e6iS9t1JCsW3Es'
	user_agent = 'Reddit Webscapping'
	reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent) #initializing instance
	post = reddit.submission(url = link)
	"""Extract the `title`, `body`, `comment` from the submitted link and store it in a dataframe"""
	title = post.title
	body = post.selftext
	comment = ''
	post.comments.replace_more(limit=0)
	for top_comment in post.comments.list():
		comment = comment + '' + top_comment.body
	df = pd.DataFrame([[title, body, comment]], columns=['title', 'body', 'comments'],dtype=float) #store it in a dataframe
	df = df.replace(np.nan, '', regex=True) #replace all the NaN to the empty string

	"""**Basic Pre-processing**

	**Lower case**: transform texts into lowercase to avoid the multiple copies of the same word in the future.
	"""
	df['body'] = df['body'].apply(lambda x: " ".join(x.lower() for x in x.split()))
	df['title'] = df['title'].apply(lambda x: " ".join(x.lower() for x in x.split()))
	df['comments'] = df['comments'].apply(lambda x: " ".join(x.lower() for x in x.split()))

	"""**Remove Punctuation**: Punctuation do not add any extra information when handling with text data. Therefore, removal of all punctuations leads to the reduction in the size of the features set."""
	df['body'] = df['body'].str.replace('[^\w\s]','')
	df['title'] = df['title'].str.replace('[^\w\s]','')
	df['comments'] = df['comments'].str.replace('[^\w\s]','')

	"""**Remove Stopwords**: Commonly occuring words should be removed as they do not add much value to the meaning of the document."""
	stop = stopwords.words('english') # define the stopword instance
	df['body'] = df['body'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
	df['title'] = df['title'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
	df['comments'] = df['comments'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

	"""**Lemmatization**: It is used to convert the word into it's root word"""
	df['body'] = df['body'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
	df['title'] = df['title'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
	df['comments'] = df['comments'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

	df['title_body_comments'] = df['title'] + df['body'] + df['comments']
	X_test_title_body_comments = tfidf_variable.transform(df['title_body_comments'])

	"""**Predit the test data on the trained model**"""
	y_predict = model.predict(X_test_title_body_comments)

	return y_predict
    
if __name__ == "__main__":
	app.run(debug=True)