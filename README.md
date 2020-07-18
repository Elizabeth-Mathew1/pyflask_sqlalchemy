<p>To open the website via local host</p>
<p>After cloning the repo,</p>
   <li> pip install flask</li>
   <li> cd desktop</li>
   <li>cd pyflask_sqlalchemy</li>
   <li>python3 app.py</li>
   <li> Run it via the local host :- http://127.0.0.1:5000/</li>
   <br>
   <br>
   
   <p>To create a database using Flask</p>
   <p>Command Line Prompts</p>
   <li>Flask shell</li>
   <li>from app import db</li>
   <li>db.create_all()</li>
   <li>exit()</li>
   <br>
   <br>
   <p>To insert data into table</p>
   <li>flask shell</li>
   <li>from app import db,User</li>
   <li>Enter entry into table and assign it to a key</li>
   <li>db.session.add(key name)</li>
   <li>db.session.commit</li>
    
