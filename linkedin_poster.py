import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

browser = Browser(
	config=BrowserConfig(
		headless=False,
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)
controller = Controller()


async def main():
	task = f"""Navigate to https://www.linkedin.com/feed/ and create a post. 
	Here are the specific steps:
	
	1. Navigate to https://www.linkedin.com/feed/. Look for the text input field at the top of the page that says "Start a post".
	2. Click the input field.
	3. Write a post that is a Bold Statement about the future of work with AI agents. The context for the post: Emphasize that AI agents 
	are not replacing humans but amplifying their potential through collaboration.
    Guidelines: The post should
    - Be professional, engaging, and concise (1-2 short paragraphs).
    - Include a hook to grab attention in the first sentence.
    - Use relevant hashtags (3-5) at the end.
    - Make it provocative yet insightful.
	4. Find and click the "Post" button
	""",
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(
		task=task,
		llm=model,
		controller=controller,
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())