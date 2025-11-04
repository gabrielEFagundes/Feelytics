from google import genai
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel

load_dotenv()

class FormattedJson(BaseModel):
    # most engaged posts
    most_scored_post_title: str
    most_scored_post_body: str
    most_scored_post_author: str
    most_scored_post_score: int

    second_most_scored_post_title: str
    second_most_scored_post_body: str
    second_most_scored_post_author: str
    second_most_scored_post_score: int

    #top dashboards
    amount_of_relevant_posts_on_analysis: int
    topic_engajement_level_in_word: str
    one_emoji_popular_opinion_about_topic: str

    #general posts
    three_similar_topics_in_one_word: list[str]
    main_subreddit_about_topic: str
    about_main_subreddit: str

    resume_about_analysis_and_popular_opinion: str

def summarizeJson(jsonData):
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=("Analyze this json and replace what you found on the Formatted Json: ", jsonData),
        config={
            'response_mime_type': 'application/json',
            'response_schema': list[FormattedJson]
        }
    )

    return json.dumps(response.text)