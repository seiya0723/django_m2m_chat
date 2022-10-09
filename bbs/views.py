from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


from django.http.response import JsonResponse
from django.template.loader import render_to_string


from .models import Topic, ChatGroup, Chat
from .forms import TopicForm, ChatForm

class IndexView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        context = {}
        context["topics"]   = Topic.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = TopicForm(copied)

        if not form.is_valid():
            print("バリデーションNG")
            return redirect("bbs:index")
        
        print("バリデーションOK")
        form.save()

        return redirect("bbs:index")

index   = IndexView.as_view()


class ChatView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        context = {}

        #TODO:ここで自分が所属するチャットグループを取得する
        context["chat_groups"]   = ChatGroup.objects.filter(member=request.user.id).order_by("-dt")


        #TODO:ここでメッセージの新着順にグループを表示させるにはどうしたら良い？
        #A: sorted関数とoperatorを使うことで、任意のモデルメソッドを実行しその結果を元に並び替えできる。
        #グループごとの最新メッセージを取得し、その日付を返すメソッドを作り、↓のやり方で呼び出してソーティングすることで実現できると思われる。
        #https://noauto-nolife.com/post/django-attr-method-sort/


        return render(request,"bbs/chat.html",context)


chat    = ChatView.as_view()

class ChatMessageView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):

        data    = {"error":True}
        context = {}

        context["chat_group"]   = ChatGroup.objects.filter(id=pk).first()


        data["error"]   = False
        data["content"] = render_to_string("bbs/chat_area.html",context,request)

        return JsonResponse(data)

    def post(self, request,  pk, *args, **kwargs):

        data    = {"error":True}
        context = {}

        copied          = request.POST.copy()
        copied["group"] = pk
        copied["user"]  = request.user.id

        form    = ChatForm(copied)

        if not form.is_valid():
            return JsonResponse(data)


        form.save()

        context["chat_group"]   = ChatGroup.objects.filter(id=pk).first()

        data["error"]   = False
        data["content"] = render_to_string("bbs/chat_area.html",context,request)

        return JsonResponse(data)


chat_message    = ChatMessageView.as_view()



