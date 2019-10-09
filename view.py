from flask import Flask, render_template, request, session
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.update(
    # SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Strict',
)

@app.route('/form', methods=['POST'])
def form():
  app.logger.warning("value = %s", request.form['sample'])
  session['sample'] = request.form['sample']
  return render_template('index.html')

@app.route('/value')
def value():
  if 'sample' in session:
    return session['sample']
  else:
    return 'not found'

@app.route('/')
def hello():
  return render_template('index.html')
