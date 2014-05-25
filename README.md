Epub Translator
=======

See `runner.py` for example usage.


Convert an epub book to another language or just replace some words with another.

Subclass `ConversionEngine` class and define your rules for translation.

An example ConversionEngine that transforms all worlds in the book to lower case would be:

    class SimpleConversionEngine(ConversionEngine):
    
        def convert(self, text):
         
            return text.lower()
            

All texts inside `<p>`, `<div>` etc tags are passed to `convert()` method, Text of one tag at a time.







Requirements
----
BeautifulSoup 3



Licence
----
BSD Licence
