from pelican import signals
import bitlyapi
from functools import wraps
import logging
log = logging.getLogger(__name__)


def bitly_wrapper(f, items_key='articles'):

    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        self = f.im_self
        bitly = bitlyapi.BitLy(self.context['BITLY_USERNAME'],
                self.context['BITLY_API_KEY'])
        for item in self.__getattribute__(items_key):
            abs_url = "%s/%s" % (self.context['SITEURL'], item.url)
            item.abs_url = abs_url
            item.bitly_url = bitly.shorten(longUrl=abs_url)['url']
            log.info('generate short url %s -> %s' % (item.abs_url, item.bitly_url))
        return result
    return wrapper


def shorten_url_articles(generator):
    if generator.context.get('BITLY_ARTICLES', True):
        generator.generate_context = bitly_wrapper(generator.generate_context)


def shorten_url_pages(generator):
    if generator.context.get('BITLY_PAGES', True):
        generator.generate_context = bitly_wrapper(generator.generate_context, items_key='pages')


def register():
    signals.article_generator_init.connect(shorten_url_articles)
    signals.pages_generator_init.connect(shorten_url_pages)
