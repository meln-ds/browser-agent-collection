import os
import sys
from pathlib import Path
from browser_use.browser.browser import Browser, BrowserConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller

"""
Example: Using the 'Scroll down' action.

This script demonstrates how the agent can navigate to a webpage and scroll down the content.
If no amount is specified, the agent will scroll down by one page height.
"""

llm = ChatOpenAI(model='gpt-4o')

browser = Browser(
	config=BrowserConfig(
		headless=False,
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)
controller = Controller()

agent = Agent(
	task = f"""Follow these instructions:
	1. Navigate to 'https://www.threads.net/' 
	2. Find the search icon on the list of icons on the left side of the screen.
	3. Click on the search icon
	4. In the search box, type 'datbike'. Hit Enter to load the posts.
	5. Read the post content on the page. Once you're done, scroll down and read more content. Repeat 2 more times.
	6. Return a paragraph summary (in English) of all content you read, and the number of posts.
    """,
	llm=llm,
	controller=controller,
	browser=browser
)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())