##Bit.ly plugin for Pelican

If you have a need to generate a short bit.ly url for your articles or page, feel free to use this plugin and report any bugs or feedbacks by opening an issues on github


###Download and install


I encourage you to install the plugin via `pip` ::

        pip install pelican.bitly

Otherwise you can download [pelican.bitly](http://pypi.python.org/pypi/pelican.bitly) on pypi 
and installing it by running ::

        python setup.py install 

###How to use it


To load the plugin, you have to add it in your settings file. 

        PLUGINS = ['pelican-bitly',]


**Note**: you can setup the plugin by specifying a string with the path to with the path to it or import it and add the module in the list
        

For being able to use this pluging you need to have `SITEURL`` defined in your settings file, otherwise the plugin has no way to guess the absolute url. 

        SITEURL = 'http://example.com' 

The last step is adding  your bit.ly username and api key in your settings file

        BITLY_USERNAME = 'username'
        BITLY_API_KEY = 'api_key'

**warning** : If you are using a public repository as Github for the keeping the source code of your pelican site then think about keeping the settings `BITLY_USERNAME` and  `BITLY_API_KEY` in a separated settings file (eg: `local_settings.py`) and added this one to your `.gitignore`
       
  
 

Now that the plugin is configured, you can rebuilt your site and you should see  the short url being created in the ``pelican`` output :: 

        -> generate short url http://example.com/post_example.html -> http://bit.ly/XXXXXX


From yor templates,you can now access the bitly url of the `article` and `page` object from the `bitly_url` attribute 

        {{ article.bitly_url }}
        {{ page.bitly_url }}


