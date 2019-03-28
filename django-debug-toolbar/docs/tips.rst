Tips
====

The toolbar isn't displayed!
----------------------------

The Debug Toolbar will only display when ``DEBUG = True`` in your project's
settings. It will also only display if the mimetype of the response is
either ``text/html`` or ``application/xhtml+xml`` and contains a closing
``</body>`` tag.

Be aware of middleware ordering and other middleware that may intercept
requests and return responses. Putting the debug toolbar middleware *after*
the Flatpage middleware, for example, means the toolbar will not show up on
flatpages.

Middleware isn't working correctly
----------------------------------

Using the Debug Toolbar in its default configuration and with the profiling
panel will cause middlewares after
``debug_toolbar.middleware.DebugToolbarMiddleware`` to not execute their
``process_view`` functions. This can be resolved by disabling the profiling
panel or moving the ``DebugToolbarMiddleware`` to the end of
``MIDDLEWARE_CLASSES``. Read more about it at
:ref:`ProfilingPanel <profiling-panel>`

Using the toolbar offline
-------------------------

The Debug Toolbar loads the jQuery_ library from the Google Hosted Libraries
CDN. Your browser will keep it in cache, allowing you to use the toolbar even
if you disconnect from the Internet temporarily.

If you want to use the Debug Toolbar without an Internet connection at all, or
if you refuse to depend on Google's services, look at the ``JQUERY_URL``
configuration option.

.. _jQuery: https://jquery.com/

Performance considerations
--------------------------

The Debug Toolbar is designed to introduce as little overhead as possible in
the rendering of pages. However, depending on your project, the overhead may
become noticeable. In extreme cases, it can make development impractical.
Here's a breakdown of the performance issues you can run into and their
solutions.

Problems
~~~~~~~~

The Debug Toolbar works in two phases. First, it gathers data while Django
handles a request and stores this data in memory. Second, when you open a
panel in the browser, it fetches the data on the server and displays it.

If you're seeing excessive CPU or memory consumption while browsing your site,
you must optimize the "gathering" phase. If displaying a panel is slow, you
must optimize the "rendering" phase.

Culprits
~~~~~~~~

The SQL panel may be the culprit if your view performs many SQL queries. You
should attempt to minimize the number of SQL queries, but this isn't always
possible, for instance if you're using a CMS and have disabled caching for
development.

The cache panel is very similar to the SQL panel, except it isn't always a bad
practice to make many cache queries in a view.

The template panel becomes slow if your views or context processors return large
contexts and your templates have complex inheritance or inclusion schemes.

Solutions
~~~~~~~~~

If the "gathering" phase is too slow, you can disable problematic panels
temporarily by deselecting the checkbox at the top right of each panel. That
change will apply to the next request. If you don't use some panels at all,
you can remove them permanently by customizing the ``DEBUG_TOOLBAR_PANELS``
setting.

By default, data gathered during the last 10 requests is kept in memory. This
allows you to use the toolbar on a page even if you have browsed to a few
other pages since you first loaded that page. You can reduce memory
consumption by setting the ``RESULTS_CACHE_SIZE`` configuration option to a
lower value. At worst, the toolbar will tell you that the data you're looking
for isn't available anymore.

If the "rendering" phase is too slow, refrain from clicking on problematic
panels :) Or reduce the amount of data gathered and rendered by these panels
by disabling some configuration options that are enabled by default:

- ``ENABLE_STACKTRACES`` for the SQL and cache panels,
- ``SHOW_TEMPLATE_CONTEXT`` for the template panel.

Also, check ``SKIP_TEMPLATE_PREFIXES`` when you're using template-based
form widgets.
