from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("lxyuan/distilbert-base-multilingual-cased-sentiments-student")
model = AutoModelForSequenceClassification.from_pretrained("lxyuan/distilbert-base-multilingual-cased-sentiments-student")

# Create a pipeline for sentiment analysis
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

word_list = []


my_file = open("C:\\Users\\celin\\OneDrive\\Documents\\GitHub\\hello\\transcription.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# replacing end of line('/n') with ' ' and 
# splitting the text it further when '.' is seen. 
data_into_list = data.replace('\n', ' ').split(" ") 


def scale_number(num, original_range, new_range) -> float:
    original_min, original_max = original_range
    new_min, new_max = new_range
    # Scale the number
    scaled_num = (new_max - new_min) * (num - original_min) / (original_max - original_min) + new_min
    return scaled_num


total_sum = 0
# Your text to analyze
for word in data_into_list:# here we need to put a url with a text and then split the words\
    #so that we can check each words
    text_to_analyze = word
    # Run sentiment analysis
    results = sentiment_pipeline(text_to_analyze)
    # print the result
    # print(results)
    score = results[0]['score']
    if results[0]['label'] == 'negative':
        score = -score * 8
    scaled_values = int(scale_number(score, (-1, 1), (-5, 5)))# change the scale from (-1,1) to rank(-5,...,5)
    # print(scaled_values)
    total_sum += scaled_values
        
    word_list += results
    
if round(total_sum/len(data_into_list), 3) > 5:
    print(4.999)
elif round(total_sum/len(data_into_list), 3) < -5:
    print(-4.999)
else: 
    print(round(total_sum/len(data_into_list), 3))