import nltk
import streamlit as st
import SessionState
from streamlit.script_runner import RerunException
from streamlit.script_request_queue import RerunData

def get_text(str) :
  return st.text_input('Bot:', str)

def tokenize(input) :
  tokenizer = nltk.RegexpTokenizer(r"\w+")
  tokens = tokenizer.tokenize(input)
  return tokens

def checkArr(first, check) : 
  for item in check : 
    for toFind in first : 
      if toFind == item :
        return True
  return False

def checkIfCurrentlyOnTheme(arr, curTopic) : 
  for item in arr : 
    if item[0] == 'C' : 
      return curTopic in item

st.title("""
MVP Training Bot  
""")

theme_keywords = ["Choose a topic!", "School Stress", "Bullying"]
stateChat = SessionState.get(chat = ["CONSOLE: start"])
theme = st.selectbox("Pick: ", theme_keywords, key = "themes")

if theme == "School Stress" : 
  stressIntroStr = "BOT: i kind of feel like i dont really belong at MIT....everyone here is so smart and im trying really hard but i can barely even pass my classes! i dont even go out that much, i work a lot... i still feel dumber than everyone around me. (Type 'sample' to see example responses.)"
  if checkIfCurrentlyOnTheme(reversed(stateChat.chat), "School Stress") == False :
    stateChat.chat.append("CONSOLE: topic is now School Stress")
    stateChat.chat.append(stressIntroStr)
  response1 = ["why", "explain", "more", "feel", "feeling"]
  response2 = ["when", "time", "start", "begin", "long"]
  response3 = ["myself", "me", "my"]
  response4 = ["subjects"]
  response5 = ["amazing", "worth", "great", "fantastic", "awesome"]
  inputStr = st.text_input("")
  inputArr = tokenize(inputStr)
  if inputStr != "" and st.button('Submit'): 
    inputStr = "YOU: " + inputStr
    stateChat.chat.append(inputStr)
    if checkArr(response1, inputArr) : 
      stateChat.chat.append("BOT: everything seems to be lowering my self-esteem. nothing that i do makes me feel worthy of being here ")
    elif checkArr(response2, inputArr) : 
      stateChat.chat.append("BOT: i began feeling this way midway through the semester ")
    elif checkArr(response3, inputArr) : 
      stateChat.chat.append("FEEDBACK: Try not to respond with your own experiences - you should be listening to your user's story and making sure that they feel heard. ")
    elif checkArr(response4, inputArr) :
      stateChat.chat.append("BOT: i love math and history, but i really don't understand my teacher's lecturing style and it throws me off ")
    elif checkArr(response5, inputArr) : 
      stateChat.chat.append("BOT: thanks, it's nice to have someone supporting me ")
    elif "sample" in inputArr : 
      stateChat.chat.append("BOT: Example responses include...  ) The fact that you were accepted into this school already means that you're worthy of being there.  ) I am sure that there are subjects that you excel at - could you tell me more about them? ")
    else : 
      stateChat.chat.append("BOT: you are stupid")

elif theme == "Bullying" : 
  bullyIntroStr = "BOT: i’ve recently been getting a lot of hate on social media. people keep commenting on my appearance, such as body shaming me and telling me that i can’t fit anyone’s beauty standards. it makes me feel really insecure.)"
  if checkIfCurrentlyOnTheme(reversed(stateChat.chat), "Bullying") == False :
    stateChat.chat.append("CONSOLE: topic is now Bullying")
    stateChat.chat.append(bullyIntroStr)
  response1 = ["explain", "more", "feel", "feeling", "think", "happened"]
  response2 = ["affect", "change", "matter"]
  response3 = ["others", "other", "conform", "conforming"]
  response4 = ["myself", "me", "my"]
  response5 = ["shouldnt", "cant", "dont"]
  response6 = ["amazing", "worth", "great", "fantastic", "awesome"]
  inputStr = st.text_input("")
  inputArr = tokenize(inputStr)
  if inputStr != "" and st.button('Submit'): 
    inputStr = "YOU: " + inputStr
    stateChat.chat.append(inputStr)
    if checkArr(response1, inputArr) :
      stateChat.chat.append("BOT: i just feel really hurt. whenever i post about things that i’m proud of, these haters completely destroy my self-esteem. i don’t even know how to feel anymore. ")
    elif checkArr(response2, inputArr) :
      stateChat.chat.append("BOT: how can i not take what they say to heart? i try to ignore them, but i still end up thinking about it and wondering if what they’re saying is true ")
    elif checkArr(response3, inputArr) :
      stateChat.chat.append("BOT: it’s hard to ignore the countless pictures in advertisements and magazines. everyone looks so perfect. i’m trying so hard to push myself (exercise more, eat less) to eventually look as beautiful as them. They’ll just end up making fun of me anyways so why even continue.")
    elif checkArr(response4, inputArr) :
      stateChat.chat.append("FEEDBACK: Try not to respond with your own experiences - you should be listening to your user's story and making sure that they feel heard.")
    elif checkArr(response5, inputArr) :
      stateChat.chat.append("FEEDBACK: Try not to use forceful vocabulary. Instead, you can say, “maybe this will work” or “try to think about it this way.”")
    elif checkArr(response6, inputArr) :
      stateChat.chat.append("BOT: thanks, it's nice to have someone supporting me. i feel so alone sometimes ")
    elif "sample" in inputArr :
      stateChat.chat.append("BOT: Example responses include...  ) Online haters are usually people who are insecure about themselves. They target others to compensate for their own struggles. Try not to take what they say seriously.  ) Everybody has their own body proportions. You can choose to embrace your uniqueness and ignore society’s impossible beauty norms.  ) It’s okay and normal to feel hurt, but try not to stay in this low for too long because it is not worth your time. You are so much better and stronger than this. ")
    else :
      stateChat.chat.append("BOT: you are stupid")

for elem in reversed(stateChat.chat) : 
  idChar = elem[0]
  if idChar == 'C' : 
    st.info(elem)
  elif idChar == 'B' : 
    st.success(elem)
  elif idChar == 'Y' :
    st.warning(elem)
  elif idChar == 'F' : 
    st.error(elem)

if st.button('Reset'):
    theme = st.selectbox("Pick: ", theme_keywords, key = "sex")
    stateChat.chat = ["CONSOLE: start"]
    stateStress = SessionState.get(stressStarted = False)
    raise RerunException(RerunData())