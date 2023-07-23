from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import openai

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        clusters_input = request.form['cluster']
        expert = request.form['expert']
        risk = request.form['risk']
        user_questions = request.form['questions']

        

        final_prompt = f"""
        You are an expert in {expert} skilled in providing detailed analysis. You will be given as input a list of 
        clusters each containing a set of co-occurring factors, the comparative risks between pairs of clusters, followed by 
        a list of questions. Please use the input in addition to your own {expert} knowledge for answering the questions as completely as possible, and 
        in an easy-to-read format.

        The Clusters include the following:
        {clusters_input}

        The comparative risk between pairs of clusters includes the following:
        {risk}

        Please provide all answers to the following questions for a cluster, before addressing them for the next cluster:

        1. What label would best describe the co-occurring factors in each cluster?
        2. Why do the factors in each cluster co-occur?
        3. What are the potential mechanisms in each cluster?
        4. What interventions could reduce the risk in each cluster?

        Please also answer the following question:

        {user_questions}
        """
        # response = openai.Completion.create(engine="text-davinci-002", prompt=final_prompt, max_tokens=100)

        response = final_prompt
        # return render_template('index.html', generated_text=response.choices[0].text.strip(), final_prompt=final_prompt)
        return render_template('index.html', generated_text=final_prompt, final_prompt=final_prompt)

    
    return render_template('index.html', generated_text=None, final_prompt=None)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)