from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

## This code defines a class, ChainOfThoughtProcessor, which interacts with OpenAI's GPT-3.5 model to help break down and refine reasoning in response to a query. It accomplishes this in two main steps: developing reasoning steps and then refining the response based on those steps


class ChainOfThoughtProcessor:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)



## This develop_reasoning_steps method generates a step-by-step breakdown of the reasoning needed to address a query.
    def develop_reasoning_steps(self, query: str, relevant_text: str, initial_response: str) -> str:
        """Generate explicit reasoning steps"""
        cot_prompt = f"""
        Given this query and relevant information, break down your reasoning process into clear steps:
        
        Query: {query}
        Relevant Information: {relevant_text}
        Initial Response: {initial_response}
        
        Please think through this step by step:
        1. What is the main intent of the query?
        2. What specific information from the relevant text addresses this?
        3. What additional context might be needed?
        4. How can we structure a comprehensive response?
        
        Format your response as numbered steps.
        """
        
        thought_process = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a logical assistant that breaks down reasoning into clear steps."},
                {"role": "user", "content": cot_prompt}
            ],
            temperature=0.3
        )

        return thought_process.choices[0].message.content
    
    
## This method refines the initial response using the reasoning steps generated in the previous method.
    def refine_response(self, query: str, relevant_text: str, thought_steps: str) -> str:
        """Refine response based on thought steps"""
        refinement_prompt = f"""
        Based on this detailed reasoning process, generate a refined, coherent response:
        
        Query: {query}
        Relevant Information: {relevant_text}
        Reasoning Steps: {thought_steps}
        
        Provide a clear, well-structured response that follows from these reasoning steps.
        """
        
        refined_response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides well-reasoned responses."},
                {"role": "user", "content": refinement_prompt}
            ],
            temperature=0.3
        )
        
        return refined_response.choices[0].message.content
