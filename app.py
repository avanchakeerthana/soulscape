from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    analysis = None
    if request.method == 'POST':
        entry = request.form.get('journal_content')
        words = entry.split()

        # Simple Logic: Count words and identify keywords
        moods = ["happy", "productive", "calm", "tired", "stressed"]
        detected = [m for m in moods if m in entry.lower()]

        analysis = {
            "count": len(words),
            "moods": ", ".join(detected) if detected else "Neutral"
        }
    return render_template('index.html', analysis=analysis)


if __name__ == '__main__':
    app.run(debug=True)