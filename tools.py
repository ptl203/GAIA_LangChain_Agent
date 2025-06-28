from langchain.tools import Tool
import random
from huggingface_hub import list_models
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from dotenv import load_dotenv
import subprocess
import os
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
import re

load_dotenv()


# Wikipedia Tool
def get_wikipedia_info(topic: str) -> str:
    """This tool retrieves information from Wikipedia about a given topic or query."""
    print("Executing get_wikipedia_info tool")
    try:
        wiki_tool = WikipediaQueryRun(
            api_wrapper=WikipediaAPIWrapper()
        )
        result = wiki_tool.run(topic)
        if result:
            return f"Wikipedia information for '{topic}':\n\n{result}"
        else:
            return f"No Wikipedia information found for '{topic}'. Please try a different search term."
    except Exception as e:
        return f"Error retrieving Wikipedia information: {str(e)}"

wikipedia_tool = Tool(
    name="get_wikipedia_info",
    func=get_wikipedia_info,
    description="This tool retrieves information from Wikipedia about a given topic or query. Input should be a topic name or search query."
)

# Execute Python File Tool
def execute_python_file(file_path: str) -> str:
    """This tool executes a given Python file and returns its stdout and stderr output as a string."""
    print("Executing execute_python_file tool")
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        output = f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        return output
    except Exception as e:
        return f"Error executing {file_path}: {str(e)}"
execute_python_file_tool = Tool(
    name="execute_python_file",
    func=execute_python_file,
    description="This tool executes a given Python file and returns its stdout and stderr output as a string. Input should be the path to a .py file."
)

# Get Question Python Contents Tool
def get_question_python_contents(question_id: str) -> str:
    """This tool returns the contents of the attached Python code with the same name as the question ID."""
    print("Executing get_question_python_contents tool")
    try:
        file_path = f"{question_id}.py"
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return f"Contents of {file_path}:\n{f.read()}"
        else:
            return f"File {file_path} not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"
get_question_python_contents_tool = Tool(
    name="get_question_python_contents",
    func=get_question_python_contents,
    description="This tool returns the contents of the attached Python code with the same name as the question ID."
)

# Get Question Excel Contents Tool
def get_question_excel_contents(question_id: str) -> str:
    """This tool returns the contents of an Excel file with the same file name as the question ID."""
    print("Executing get_question_excel_contents tool")
    try:
        file_path = f"{question_id}.xlsx"
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            return f"Contents of {file_path}:\n{df.to_string()}"
        else:
            return f"File {file_path} not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"

get_question_excel_contents_tool = Tool(
    name="get_question_excel_contents",
    func=get_question_excel_contents,
    description="Given a question ID string, returns the contents of an Excel file with the same name as the question ID."
)

# YouTube Transcript Tool
def get_youtube_transcript(url: str) -> str:
    """This tool retrieves the transcript of a YouTube video given its URL."""
    print("Executing get_youtube_transcript tool")
    try:
        # Extract video ID from URL
        video_id_match = re.search(r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)', url)
        if not video_id_match:
            return "Error: Could not extract video ID from the provided URL. Please provide a valid YouTube URL."
        
        video_id = video_id_match.group(1)
        
        # Get transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine all transcript parts into a single text
        full_transcript = ""
        for transcript_part in transcript_list:
            full_transcript += transcript_part['text'] + " "
        
        return f"Transcript for video {video_id}:\n\n{full_transcript.strip()}"
        
    except Exception as e:
        return f"Error retrieving transcript: {str(e)}"

youtube_transcript_tool = Tool(
    name="get_youtube_transcript",
    func=get_youtube_transcript,
    description="This tool retrieves the transcript of a YouTube video. Input should be a YouTube video URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)."
)

# Google Search Tool
def get_google_search_info(query: str) -> str:
    """This tool retrieves information from Google search about a given topic or query."""
    print("Executing get_google_search_info tool")
    try:
        search = GoogleSearchAPIWrapper()
        results = search.run(query)
        if results:
            return f"Google search results for '{query}':\n\n{results}"
        else:
            return f"No Google search results found for '{query}'. Please try a different search term."
    except Exception as e:
        return f"Error retrieving Google search information: {str(e)}"

search_tool = Tool(
    name="get_google_search_info",
    func=get_google_search_info,
    description="This tool retrieves information from Google search about a given topic or query. Input should be a search term or topic."
)

