from haystack import indexes
from .models import Product


class search(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document =True, use_template=True)
    name = indexes.CharField(model_attr='name')
    desc = indexes.CharField(model_attr='description')

    def get_model(self):
        return Product

    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()