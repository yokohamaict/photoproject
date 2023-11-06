from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from .models import PhotoPost

# ログインを必須にするための仕組み
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 4

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    template_name = 'post_photo.html'
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        # フォームに入力された内容を保存(データベースにはまだ保存しない)
        post_data = form.save(commit=False)
        # 画像をアップロードしたユーザーのユーザーIDを追加で保存
        post_data.user = self.request.user
        # フォームの内容+ユーザの情報をまとめてデータベースに保存
        post_data.save()

        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
