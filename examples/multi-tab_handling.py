"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

from agent_amory_core import Agent
from langchain_openai import ChatOpenAI
import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# video: https://preview.screen.studio/share/clenCmS6
llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
    task='open 3 tabs with elon musk, trump, and steve jobs, then go back to the first and stop',
    llm=llm,
)


async def main():
    await agent.run()


asyncio.run(main())
