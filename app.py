from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if data and 'prompt' in data:
        input_prompt = data['prompt']
        
        response = openai.ChatCompletion.create(
            
            model = 'gpt-3.5-turbo',
            messages = [
                {"role": "system", "content":"You are a helpful assistant that will provide in depth response to the users requests"},
                {"role": "user", "content":input_prompt}],
            temperature = 0,
            max_tokens = 2000
        )
        
        print(f"the prompt is: {input_prompt}")
        print()
        print(response)
        print()
        
        print(f"finer response is {response['choices'][0]['message']['content']}")
        return jsonify({'output': response['choices'][0]['message']['content']})
    else:
        return jsonify({'error': 'Missing prompt in request'}), 400

if __name__ == '__main__':
    app.run(debug=True)