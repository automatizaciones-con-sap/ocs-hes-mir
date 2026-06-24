<h1>OCS CREATION AND HES RELEASE</h1>
<p>Objective: Automate the process of creating OCS and releasing HES.</p>
<p><strong>Requirements</strong></p>
<ul>
    <li>Python 3.13.5</li>
    <li>Visual Studio Code</li>
    <li>Basic knowledge of Python programming</li>
    <li>Basic knowledge of Domain-Driven Design (DDD)</li>
</ul>
<h3>Dev Guide - Local Running</h3>
<ol>
    <li>Create a virtual environment with .venv (cntrl+ñ) in command prompt with <code>python -m venv .venv</code></li>
    <li>Activate the virtual environment with <code>.venv\Scripts\activate</code></li>
    <li>Install the required dependencies with <code>pip install -r requirements.txt</code></li>
    <li>Create a .env file in the root directory</li>
    <li>Install the modules with <code>pip install python-dotenv</code></li>
    <li>Update with your credentials like <code>MY_KEY = "kishankaushik12353"</code></li>
    <li>To access the .env file use: <br><code>import os <br>from dotenv impor load_dotenv<br> load_dotenv()<br>print(os.getenv("MY_KEY"))</code></li>
</ol>
<h3>Ubiquitous Language</h3>
<ul>
    <li><strong>OC</strong>: A buy order is the request created on SAP from the facture registered by Katherine on the sharepoint.</li>
    <li><strong>HES</strong>: The service entry sheet is a document that certificates the realization of a service. These HES work with the sharepoint too.</li>
</ul>