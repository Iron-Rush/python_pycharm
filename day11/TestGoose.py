# TestGoose.py
from goose3 import Goose
url = 'http://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2'
g = Goose({'use_meta_language': False, 'target_language': 'es'})
article = g.extract(url=url)
article.cleaned_text[: 150]
print(article.title)
# article.title
# u'Occupy London loses eviction fight'
# article.meta_description
# "Occupy London protesters who have been camped outside the landmark St. Paul's Cathedral for the past four months lost their court bid to avoid eviction Wednesday in a decision made by London's Court of Appeal."
# article.cleaned_text[:150]
# "(CNN) - Occupy London protesters who have been camped outside the landmark St. Paul's Cathedral for the past four months lost their court bid to avoi"
# article.top_image.src
# 'http://i2.cdn.turner.com/cnn/dam/assets/111017024308-occupy-london-st-paul-s-cathedral-story-top.jpg'