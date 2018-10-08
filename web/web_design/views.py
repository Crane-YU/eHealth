from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import User
from django.db.models import Avg
from django.views.decorators.csrf import csrf_exempt

# Create views
# def homepage(request):
#     template = get_template('index.html')
#     posts = Post.objects.all()
#     now = datetime.now()
#     html = template.render(locals())
#     return HttpResponse(html)
#     # post_lists = list()
#     #
#     # for count, post in enumerate(posts):
#     #     post_lists.append("No.{}: ".format(str(count)) + str(post)+"<hr>")
#     #     post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")
#     #
#     # return HttpResponse(post_lists)
#
#
# def showpost(request, slug):
#     template = get_template("post.html")
#     try:
#         post = Post.objects.get(slug=slug)
#         if post is not None:
#             html = template.render(locals())
#             return HttpResponse(html)
#
#     except:
#         return redirect('/')


# using Django to connect to an existing database
def homepage(request):
    value = User.objects.values()
    print(value)

    # The following commands calculate the average of balance
    posts = User.objects.all()
    average = posts.aggregate(Avg('balance'))
    print(average["balance__avg"])

    # for count, post in enumerate(posts):
    #   print(str(count) + str(post))

    # list_post = list(posts)
    # print(list_post, type(list_post))
    # for item in list_post:
    #     print(item)

    return render_to_response("table.html", locals())


# sending json file
def send_json(request):
    # Get all fields of values from database
    value = User.objects.all().values()

    # Convert the QuerySet to a list object
    user_list = list(value)
    print(user_list)

    # Returned result is an array of objects
    return JsonResponse(user_list, safe=False)


# using ajax to exchange the data without refreshing
@csrf_exempt
def send_ajax(request):

    value = User.objects.all().values()
    user_list = list(value)
    post_list = list()
    # print(value)
    # Get the average value
    average = User.objects.all().aggregate(Avg('balance'))

    if request.method == 'POST':
        # print(request.POST)
        print(post_list)

        data = {'status': 0, 'msg': 'Post successful', 'data': post_list+user_list}
        # data = {
        #     'spo2_value': 0,
        #     'pulse_value': 0,
        #     'emg_value': 0,
        #     'bp_value': 0,
        # }

        return JsonResponse(data, safe=False)
    else:
        return render(request, 'ajax.html')

