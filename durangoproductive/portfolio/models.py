from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from markdown import markdown
from typogrify.filters import typogrify


def markup(text):
    """
    Mark up plain text into fancy HTML.

    """
    return typogrify(
        markdown(
            text,
            lazy_ol=False,
            output_format='html5',
            extensions=[
                'abbr',
                'codehilite',
                'fenced_code',
                'sane_lists',
                'smart_strong']))


class FeaturedProjectManager(models.Manager):
    """
    Manager to fetch only featured projects.
    Since we only need one featured project, we'll grab the latest using
    the completion date.
    """
    def get_query(self):
        return super(
            FeaturedProjectManager, self).get_query_set().filter(
            is_featured=True).latest(
            'completion_date')


class PublicProjectManager(models.Manager):
    """
    Manager to fetch only public projects.
    """
    def get_query(self):
        return super(PublicProjectManager, self).get_query_set().filter(
            is_public=True)


@python_2_unicode_compatible
class Project(models.Model):
    """
    A project in the portfolio.
    """
    client_name = models.CharField(
        max_length=100,
        help_text='Limited to 100 characters.')
    slug = models.SlugField(
        help_text='Populates from the client name field automatically.')
    description = models.TextField(
        help_text='No HTML allowed')
    description_html = models.TextField(
        editable=False,
        blank=True)
    lead_art = models.ImageField(
        help_text='Used for project representation on homepage and list view.',
        upload_to='images/portfolio/projects')
    is_featured = models.BooleanField(
        default=False,
        help_text='Determines whether the project will \
        be displayed on the homepage.')
    is_public = models.BooleanField(
        default=True,
        help_text='Determines whether the project is public on \
        the website. Admins can view if false.')
    completion_date = models.DateField(
        help_text='When was this project completed?')
    categories = models.ManyToManyField('Category')

    public = PublicProjectManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('completion_date',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description_html = markup(self.description)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio_project_detail', (), {'slug': self.slug})


@python_2_unicode_compatible
class Asset(models.Model):
    description = models.CharField(
        max_length=250,
        help_text='Briefly describe the asset. Limited to 250 characters.')
    project = models.ForeignKey(Project)
    art = models.ImageField(
        upload_to='images/portfolio/assets'
        help_text='The art to associated with this project asset.')

    class Meta:
        verbose_name_plural = 'Assets'
        ordering = ('id',)

    def __unicode__(self):
        return self.description


@python_2_unicode_compatible
class Category(models.Model):
    """
    A category for managing project types.

    """
    title = models.CharField(
        max_length=250,
        help_text='Limited to 250 characters')
    slug = models.SlugField(unique=True)
    description = models.TextField(
        help_text='No HTML allowed')
    description_html = models.TextField(
        editable=False,
        blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description_html = markup(self.description)
        super(Category, self).save(*args, **kwargs)
