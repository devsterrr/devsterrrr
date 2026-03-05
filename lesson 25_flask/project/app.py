from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

events = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        date = request.form.get('date')
        time = request.form.get('time')
        priority = request.form.get('priority')

        if title:
            events.append({
                'title': title,
                'date': date,
                'time': time,
                'priority': priority
            })

        return redirect(url_for('index'))

    return render_template('index.html', events=events)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(events):
        events.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)