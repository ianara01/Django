from django.db import models

# create yout models here
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='news')
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"News by {self.company.name} on {self.content}"
    