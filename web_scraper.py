import requests #Retrieves the information from the website
from bs4 import BeautifulSoup #Helps in parsing the information from the website
import matplotlib.pyplot as plt #Library to visualize the data collected

def main():

    #Can alter the url to the desired website, but make sure to also change class_
    url = "https://news.ycombinator.com/item?id=40846428"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    job_title = soup.find_all(class_="ind", indent=0)
    
    description = []
    #Adds only the job description into a list
    for i in job_title:
        comment = i.find_next(class_="comment")
        description.append(comment)
    
    #Dictionary of words to look out for
    keywords = {
        "python": 0,
        "javascript": 0,
        "c++": 0,
        "sql": 0,
        "frontend": 0,
        "backend": 0,
    }
    
    #Sets the text from the description to lowercase to solve case sensitivity issues
    #and splits the string at each instance of a space to create an array
    for j in description:
        comment_text = j.get_text().lower() 
        words = comment_text.split(" ") 
        #Create a set instead of a list to consider unique instances of a word (no duplicates)
        cleaned_words = set() 
        #Cleans each word and removes any unwanted characters
        for w in words:
            cleaned_word = w.strip(".,/:;!@?<>[]''") 
            cleaned_words.add(cleaned_word)

        #Parses through the cleaned data and adds one to every occurence of a key if found.
        #Each key is considered once since the set was declared previously     
        for k in keywords: 
            if k in cleaned_words: 
                keywords[k] += 1 

    #Displays the number of occurrences of each keyword as a bar graph
    print(keywords)
    plt.bar(keywords.keys(), keywords.values()) 
    plt.title("Web Scraper") 
    plt.xlabel("Languages/Software") 
    plt.ylabel("Number of Instances")
    plt.show() 


if __name__ == "__main__":
    main()