from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your IBM Granite / WatsonX API key here
openai.api_key = "YOUR_IBM_GRANITE_API_KEY"
model_id = "ibm/granite-13b-chat-v1"

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        prompt = f"You are an intelligent health assistant. {user_input}"
        
        try:
            response = openai.ChatCompletion.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=150
            )
            response_text = response["choices"][0]["message"]["content"]
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
