import requests

url = "https://reddit-flare-detection.herokuapp.com/automated_testing"
files = {'upload_file': open('sample_test_file.txt', 'rb')}
r = requests.post(url, files=files)
print (r.text)
