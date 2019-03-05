from flask import Flask
from flask import render_template

app = Flask(__name__)


link_linkedin = 'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=77se22zag9iejz&redirect_uri=http://68.183.125.29:5000&state=987654321&scope=r_basicprofile'

@app.route('/')
def home():
	return render_template('index.html',
			link_linkedin=link_linkedin
		         )


if __name__ == "__main__":
    app.run(host='0.0.0.0')

