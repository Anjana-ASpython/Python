def emoji_replacer(message):
  
  emoji_dict={"sleepy":"🥱","drained":"😮‍💨","rich":"🤑","scared":"😨" }
  words=message.split()
  result=[]
  for word in words:
    result.append(emoji_dict.get(word.lower(),word))
  return " ".join(result)
user_input=input("enter your message:")
print("converted message is:",emoji_replacer(user_input))




   
