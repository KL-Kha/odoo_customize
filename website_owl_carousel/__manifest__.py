{
    'name' 'OWL Carousel',
    'category' 'website',
    'summary' 'Improve website with this amazing carousel',
    'version' '16.0.0.0.1',
    'description' 
    ,
    'author' 'Trey (www.trey.es)',
    'license' 'AGPL-3',
    'depends' [
        'website',
    ],

    'assets': {'web.assets_backend':
				   ['website_owl_carousel/static/lib/owl-carousel/owl.carousel.css',
					'website_owl_carousel/static/lib/owl-carousel/owl.theme.css',
					'website_owl_carousel/static/lib/owl-carousel/owl.carousel.min.js',
					],
			   },
    'installable' True,
    'application' False,
    'auto_install' False,
}
