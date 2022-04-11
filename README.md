# API in Python

A basic REST API written in Python using the Flask framework, made for a school assignment.

## Installation

**Install the dependencies**

```sh
pip install -r requirements.txt
```

**Run the app**

```sh
python server.py
```

The server runs on localhost port 5000.

[http://localhost:5000](http://localhost:5000)

## Routes

| Route | method | parameters |
| :---: | :---: | :---: |
| /articles | GET | none |
| /articles/\<id> | GET | id |
| /add-article | POST | title, content |
| /update-article | PUT | id |
| /delete-article | DELETE | id |

## Database

```sql
CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` varchar(256) NOT NULL,
  `content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
