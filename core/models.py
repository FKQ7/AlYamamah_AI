from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class News(models.Model):
    class Meta:
        ordering = ['-date_start']  # Default sorting by date_start in descending order
    img = models.ImageField(upload_to='news_images/')
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=700)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    tag_1 = models.CharField(max_length=100)
    tag_2 = models.CharField(max_length=100, null=True, blank=True)
    tag_3 = models.CharField(max_length=100, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.img:
            img = Image.open(self.img)
            
            # Resize the image to 500x200 pixels using LANCZOS (formerly known as ANTIALIAS)
            img = img.resize((500, 200), Image.Resampling.LANCZOS)

            # Save the resized image back to the model's img field
            img_io = BytesIO()
            img.save(img_io, format='PNG')  # Save as JPEG; use 'PNG' if needed
            img_io.seek(0)
            
            # Save the image as an InMemoryUploadedFile
            self.img = InMemoryUploadedFile(img_io, None, self.img.name, 'image/jpeg', img_io.tell(), None)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title