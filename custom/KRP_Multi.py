"""
Basic example of scraping pipeline using ScriptCreatorGraph
"""

import os

from dotenv import load_dotenv

from scrapegraphai.graphs import ScriptCreatorMultiGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()

# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = {
    "llm": {
        "model": "ollama/phi3",
        "temperature": 0,
        # "model_tokens": 2000, # set context length arbitrarily,
        "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    },
    "library": "beautifoulsoup",
    "verbose": True,
}

# ************************************************
# Create the ScriptCreatorGraph instance and run it
# ************************************************

urls = [
   "https://virginiabeach.gov",
   "https://pw.virginiabeach.gov",
   "https://cityofchesapeake.net",
   "https://portsmouthva.gov", 
   "https://suffolkva.us",
   "https://hampton.gov",
   "https://hampton.gov/4077/Public-Works",
   "https://newportnewsva.gov",
   "https://williamsburgva.gov",
   "https://jamescitycountyva.gov",
   "https://gloucesterva.gov",
   "https://yorkcountyva.gov",
   "https://poquosonva.gov",
   "https://smithfield-va.gov",
   "https://isleofwightcounty.com",
   "https://surrycountyva.gov",
   "https://www.southamptoncounty.org/",
   "https://franklinva.gov",
]

# ************************************************
# Create the ScriptCreatorGraph instance and run it
# ************************************************

script_creator_graph = ScriptCreatorMultiGraph(
    prompt="Source contact information of key role players in the development of the technologies mentioned in the following URLs: ",
    source=urls,
    config=graph_config,
)

result = script_creator_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = script_creator_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))
