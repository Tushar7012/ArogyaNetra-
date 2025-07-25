import os
import requests
from pathlib import Path
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from skinCancer.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_image(self, url: str, save_path: Path):
        try:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            response = requests.get(url, stream=True)
            response.raise_for_status() 

            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Successfully downloaded image to {save_path}")
            return True
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            raise e

    def initiate_data_ingestion(self):
        try:
            # --- Load environment variables from .env file ---
            load_dotenv()
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                raise ValueError("GROQ_API_KEY not found in environment variables. Please create a .env file and add it.")

            print("Starting data ingestion process with CrewAI using Groq.")
            
            llm = ChatGroq(
                groq_api_key=os.getenv("GROQ_API_KEY"),
                model_name="nomic-embed-text:latest"
            )

            web_scraper = ScrapeWebsiteTool()

            # --- Define the Agent with the specified LLM ---
            researcher = Agent(
                role='Senior Image Research Analyst',
                goal=f'Find all image source URLs from the gallery page: {self.config.source_url}',
                backstory=(
                    "You are an expert at parsing HTML to find direct links to images. "
                    "You meticulously scan a webpage to extract all '.jpg' or '.png' image URLs."
                ),
                verbose=True,
                allow_delegation=False,
                tools=[web_scraper],
                llm=llm # Explicitly assigning the Groq LLM to the agent
            )

            research_task = Task(
                description=(
                    f"Visit the URL {self.config.source_url} and extract the source URLs of all images you find. "
                    "Focus only on the image links themselves. Present the result as a clean Python list of URLs."
                ),
                expected_output='A Python list of strings, where each string is a direct URL to an image.',
                agent=researcher
            )

            crew = Crew(
                agents=[researcher],
                tasks=[research_task],
                process=Process.sequential
            )

            print("Crew assembled. Kicking off the research task...")
            image_url_list_str = crew.kickoff()
            
            print("CrewAI task finished. Processing found URLs.")
            image_urls = eval(image_url_list_str)
            if not isinstance(image_urls, list):
                raise ValueError("CrewAI did not return a list of URLs.")

            raw_data_dir = Path(self.config.local_data_file)
            raw_data_dir.mkdir(parents=True, exist_ok=True)
            
            print(f"Starting download of {len(image_urls)} images to {raw_data_dir}...")

            for i, url in enumerate(image_urls):
                if not url.startswith('http'):
                    base_url = '/'.join(self.config.source_url.split('/')[:3])
                    full_url = f"{base_url}{url}"
                else:
                    full_url = url
                
                image_name = f"image_{i+1}.jpg"
                save_path = raw_data_dir / image_name
                self.download_image(full_url, save_path)
            
            print("Data ingestion process completed successfully.")

        except Exception as e:
            raise e
