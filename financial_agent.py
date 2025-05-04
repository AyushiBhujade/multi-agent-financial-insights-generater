from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
import openai 

import os 
from dotenv import load_dotenv 
load_dotenv() 
# openai.api_key = os.getenv("OPENAI_API_KEY")


#web search agent
web_search_agent= Agent(
    name= "Web Search Agent",
    role = "Search the web for the information",
    model = Groq(
        id= "llama-3.3-70b-versatile",

        ),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True,
)

##Financial Agent
finance_agent = Agent(
    name= "Finance Agent",
    role = "Answer financial questions",
    model = Groq(
        id= "llama-3.3-70b-versatile",
        ),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True)],
    instructions = ["Use tables to display the data"],
    show_tool_calls = True,
    markdown = True,
)

multi_ai_agent= Agent(
     model = Groq(
        id= "llama-3.3-70b-versatile",
        ),
    team= [web_search_agent, finance_agent],
    instructions= ["Always include sources", "Use tables to display data"],
    show_tool_calls = True,
    markdown = True,
)


multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
