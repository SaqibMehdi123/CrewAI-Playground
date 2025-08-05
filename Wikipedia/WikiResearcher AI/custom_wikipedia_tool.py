# custom_wikipedia_tool.py
import wikipedia
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class WikipediaSearchInput(BaseModel):
    """Input schema for Wikipedia search"""
    query: str = Field(..., description="The topic to search on Wikipedia")

class WikipediaSearchTool(BaseTool):
    name: str = "search_wikipedia"
    description: str = "Searches Wikipedia and returns a summary for a given query"
    args_schema: Type[BaseModel] = WikipediaSearchInput
    
    def _run(self, query: str) -> str:
        """Execute the Wikipedia search"""
        try:
            # Set a reasonable sentence limit and auto_suggest for better results
            summary = wikipedia.summary(query, sentences=5, auto_suggest=True)
            return f"Wikipedia Summary for '{query}':\n\n{summary}"
        except wikipedia.exceptions.DisambiguationError as e:
            # Return the first few options for disambiguation
            options = e.options[:5]  # Limit to first 5 options
            return f"Multiple entries found for '{query}'. Please be more specific. Options include: {', '.join(options)}"
        except wikipedia.exceptions.PageError:
            return f"No Wikipedia page found for '{query}'. Please check the spelling or try a different search term."
        except Exception as e:
            return f"An error occurred while searching Wikipedia: {str(e)}"