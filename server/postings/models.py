from django.db import models


class PostModel(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="author")
    title = models.TextField()
    desc = models.TextField()
    file_name = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now=True)
    update_author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="update_author")


class CommentModel(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    photo = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
