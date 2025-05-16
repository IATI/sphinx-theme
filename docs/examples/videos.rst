======
Videos
======

Youtube
-------

Videos on YouTube or Vimeo can be embedded using the `sphinxcontrib-youtube plugin <https://github.com/sphinx-contrib/youtube>`_:

.. code-block:: rst

    .. youtube:: mL72ArkyAJs

.. youtube:: mL72ArkyAJs

Other Services
--------------

Videos on other services can be embedded as long as there is an iframe option:

.. code-block:: html

    .. raw:: html

    <iframe src="https://commons.wikimedia.org/wiki/File:Animation_Of_Webb%27s_Orbit.webm?embedplayer=yes" 
        width="512" 
        height="288" 
        frameborder="0" 
        loading="lazy" 
        allow="autoplay; picture-in-picture" 
        allowfullscreen>
    </iframe>

.. raw:: html

    <iframe src="https://commons.wikimedia.org/wiki/File:Animation_Of_Webb%27s_Orbit.webm?embedplayer=yes" 
        width="512" 
        height="288" 
        frameborder="0" 
        loading="lazy" 
        allow="autoplay; picture-in-picture" 
        allowfullscreen>
    </iframe>



Videos not already online
-------------------------

If the video is not already on the web somewhere or there isn't a good way to embed it (e.g. if the embedding is serving adverts), then video can be added to the Sphinx site. To do this, place the video file in the docs/_static directory and add it to git. 

The video can then be added to a page using the `sphinxcontrib-video plugin <https://pypi.org/project/sphinxcontrib-video/>`_ . See the plugin's website for all available options and usage instructions. 

Adding large (> 10MB) or multiple videos may make the repo quite large, and therefore slow to work with. If this becomes an issue, speak with a friendly dev about solutions. 

.. code-block:: rst

    .. video:: ../_static/Animation_of_Rotating_Earth_at_Night.webm
    :align: center

.. video:: ../_static/Animation_of_Rotating_Earth_at_Night.webm
    :align: center

(This is in the public domain because it was solely created by NASA. NASA copyright policy states that its material is `not subject to copyright <https://www.nasa.gov/nasa-brand-center/images-and-media/#:~:text=generally%20are%20not%20subject%20to%20copyright%20>`_. )

