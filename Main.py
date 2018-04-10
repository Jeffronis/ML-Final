from watson_developer_cloud import VisualRecognitionV3
from chatterbot  import  ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

visonChatbot = ChatBot

visonChatbot.set_trainer(ChatterBotCorpusTrainer)

visonChatbot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.humor"
)

viual_recgognition = VisualRecognitionV3(
    #get my api key and set version
    version='2017-04-21',
    api_key="14f3b27357f0ec4098392574d36d491e0f446649")

img = viual_recgognition.classify(
    images_file="",
   # parameters = json.dumps({
        #create own classifer for gestures
       # 'classifier_ids': ["default"]
    #})
)
print(img)

while True:
    #user input
    inputText = input("Talk to bot")
    #get response
    response = visonChatbot.get_response(inputText)
    print(response)
