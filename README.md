# CDN Collector
Small util for creation dump of JS libraries.

## Requires
* Linux
* Bower (nodejs)

## Libraries
    
    http://bower.io/search/

## To run

    python collector.py
  
without debug messages:  

    python collector.py | grep -v DEBUG
    
with only error log:

    python collector.py | grep ERROR
