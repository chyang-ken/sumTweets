

import os,re
from datetime import datetime,timedelta
import pandas as pd
import requests
from bs4 import BeautifulSoup
from litellm import completion
import litellm
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from markdown import markdown
from dotenv import load_dotenv, find_dotenv

litellm.set_verbose=True

model='openai/gpt-3.5-turbo-1106'

prompt = '''content 0,"02 Jan 2024 12:06:01@joaomdmoura:

Someone hunted crewAI on @ProductHunt and we are now #2 and closing in on #1 🙃 Not sure I was ready for it, but let's go (?!) If you don't mind voting, to would nbe much appreciated 🙏 producthunt.com/posts/crewai

" 1,"02 Jan 2024 11:27:34@RisingSayak:
🧨 diffusers reached 20k stars on GitHub 💫

But like many others, I am not a firm believer in this metric. So, let's also consider the number of repos that rely on it and the SUM of their stars. This gives a better view point about the library 🤗

Thanks to all our contributors for making it awesome!

 " 以上是一些推，你是一名中文专栏『AI/人工智能/Artificial Intelligence最新资讯』的资深作者，请在以上推中，挑选出和『AI/人工智能/Artificial Intelligence』相关信息(若有)的推,汇编成一篇用排版的中文文章，包含发推时间、作者(若有)、推特链接(若有)和推特内容以及你的解读和评论，如果没有AI/人工智能/Artificial Intelligence相关资讯请回复『NOT FOUND』'''
result = completion (model=model, messages=[{"role": "user", "content": prompt, }], api_key='sk-9ulDRvvMoPifOn4NExgwm5Nx3XiMtkYuPr7sg0OMOcGIsYNa',
                base_url='https://api.chatanywhere.tech')["choices"][0]["message"]["content"]
print(result)

