# find the phone for you
This website uses phones that have recently been released and are put into categories to reccomend which phones have the best cameras or the best screens or the best battery life.
# Requirements
<ul>
 <li>Flask</li> 
 <li>Pymongo</li>
 <li>MongoDB</li>
 <li>Bootstrap</li>
</ul>

# Installing Flask in the terminal
```
$ pip3 install flask
```

# Installing MongoDB in the terminal
```
$ brew update
$ brew tap mongodb/brew
```

# Installing MongoDB in the terminal
```
$ brew update
$ brew tap mongodb/brew
```

# To start running MongoDb
```
$ mongosh
```

# To install PyMongo library
```
$ pip3 install pymongo
```

# Create an app.py folder and add this to the very top
```
from pymongo import MongoClient

client = MongoClient()
db = client.Phones
Phones = db.Phones
```

# Bootstrap Used for Nav Off Canvas
![Jan-12-2022 07-53-30](https://user-images.githubusercontent.com/92564077/149153833-8181b5bf-82b6-4d9a-892c-b577d9e89d25.gif)
