# Atlaspad Chatbot-AI (NLP/LLM-Launchpad)
The chatbot receives text-based messages from users and analyzes these messages using natural language processing (NLP) techniques. During this analysis process, key words, sentence structure, and meaning are extracted from the text. Afterwards, the chatbot utilizes a trained artificial intelligence model to determine the user's intent. This model is typically fed with large amounts of data and is capable of recognizing various user intentions. Once the user's intent is identified, the chatbot generates an appropriate response. This response can vary, such as providing information, performing a task, or giving directions, based on the user's request or query. The chatbot continuously improves and enhances itself by using feedback obtained from interactions with users. This enables it to provide more accurate and effective responses over time.

# Step 1
Clone the project and move it to your local location:<br>
``` git clone https://github.com/atlaspad/Chatbot-AI.git``` 

# Step 2
Now enter the necessary command to run the project: <br>
``` docker build -t < your docker username / project name >. ``` <br>
then <br>
``` docker run -p 8080:8080 -e ENVIRONMENT=development --rm < your docker username / project name > . => This is used for developer port```  <br>
and <br>
``` docker run -p 8080:8080 -e ENVIRONMENT=development --rm < your docker username / project name > .``` 

# Architecture
<img width="944" alt="chatbot" src="https://github.com/atlaspad/Chatbot-AI/assets/95518574/e25ded0a-fa73-4bdc-86df-5fd6bbdc3758">
