from django.db import models

# Create your models here.

class GptIO(models.Model):
    input_text = models.TextField()
    output_text = models.TextField()
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of the gpt input/output."""
        date = timezone.localtime(self.log_date)
        return f"Input: '{self.input_text}'\nOutput: '{self.output_text}'\nlogged on {date.strftime('%A, %d %B, %Y at %X')}"
