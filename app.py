#!/home/amber/contact.amberying.com/venv/bin/python


from flask import Flask, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

def generate_captcha():
	"""Generates two random numbers and saves them/the answer to the session."""
	num1 = random.randint(1, 10)
	num2 = random.randint(1, 10)
	session['captcha_num1'] = num1
	session['captcha_num2'] = num2
	session['captcha_answer'] = num1 + num2

@app.route("/", methods=["GET", "POST"])
def index():
	generate_captcha()
	
	if request.method == "POST":
	
		# Human validation
		user_answer = request.form.get('captcha_input')
		correct_answer = session.get('captcha_answer')
	
		# Safety Check: Ensure the session captcha hasn't expired or been cleared
		if correct_answer is None:
			flash("Session expired. Please try again.", "error")
			return redirect(url_for('index'))
	
		# Validate the answer
		try:
			if int(user_answer) == correct_answer:
				flash("Success! You are human. Form processed.", "success")
				# Clear the captcha from session so it cannot be re-used
				session.pop('captcha_answer', None)
				return redirect(url_for('index'))
		except (ValueError, TypeError):
			pass
	
		# If verification fails, reload with a fresh error
		flash("Incorrect CAPTCHA answer. Please try again.", "error")
		return redirect(url_for('index'))	
	
		# TODO: Add the user's entry into the database
	
		firstName = request.form.get("firstName")
		lastName = request.form.get("lastName")
		email = request.form.get("email")
		phone = request.form.get("phone")
		url = request.form.get("url")
		linkedin = request.form.get("linkedin")
		howWeMet = request.form.get("howWeMet")
	
		return redirect("/")
	
	else:
		render_template("index.html")

if __name__ == '__main__':
		app.run(debug=True)