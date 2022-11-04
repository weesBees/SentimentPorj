from textblob import TextBlob
data=input("How are you ?")
x=TextBlob(data)
sentiScore=x.sentiment.polarity
print(sentiScore)