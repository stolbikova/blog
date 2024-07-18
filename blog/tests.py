from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment


class BlogTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post', text='Test Content', author=self.user)

    def test_post_creation(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('post_new'), {
            'title': 'New Post',
            'text': 'New content',
        })
        # Should redirect after creation
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_post_edit(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('post_edit', kwargs={'pk': self.post.pk}), {
            'title': 'Updated Post',
            'text': 'Updated content',
        })
        # Should redirect after editing
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_add_comment(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_comment_to_post', kwargs={'pk': self.post.pk}), {
            'author': self.user.username,
            'text': 'Test comment',
        })
        # Should redirect after adding comment
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)

    def test_comment_approve(self):
        self.client.login(username='testuser', password='12345')
        comment = Comment.objects.create(
            post=self.post, author=self.user, text='Test comment')
        response = self.client.post(
            reverse('comment_approve', kwargs={'pk': comment.pk}))
        # Should redirect after approving comment
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertTrue(comment.approved_comment)

    def test_comment_remove(self):
        self.client.login(username='testuser', password='12345')
        comment = Comment.objects.create(
            post=self.post, author=self.user, text='Test comment')
        response = self.client.post(
            reverse('comment_remove', kwargs={'pk': comment.pk}))
        # Should redirect after removing comment
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 0)
