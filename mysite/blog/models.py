from django.db import models
from django import forms
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from readtime import of_html, of_markdown, of_text



from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable, PageManager
from wagtail.images.blocks import ImageChooserBlock 
from django.shortcuts import render
from wagtail.snippets.models import register_snippet
from wagtail import blocks
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.search import index



from blog import blocks as my_blocks

from wagtail.contrib.routable_page.models import RoutablePageMixin, path, route, re_path
from wagtailmetadata.models import MetadataPageMixin

from django.http import HttpResponse

from django.utils.text import slugify



from django_htmx.http import HttpResponseClientRefresh

from django.db.models import Count



class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogDetailPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )



class BlogAuthorsOrderable(Orderable):
     page = ParentalKey("blog.BlogDetailPage", related_name="blog_authors")
     author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
    )

     panels = [
        FieldPanel("author"),
    ]



class BlogAuthor(ClusterableModel):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    image = models.ForeignKey(
        ('home.CustomImage'),
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )
    facebook = models.CharField(max_length=200, blank=True, default="facebook")
    twitter = models.CharField(max_length=200, blank=True, default="twitter")
    instagram = models.CharField(max_length=200, blank=True, default="instagram")
    
    panels = [
    MultiFieldPanel(
        [
            FieldPanel("name"),
            FieldPanel("image"),
            FieldPanel("bio"),
        ],
        heading="Name, Image and Bio",
    ),
    MultiFieldPanel(
        [
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram"),
        ],
        heading="Social"
    ),
    
    InlinePanel('author_socials', label="Socials"),

]
    
    def __str__(self):
        return self.name
    
    class Meta:  
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)


SOCIAL_CHOICES = (
    ("Facebook", "Facebook"),
    ("Twitter", "Twitter"),
    ("Github", "Github"),

   )

class AuthorSocials(Orderable):
    page = ParentalKey("blog.BlogAuthor", on_delete=models.CASCADE, related_name='author_socials')
    network = models.CharField(max_length = 20, choices = SOCIAL_CHOICES, default="Facebook")
    url = models.URLField()

    panels = [
       
        FieldPanel('url'),
        FieldPanel('network'),
        

       
        
    ]
    

    

class BlogListingPage(MetadataPageMixin, RoutablePageMixin, Page):
    """Listing page lists all the Blog Detail Pages."""

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_template(self, request, *args, **kwargs):
        if request.htmx and request.GET.get('elements'):
             
             print("htmx")
             return 'partials/blog_list_element.html'
        
        

        else:
            return 'blog/blog_listing_page.html'
        
    
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        if request.htmx and request.GET.get('category'):
            category_arg = request.GET.get('category_arg', None)
            
            context["category_select"] = category_arg
            category = BlogCategories.objects.get(name=category_arg)
            context["cats"] = BlogCategories.objects.annotate(num_blogs=Count('blogdetailpage')).filter(num_blogs__gt=0)
            context["posts"] = BlogDetailPage.objects.live().public().filter(categories__in=[category])
            
        else:

            context["posts"] = BlogListingPage.get_children(self).live().order_by('-first_published_at')
            context["cats"] = BlogCategories.objects.annotate(num_blogs=Count('blogdetailpage')).filter(num_blogs__gt=0)
           
        
        
        paginator = Paginator(context["posts"], 2)
        page = request.GET.get("page")
        try:
           posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
           posts = paginator.page(paginator.num_pages)
        context["posts"] = posts
        return context
    
    
   
    


    @re_path(r'^tagged/(?P<tag>\w+)/(?P<pk>\d+)/$')
    def post_by_tag(self, request, tag, pk, *args, **kwargs):
        all_post = BlogDetailPage.objects.all()
        context = all_post.filter(tags__name=tag).exclude(pk=pk)
       
        print(context)   
        return self.render(request, template="partials/blog_by_tag.html", context_overrides = {'posts': context, 'tagged':tag})  
    
    search_fields = Page.search_fields + [
        index.AutocompleteField('custom_title'),
        
    ]

    # @re_path(r'^category/(\w+)/$')
    # def post_by_category(self, request, name, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     category = BlogCategories.objects.get(name=name)
    #     context["category_posts"] = BlogDetailPage.objects.live().public().filter(categories__in=[category])
        
         
    #     return self.render(request, template="partials/blog_by_category.html", context_overrides = {'category_posts': context["category_posts"]})  
    
#related posts was referenceing this https://www.yellowduck.be/posts/showing-related-pages-similar-tags-wagtail/   
class BlogPostManager(PageManager):
    def related_posts(self, post, max_items=4):
        type = post.type.all()
        matches = BlogDetailPage.objects.filter(type__in=type).live()
        matches = matches.exclude(pk=post.pk)
        related = matches.order_by('-last_published_at')
        return related[:max_items]
    
  
    
class BlogDetailPage(MetadataPageMixin, Page):
    """Blog detail page."""
    objects = BlogPostManager()

    title_background = models.ForeignKey(
        ('home.CustomImage'),
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    background = models.BooleanField(default=True)
    
    blog_image = models.ForeignKey(
        ('home.CustomImage'),
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='''This is the main blog image appearing at the top of the post 
        and it's 'thumbnail; across the site'''
    )
    
    categories = ParentalManyToManyField('blog.BlogCategories', blank=True)
    type = ParentalManyToManyField('blog.BlogType', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    summary = models.CharField(max_length=100, blank=True, default="sumamry", help_text='''This appears under the blog on 
                               recent posts section of the Homepage''')

    content = StreamField(
        [
            
            ("title_and_text", my_blocks.TitleAndTextBlock()),
            ("image", my_blocks.ImageBlock()),
            ("text_body", my_blocks.WritingBlock()),
            ('gallery', my_blocks.GalleryBlock()),
            ('code', my_blocks.CodeBlock()),
            ('quote', my_blocks.QuoteBlock()),
            ('embed', my_blocks.EmbedBlock()),
            ('full_width_image', my_blocks.FullWidthImage()),
            ('strava_embed', my_blocks.StravaBlock()),
            ('text', blocks.CharBlock()),
            ('slideshow', my_blocks.Slideshowblock()),
            ('image_group', my_blocks.ImageGroupBlock())
          
          
           
        ],
         use_json_field=True)

    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                 FieldPanel("title_background"),
                 FieldPanel("background"),
            ]
        ),
        
        FieldPanel("summary"),
        FieldPanel("blog_image"),
        FieldPanel("content"),
        FieldPanel("tags"),
        FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
        FieldPanel("type", widget=forms.CheckboxSelectMultiple),
        
         MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=4)
                
            ],
            heading="Author(s)"
        ),

        
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
        
        index.AutocompleteField('slug'),
        index.AutocompleteField('summary'),
        
    ]

    def get_context(self, request, *args, **kwargs):
        
        context = super(BlogDetailPage, self).get_context(request)
        context['related_posts'] = BlogDetailPage.objects.related_posts(self)
        context['head_tags'] = self.specific.tags.all()
        return context

    
  



    @property
    def next_post(self):
        return self.get_next_sibling()
        
       
    @property
    def previous_post(self):
        return self.get_prev_sibling()
    
    
    def __str__(self):
        return self.title
    
    
@register_snippet
class BlogCategories(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    icon = models.ForeignKey(
        ('home.CustomImage'), null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


@register_snippet
class BlogType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
   

    panels = [
        FieldPanel('name'),
       
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog type'