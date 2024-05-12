<h1 align="center" id="title">Quiz App</h1>

<p id="description">Welcome to the Quiz App! This is a multiple-choice question-based quiz application with email OTP-based authentication. Users can answer questions view their scores compete with others on the leaderboard and manage their personal data.</p>

<h2>🚀 Demo</h2>

[http://quiz-app-yl47.onrender.com/](http://quiz-app-yl47.onrender.com/)

<h2>Project Screenshots:</h2>

<img src="https://i.ibb.co/rs73MbS/Screenshot-187.png" alt="project-screenshot" width="100%" height="400/">

<img src="https://i.ibb.co/T1k5Yqp/Screenshot-188.png" alt="project-screenshot" width="100%" height="400/">

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Email OTP Authentication
*   User Personal Data Management
*   Multiple Choice Questions
*   Leaderboard

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the Repository</p>

```
git clone https://github.com/aditya-Kumar421/Quiz_app
```

<p>2. Create a Virtual Environment:</p>

```
python -m venv env
```

<p>3. Activate the Virtual Environment:</p>

```
env\Scripts\activate
```

<p>4. Install Dependencies:</p>

```
pip install -r requirements.txt
```

<p>5. Set Up Database:</p>

```
python manage.py migrate
```

<p>6. Run the Development Server:</p>

```
python manage.py runserver
```

<p>7. Access the Endpoints:</p>

```
http://localhost:8000/auth/otp/
```

<h2>🍰 Contribution Guidelines:</h2>

Please contribute using GitHub Flow. Create a branch add commits and open a pull request

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Django Rest Framework
*   SQLite
*   JWT
*   ReCaptcha