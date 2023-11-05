from google.cloud import language

from google.oauth2 import service_account

service_account_file = 'place_holder'  #service account key 

# Create a client for the Natural Language API
credentials = service_account.Credentials.from_service_account_file(service_account_file)
client = language.LanguageServiceClient(credentials=credentials)

text_to_analyze = "Backend\transcription.text.txt"  #  MIGHT BE WRONG FILE 

# Analyzing the sentiment
document = language.Document(content=text_to_analyze, type_=language.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(request={'document': document})

def scores() -> any:   # need to fix this function 
    return sentiment.document_sentiment.score






# print(sentiment.document_sentiment.score)

# import requests

# api_url = ""  # the link to the api 
# api_key = "your_api_key_here"  

# text_to_analyze = "This is a great product. I love it!"

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# data = {
#     "text": text_to_analyze
# }

# response = requests.post(api_url, headers=headers, json=data)
# result = response.json()