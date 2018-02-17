
 The market leaders in Python web servers are Django, Pyramid and Flask.
 So why not use them?

Django is for mapping a website, a tree of web pages into relational tables.
It just does not fit.  It is like having to assemble your car, everytime
you take it out of the garage. Routes can be quite complex.  Usually one
first gives the table name, then the object name.  Traversal leads to a
much simpler URL map.

```
/
/contact
/about
/bloggers
     blogger1
          contact
          postings
	    posting1
	    posting2

     blogger2									      contact
        postings									 posting3
           posting4
```

In contrast in the Cromlech + ZODB site map,
there is no need to name the tables, and a node
can direclty contain multiple different content types.
And both bloggers can post something called 'Article1'.
Here is what it would look like.
```
/

/contact

/about
/blogger1
    posting1
    posting2
/blogger2
   contact
   posting1
   posting2
```

On the ease of use side, Django is pretty good.  It has tools for bringing
up applications quite easily.  Flask, I believe does not.  Pyramid has
SubstanceD, but that only allows one to create content types, it is by no
means a TTW Javascript IDE. Zopache makes for a much easier introduction
into these tall software stacks.
