# **We can control the format of the response that we get back, either by using the Accept header:**

​		http http://127.0.0.1:8000/snippets/ Accept:application/json  # Request JSON
​		http http://127.0.0.1:8000/snippets/ Accept:text/html             # Request HTML

# **Or by appending a format suffix:**

​		http http://127.0.0.1:8000/snippets.json  # JSON suffix
​		http http://127.0.0.1:8000/snippets.api   # Browsable API suffix

# Similarly, we can control the format of the request that we send, using the Content-Type header.

**POST using form data**
		http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

```
{
  "id": 3,
  "title": "",
  "code": "print(123)",
  "linenos": false,
  "language": "python",
  "style": "friendly"
}
```



**POST using JSON**
		http --json POST http://127.0.0.1:8000/snippets/ code="print(456)"

```
{
    "id": 4,
    "title": "",
    "code": "print(456)",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}
```

