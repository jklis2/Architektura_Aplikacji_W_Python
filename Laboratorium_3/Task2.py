import requests
import json
import logging 

url = 'https://jsonplaceholder.typicode.com/comments'

try:
    response = requests.get(url)

    if response.status_code == 200:
        comments = response.json()  
        enhanced_comments = []
        for comment in comments:
            char_count = len(comment['body'])  
            word_count = len(comment['body'].split()) 
            
            comment['charCount'] = char_count
            comment['wordCount'] = word_count

            
            enhanced_comments.append(comment)

        with open('enhanced_comments.json', 'w') as json_file:
            json.dump(enhanced_comments, json_file, indent=4)

    else:
        logging.warning(f"Error while retrieving data:: {response.status_code}")

except requests.exceptions.RequestException as e:
    logging.warning(f"Error occurred during HTTP request: {e}")
