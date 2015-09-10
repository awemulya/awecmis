from django.shortcuts import render
from employee.models import DEFAULT_GUESTBOOK_NAME, Greeting, guestbook_key, Author


def employee(request):
    p = Author(identity='Arthur Dentee', email="dentee@gmail")
    p.put()
    g = Greeting(author=p, content="dent@gmail")
    g.put()
    gr = Greeting()
    greetings = gr.populate(author=p)

    # guestbook_name = request.GET.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
    # greetings_query = Greeting.query(
    #     ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
    # greetings = greetings_query.fetch(10)
    return render(request, "employee.html", {'objlist': greetings})
