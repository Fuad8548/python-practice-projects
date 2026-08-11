- ## Why both ```setattr()``` AND ```__setattr__()```?
    - ```setattr(obj, name, value)``` is a function we call — it's the trigger. It means "hey Python, please set this attribute."
    - ```__setattr__(self, name, value)``` is a method we define — it's the handler. It's what Python actually runs, every single time any attribute gets set on that object.
    - ```for key, value in data.items()```: ```setattr(self, key, value)``` loop is just a convenient way to write self.name = ..., self.email = ... every one of those assignments still passes through our custom ```__setattr__``` validation.

Normally you'd write self.name = data["name"], self.email = data["email"], one line per field. But if the form has 20 fields, or you don't know the field names in advance, that's painful. setattr(self, key, value) does self.<whatever key is> = value dynamically, looping through however many keys exist. This is exactly how libraries like Django or Pydantic build objects from JSON/form data under the hood.

- **Trace it carefully:**
    - ```setattr(self, "email", "fuad@mail.com")``` runs
    - Python doesn't just store it — it calls ```self.__setattr__("email", "fuad@mail.com")``` automatically, because we overrode that method
    - Inside, we check validity, print a log, then call ```super().__setattr__(...)``` to actually save it

- ## Why ```super().__setattr__(...)```? Why not just ```self.name = value``` inside ```__setattr__``` itself?
    - The line ```self.name = value``` would trigger ```__setattr__``` again → which calls ```self.name = value``` again → infinite loop → crash. ```super().__setattr__()``` bypasses our custom version and goes straight to Python's built-in storage mechanism, breaking that loop.


- ## Why dir(user) includes dunders, and why we skip them
    - ```dir(user)``` returns every single attribute name that exists on the object — not just the ones we personally created. That includes Python's built-in machinery:
        ```Python 
        print(dir(user))
        # ['__class__', '__delattr__', '__dict__', '__eq__', '__init__', ..., 'country', 'name']
        ```
    Since Python's internal dunder names always start and end with __, filtering with ```attr.startswith("__")``` is a cheap, standard way to say "skip Python's internals, show me only what a human defined."

- ## Why not callable(...)?
    - ```dir(user)``` also lists methods, not just data. A method (like __init__) is itself a value we can fetch with ```getattr()``` — and it's a function object, not data we want printed as a "field." Since we only want data fields like name and country, not the object's behavior, so the filter says: "show me attributes that (1) aren't Python's internal dunders, and (2) aren't functions — just plain stored data."

To sum up, dynamic attributes let you work with attribute names that only exist as data (strings) at runtime, not as literal names you typed into your code.